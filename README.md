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

![Screenshot 2025-06-06 182610](https://github.com/user-attachments/assets/4e989bce-ea22-40f2-8868-2c7a1f314d70)

> **Important**: Please ensure you use only the `finalall.xlsx` file.  
> Other Excel sheets are partial sources or incomplete and **should not** be used for gameplay.

This file contains a **comprehensive and cleaned list of places** used by both the player and the bot.

---

## 🖥️ Download the Game

🎯 Download the standalone `.exe` file (no installation needed):

👉 [Download Atlas Game (EXE)](https://drive.google.com/file/d/1d9jQ0_ZuLfmgxOdHXsJDICVGm4eABUYt/view?usp=drive_link)

- Just double-click the `.exe` to play.
- No Python installation required.
- All assets are bundled within the file.

> ⚠️ **Windows SmartScreen Warning**:  
> When you run the `.exe`, you may see a warning like “Windows protected your PC.”  
> Click **More info** → **Run anyway** to proceed. This is normal for unsigned apps.

---

## 🛠️ Requirements (for developers)

If you want to run the code manually (not using the `.exe`), make sure the following Python libraries are installed:

```bash
pip install pandas pillow openpyxl
