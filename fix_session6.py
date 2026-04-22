import json
import os

NOTEBOOK_PATH = "lv1-beginner-v2/Session 6/Session_6_The_Ultimate_AI_Game_Student_v2.ipynb"

SETUP_CELL = {
    "cell_type": "code",
    "execution_count": None,
    "id": "setup-fix",
    "metadata": {},
    "outputs": [],
    "source": [
        "# 🛠️ Setup: Install required libraries and fix version conflicts\n",
        "!pip install --quiet --upgrade gtts gradio typer click\n",
        "# Clear output to keep it clean\n",
        "from IPython.display import clear_output\n",
        "clear_output()\n",
        "print(\"✅ Libraries installed and conflicts resolved!\")"
    ]
}

def fix_notebook():
    if not os.path.exists(NOTEBOOK_PATH):
        print(f"File not found: {NOTEBOOK_PATH}")
        return

    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Check if setup cell already exists
    for cell in nb.get("cells", []):
        if cell.get("id") == "setup-fix":
            print("Setup cell already exists.")
            return

    # Insert after the colab badge (cell 0)
    if len(nb["cells"]) > 0:
        nb["cells"].insert(1, SETUP_CELL)
    else:
        nb["cells"].append(SETUP_CELL)

    with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print(f"Successfully added setup cell to {NOTEBOOK_PATH}")

if __name__ == "__main__":
    fix_notebook()
