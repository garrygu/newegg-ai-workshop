# 🎓 Newegg YouthAI Program

## **Full Curriculum Specification (Lv0–Lv4)**

**Audience:** Students ages 10–17+
**Format:** In-person, project-based, mentor-guided
**Pedagogical Principle:** *Explore → Build → Understand → Improve → Contribute*

---

## 🧭 Program Design Philosophy

YouthAI is designed as a **progressive pathway**, not isolated workshops.

Each level:

* Has a **clear learner identity**
* Assumes mastery of the previous level
* Produces **tangible, portfolio-ready outcomes**
* Aligns with **real-world AI practice**, not academic abstraction

---

# 📙 Level 0 — Explorer

### *AI Storyteller*

**Recommended Age:** 10–14
**Duration:** 3 sessions (2 hours each)
**Primary Focus:** Understanding AI through creative, no-code experiences

---

## 🎯 Level Objective

By the end of Lv0, students can:

> **Use AI tools to create original stories with text, images, and audio — understanding AI as a creative partner.**

---

## 🧠 Core Learning Themes

### 1. AI as a Creative Tool
* What is AI? (intuitive understanding)
* AI text generation (ChatGPT, Gemini)
* AI image generation (DALL-E, Runway)
* AI audio/voice (TTS, basic audio tools)

### 2. Storytelling with AI
* Planning a narrative
* Creating visual assets
* Assembling multimedia stories
* Presenting and sharing

---

## 🏗️ Lv0 Capstone Project

**Create an AI-powered story** that includes:
* AI-generated script/narrative
* AI-generated images or video
* AI-generated voiceover (optional)
* A complete presentation

---

## 🚫 Explicit Non-Goals (Lv0)
* Writing code
* Understanding model architecture
* API usage
* Training or fine-tuning

---

# 📗 Level 1 — Beginner

### *AI Builder*

**Recommended Age:** 13–16
**Duration:** 6 sessions (2 hours each)
**Primary Focus:** First coding experience through hands-on AI projects

---

## 🎯 Level Objective

By the end of Lv1, students can:

> **Write Python code to use AI APIs, generate images, classify data, and build interactive AI applications.**

---

## 🧠 Core Learning Themes

### 1. Python & Jupyter Fundamentals
* Variables, loops, conditionals
* Jupyter notebook workflow
* Installing and importing libraries

### 2. Prompt Engineering & LLMs
* LLM basics and API usage
* Prompt techniques (zero-shot, few-shot, chain-of-thought)
* Building conversational AI assistants

### 3. AI Image Generation
* Stable Diffusion / text-to-image
* Prompt crafting and negative prompts
* Creating game assets

### 4. Image Classification
* CNN architecture concepts
* Training on CIFAR-10
* Model evaluation and saving

### 5. Chatbots & Sentiment Analysis
* Hugging Face Transformers
* Sentiment-aware responses
* Voice integration (optional)

---

## 🏗️ Lv1 Capstone Project

**Build an AI Guessing Game** that integrates:
* Image generation
* Image classification
* Chatbot interaction
* (Optional) Voice input/output

---

## 🚫 Explicit Non-Goals (Lv1)
* Custom model training from scratch
* Production deployment
* RAG or embeddings
* Multi-agent systems

---

# 📘 Level 2 — Intermediate

### *AI System Builder*

**Recommended Age:** 15+
**Duration:** 6–8 sessions (2 hours each)
**Primary Focus:** Building domain-aware AI systems using modern tooling

---

## 🎯 Level Objective

By the end of Lv2, students can:

> **Design and build an AI assistant that reasons over external knowledge, tools, and data — not just prompts.**

---

## 🧠 Core Learning Themes (Mandatory)

### 1. Retrieval-Augmented Generation (RAG)

* Why LLMs need external knowledge
* Embeddings: intuition and usage
* Vector databases (ChromaDB / Pinecone)
* Chunking, indexing, and retrieval strategies
* Context window management
* Evaluating RAG output quality

### 2. LLM System Design

* Prompt templates vs system prompts
* Tool calling and function usage
* Failure modes (hallucination, context loss)
* Cost, latency, and accuracy tradeoffs

---

## 🧩 Supporting Topics (Limited Scope)

These topics are **introduced conceptually** and used **only if relevant** to the capstone.

* **Fine-tuning (LoRA / QLoRA)**
  *Conceptual overview + guided demo only*
* **AI Agents (Intro)**
  Tool usage, ReAct-style reasoning (single-agent only)
* **Multimodal Inputs (Optional)**
  Vision-language models for document or image grounding

> ⚠️ Lv2 does **not** require students to train models from scratch.

---

## 🏗️ Lv2 Capstone Project

**Build a domain-specific AI assistant** that:

