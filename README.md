# US States Guessing Game (Python: `turtle` + `pandas`)

A quick, fun learning game to memorize all 50 U.S. states.  
Type state names into a dialog; each correct guess gets labeled on the map.  
Type **`Exit`** at any time to finish—the game will create **`states_to_learn.csv`** listing the states you missed.

---

## ✨ Features
- Interactive map powered by `turtle`
- Case-insensitive guessing with live labels
- Progress shown in the window title (e.g., `US GAME 3/50`)
- On exit, auto-generates **`states_to_learn.csv`** with remaining states
- Simple, dependency-light code

---

## 📦 Requirements
- Python 3.8+
- `pandas` (install with `pip install pandas`)
- `turtle` is included with standard Python on most platforms

---

## 📁 Project Structure (suggested)
us-states-game/
├─ main.py
├─ 50_states.csv # columns: state,x,y (coords for labeling)
├─ blank_states_img.gif # background map image
├─ states_to_learn.csv # (auto-created after Exit)
└─ assets/
├─ screenshot-gameplay.png
└─ screenshot-missing-csv.png

yaml
Copy code

> **Note:** `50_states.csv` should contain at least the columns `state`, `x`, and `y`.  
> Example row: `Alabama,139,-77`

---

## ▶️ Run
```bash
pip install pandas
python main.py
🕹️ How to Play
A map window opens; a prompt asks for a state name.

Type a state (e.g., Ohio) and press OK.

If correct and not already guessed, its name appears on the map at the proper coordinates.

Continue until you’re done.

Type Exit to stop. The game writes states_to_learn.csv with all the states you didn’t guess—perfect for studying later.

🔄 Core Idea (pseudocode)
text
Copy code
- Load all states from 50_states.csv into a list
- While guessed_count < 50:
    - Ask user for a state name (title-case, strip spaces)
    - If "Exit": break
    - If valid new state:
        - Add to guessed list
        - Move turtle to (x, y) and write the state name
- Compute remaining = all_states - guessed_states
- Save remaining to states_to_learn.csv
🖼️ Screenshots
Gameplay

Auto-generated study list

If you’re using different paths, update the image links above.
You can use the screenshot in this repo or replace with your own.

🧠 Why Exit creates a CSV?
When you type Exit, the script compares:

All states (from 50_states.csv)
vs.

Your correct guesses

The set difference becomes states_to_learn.csv, e.g.:

csv
Copy code
state
Alabama
Delaware
Hawaii
...
🙌 Acknowledgements
Base map: blank_states_img.gif (commonly used in educational projects)

Python standard library: turtle

Data handling: pandas

📜 License
MIT — do whatever you like, just keep the notice.

markdown
Copy code

**Tip:** Save your screenshot(s) as:
- `assets/screenshot-gameplay.png` (the one you shared),
- `assets/screenshot-missing-csv.png` (a cropped image of the generated CSV in your editor),
and the image links in the README will render automatically on GitHub.
