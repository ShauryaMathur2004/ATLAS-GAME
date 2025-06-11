# 🌍 Atlas Game

A simple and fun word game built with Python and Tkinter where you and the bot take turns naming places. Each new place must start with the last letter of the previous place. Play continues until the bot runs out of options!

---

## 🎮 How to Play

- You enter a **valid place name**.
- The bot responds with another place starting with the **last letter** of your input.
- You and the bot keep alternating turns.
- The same place **cannot be repeated**.
- If the bot can't find a valid place, **you win! 🎉**

---

![Screenshot](https://github.com/user-attachments/assets/4e989bce-ea22-40f2-8868-2c7a1f314d70)

> **Important**: Only the `finalall.xlsx` file is to be used for gameplay.  
> Other Excel sheets are partial or outdated and **should not be used**.

This file contains a **cleaned and complete list of places** for the game.

---

## 🖥️ Download the Game

🎯 Download the `.exe` file (no installation needed):

👉 [Download Atlas Game (EXE)](https://drive.google.com/file/d/1d9jQ0_ZuLfmgxOdHXsJDICVGm4eABUYt/view?usp=drive_link)

- Just **double-click the `.exe`** to play.
- **No Python** or any setup required.
- All required files (`GIF`, `background`, `Excel`) are already bundled.
- The game may take **30–60 seconds to launch**, depending on your system.

> ⚠️ **Windows SmartScreen Warning**:  
> You might see a warning like “Windows protected your PC.”  
> Click **More info** → **Run anyway** to launch the game.  
> This is normal for unsigned apps.

---

## 🛠️ Requirements (for developers)

If you're running the project manually (not using the `.exe`), install dependencies:

```bash
pip install pandas pillow openpyxl
