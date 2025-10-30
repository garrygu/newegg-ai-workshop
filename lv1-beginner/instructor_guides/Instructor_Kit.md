📄 **`instructor_guides/Instructor_Kit.md`**
* time allocation per section,
* key learning checkpoints,
* troubleshooting and fallback options,
* expected outputs (screenshots or text placeholders),
* teaching tips and sample dialogues.

---
# 👩‍🏫 Newegg AI Workshop — Instructor Kit
> Comprehensive teaching guide for Sessions 0–4 + Demo Day  
> Designed for beginner-level high school students  

---

## 🧭 Overview

| Item | Details |
|:--|:--|
| **Audience** | High school students (ages 13–18) with little or no coding experience |
| **Goal** | Build understanding of core AI concepts through hands-on activities |
| **Duration** | 4 sessions × 2 hours each + optional Demo Day |
| **Teaching Mode** | Hands-on coding with short explanations |
| **Required Tools** | Jupyter Notebook (local or Colab) + NiceGPU (if available) |

---

## 🗂️ Preparation Checklist

✅ Install environment / test all notebooks  
✅ Verify datasets load properly (CIFAR-10, Stable Diffusion)  
✅ Print attendance list and name tags  
✅ Prepare projector or large screen  
✅ Have backup demo outputs ready (for API or GPU failure)  
✅ Load certificate templates in `/certificates`  
✅ Optional: pre-download notebooks to USB or local folder  

---

## 🧰 Session 0 – Setup & Orientation (2 hrs)

| Phase | Duration | Activity | Instructor Notes |
|:--|:--:|:--|:--|
| Welcome & intro | 10 min | Overview of AI and program | Use slides: *What is AI?* |
| Jupyter basics | 20 min | Explain cells, code vs text | Show a “print(‘Hello AI!’)” example |
| Run test notebook | 20 min | Students try first notebook | Verify GPU / Colab connection |
| Discussion | 15 min | AI in daily life | Encourage sharing (e.g. TikTok, ChatGPT) |
| Mini challenge | 10 min | Customize greeting output | Introduce emoji and print colors |
| Wrap-up | 5 min | Recap key ideas | Review “AI = Data + Model + Task” |

**Expected Output:**  
```

Hello AI World! 🧠

```

**Common Issues**
- *Error: Module not found* → `!pip install <module>`
- *GPU not detected* → use Colab or switch runtime
- *Notebook doesn’t run* → Kernel restart

---

## 🎨 Session 1 – Image Generation (2 hrs)

| Phase | Duration | Activity | Instructor Notes |
|:--|:--:|:--|:--|
| Intro to Generative AI | 15 min | Slides + demo image | Use analogy: “AI = artist with guidance” |
| Prompt design | 15 min | Show how prompts affect results | Compare simple vs detailed prompts |
| Generate images | 40 min | Students create 3–5 images | Save under `game_assets/` |
| Discussion | 15 min | Ethical use of AI images | Highlight copyright & fairness |
| Challenge | 20 min | “Design a poster” task | Encourage creative story concepts |
| Reflection | 5 min | Quick recap | Show 3 favorite images |

**Expected Outputs**
- Folder: `/game_assets/` with 3–5 `.png` files  
- Example: `dog_in_spacesuit.png`

**Plan B (No GPU / API Quota)**
- Use cached images.
- Use online demo (e.g., Hugging Face Spaces).

---

## 🧠 Session 2 – Train a Classifier (2 hrs)

| Phase | Duration | Activity | Instructor Notes |
|:--|:--:|:--|:--|
| Recap + goal | 10 min | “How does AI learn to see?” | Use cat/dog analogy |
| Dataset loading | 20 min | Load CIFAR-10 + preview images | Explain classes |
| Training model | 40 min | Run ResNet18, observe loss/accuracy | Show live accuracy updates |
| Evaluate results | 20 min | Visualize results & misclassifications | “Why do mistakes happen?” |
| Challenge | 20 min | Improve accuracy / add new class | Give hint: adjust epochs |
| Reflection | 10 min | Review model steps | Summarize pipeline: data → model → output |

**Expected Output**
```

Training accuracy: ~60%
Validation accuracy: ~55%

```

**Troubleshooting**
- *Out of memory* → reduce batch size  
- *Dataset not found* → auto-download CIFAR-10  
- *Long runtime* → use pre-trained weights

**Plan B**
- Load a pre-trained model from `/models/classifier.pt`

---

## 💬 Session 3 – Chatbot & Sentiment (2 hrs)

