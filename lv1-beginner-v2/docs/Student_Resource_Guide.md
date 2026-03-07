# 🎓 Lv1 Beginner v2 — Per-Student Resource Evaluation

> **Class starts:** Wednesday, March 11, 2026  
> **Format:** 6 sessions × 2 hours = 12 hours total  
> **Students:** Ages 13–16, no prior coding experience required  
> **Hardware:** Gaming PCs (with GPUs) provided; Google Colab & NiceGPU available as cloud options

---

## 📋 Session-by-Session Resource Summary

### Session 0 — Setup & AI Fundamentals 🧰

| Resource | Details | Required? |
|:--|:--|:--:|
| **Python environment** | Python 3.8+ with Jupyter Notebook | ✅ Must |
| **Standard libraries** | `sys`, `platform` (built-in, no install) | ✅ Auto |
| **PyTorch** (optional check) | Used only for GPU detection demo | ⚠️ Optional |
| **API key** | None used this session | ❌ None |
| **GPU** | Not required | ❌ None |

> **Notes:** Pure setup, Python basics, and conceptual overview. Lightest session — no external APIs or heavy models. Confirm Jupyter/JupyterLab is installed on gaming PCs and validate GPU is detected (`torch.cuda.is_available()` should return `True`).

**📖 Pre-Class Reading**
1. [AI for Everyone – Week 1](https://www.coursera.org/learn/ai-for-everyone) (Andrew Ng, Coursera – free audit) — best plain-English intro to AI
2. [Python in 100 Seconds](https://www.youtube.com/watch?v=x7X9w_GIm1s) (Fireship, YouTube) — 2-min Python mental model
3. [What is a Jupyter Notebook?](https://realpython.com/jupyter-notebook-introduction/) (Real Python) — understand the tool used every session

---

### Session 1 — Prompt Engineering & LLMs 🧠 ⭐NEW

| Resource | Details | Required? |
|:--|:--|:--:|
| **`openai` package** | `pip install openai` | ✅ Must |
| **OpenAI API Key** | Instructor-provided; set as env variable | ✅ Must |
| **GPU** | Not required (API-based) | ❌ None |

> **Alternatives:** Gemini API (`google-generativeai`) can substitute OpenAI — notebook mentions both.  
> **Key Action:** Instructor must supply a shared or per-student `OPENAI_API_KEY` before class.

**📖 Pre-Class Reading**
1. [How ChatGPT Works](https://www.youtube.com/watch?v=flXrLGPY3SU) (Computerphile, YouTube) — intuitive, no-math explanation of LLMs
2. [Prompt Engineering Guide – Intro](https://www.promptingguide.ai/introduction/basics) — zero-shot, few-shot, chain-of-thought
3. [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) (DeepLearning.AI – free) — first 2 lessons only

---

### Session 2 — AI Image Generation 🎨

| Resource | Details | Required? |
|:--|:--|:--:|
| **`diffusers` package** | `pip install diffusers transformers accelerate safetensors matplotlib Pillow` | ✅ Must |
| **`PyTorch`** | Included via diffusers dependencies | ✅ Auto |
| **Model download** | `stabilityai/sd-turbo` (~3–4 GB from HuggingFace) | ✅ Must |
| **GPU (CUDA)** | Gaming PC GPUs work great; float16 enabled automatically | ✅ Available |
| **GPU VRAM** | Minimum ~4 GB VRAM; most gaming GPUs (RTX 3060+) have 8–12 GB | ✅ Available |
| **API key** | None (local model) | ❌ None |

> **With gaming GPUs:** Image generation with `sd-turbo` should complete in **5–15 seconds** per image (RTX class GPU). Pre-download the model (~4 GB) before class to avoid first-run delays.  
> **Cloud fallback:** If any PC has GPU issues, switch that student to **Google Colab** (free T4) or **NiceGPU** — no setup change needed, just upload the notebook.  
> **HuggingFace Token:** Not required for `sd-turbo` (public model).

**📖 Pre-Class Reading**
1. [How AI Image Generators Work](https://www.youtube.com/watch?v=1CIpzeNxIhU) (Computerphile, YouTube) — visual explanation of diffusion
2. [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/) (Jay Alammar) — best visual walkthrough, no heavy math
3. [Lexica.art](https://lexica.art) — browse real prompts & outputs to build intuition

---

### Session 3 — Image Classification 🔍

| Resource | Details | Required? |
|:--|:--|:--:|
| **`torch`, `torchvision`** | Pre-installed with PyTorch | ✅ Must |
| **`matplotlib`, `numpy`** | Standard ML libraries | ✅ Must |
| **CIFAR-10 dataset** | Auto-downloaded via torchvision (~170 MB) | ✅ Must |
| **GPU (CUDA)** | Strongly recommended for CNN training; CPU works but slow | ⚠️ Recommended |
| **GPU VRAM** | 2+ GB sufficient for CIFAR-10 CNN | ⚠️ If GPU |
| **API key** | None | ❌ None |

> **Training time estimate with gaming GPU:** ~1–3 min for small CNN on RTX 3060+. Well within the 2-hour session.  
> **Pre-download CIFAR-10** (~170 MB) before class to avoid first-run delay.

**📖 Pre-Class Reading**
1. [But What *is* a Neural Network?](https://www.youtube.com/watch?v=aircAruvnKk) (3Blue1Brown, YouTube) — gold-standard visual intro, ~20 min
2. [Image Classification – Google ML Crash Course](https://developers.google.com/machine-learning/practica/image-classification) — first two sections only
3. [What is CIFAR-10?](https://paperswithcode.com/dataset/cifar-10) (Papers With Code) — see the dataset they'll train on

---

### Session 4 — Chatbot, Sentiment & Voice 💬

| Resource | Details | Required? |
|:--|:--|:--:|
| **`transformers` package** | `pip install transformers torch` | ✅ Must |
| **Sentiment model** | `distilbert-base-uncased-finetuned-sst-2-english` (~260 MB, auto-downloaded) | ✅ Must |
| **Emotion model** (bonus) | `j-hartmann/emotion-english-distilroberta-base` (~300 MB) | ⚠️ Optional |
| **GPU** | Not required; CPU runs fine for inference | ❌ Optional |
| **Voice input** *(optional)* | `openai-whisper`, `sounddevice`, `scipy` + microphone | ⚠️ Optional |
| **Voice output** *(optional)* | `pyttsx3` + speakers | ⚠️ Optional |
| **API key** | None for base session | ❌ None |

> **Voice Features:** Marked optional in notebooks. `pyttsx3` works offline; Whisper requires download (~140 MB for base model). If microphones are unavailable, voice section can be skipped with no loss to core learning.

**📖 Pre-Class Reading**
1. [What is NLP?](https://www.youtube.com/watch?v=CMrHM8a3hqw) (IBM Technology, YouTube) — 9-min overview, no math
2. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) (Jay Alammar) — read intro + encoder sections
3. [HuggingFace NLP Course – Chapter 1](https://huggingface.co/learn/nlp-course/chapter1/1) — first two pages; directly relevant to the pipeline used

---

### Session 5 — AI Game & Agents 🎮

| Resource | Details | Required? |
|:--|:--|:--:|
| **`transformers` package** | Reuses Session 4 install | ✅ Already done |
| **Sentiment model** | Reuses Session 4 model cache | ✅ Already done |
| **`openai` package** | Reuses Session 1 install | ✅ Already done |
| **OpenAI API Key** | Used for AI agent behavior | ✅ Must |
| **GPU** | Not required | ❌ None |

> **Integration session** — relies entirely on libraries and models from prior sessions. If Session 1–4 are complete, no new installations are needed. Focus is on combining components.

**📖 Pre-Class Reading**
1. [What are AI Agents?](https://www.youtube.com/watch?v=F8NKVhkZZWI) (IBM Technology, YouTube) — plain-English intro to agentic AI
2. [ReAct: Reason + Act](https://react-lm.github.io/) — read the intro paragraph; connects to the agent pattern in the notebook
3. Review your own notebooks from Sessions 1–4 — best prep is re-reading your own code

---

## 📊 Cumulative Per-Student Resource Requirements

| Category | Details |
|:--|:--|
| **GPU** | Gaming PC GPUs cover Sessions 2 & 3; Google Colab / NiceGPU as per-student fallback |
| **Python Packages** | `openai`, `diffusers`, `transformers`, `torch`, `torchvision`, `accelerate`, `safetensors`, `matplotlib`, `Pillow`, `numpy` |
| **API Keys** | **OpenAI API Key** (Sessions 1 & 5) — instructor-provided |
| **Microphone** | Optional (Session 4 voice feature) |
| **Speakers** | Optional (Session 4 TTS feature) |

---

## 👤 Account Requirements

| Account | Sessions | Required? | Notes |
|:--|:--|:--:|:--|
| **Google Account** | All (if using Colab) | ⚠️ If Colab | Free gmail.com works; recommend setting up before class |
| **NiceGPU Account** | All (if using NiceGPU) | ⚠️ If NiceGPU | Requires registration; set up ahead of class day |
| **OpenAI Account** | 1, 5 | ❌ No | Instructor-provided key — students don't need their own account |
| **HuggingFace Account** | 2, 3, 4 | ❌ No | All models used are public and download anonymously |
| **GitHub Account** | Optional | ❌ No | Only needed if students want to clone/fork the repo |

> **Primary path (gaming PCs):** Students need **no accounts at all** — everything runs locally with instructor-provided keys.  
> **Cloud fallback:** Ensure each student has a **Google account** (Colab) or **NiceGPU account** registered *before* class day to avoid onboarding delays.

## 🔑 Instructor Pre-Class Checklist

- [ ] **API Key ready**: OpenAI key provisioned and tested
- [ ] **Colab or GPU plan**: Decide if students use local machines (need GPU) or Google Colab
- [ ] **Pre-download models**: Run Sessions 2, 3, 4 cells once to cache models (`sd-turbo`, CIFAR-10, distilbert)
- [ ] **Python environment**: Install all packages in advance (`pip install openai diffusers transformers torch torchvision accelerate safetensors matplotlib Pillow numpy`)
- [ ] **Test Session 0 notebook**: Verify Jupyter opens and runs on all student machines
- [ ] **Voice test** (optional): Check microphone & speakers if planning Session 4 voice demo

---

## ⚠️ Key Risks & Mitigations

| Risk | Impact | Mitigation |
|:--|:--|:--|
| Gaming PC GPU driver not set up | Sessions 2 & 3 slow | Test `torch.cuda.is_available()` before class; fallback to Colab/NiceGPU per student |
| Model download time in class | Session startup delay | **Pre-download all models before class** (sd-turbo ~4 GB, CIFAR-10 ~170 MB, distilbert ~260 MB) |
| NiceGPU/Colab unfamiliar to students | Onboarding delay | Show 5-min walkthrough in Session 0 if cloud will be used |
| Voice hardware unavailable | Session 4 optional section | Skip voice; core chatbot works without it |
