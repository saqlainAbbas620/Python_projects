# 🎲 Number Guessing Game (with Dinosaurs & their Friends!)

A fun, interactive command-line guessing game built with Python. Guess the hidden number between 1 and 100 while receiving proximity hints. When you win, a randomly chosen dinosaur will congratulate you!

[![Run on Replit](https://replit.com)](https://replit.com)

---

## ✨ Features
*   **Proximity Tracking:** The game tells you if your guess is "Too High/Low", "High/Low", or "Almost Correct" (within 5 numbers!).
*   **Dynamic ASCII Art:** Displays funny visual messages using `cowsay` and `dinosay`.
*   **Infinite Replayability:** Uses a dynamic game loop that lets you play again to unlock and see all 15 different dinosaur species.

---

## 🛠️ Requirements & Installation

Before running the game, make sure you have Python installed and install the required text-art modules using your terminal:

```bash
pip install cowsay dinosay
```

---

## 🚀 How to Play Local

1. Navigate to your project folder inside your terminal.
2. Run the game script using Python:
   ```bash
   python game.py
   ```
3. Type your numerical guess when prompted.
4. Follow the warm/cold clues to zero in on the secret code.
5. Once you win, choose `Y` to play another round with a different random prehistoric friend, or any other key to exit!

---

## 👥 Meet the Dinosaurs Included:
Every victory screen pulls randomly from a roster of 15 species:
*   `trex` / `tyrannosaurus`
*   `stegosaurus`
*   `triceratops`
*   `brachiosaur`
*   `pterodactyl`
*   ...and many more hidden profiles!
