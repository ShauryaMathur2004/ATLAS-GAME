import tkinter as tk
from tkinter import messagebox
import pandas as pd
from PIL import Image, ImageTk, ImageSequence
import sys
import os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS  # PyInstaller creates this
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


df = pd.read_excel(resource_path("finalall.xlsx"))
places = df[df.columns[0]].dropna().astype(str).str.strip().str.title().unique().tolist()
used = []
last_bot_place = None  

def is_valid(place):
    return place.title() in places and place.title() not in used

def get_bot_response(user_input):
    last_letter = user_input.strip()[-1].lower()
    for place in places:
        if place.lower().startswith(last_letter) and place not in used:
            return place
    return None

def play():
    global last_bot_place
    user_input = entry.get().strip().title()
    
    if not user_input:
        messagebox.showinfo("Error", "Enter a place!")
        return

    if not is_valid(user_input):
        messagebox.showinfo("Invalid", f"'{user_input}' is not valid or already used.")
        return

    if last_bot_place:
        expected_start = last_bot_place[-1].lower()
        if user_input[0].lower() != expected_start:
            messagebox.showinfo("Wrong Letter", f"❌ '{user_input}' must start with '{expected_start.upper()}' (last letter of '{last_bot_place}')")
            return

    used.append(user_input)
    log.insert(tk.END, f"You: {user_input}")

    bot_response = get_bot_response(user_input)
    if bot_response:
        used.append(bot_response)
        log.insert(tk.END, f"Bot: {bot_response}")
        log.yview_moveto(1)
        last_bot_place = bot_response
    else:
        log.insert(tk.END, "Bot: I give up! You win 🎉")
        log.yview_moveto(1)
        last_bot_place = None
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Atlas Game")
root.geometry("1920x1080")

bg_img = Image.open(resource_path("17499.png"))
bg_img = bg_img.resize((1920, 1080), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)

background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

main_frame = tk.Frame(root, bg="black")
main_frame.pack(pady=20)

gif_image = Image.open(resource_path("Climate Change Earth GIF.gif"))
gif_frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif_image)]
gif_label = tk.Label(main_frame, bg="black")
gif_label.pack()

def update_gif(ind):
    frame = gif_frames[ind]
    gif_label.configure(image=frame)
    ind = (ind + 1) % len(gif_frames)
    root.after(100, update_gif, ind)

update_gif(0)

title_label = tk.Label(main_frame, text="A-T-L-A-S : ATLAS!", font=("Arial Black", 28), fg="white", bg="black")
title_label.pack(pady=10)

entry = tk.Entry(main_frame, font=('Arial', 16), width=40)
entry.pack(pady=10)
entry.bind("<Return>", lambda event: play())

submit_btn = tk.Button(main_frame, text="Submit", font=('Arial', 14), command=play)
submit_btn.pack(pady=5)

log = tk.Listbox(main_frame, width=60, height=20, font=('Courier', 12))
log.pack(pady=10)

root.mainloop()
