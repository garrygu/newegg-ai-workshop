import json
import os
import urllib.parse
from pathlib import Path

GITHUB_USER = "garrygu"
GITHUB_REPO = "newegg-ai-workshop"
GITHUB_BRANCH = "main"

# Directories to process
TARGET_DIRS = [
    "lv0-explorer",
    "lv0-explorer-v2",
    "lv1-beginner",
    "lv1-beginner-v2",
    "lv2-intermediate",
    "lv3-advanced",
    "lv4-expert"
]

BADGE_TEMPLATE = (
    "[![Open In Colab]"
    "(https://colab.research.google.com/assets/colab-badge.svg)]"
    "({url})"
)

def add_badge_to_notebook(notebook_path):
    # Construct the GitHub URL
    # notebook_path is relative to the repo root
    relative_path = os.path.relpath(notebook_path, ".")
    encoded_path = urllib.parse.quote(relative_path)
    colab_url = f"https://colab.research.google.com/github/{GITHUB_USER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{encoded_path}"
    badge_md = BADGE_TEMPLATE.format(url=colab_url)

    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except Exception as e:
        print(f"Error reading {notebook_path}: {e}")
        return

    if not nb.get("cells"):
        print(f"No cells in {notebook_path}")
        return

    # Check if badge already exists in the first cell
    first_cell = nb["cells"][0]
    if first_cell.get("cell_type") == "markdown":
        source = "".join(first_cell.get("source", []))
        if "colab-badge.svg" in source:
            # Update the source if it's already a badge cell
            first_cell["source"] = [badge_md + "\n"]
            print(f"Updated badge in {notebook_path}")
            # Write back
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return

    # Create new badge cell
    badge_cell = {
        "cell_type": "markdown",
        "id": "colab-badge",
        "metadata": {},
        "source": [badge_md + "\n"]
    }

    # Insert at the beginning
    nb["cells"].insert(0, badge_cell)

    try:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"Added badge to {notebook_path}")
    except Exception as e:
        print(f"Error writing {notebook_path}: {e}")

def main():
    repo_root = Path(".")
    for target in TARGET_DIRS:
        target_path = repo_root / target
        if not target_path.exists():
            continue
        
        for root, dirs, files in os.walk(target_path):
            # Skip .ipynb_checkpoints
            if ".ipynb_checkpoints" in root:
                continue
                
            for file in files:
                if file.endswith(".ipynb"):
                    add_badge_to_notebook(os.path.join(root, file))

if __name__ == "__main__":
    main()
