import os
from pathlib import Path
import random
import torch
import torchvision.transforms as T
from torchvision.models import resnet18
from PIL import Image
import streamlit as st

# ---------- Paths ----------
BASE = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE / "game_assets"
MODELS_DIR = BASE / "models"
DIALOGUE_DIR = BASE / "dialogue"
MODEL_PATH = MODELS_DIR / "classifier.pt"
CLASSES_PATH = MODELS_DIR / "classes.txt"

# ---------- UI Setup ----------
st.set_page_config(page_title="AI Guessing Game", page_icon="🎮", layout="centered")
st.title("🎮 AI Guessing Game (NiceGPU)")
st.caption("Generate images → train a classifier → add a Game Master → play!")

# ---------- Load Classes ----------
if CLASSES_PATH.exists():
    classes = [c.strip() for c in CLASSES_PATH.read_text().splitlines() if c.strip()]
else:
    classes = [f"class{i}" for i in range(10)]

# ---------- Caches ----------
@st.cache_resource
def load_model():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = resnet18(num_classes=len(classes)).to(device)
    if MODEL_PATH.exists():
        state = torch.load(MODEL_PATH, map_location=device)
        model.load_state_dict(state, strict=False)
        st.success(f"Loaded classifier: {MODEL_PATH.name}")
    else:
        st.warning("No trained classifier found (models/classifier.pt). Using untrained model → random guesses.")
    model.eval()
    return model, device

@st.cache_resource
def load_nlp():
    try:
        from transformers import pipeline
        device_idx = 0 if torch.cuda.is_available() else -1
        sentiment = pipeline("sentiment-analysis", device=device_idx)
        gen = pipeline("text-generation", model="gpt2", device=device_idx)
        return sentiment, gen
    except Exception as e:
        st.warning(f"NLP pipelines unavailable: {e}")
        return None, None

# ---------- Helpers ----------
def predict(model, device, img_path):
    tfm = T.Compose([T.Resize((32,32)), T.ToTensor()])
    img = Image.open(img_path).convert("RGB")
    x = tfm(img).unsqueeze(0).to(device)
    with torch.no_grad():
        logits = model(x)
        pred_idx = logits.argmax(1).item()
    label = classes[pred_idx] if 0 <= pred_idx < len(classes) else str(pred_idx)
    return label, img

def gm_reply(gen, persona, context, max_new_tokens=60):
    if gen is None:
        return "Game Master is resting (no NLP model loaded)."
    prompt = f"""{persona}
Context: {context}
Reply:"""
    out = gen(prompt, max_new_tokens=max_new_tokens, do_sample=True, temperature=0.9)[0]['generated_text']
    return out

# ---------- Session State ----------
if "score" not in st.session_state: st.session_state.score = 0
if "round" not in st.session_state: st.session_state.round = 0
if "round_limit" not in st.session_state: st.session_state.round_limit = 5
if "current_image" not in st.session_state: st.session_state.current_image = None

# ---------- Sidebar ----------
st.sidebar.header("Game Settings")
st.session_state.round_limit = st.sidebar.slider("Rounds", 1, 10, st.session_state.round_limit, 1)
persona_default = "You are a friendly Game Master. Encourage players, keep answers under 40 words, and be school-appropriate."
persona_path = DIALOGUE_DIR / "persona.txt"
if persona_path.exists():
    persona_default = persona_path.read_text().strip() or persona_default
persona = st.sidebar.text_area("Game Master Persona", persona_default, height=120)

if st.sidebar.button("🔁 Reset Game"):
    st.session_state.score = 0
    st.session_state.round = 0
    st.session_state.current_image = None
    st.experimental_rerun()

# ---------- Load resources ----------
model, device = load_model()
sentiment, gen = load_nlp()

# ---------- Choose images ----------
asset_paths = sorted([p for p in ASSETS_DIR.glob("**/*") if p.suffix.lower() in {".png",".jpg",".jpeg"}])
if not asset_paths:
    st.info("No images found. Add images to `game_project/game_assets/` and refresh.")
    st.stop()

# Set current image
if st.session_state.current_image is None:
    st.session_state.current_image = random.choice(asset_paths)

# ---------- Main Panel ----------
st.subheader(f"Round {st.session_state.round+1} of {st.session_state.round_limit}")
label, pil_img = predict(model, device, st.session_state.current_image)
st.image(pil_img.resize((384,384)), caption=f"Guess the image! ({st.session_state.current_image.name})")

guess = st.text_input("Your guess:", value="", max_chars=50)

col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Submit Guess"):
        correct = (guess.strip().lower() == str(label).lower())
        if correct:
            st.session_state.score += 1
        # Sentiment feedback (optional)
        if sentiment is not None:
            fb = sentiment(f"I guessed: {guess}")[0]
            st.write(f"Sentiment on your guess: **{fb['label']}** (score={fb['score']:.2f})")
        # Game Master reply
        gm = gm_reply(gen, persona, f"Player guessed '{guess}'. Truth is '{label}'. Correct={correct}")
        st.markdown(f"**Game Master:** {gm}")
        # Reveal answer
        st.success(f"Answer: {label}" if correct else f"Not quite! It was: {label}")
with col2:
    if st.button("➡️ Next Round"):
        st.session_state.round += 1
        if st.session_state.round >= st.session_state.round_limit:
            st.balloons()
            st.success(f"Game over! Final score: {st.session_state.score}/{st.session_state.round_limit}")
            st.session_state.round = 0
            st.session_state.score = 0
        st.session_state.current_image = random.choice(asset_paths)
        st.experimental_rerun()

st.markdown(f"### Score: {st.session_state.score} / {st.session_state.round_limit}")
st.caption("Tip: update classes in models/classes.txt to match your training labels.")