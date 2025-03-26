# 🧠 Tic-Tac-Toe with AI

This is a **Tic-Tac-Toe** project with artificial intelligence, developed in **Python** using **Pygame**. It implements two AI approaches to play against the user:

1. **Minimax Algorithm**
2. **Minimax with Alpha-Beta Pruning** (optimized Minimax)

---

## 📂 Project Structure

```markdown
Ta_Te_Ti-con-IA/
│── TA_TE_TI_con_MIN_MAX.py  # Minimax implementation
│── TA_TE_TI_con_Poda.py      # Minimax + Alpha-Beta Pruning implementation
│── IMG/
│   ├── tablero.png           # Board image
│   ├── cruz.png              # "X" image
│   ├── circulo.png           # "O" image
│── README.md                 # Project documentation
```

---

## 🚀 Installation and Execution

### 1️⃣ Clone the repository
```bash
git clone https://github.com/facuezequielpat/Ta_Te_Ti-con-IA.git
cd Ta_Te_Ti-con-IA
```

### 2️⃣ Install dependencies
Make sure you have **Python 3.x** installed and run:
```bash
pip install pygame
```

### 3️⃣ Run the game
To play with **Minimax**:
```bash
python TA_TE_TI_con_MIN_MAX.py
```
To play with **Minimax + Alpha-Beta Pruning**:
```bash
python TA_TE_TI_con_Poda.py
```

---

## 🎮 How to Play?
- The player is **"X"** and the AI is **"O"**.
- Click on a cell to make your move.
- The AI will automatically respond with its optimal move.
- The winner is the one who aligns 3 symbols (horizontal, vertical, or diagonal).

---

## 🧠 AI Explanation
- **Minimax**: Evaluates all possible moves and selects the best option.
- **Alpha-Beta Pruning**: Improves Minimax performance by eliminating unnecessary branches from the decision tree.

---

## 📌 Notes
- The game uses images (`tablero.png`, `cruz.png`, `circulo.png`), make sure they are in the `IMG/` folder.
- It is recommended to play in a **300x300 pixel** window for better visualization.

---

## 🏆 Credits
Developed by **Facundo Ezequiel Patiño** 🚀

