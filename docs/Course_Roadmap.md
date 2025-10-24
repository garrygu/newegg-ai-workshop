# 🧭 Newegg AI Workshop — Course Roadmap  
**Audience:** High-school students (ages 13–18) with little or no coding experience  
**Format:** 4 sessions (2 hours each) + optional Demo Day  
**Platform:** Jupyter / Colab / NiceGPU  
**Languages:** Python + PyTorch + basic AI concepts  
**Outcome:** Students build their own **AI Guessing Game** integrating image generation, classification, and chatbot sentiment.  

---

## 🗓️ Session Overview

| Session | Theme | Core Skills | Deliverable |
|:--:|:--|:--|:--|
| **0** | Setup + Orientation 🧰 | Jupyter basics, intro to AI & datasets | “Hello AI World!” test notebook |
| **1** | Image Generation 🎨 | Prompt engineering, Stable Diffusion | 3–5 custom images in `game_assets/` |
| **2** | Train a Classifier 🧠 | Model training (ResNet18), dataset handling | `models/classifier.pt` |
| **3** | Chatbot & Sentiment 💬 | Rule-based vs ML, text processing | Mini-chatbot detecting mood |
| **4** | AI Guessing Game 🎮 | Game loop integration, teamwork | Playable AI game + demo |
| **Demo Day (optional)** | Showcase 🌟 | Presentation & reflection | Certificate + Leaderboard |

---

## 🏗️ Detailed Session Plans

### Session 0 – Setup & Orientation 🧰
**Goal:** Get everyone running code and understanding what “AI” means.  
**Students will learn to …**
- Open and run Jupyter / Colab.  
- Understand datasets, models, and training concepts.  
- Run a first cell printing `Hello AI World!`.  

**Instructor Checklist**
- 3 intro slides: *What is AI → How computers learn → AI in daily life*.  
- Verify GPU availability and file structure.  
- Optional icebreaker: “Guess what AI made this image?”  

**Mini-Challenge 💡**
> Change the printed text color, font, or emoji output.  

---

### Session 1 – Image Generation 🎨
**Goal:** Create unique AI-generated images.  

**Students will learn to …**
- Understand text-to-image concept.  
- Generate and refine images using Stable Diffusion.  
- Save results to `game_assets/`.  

**Instructor Tips**
- Use Stable Diffusion Lite or OpenAI Image API for speed.  
- Emphasize safe & respectful prompt use.  

**Mini-Challenges**
- 🐶 Create an animal wearing sunglasses.  
- 👾 Make a self-portrait in anime style.  
- 📖 Bonus: a 3-image story sequence.  

---

### Session 2 – Train a Classifier 🧠
**Goal:** Teach computers to “see.”  

**Students will learn to …**
- Load and explore the CIFAR-10 dataset.  
- Train a ResNet18 model and measure accuracy.  
- Save a trained model to `models/classifier.pt`.  

**Instructor Tips**
- Show GPU vs CPU timing differences.  
- Visualize misclassified images and confusion matrix.  

**Mini-Challenges**
- 🎯 Reach > 60 % accuracy.  
- 🧩 Add a new custom class.  
- 🔍 Display 5 misclassified samples.  

---

### Session 3 – Chatbot & Sentiment 💬
**Goal:** Build AI that “talks” and “feels.”  

**Students will learn to …**
- Create a rule-based chatbot.  
- Detect sentiment with simple logic or Hugging Face pipeline.  

**Instructor Tips**
- Discuss good vs bad AI responses.  
- Relate back to the final game: “Your AI should react nicely.”  

**Mini-Challenges**
- 😊 Add a new emotion (e.g., surprise).  
- 🤖 Make different responses when sad.  
- 🧠 Bonus: try a transformer model.  

---

### Session 4 – AI Guessing Game 🎮
**Goal:** Combine everything into a fun game.  

**Students will learn to …**
- Integrate generated images, classifier, and chatbot.  
- Create a game loop (show image → player guess → AI respond).  
- Adjust scoring and difficulty.  

**Instructor Tips**
- Start from scaffolded notebook.  
- Encourage themes and teamwork.  

**Mini-Challenges**
- ⏱️ Add a timer or sound effects.  
- 🧑‍🤝‍🧑 Implement leaderboard.  
- 🔮 Chatbot gives hints based on sentiment.  

---

### Demo Day 🌟 (optional)
**Goal:** Celebrate learning and reflect.  

**Activities**
1. Team demos (5 min each).  
2. Voting for *Most Creative AI* & *Best Teamwork*.  
3. Certificate presentation.  
4. Reflection discussion – “How will AI shape your future?”  

---

## 📚 Supporting Folders

| Folder | Contents | Purpose |
|:--|:--|:--|
| `/docs` | Syllabus, slides, roadmap (this file) | Reference |
| `/instructor_guides` | Timing, troubleshooting, outputs | Teaching support |
| `/game_assets` | Sample images + sound | Demo assets |
| `/UI` | Optional Streamlit/Gradio interface | Future web version |
| `/data` | CIFAR-10 subset | Faster training |
| `/certificates` | Templates | Motivation |

---

## 🧠 Teaching Framework

| Phase | Focus | Example |
|:--|:--|:--|
| Engage | Spark curiosity | “Can AI draw a cat wearing a hat?” |
| Explore | Run code and observe | Notebook hands-on |
| Explain | Discuss concept | Instructor debrief |
| Elaborate | Extend idea | Mini-challenge |
| Evaluate | Reflect | Peer feedback |

---

## 🧩 Optional Extensions

| Track | Add-on | Description |
|:--|:--|:--|
| Intermediate | Fine-tune classifier | Use own images + retrain |
|  | Text-to-speech | Add voice to chatbot |
|  | Web game | Convert to Streamlit app |
| Ethics & Impact | AI Bias & Fairness | 10 min reflection |
| Mentor Corner | Career Q&A | Invite Newegg engineers |

---

## 🪄 Instructor Tips
- Timebox each concept (20–30 min max).  
- Encourage creativity > accuracy.  
- Prepare offline fallbacks (cached outputs).  
- Take photos for social media & flyers.  
- Emphasize safe and positive AI use.  

---

## 📈 Learning Outcomes

| Area | Students can … |
|:--|:--|
| AI Literacy | Explain train/test/infer cycle |
| Python Skills | Modify loops and functions |
| Teamwork | Collaborate and present |
| Creativity | Design unique AI outputs |
| Ethics | Recognize bias & limitations |

---

## 🚀 Next Steps
1. Add this file as `docs/Course_Roadmap.md`.  
2. Unify `requirements.txt` + optional Colab links.  
3. Add PDF slides and mentor guides.  
4. Plan Demo Day and certificate templates.  
5. Promote with flyer + Newegg social posts.  

---