| Phase | Duration | Activity | Instructor Notes |
|:--|:--:|:--|:--|
| Intro | 10 min | “Can AI understand feelings?” | Show real-world chatbot examples |
| Rule-based bot | 30 min | Write `if`/`else` responses | Keep <10 rules for clarity |
| Sentiment detection | 30 min | Introduce positive/negative logic | Optional: Hugging Face model |
| Combine with persona | 20 min | Add emotion-based reply | e.g., Happy → “Yay!”, Sad → “Cheer up!” |
| Challenge | 20 min | Create 5 moods | Test with friends |
| Wrap-up | 10 min | Discussion | “What makes conversation human?” |

**Expected Output Example**
```

User: I failed my test.
Bot: I’m sorry to hear that 😢 You can try again next time!

```

**Common Issues**
- *Input not recognized* → add `.lower()` normalization  
- *RuntimeError for model import* → fallback to rule-based version  

**Plan B**
- Skip Hugging Face model; use static sentiment dictionary.

---

## 🎮 Session 4 – AI Guessing Game (2 hrs)

| Phase | Duration | Activity | Instructor Notes |
|:--|:--:|:--|:--|
| Intro | 10 min | Recap: combine vision + language | Show demo notebook |
| Load assets | 20 min | Import images + model | Review saved checkpoints |
| Build game loop | 40 min | Write game logic | Input guess → AI responds |
| Add chatbot | 20 min | Integrate Session 3 responses | “Great guess!” vs “Try again!” |
| Polish & test | 20 min | Tune difficulty, design layout | Encourage team collaboration |
| Present results | 10 min | Team mini-demo | Celebrate progress! |

**Expected Output Example**
```

AI shows image of a dog
Player: "cat"
Bot: "Not quite! 🐾 Try again!"

```

**Plan B**
- If model not loading: replace classifier with random choice logic.
- Use pre-generated image folder for testing.

---

## 🌟 Demo Day (Optional)

| Phase | Duration | Activity |
|:--|:--:|:--|
| Setup | 10 min | Arrange teams + check displays |
| Team demos | 60 min | Each team presents for 5 min |
| Voting & feedback | 20 min | Peer + mentor votes |
| Certificates | 10 min | Hand out participation awards |
| Wrap-up | 10 min | Group photo + reflection |

**Categories for Voting**
- 🎨 Most Creative Game  
- 🤖 Best AI Personality  
- 🧠 Best Technical Execution  
- ❤️ Audience Favorite  

---

## 💡 Instructor Tips & Best Practices

| Area | Advice |
|:--|:--|
| **Time Management** | Keep lectures ≤10 minutes per concept; focus on coding. |
| **Encourage Creativity** | Allow artistic freedom in prompts and themes. |
| **Pair Programming** | Pair stronger students with beginners for peer learning. |
| **Debugging Culture** | Use “Let’s solve this together!” instead of “You did it wrong.” |
| **Feedback Moments** | Ask: “What surprised you today?” “What was hardest?” |
| **Backup Plan** | Always have demo videos or pre-run outputs ready. |
| **Safety & Ethics** | Reinforce respectful prompt and data usage. |

---

## 🧩 Appendix: Quick Commands

| Task | Command |
|:--|:--|
| Install torch | `!pip install torch torchvision` |
| Install transformers | `!pip install transformers` |
| Check GPU | `!nvidia-smi` |
| Save model | `torch.save(model.state_dict(), 'models/classifier.pt')` |
| Load model | `model.load_state_dict(torch.load('models/classifier.pt'))` |

---

## 📦 Folder Reference

| Folder | Purpose |
|:--|:--|
| `/Session_0_Setup_and_Orientation.ipynb` | Intro to environment |
| `/Session_1_Image_Generation_Beginner_Final.ipynb` | Text-to-image |
| `/Session_2_Train_Classifier_Beginner_Final.ipynb` | Image classification |
| `/Session_3_Chatbot_Sentiment_Beginner_Final.ipynb` | Sentiment & chatbot |
| `/Session_4_AI_Guessing_Game_Beginner_Final.ipynb` | Game integration |
| `/instructor_guides/Instructor_Kit.md` | This file |
| `/docs/Course_Roadmap.md` | Student-facing outline |

---

## 🪄 Future Enhancements
- Add Streamlit UI in `/UI` for web game.  
- Include ethics mini-lesson: “AI and Fairness.”  
- Optional “AI Game Jam” event template.  
- Add QR code link to feedback survey.

---

© 2025 Newegg AI Workshop  
**Developed by:** Garry Gu 