# DRS review system
import tkinter
import cv2  # pip install opencv-python
import PIL.Image, PIL.ImageTk  # pip install pillow
from functools import partial
import threading
import time
import imutils  # pip install imutils

stream = cv2.VideoCapture("clip.mp4")
flag = True


def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag


def pending(decision):
    # 1. display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # 2. wait for one second
    time.sleep(1.5)

    # 3. display sponser image
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(2.5)

    # 4. display out/not out image
    if decision == 'out':
        decisionImg = 'out.png'
    else:
        decisionImg = 'not_out.png'
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not_out",))
    thread.daemon = 1
    thread.start()
    print("player is not out")


# width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368

# TKINTER GUI START HERE

window = tkinter.Tk()
window.title("DECISION REVIEW KIT BY RITU AND RIYAZ")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()

# BUttons to control

btn = tkinter.Button(window, text="<<previous (fast)", width=50, command=partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text="<<previous (slow)", width=50, command=partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text="next(slow)>>", width=50, command=partial(play, 2))
btn.pack()
btn = tkinter.Button(window, text="next(fast)>>", width=50, command=partial(play, 25))
btn.pack()
btn = tkinter.Button(window, text="give out", width=50, command=out)
btn.pack()
btn = tkinter.Button(window, text="give not out", width=50, command=not_out)
btn.pack()

window.mainloop()
