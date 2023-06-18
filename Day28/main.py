import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WINTER = "#213555"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
fg = "#B31312"
marks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():

    window.after_cancel(timer)
    
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    
    global marks
    marks = ""
    check_marks.config(text=marks)
    
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    global marks     
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg="#F2BE22")

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg="#F2BE22")
        marks += "✔"
        check_marks.config(text=marks)

    else:
        count_down(work_sec)
        title_label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = count // 60
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50, bg=WINTER)


title_label = tk.Label(text="Timer",font=(FONT_NAME, 35, "bold"), fg=fg, bg=WINTER)
title_label.grid(column=1, row=0)

tomato_img = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=224, bg=WINTER, highlightthickness=0)
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(103,120, text ="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1) 



start_button = tk.Button(text="Start",font=(FONT_NAME, 15, "bold"), fg=fg, bg=WINTER, command=start_timer)
start_button.grid(column=0 , row=2)

reset_button = tk.Button(text="Reset",font=(FONT_NAME, 15, "bold"), fg=fg, bg=WINTER, command=reset_timer)
reset_button.grid(column=2 , row=2)

check_marks = tk.Label(fg=GREEN, bg=WINTER,font=(FONT_NAME, 15, "bold"))
check_marks.grid(column=1 , row=3)

window.mainloop()