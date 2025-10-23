# ✅ Newegg AI Workshop — Instructor Quick Checklist
> One-page guide for classroom use  
> (Covers Sessions 0–4 + Demo Day)

---

## 🧰 Before Class (Daily Prep)
| ✔ | Task |
|:--:|:--|
| ☐ | Confirm classroom Wi-Fi and power access |
| ☐ | Projector or big screen connected |
| ☐ | All notebooks open and tested |
| ☐ | CIFAR-10 dataset accessible or cached |
| ☐ | API keys (if using Stable Diffusion / OpenAI) ready |
| ☐ | GPU or Colab environment verified |
| ☐ | Certificates printed (for final session) |
| ☐ | Demo videos or fallback outputs loaded |
| ☐ | Attendance sheet & name tags ready |

---

## 🗓️ Session-by-Session Snapshot

| Session | Duration | Goal | Expected Output | Plan B (If GPU/API fails) |
|:--:|:--:|:--|:--|:--|
| **0** | 2h | Environment setup + AI intro | `Hello AI World! 🧠` | Use local Jupyter instead of Colab |
| **1** | 2h | Text-to-image generation | 3–5 PNG images in `game_assets/` | Show cached or HuggingFace samples |
| **2** | 2h | Train image classifier | `models/classifier.pt` (~60% accuracy) | Load pre-trained model |
| **3** | 2h | Chatbot + sentiment logic | Console chat output with emotions | Use rule-based fallback |
| **4** | 2h | Combine all into game | Playable guessing game | Use mock classifier outputs |
| **Demo** | 2h | Showcase & reflection | Team presentations + certificates | Play cached demo video |

---

## ⚙️ Common Troubleshooting

| Issue | Quick Fix |
|:--|:--|
| `ModuleNotFoundError` | `!pip install <package>` |
| GPU not detected | `Runtime → Change runtime → GPU` |
| Model load error | Re-run cell with correct file path |
| CIFAR download fail | Provide local copy via USB |
| Notebook frozen | Kernel → Restart and clear output |
| API quota exceeded | Use offline or cached results |

---

## 🧩 Student Progress Checkpoints

| Stage | Student Can... | Verification |
|:--|:--|:--|
| After Session 0 | Run a notebook cell | `print("Hello AI World!")` output |
| After Session 1 | Generate and save AI images | Images exist in `/game_assets/` |
| After Session 2 | Train model + plot accuracy | `.pt` file saved + chart shown |
| After Session 3 | Run chatbot with sentiment | Text conversation output visible |
| After Session 4 | Combine model + chatbot | Full AI guessing game plays |
| After Demo Day | Present and reflect | Certificates distributed |

---

## 💡 Quick Reminders

| Category | Tip |
|:--|:--|
| **Timing** | 10–15 min lecture + 45–60 min coding + 10 min recap |
| **Pacing** | Help students type, not copy-paste — understanding > speed |
| **Encouragement** | Celebrate small wins (“Great prompt!”, “That’s a cool idea!”) |
| **Backup Plan** | Always have offline outputs to keep class moving |
| **Safety & Ethics** | Reinforce respectful prompts and positive AI use |
| **Engagement** | Ask open questions: “What do you think the model is seeing?” |

---

## 🧑‍🏫 End-of-Day Tasks
| ✔ | Task |
|:--:|:--|
| ☐ | Save all student notebooks |
| ☐ | Upload selected outputs for demo |
| ☐ | Collect feedback (QR survey link) |
| ☐ | Clean workspace and shut down PCs |
| ☐ | Note any issues for next session |

---

### 🪄 Contact & Credits
**Developed by:** Garry Gu  
**Repo:** [garrygu/newegg-ai-workshop](https://github.com/garrygu/newegg-ai-workshop)  
**Version:** v1.0 (Instructor Quick Reference)  
