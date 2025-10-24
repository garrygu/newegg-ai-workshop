# 🎓 Newegg AI Foundations Workshop

> **Transform high school students into AI creators through hands-on coding and creative projects**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🌟 **Course Overview**

The **Newegg AI Foundations Workshop** is a comprehensive 4-session program designed to introduce high school students (ages 13-18) to artificial intelligence through hands-on coding projects. Students build their own **AI Guessing Game** that combines image generation, image classification, and sentiment-aware chatbots.

### 🎯 **Learning Outcomes**
By the end of this workshop, students will:
- ✅ **Understand AI fundamentals** through practical experience
- ✅ **Generate AI images** using text-to-image technology
- ✅ **Train image classifiers** using PyTorch and neural networks
- ✅ **Build sentiment-aware chatbots** with emotion detection
- ✅ **Integrate multiple AI components** into a cohesive game
- ✅ **Develop Python programming skills** through real-world projects
- ✅ **Gain confidence in AI technology** and its applications

---

## 📚 **Course Structure**

| Session | Duration | Theme | Core Skills | Deliverable |
|:--:|:--:|:--|:--|:--|
| **0** | 2 hours | 🧰 Setup & Orientation | Jupyter basics, AI concepts, Python fundamentals | "Hello AI World!" test notebook |
| **1** | 2 hours | 🎨 Image Generation | Text-to-image AI, prompt engineering, Stable Diffusion | 3-5 custom images in `game_assets/` |
| **2** | 2 hours | 🧠 Train a Classifier | Neural networks, model training, PyTorch, CIFAR-10 | `models/classifier.pt` |
| **3** | 2 hours | 💬 Chatbot & Sentiment | Natural language processing, emotion detection, chatbots | Sentiment-aware chatbot |
| **4** | 2 hours | 🎮 AI Guessing Game | Game development, AI integration, project completion | Playable AI game + demo |
| **Demo Day** | 2 hours | 🌟 Showcase & Reflection | Presentation skills, peer feedback, certificates | Team presentations + awards |

---

## 🚀 **Quick Start**

### **For Students**
1. **Clone this repository**: `git clone https://github.com/garrygu/newegg-ai-workshop.git`
2. **Open Jupyter Notebook** (local or Google Colab)
3. **Start with Session 0**: `Session_0_Setup_and_Orientation.ipynb`
4. **Follow the sessions in order**: 0 → 1 → 2 → 3 → 4
5. **Celebrate your AI game** at Demo Day!

### **For Instructors**
1. **Review instructor materials**: Check `instructor_guides/` folder
2. **Prepare environment**: Verify GPU access and required libraries
3. **Test all notebooks**: Ensure smooth execution before class
4. **Use teaching guides**: Follow `Instructor_Kit.md` for detailed lesson plans

---

## 📖 **Session Details**

### 🧰 **Session 0: Setup & Orientation**
**Goal**: Get everyone comfortable with coding and AI concepts

**What Students Learn**:
- How to use Jupyter Notebooks
- Basic Python programming (variables, loops, functions)
- What AI really means and how it works
- GPU vs CPU for AI processing
- Introduction to datasets, models, and training

**Key Activities**:
- Interactive Python exercises
- GPU detection and setup
- "Hello AI World!" programming
- AI concept discussions

**Deliverable**: Working Python environment with AI understanding

---

### 🎨 **Session 1: Image Generation**
**Goal**: Create unique AI-generated images using text prompts

**What Students Learn**:
- How text-to-image AI works (Stable Diffusion)
- Prompt engineering techniques
- Image generation libraries (`diffusers`, `transformers`)
- Ethical AI image creation
- File management and organization

**Key Activities**:
- Generate images from text descriptions
- Experiment with different prompt styles
- Save images for game assets
- Explore AI creativity boundaries

**Deliverable**: 3-5 custom AI-generated images in `game_assets/` folder

---

### 🧠 **Session 2: Train a Classifier**
**Goal**: Teach computers to "see" and recognize images

