# AI Guessing Game (NiceGPU)

## Overview
Assemble a simple AI game using:
- Stable Diffusion images (Session 1)
- ResNet18 classifier (Session 2)
- Sentiment analysis & a small chatbot (Session 3)
- Game loop (Session 4)

## Steps
1) Put your generated images in `game_assets/`.
2) Place your trained model checkpoint at `models/classifier.pt` and set `num_classes` & `classes` in the notebook.
3) Run the notebook top-to-bottom.
4) Playtest: adjust scoring, rounds, and chatbot persona.
5) Present your demo!

## Tips
- Keep rounds short (5–7 images).
- Replace GPT-2 with an instruction model if allowed on your setup.
- Edit the `classes = [...]` list to match your model's training labels.
