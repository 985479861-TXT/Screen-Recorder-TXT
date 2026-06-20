from tkinter import *
import cv2
import numpy as np
from PIL import ImageGrab
import threading
import random

fmt = f"v_op_{random.randint(1, 9000)}"
vpt = f"C:/Users/DELL/Videos/Captures/{fmt}.avi"

window = Tk()
window.geometry("500x200+400+170")
window.resizable(0,0)
window.configure(bg="#030818")
window.title("Screen Recorder")

screen_size = (1366, 768)
recording = threading.Event()

label = Label(window,text="Not recording")
label.place(x=210, y=160)


def recorder():
    label.config(text="Recording Started")
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 20.0
    output = cv2.VideoWriter(vpt, fourcc, fps, screen_size)
    recording.set()
    while recording.is_set():
        img = ImageGrab.grab().resize(screen_size)
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        output.write(frame)
    output.release()
    cv2.destroyAllWindows()
    label.config(text="Recording Stopped")

def start_rec():
    if not recording.is_set():
        threading.Thread(target=recorder).start()

def stop_rec():
    recording.clear()

Label(window, text="SCREEN RECORDER", fg="white", bg="#030818", font=("Helvetica", 23, "bold")).pack()
start = Button(window, text="Start Recording", command=start_rec, bd=0, bg="grey", fg="White", font=("Helvetica", 16, "bold"))
start.place(x=170, y=60)
start.config(bg="red")

stop = Button(window, text="Stop Recording", command=stop_rec, bd=0, bg="grey", fg="White", font=("Helvetica", 16, "bold"))
stop.place(x=170, y=110)

window.mainloop()
