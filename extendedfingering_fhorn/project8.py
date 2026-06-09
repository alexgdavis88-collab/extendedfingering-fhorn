import tkinter as tk
import pygame
from tkinter import ttk
from functools import partial
import os

window = tk.Tk()
window.geometry("875x400")
window.title("Sound App")
#Creates window/title


main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=1)
#Creates main frame (frame where the scrollbar scrolls)
my_canvas= tk.Canvas(main_frame)
my_canvas.pack(side=tk.LEFT,fill=tk.BOTH, expand=1)
scrollbar=ttk.Scrollbar(main_frame, orient=tk.VERTICAL,command=my_canvas.yview)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
my_canvas.configure(yscrollcommand=scrollbar.set)
my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))#another frame

frame_2=tk.Frame(my_canvas)


my_canvas.create_window((0,0),window=frame_2,anchor="nw")
# Allows sounds to be played
pygame.mixer.init()
def play(note):
    relative_path = os.path.join("horn_notes", note)  # Joins folder and file name
    sound = pygame.mixer.Sound(relative_path)
    sound.play()



#Title buttons:
title=tk.Label(frame_2,text=" Note  ",bd=9,relief=tk.GROOVE,font=("times new roman",50,"bold"),bg="white",fg="pink") 
title_1=tk.Label(frame_2, text ="   Sound   ", bd=9, relief =tk.GROOVE,font=("times new roman",50,"bold"),bg="white",fg="pink")
title_2=tk.Label(frame_2, text ="  Fingering ", bd=9, relief =tk.GROOVE,font=("times new roman",50,"bold"),bg="white",fg="pink")
#creates notes,button, and fingerings |Partial allows commands to take functions with arguments
note_1 =tk.Label (frame_2,text=" C2 ",font=("Helvetica", 32))
button_1 = tk.Button(frame_2, text="Sound", font=("Helvetica", 32),relief=tk.RAISED , command=partial(
    play,"C2.mp3"))
finger_1 = tk.Label (frame_2,text = "Open", font=("Helvetica",32,"bold"))
note_2 =tk.Label (frame_2,text=" C#2/Db ",font=("Helvetica", 32))
button_2 = tk.Button(frame_2, text="Sound", font=("Helvetica", 32),
                     relief=tk.RAISED , command=partial(
    play,"Cs2.mp3"))
finger_2 = tk.Label (frame_2,text = "T23", font=("Helvetica",32,"bold"))
note_3 =tk.Label (frame_2,text=" D2 ",font=("Helvetica", 32))
button_3 = tk.Button(frame_2, text="Sound", font=("Helvetica", 32),
                     relief=tk.RAISED , command=partial(
    play,"D2.mp3"))
finger_3 = tk.Label (frame_2,text = "T12", font=("Helvetica",32,"bold"))
note_4 =tk.Label (frame_2,text=" D#2/Eb ",font=("Helvetica", 32))
button_4 = tk.Button(frame_2, text="Sound", font=("Helvetica", 32),
                     relief=tk.RAISED , command=partial(
    play,"Ds2.mp3"))
finger_4 = tk.Label (frame_2,text = "T1", font=("Helvetica",32,"bold"))
note_5 =tk.Label (frame_2,text=" E2 ",font=("Helvetica", 32))
button_5 = tk.Button(frame_2, text="Sound", font=("Helvetica", 32),
                     relief=tk.RAISED , command=partial(
    play,"E2.mp3"))
finger_5 = tk.Label (frame_2,text = "T2", font=("Helvetica",32,"bold"))
note_6 =tk.Label (frame_2,text=" F2 ",font=("Helvetica", 32))
button_6 = tk.Button(frame_2, text="Sound", font=("Helvetica", 32),
                     relief=tk.RAISED , command=partial(
    play,"F2.mp3"))
finger_6 = tk.Label (frame_2,text = "T Open", font=("Helvetica",32,"bold"))
note_7 =tk.Label (frame_2,text=" F#2/Gb ",font=("Helvetica", 32))
button_7 = tk.Button(frame_2, text="Sound", font=("Helvetica", 32),
                     relief=tk.RAISED , command=partial(
    play,"Fs2.mp3"))
finger_7 = tk.Label (frame_2,text = "1 2 3", font=("Helvetica",32,"bold"))
note_8 =tk.Label (frame_2,text=" G ",font=("Helvetica", 32))
button_8 = tk.Button(frame_2, text="Sound", font=("Helvetica", 32),
                     relief=tk.RAISED , command=partial(
    play,"G2.mp3"))
finger_8 = tk.Label (frame_2,text = "1 3", font=("Helvetica",32,"bold"))
title.grid(row=1, column=1) 
title_1.grid(row=1,column = 2)
title_2.grid(row=1,column=3)
note_1.grid(row=2, column=1)
button_1.grid(row=2, column=2)
finger_1.grid(row=2, column=3)
note_2.grid(row=3, column=1)
button_2.grid(row=3, column=2)
finger_2.grid(row=3, column=3)
note_3.grid(row=4, column=1)
button_3.grid(row=4, column=2)
finger_3.grid(row=4, column=3)
note_4.grid(row=5, column=1)
button_4.grid(row=5, column=2)
finger_4.grid(row=5, column=3)
note_5.grid(row=6, column=1)
button_5.grid(row=6, column=2)
finger_5.grid(row=6, column=3)
note_6.grid(row=7, column=1)
button_6.grid(row=7, column=2)
finger_6.grid(row=7, column=3)
note_7.grid(row=8, column=1)
button_7.grid(row=8, column=2)
finger_7.grid(row=8, column=3)
note_8.grid(row=9, column=1)
button_8.grid(row=9, column=2)
finger_8.grid(row=9, column=3)

print(os.path.exists("horn_notes/A2.mp3"))

print(os.listdir()) 

window.mainloop()