* Uses RAG over a custom dataset
* Explains where its answers come from
* Handles user queries robustly
* Demonstrates safe and responsible AI usage

Examples:

* Study assistant
* Product advisor
* Knowledge-base chatbot

---

## 🚫 Explicit Non-Goals (Lv2)

* Distributed training
* Multi-agent orchestration
* Neural network math
* Production deployment at scale

---

# 📕 Level 3 — Advanced

### *Production AI Engineer*

**Recommended Age:** 16+
**Duration:** 8–10 sessions
**Primary Focus:** Running AI systems reliably in real-world environments

---

## 🎯 Level Objective

By the end of Lv3, students can:

> **Deploy, monitor, and secure AI systems while understanding their operational risks and limitations.**

---

## 🧠 Core Learning Themes

### 1. Model & System Internals (High-Level)

* Transformer architecture (intuition-first)
* Attention and positional encoding (conceptual)
* Model size vs capability tradeoffs

### 2. Training & Optimization (Practical)

* Fine-tuning workflows
* Mixed precision concepts
* Resource-aware training (GPU limits)

> ⚠️ Focus is on *how training behaves*, not math derivations.

---

### 3. MLOps Foundations

* Experiment tracking (MLflow)
* Model versioning
* Model serving (FastAPI / Gradio)
* Monitoring performance and drift

---

### 4. Advanced Agents & Workflows

* Multi-step reasoning
* Simple multi-agent coordination
* Planning vs execution
* When agents fail

---

### 5. AI Safety & Security

* Prompt injection
* Jailbreak patterns
* Data leakage
* Guardrails and policy enforcement

---

## 🏗️ Lv3 Capstone Project

**Deploy a production-style AI application** that includes:

* A served model or AI system
* Monitoring or logging
* Basic security guardrails
* A user-facing interface

Students must explain:

* System architecture
* Failure modes
* Ethical considerations

---

## 🚫 Explicit Non-Goals (Lv3)

* Large-scale distributed clusters
* Training foundation models from scratch
* Advanced reinforcement learning math

---

# 📗 Level 4 — Expert

### *AI Researcher & Open-Source Contributor*

**Recommended Age:** 17+
**Duration:** 10–12 sessions
**Primary Focus:** Research literacy, experimentation, and contribution

---

## 🎯 Level Objective

By the end of Lv4, students can:

> **Read, reproduce, and contribute to cutting-edge AI research responsibly.**

---

## 🧠 Core Learning Themes

### 1. Pre-training Fundamentals (Small Scale)

* Tokenization and vocabularies
* Data curation and filtering
* Training small language models
* Ethics of data sourcing

> ⚠️ Emphasis on *process*, not scale.

---

### 2. Alignment & Control (Conceptual)

* RLHF pipeline overview
* Reward modeling
* PPO / DPO intuition
* Constitutional AI principles

---

### 3. Diffusion & Generative Models

* Intuition behind diffusion
* Latent space manipulation
* ControlNet and IP-Adapter concepts
* Custom model experimentation

---

### 4. Video, Robotics & Embodied AI (Exploratory)

* Video diffusion concepts
* Temporal consistency challenges
* Simulation environments (Isaac Sim)
* Vision–language–action loops

---

### 5. Research Methods

* Reading academic papers
* Reproducing experiments
* Ablation studies
* Responsible reporting

---

### 6. Open Source Contribution

* Hugging Face ecosystem
* Model cards and documentation
* Responsible release practices
* Community collaboration

---

## 🏗️ Lv4 Capstone Project

**Choose one:**

1. Original research mini-project
2. Reproducibility study of a published paper
3. Open-source contribution (code, model, or documentation)

Deliverables:

* Written report
* Demo or code artifact
* Reflection on limitations and ethics

---

## 📊 Skills Progression Matrix (Official)

| Dimension  | Lv0       | Lv1         | Lv2       | Lv3         | Lv4        |
| ---------- | --------- | ----------- | --------- | ----------- | ---------- |
| APIs       | None      | Use         | Embed     | Serve       | Build      |
| Models     | None      | Pre-trained | Fine-tune | Train       | Design     |
| Agents     | None      | Basic       | Tool use  | Multi-agent | Autonomous |
| Vision     | Generate  | Classify    | Detect    | Segment     | Generate   |
| Code       | No code   | Notebooks   | Scripts   | Packages    | Libraries  |
| Deployment | None      | Local       | Gradio    | Docker      | Kubernetes |

---

## 🧩 Governance Principles

* Each level has **hard scope boundaries**
* Projects matter more than exams
* Ethics and responsibility are mandatory at every level
* Advancement is based on **capability**, not age alone

---

## 🏁 One-Line Program Promise

> **YouthAI graduates don’t just use AI — they build, operate, and responsibly advance it.**
