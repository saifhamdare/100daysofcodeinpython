from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
#---- Timer Reset ----#
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
#---- Timer Mechanism ----#
def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN *60
    long_break_sec= LONG_BREAK_MIN*60
    if reps % 8==0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)
    

#---- Countdown Mechanism ----#
def count_down(count):
    count_min= math.floor(count/60)
    count_sec= count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=(f"{count_min}:{count_sec}"))
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+= "✔"
        check_mark.config(text=marks)

#---- UI Setuo ----#

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
timer_label= Label(text="Timer",bg=YELLOW, fg=GREEN,font=(FONT_NAME,40,"bold"))
timer_label.grid(row=1,column=2)
canvas= Canvas(width=200,height=200,bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomatoo.png.crdownload")
canvas.create_image(99, 95 ,image=tomato_img)
timer_text=canvas.create_text(103,108,text="00:00", fill="white",font=(FONT_NAME,32,"bold"))
canvas.grid(row=2, column=2)

start_button= Button(text="Start",command=start_timer,bg="black",fg=RED,font=(FONT_NAME,10,"bold"))
start_button.grid(row=3,column=1)

Reset_button= Button(text="Reset",command=reset_timer,fg=RED,bg="black",font=(FONT_NAME,10,"normal"))
Reset_button.grid(row=3,column=3)
check_mark= Label(bg=YELLOW, fg=GREEN,font=(FONT_NAME,20,"bold"))
check_mark.grid(row=4,column=2)

window.mainloop()
