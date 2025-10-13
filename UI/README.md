# Streamlit Web UI — AI Guessing Game (NiceGPU)

This is a simple Streamlit app that ties together your **game assets**, **image classifier**, and **Game Master** persona.

## Folder Layout (expected)
```
game_project/
  game_assets/            # images generated in Session 1
  models/
    classifier.pt         # saved in Session 2
    classes.txt           # one class name per line
  dialogue/
    persona.txt           # optional persona (Session 3)
  streamlit_app/
    app.py
    requirements.txt
```

## How to Run (on NiceGPU or any GPU machine)
1. Place this `streamlit_app` folder inside your `game_project` (it is already, if you unzipped here).
2. Ensure your assets and model files exist (see structure above).
3. Install requirements (ideally in a fresh virtualenv):
   ```bash
   pip install -r requirements.txt
   ```
4. Launch the app:
   ```bash
   streamlit run app.py
   ```
5. Open the provided local URL in your browser.

## Tips
- If you don't have a trained model yet, the app will still run but guesses are effectively random.
- Update `models/classes.txt` to match the labels you used when training.
- Edit the Game Master persona from the sidebar or by writing to `dialogue/persona.txt`.