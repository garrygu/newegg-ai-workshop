import json
import os

NOTEBOOK_PATH = "lv1-beginner-v2/Session 6/Session_6_The_Ultimate_AI_Game_Student_v2.ipynb"

SETUP_CELL_SOURCE = [
    "# 🛠️ Setup: Install required libraries and fix version conflicts\n",
    "!pip install --quiet --upgrade gtts typer click gradio openai\n",
    "\n",
    "# ⚠️ IMPORTANT: In Colab, you MUST restart the session after installing libraries\n",
    "from IPython.display import clear_output, display, HTML\n",
    "clear_output()\n",
    "display(HTML(\"\"\"\n",
    "<div style='background-color: #ffe6e6; padding: 15px; border-radius: 5px; border: 1px solid #ff4d4d;'>\n",
    "    <h3 style='color: #cc0000; margin-top: 0;'>⚠️ Action Required: Restart Runtime</h3>\n",
    "    <p>Libraries (including OpenAI SDK) have been updated. To avoid <b>ImportErrors</b>, you <b>must</b> restart the session:</p>\n",
    "    <ol>\n",
    "        <li>Go to the top menu: <b>Runtime</b> &rarr; <b>Restart session</b></li>\n",
    "        <li>Then run the cells again starting from the imports!</li>\n",
    "    </ol>\n",
    "</div>\n",
    "\"\"\"))"
]

def fix_notebook():
    if not os.path.exists(NOTEBOOK_PATH):
        print(f"File not found: {NOTEBOOK_PATH}")
        return

    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    modified = False

    # 1. Update or Insert Setup Cell
    setup_exists = False
    for cell in nb.get("cells", []):
        if cell.get("id") == "setup-fix":
            cell["source"] = SETUP_CELL_SOURCE
            setup_exists = True
            modified = True
            break
    
    if not setup_exists:
        setup_cell = {
            "cell_type": "code",
            "execution_count": None,
            "id": "setup-fix",
            "metadata": {},
            "outputs": [],
            "source": SETUP_CELL_SOURCE
        }
        if len(nb["cells"]) > 0:
            nb["cells"].insert(1, setup_cell)
        else:
            nb["cells"].append(setup_cell)
        modified = True

    # 2. Migration and Layout
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            source = "".join(cell.get("source", []))
            
            # OpenAI Migration
            if "import google.generativeai as genai" in source:
                source = source.replace("import google.generativeai as genai", "from openai import OpenAI")
                modified = True
            
            if "GOOGLE_API_KEY" in source:
                source = source.replace("GOOGLE_API_KEY", "OPENAI_API_KEY")
                source = source.replace("genai.configure(api_key=OPENAI_API_KEY)", "")
                source = source.replace("chat_model = genai.GenerativeModel('gemini-1.5-flash')", "client = OpenAI(api_key=OPENAI_API_KEY)")
                source = source.replace("chat_model = None", "client = None")
                modified = True
                
            if "response = chat_model.generate_content(prompt)" in source:
                openai_logic = """response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()"""
                source = source.replace("response = chat_model.generate_content(prompt)\n    return response.text.replace('*', '').strip()", openai_logic)
                modified = True

            # Gradio Layout and Compatibility
            if "gr.Blocks(theme=gr.themes.Soft())" in source:
                source = source.replace("gr.Blocks(theme=gr.themes.Soft())", "gr.Blocks()")
                if "demo.launch(" in source:
                    if "theme=" not in source:
                        source = source.replace("demo.launch(", "demo.launch(theme=gr.themes.Soft(), ")
                modified = True

            if "with gr.Column():" in source:
                source = source.replace("with gr.Column():", "with gr.Column(scale=1):")
                if "score_display =" in source and "with gr.Group():" not in source:
                    source = source.replace("score_display =", "with gr.Group():\n                score_display =")
                modified = True

            if "demo.launch(" in source and "share=True" not in source:
                if "share=False" in source:
                    source = source.replace("share=False", "share=True")
                else:
                    source = source.replace("demo.launch(", "demo.launch(share=True, ")
                modified = True
            
            if modified:
                cell["source"] = [line + ("\n" if not line.endswith("\n") else "") for line in source.splitlines()]

    if modified:
        with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"Successfully updated {NOTEBOOK_PATH}")
    else:
        print(f"No changes needed for {NOTEBOOK_PATH}")

if __name__ == "__main__":
    fix_notebook()
