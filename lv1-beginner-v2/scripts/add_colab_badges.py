"""
Add "Open in Colab" badge as the first markdown cell in each session notebook.
Run once from the lv1-beginner-v2 directory.
"""
import json
from pathlib import Path

GITHUB_USER = "garrygu"
GITHUB_REPO = "newegg-ai-workshop"
GITHUB_BRANCH = "main"
NOTEBOOK_DIR = "lv1-beginner-v2"

notebooks = [
    "Session_0_Setup_and_AI_Fundamentals.ipynb",
    "Session_1_Prompt_Engineering_LLMs.ipynb",
    "Session_2_Image_Generation.ipynb",
    "Session_3_Image_Classification.ipynb",
    "Session_4_Chatbot_Sentiment_Voice.ipynb",
    "Session_5_AI_Game_and_Agents.ipynb",
]

base_url = (
    f"https://colab.research.google.com/github/"
    f"{GITHUB_USER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{NOTEBOOK_DIR}"
)

badge_cell_template = (
    "[![Open In Colab]"
    "(https://colab.research.google.com/assets/colab-badge.svg)]"
    "({url})"
)

script_dir = Path(__file__).parent

for nb_name in notebooks:
    path = script_dir / nb_name
    if not path.exists():
        print(f"  ⚠️  Not found: {nb_name}")
        continue

    nb = json.loads(path.read_text(encoding="utf-8"))

    colab_url = f"{base_url}/{nb_name}"
    badge_md = badge_cell_template.format(url=colab_url)

    badge_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [badge_md]
    }

    # Check if badge already exists in the first cell
    first_cell = nb["cells"][0] if nb["cells"] else None
    if first_cell and first_cell.get("cell_type") == "markdown":
        src = "".join(first_cell.get("source", []))
        if "colab-badge.svg" in src:
            print(f"  ✅ Badge already present: {nb_name}")
            continue

    nb["cells"].insert(0, badge_cell)
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"  ✅ Badge added: {nb_name}")

print("\nDone! Commit and push to make Colab links live.")
