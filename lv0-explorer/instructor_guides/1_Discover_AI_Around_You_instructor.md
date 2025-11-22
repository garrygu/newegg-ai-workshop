## 🌟 Instructor Guide: Session 1 - Discover AI Around You

This guide is designed for the first 2-hour session of the Explorer Level workshop. The goal is to introduce the core concept of AI and its presence in daily life, focusing on hands-on exploration of popular tools.

### 📚 Materials and Preparation

| Item | Requirement | Notes for Instructor |
| :--- | :--- | :--- |
| **Web Access** | Stable Wi-Fi for all students | Essential for ChatGPT, DeepL, and the Deepfake game. |
| **Projector** | To display the notebook and examples. | Use the provided [1_Discover_AI_Around_You.ipynb](https://github.com/garrygu/newegg-ai-workshop/blob/main/lv0-explorer/1_Discover_AI_Around_You.ipynb) |
| **ChatGPT** | Access to the website | Ensure students can sign up/log in quickly. Use the link provided in the notebook. |
| **DeepL Translator** | Access to the website | Use the link provided in the notebook's [AI Translation & Language](https://github.com/garrygu/newegg-ai-workshop/blob/fe6e3abf5ebe89bbe853d43e55953bfb78b0c71b/lv0-explorer/#translation) section. |
| **Deepfake Game** | Access to the game | Use the link provided in the notebook's [Spot the Fake: AI Deepfakes](https://github.com/garrygu/newegg-ai-workshop/blob/fe6e3abf5ebe89bbe853d43e55953bfb78b0c71b/lv0-explorer/#deepfakes) section. |
| **Warm-up Examples** | Pre-loaded visual/text examples | See the detailed examples below. |
| **Example AI Story** | Pre-made multimedia story (video/slideshow) | Show students what they'll create by the end! See details below. |

---

### 🎬 Opening: Show Example AI Story (5-10 min) - **RECOMMENDED**

**Goal:** Inspire students by showing them what they'll create by the end of the workshop.

**Why This Matters:** Showing the end goal at the beginning helps students:
- Understand the bigger picture
- Stay motivated throughout the sessions
- See how all the pieces (images, videos, voices) come together
- Get excited about the creative possibilities

**What to Show:**
Create or find a **1-2 minute example AI story** that demonstrates:
- ✅ AI-generated images (characters, scenes)
- ✅ AI-generated video/animation
- ✅ AI-generated voice narration
- ✅ Simple story structure (beginning, middle, end)
- ✅ Creative use of AI tools

**📖 Complete Example Story Guide Available:**
See **[Example_AI_Story_Guide.md](./Example_AI_Story_Guide.md)** for a complete, ready-to-use example story called "Luna's AI Adventure" with:
- Full story script and narration
- Scene-by-scene breakdown
- Image prompts for each scene
- Step-by-step creation instructions
- Tools and resources needed

**Example Story Ideas (if creating your own):**
- "A Day in the Life of My AI Helper" — A student's morning routine with an AI assistant
- "Space Adventure with an AI Friend" — A short sci-fi adventure
- "The Art That Came to Life" — An artwork that becomes animated

**How to Present:**
1. **Before class starts:** Have the example story ready to play (video file, slideshow, or online link)
2. **Opening (5-10 min):** 
   - Say: *"By the end of this workshop, you'll create something like this!"*
   - Play/show the example story
   - Ask: *"What AI tools do you think were used to create this?"*
   - Briefly explain: *"We'll learn to create images, videos, and voices with AI, then combine them into your own story!"*
3. **Connect to today:** *"Today, we're starting with the basics — understanding what AI is and how it works. But keep this example in mind — this is where we're heading!"*

**If You Don't Have an Example:**
- You can create a simple one using the tools from later sessions (DALL·E for images, RunwayML for video, ElevenLabs for voice)
- Or show a student example from a previous workshop
- Or skip this and mention the final project goal verbally

**Alternative:** If time is tight, you can mention the final project goal verbally during the welcome/introduction instead of showing a full example.

---

### ⏰ Suggested Schedule (2 Hours)

| Timeframe | Duration | Activity Focus | Goal |
| :--- | :--- | :--- | :--- |
| **00:00 - 00:10** | 10 min | **Welcome & Example Story** | Show example AI story (optional but recommended) and introduce workshop goals. |
| **00:10 - 00:25** | 15 min | What is AI? & Warm-Up | Introduce AI definition and engage students with a quick game. |
| **00:25 - 00:45** | 20 min | AI in Daily Life Exploration | Relate AI to their phones, streaming, and daily activities. **Technical concepts:** Neural Networks (face recognition) and Decision Trees (gaming). |
| **00:45 - 01:15** | 30 min | **Hands-On ChatGPT Session** | The core hands-on activity. Protect this time! |
| **01:15 - 01:30** | 15 min | **BREAK** ☕ | Stretch break. Encourage informal AI discussions. |
| **01:30 - 01:50** | 20 min | Translation & Deepfakes | Show AI's language and authenticity challenges. |
| **01:50 - 02:20** | 30 min | AI for Good Challenge & Reflection | Teamwork activity and final wrap-up discussion. |

---

### 🧠 Technical Concepts Introduced (No Coding Required)

This session introduces **6 key technical concepts** through simple explanations and analogies. Students will encounter these in "🧠 Tech Talk" callout boxes throughout the notebook. Here's what you need to know:

| Concept | Where It Appears | Simple Explanation for Students |
| :--- | :--- | :--- |
| **Machine Learning** | "What is AI" section | AI learns from data/examples instead of being programmed with rules. Like teaching someone to recognize cats by showing thousands of cat photos. |
| **Neural Network** | Face Recognition (Smartphones) | AI sees images as grids of numbers (pixels). Uses layers of math to find patterns: edges → shapes → features (eyes, nose, mouth). Like looking through multiple filters. |
| **Decision Tree** | Gaming AI | Game AI uses a flowchart-like process: Is player visible? → Yes → Is player close? → Yes → Attack! Each question leads to a decision. |
| **Large Language Model (LLM)** | ChatGPT section | AI trained on massive amounts of text. Predicts the next most likely word, building responses one word at a time. Like a super-smart friend who's read everything online. |
| **Natural Language Processing (NLP)** | Translation/Ambiguity section | The challenge of understanding human language: words have multiple meanings, sentences can be ambiguous, context matters. AI uses context clues and patterns to guess meaning. |
| **Generative Adversarial Networks (GANs)** | Deepfakes section | Two AIs compete: Generator creates fake images, Discriminator tries to spot fakes. They train each other, making both better. Like two players practicing together. |

**Instructor Tips:**
- **Don't worry if students ask deeper questions** — it's okay to say "That's a great question! We'll explore that more in later sessions."
- **Use the analogies** from the notebook — they're designed to be accessible.
- **Encourage curiosity** — if a student wants to know more, that's a sign of engagement!
- **Focus on the "what" and "why"** — not the "how" (no coding/math details needed).

---

### 🎭 Activity Guide & Needed Examples

#### 1. Warm-Up: "AI or Human?" (15 min)

**Goal:** Challenge students to immediately use critical thinking to distinguish between human and machine creativity.

**Technical Concept:** After this activity, students will learn about **Machine Learning** in the "What is AI" section — the core way AI learns from data rather than being programmed with rules.

**Instructor Action:** Show the class 3-4 examples (mix of human and AI) and have them vote or write down their guess.

| Example Type | Example Content (Instructor should use) | Correct Answer | Talking Point |
| :--- | :--- | :--- | :--- |
| **Poem** (📝) | *The fog curled white around the oak tree's height,* *A silent, silver blanket in the night.* *No birdsong woke the wood, no breeze did pass,* *Just the soft sigh of dewdrops on the grass.* | **AI** (Generated quickly) | The language is technically perfect but might lack deep emotion or an unusual perspective. |
| **Photo** (🎨) | A clear, detailed photograph of a rusty bicycle leaning against a vibrant, graffiti-covered wall. | **Human** (Taken by a photographer) | Discuss the 'human' choices: framing, selecting the location, and capturing the moment. |
| **Chat Log** (💬) | **Student:** What's the capital of Finland? **Assistant:** The capital of Finland is Helsinki. **Student:** What is the average daily temperature there in November? **Assistant:** The average temperature in Helsinki in November is about 1 to 3 degrees Celsius. | **AI** (Simple, transactional) | This is AI assisting with factual retrieval—fast and accurate, but not creative. |

> Ref: AI Dector Tool: https://gptzero.me/ <br>
> Typical Prompt: "Write a short, four-line rhyming poem about fog at night in the woods."

#### 1.5. AI in Daily Life Exploration (20 min)

**Goal:** Help students recognize AI in their everyday experiences.

**Technical Concepts:** Students will encounter two "🧠 Tech Talk" boxes:
- **Neural Networks** (Face Recognition): Explain that AI sees photos as grids of numbers and uses layers to find patterns. Great analogy: "like looking through multiple filters."
- **Decision Trees** (Gaming): Explain game AI's decision-making process using the flowchart analogy. Students can relate to this if they play games!

**Instructor Action:** 
- Walk through the examples in the notebook (Smartphones, Gaming, etc.)
- When you reach face recognition, pause and read the Neural Network explanation together.
- When you reach gaming, pause and read the Decision Tree explanation together.
- Ask: *"Can you think of other places you've seen AI today?"*

#### 2. Hands-On: ChatGPT Session (30 min)

**Goal:** Ensure every student successfully logs in and interacts with a large language model.

**Technical Concept:** Students will see a "🧠 Tech Talk" box explaining **Large Language Models (LLMs)**. Be prepared to answer questions like "How does it know what to say?" — the simple answer: it predicts the next word based on patterns from training data.

**Instructor Action:** Walk students through the login process. Have them try the following:

* **First Conversation Ideas (5-10 min):**
    * "Tell me a fun fact about space."
    * "What's the best flavor of ice cream?"
    * "Help me plan my perfect weekend"
* **Challenge 1: Dream Vacation Planner (10-15 min):** Have students use the prompt: *"Plan a perfect day for me at [your dream destination]. Include activities, food, and fun things to do!"*
* **Challenge 3: Creative Writing (5-10 min):** Encourage them to iterate on a request, e.g., "Make that story about a robot friend funny," or "Now make the poem rhyme."

#### 3. AI Translation & Deepfake Detection (20 min)

**Goal:** Introduce AI's power and potential for misuse/error.

* **AI Translation (15 min):**
    * Direct students to the [DeepL Translator](https://github.com/garrygu/newegg-ai-workshop/blob/fe6e3abf5ebe89bbe853d43e55953bfb78b0c71b/lv0-explorer/#translation) link in the notebook.
    * **Activity 1 - Basic Translation (5 min):** Have them write 2-3 complex sentences (e.g., using idioms) and translate them to a non-English language (like Spanish or Japanese) and back to English.
    * **Activity 2 - Ambiguity Challenge (10 min):** NEW! Students will explore the ambiguous sentence: *"The man saw the dog with the telescope."* 
        - Ask: *Who had the telescope?* (Both interpretations are possible!)
        - Have them translate it and see which meaning the AI picks.
        - Then add context: *"The astronomer looked through his telescope. The man saw the dog with the telescope."*
        - **Discussion:** *How did adding context help? Why is this hard for AI?*
    * **Technical Concept:** This introduces **Natural Language Processing (NLP)** — the challenge of understanding ambiguous language. Students learn that AI uses context clues to guess meaning.
    * **Discussion:** *What changed? Was the meaning preserved?* (Focus on **cultural context**, **idioms**, and **ambiguity**).
* **Spot the Fake (10 min):**
    * Direct students to the ["Which Face Is Real?" Game](https://github.com/garrygu/newegg-ai-workshop/blob/fe6e3abf5ebe89bbe853d43e55953bfb78b0c71b/lv0-explorer/#deepfakes) link in the notebook.
    * **Activity:** Have them play 5-10 rounds.
    * **Technical Concept:** Students will see a "🧠 Tech Talk" box explaining **Generative Adversarial Networks (GANs)**. The two-AI competition (Generator vs. Discriminator) explains why deepfakes are so realistic.
    * **Discussion:** Ask: *What physical clues did you look for?* (e.g., blurry backgrounds, asymmetrical ears/glasses, strange lighting). Discuss the **importance of media literacy.**

#### 4. AI for Good Challenge (15 min)

**Goal:** Shift the focus from consumption to constructive application of AI.

* **Brainstorming:** Prompt students to ask ChatGPT: *"Give me 5 creative ideas for how AI can help the environment."*
* **Team Challenge:** Divide the class into small groups (3-4 students).
    * **Task:** Choose one AI for Good idea and create a simple, **1-minute pitch** explaining the problem, the AI solution, and the impact.
    * *Time Allocation:* 5 minutes to discuss/choose, 5 minutes to write the pitch, 5-15 minutes for presentations (depending on class size).

---

### 🧠 Reflection and Wrap-up (15 min)

* **Key Question:** *What responsibility do we have when using AI?* (This question ties into the ethics discussions from Deepfakes and AI for Good.)
* **Review:** Quickly recap the main concepts:
    - **What is AI** (and Machine Learning)
    - **AI in Daily Life** (Neural Networks for face recognition, Decision Trees for gaming)
    - **ChatGPT** (Large Language Models)
    - **AI Translation** (Natural Language Processing and ambiguity)
    - **Deepfakes** (Generative Adversarial Networks)
    - **AI for Good** (Ethics and responsibility)
* **Technical Concepts Recap:** You can mention that students learned 6 technical terms today — all without coding! This builds their technical vocabulary while keeping things accessible.
* **Look Ahead:** Tease the next session: **Create with AI Images**.

***