**What Students Learn**:
- How image classification works
- Neural networks and CNNs (Convolutional Neural Networks)
- PyTorch framework for deep learning
- Training vs testing data
- Model accuracy and evaluation

**Key Activities**:
- Load and explore CIFAR-10 dataset
- Train a ResNet18 model
- Monitor training progress
- Evaluate model performance
- Visualize results and errors

**Deliverable**: Trained image classifier saved as `models/classifier.pt`

---

### 💬 **Session 3: Chatbot & Sentiment**
**Goal**: Build AI that understands emotions and responds appropriately

**What Students Learn**:
- Natural language processing basics
- Sentiment analysis techniques
- Rule-based vs machine learning approaches
- Hugging Face Transformers library
- Chatbot design principles

**Key Activities**:
- Create rule-based chatbot responses
- Implement sentiment analysis
- Combine emotion detection with responses
- Test chatbot interactions
- Design AI personality

**Deliverable**: Sentiment-aware chatbot with emotional responses

---

### 🎮 **Session 4: AI Guessing Game**
**Goal**: Combine all AI components into an interactive game

**What Students Learn**:
- Game development concepts
- AI component integration
- User interaction design
- Project completion skills
- Debugging and testing

**Key Activities**:
- Integrate image generation, classification, and chatbot
- Create game loop and scoring system
- Add personality and difficulty levels
- Test and refine gameplay
- Prepare for demonstration

**Deliverable**: Complete AI-powered guessing game

---

## 🛠️ **Technical Requirements**

### **Software Requirements**
- **Python 3.8+** with Jupyter Notebook
- **PyTorch 2.0+** for deep learning
- **Google Colab** or **NiceGPU** (recommended for GPU access)
- **Required Libraries**: `torch`, `torchvision`, `transformers`, `diffusers`, `matplotlib`, `PIL`

### **Hardware Requirements**
- **GPU recommended** (CUDA-compatible) for faster training
- **Minimum 8GB RAM** for model training
- **Stable internet connection** for downloading models and datasets

### **Installation**
```bash
# Install required packages
pip install torch torchvision transformers diffusers matplotlib pillow

# Or use the provided requirements file
pip install -r UI/requirements.txt
```

---

## 📁 **Project Structure**

```
newegg-ai-workshop/
├── 📚 Session Notebooks
│   ├── Session_0_Setup_and_Orientation.ipynb
│   ├── Session_1_Image_Generation_Beginner_Final.ipynb
│   ├── Session_2_Train_Classifier_Beginner_Final.ipynb
│   ├── Session_3_Chatbot_Sentiment_Beginner_Final.ipynb
│   └── Session_4_AI_Guessing_Game_Beginner_Final.ipynb
├── 👩‍🏫 Instructor Materials
│   ├── instructor_guides/
│   │   ├── Instructor_Checklist.md
│   │   ├── Instructor_Kit.md
│   │   └── Session-specific guides
├── 📖 Documentation
│   ├── docs/
│   │   ├── Course_Roadmap.md
│   │   └── Workshop flyers
├── 🎮 Game Assets
│   ├── game_assets/          # AI-generated images
│   └── models/              # Trained classifiers
├── 🌐 Web Interface
│   └── UI/                  # Streamlit web app
└── 📊 Data
    └── data/                # CIFAR-10 dataset
```

---

## 🎯 **Learning Philosophy**

### **Hands-On Learning**
- **Learn by doing**: Students code from day one
- **Progressive complexity**: Each session builds on previous knowledge
- **Real-world applications**: Every skill connects to practical uses

### **Beginner-Friendly Approach**
- **No prior coding experience required**
- **Clear explanations** with analogies and examples
- **Expandable sections** for deeper learning
- **Multiple learning styles** supported

### **Creative Expression**
- **Artistic freedom** in image generation
- **Personalized chatbots** with unique personalities
- **Custom game themes** and mechanics
- **Celebration of creativity** over perfection

---

## 🌟 **Special Features**

### **Comprehensive Educational Content**
- **Detailed explanations** for every code block
- **Library breakdowns** with purpose and origin
- **Visual diagrams** showing AI processes
- **Real-world analogies** for complex concepts
- **Expandable resources** for continued learning

### **Professional-Grade Tools**
- **Industry-standard libraries**: PyTorch, Hugging Face, Diffusers
- **Modern AI models**: Stable Diffusion, Transformers
- **Best practices**: Proper code structure and documentation
- **Scalable architecture**: Easy to extend and modify

### **Complete Instructor Support**
- **Detailed lesson plans** with timing and activities
- **Troubleshooting guides** for common issues
- **Backup plans** for technical difficulties
- **Assessment rubrics** and progress tracking
- **Certificate templates** for student recognition

---

## 🎮 **Final Project: AI Guessing Game**

Students create a complete AI-powered guessing game that:

1. **🎨 Generates Images**: Uses AI to create visual clues
2. **🧠 Recognizes Objects**: Classifies images using trained models
3. **💬 Understands Emotions**: Responds to player sentiment
4. **🎯 Provides Feedback**: Gives hints based on player reactions
5. **🎮 Creates Engagement**: Combines all AI components into fun gameplay

### **Game Features**
- **Multi-modal AI**: Combines vision, language, and emotion
- **Adaptive difficulty**: Adjusts based on player performance
- **Personality-driven**: AI responds with unique character
- **Educational value**: Teaches AI concepts through play
- **Scalable design**: Easy to extend with new features

---

## 🏆 **Success Stories**

> *"This workshop completely changed how I think about AI. I went from being intimidated by technology to building my own AI game!"* - Sarah, 16

> *"The hands-on approach made everything click. I finally understand how AI actually works!"* - Marcus, 17

> *"Creating my own AI images was amazing. I never thought I could be an AI artist!"* - Aisha, 15

---

## 🤝 **Contributing**

We welcome contributions to make this workshop even better!

### **How to Contribute**
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-improvement`
3. **Make your changes** and test thoroughly
4. **Commit your changes**: `git commit -m 'Add amazing improvement'`
5. **Push to the branch**: `git push origin feature/amazing-improvement`
6. **Open a Pull Request**

### **Areas for Contribution**
- **New session topics** (e.g., audio AI, robotics)
- **Additional languages** (Spanish, Chinese, etc.)
- **Accessibility improvements** (screen readers, keyboard navigation)
- **Advanced extensions** (web deployment, mobile apps)
- **Assessment tools** (quizzes, progress tracking)

---

## 📞 **Support & Community**

### **Getting Help**
- **📧 Email**: [garrygu@newegg.com](mailto:garrygu@newegg.com)
- **🐛 Issues**: [GitHub Issues](https://github.com/garrygu/newegg-ai-workshop/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/garrygu/newegg-ai-workshop/discussions)

### **Community Resources**
- **📚 Documentation**: Comprehensive guides in `/docs`
- **🎥 Video Tutorials**: Coming soon!
- **👥 Instructor Network**: Connect with other educators
- **🏆 Student Showcase**: Share your AI creations

---

## 📄 **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **Newegg** for supporting AI education initiatives
- **Hugging Face** for providing open-source AI models
- **PyTorch Team** for the amazing deep learning framework
- **Stability AI** for Stable Diffusion image generation
- **All contributors** who help make this workshop better

---

## 🚀 **What's Next?**

After completing this workshop, students are ready to:
- **🎓 Pursue AI/ML courses** in college
- **💼 Explore AI careers** in tech companies
- **🔬 Conduct AI research** projects
- **🚀 Build advanced AI applications**
- **🌟 Become AI advocates** in their communities

---

**Ready to start your AI journey? Begin with [Session 0: Setup & Orientation](Session_0_Setup_and_Orientation.ipynb)!** 🎉

---

*© 2025 Newegg AI Workshop. Developed with ❤️ for the next generation of AI creators.*