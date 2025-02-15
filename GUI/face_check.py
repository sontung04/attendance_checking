import tkinter as tk
from pymongo import MongoClient
import cv2
from PIL import Image, ImageTk
from back_end import face_scanning

FPS = 10

def update_frame(img: Image, class_ID):
    imgtk = ImageTk.PhotoImage(image=img)
    video_label.imgtk = imgtk
    video_label.config(image=imgtk)
    ms = int(1000/FPS)
    video_label.after(ms, lambda: face_scanning.scanning(class_ID))

def window(face_checking_frame: tk.Frame, class_ID):
    global video_label 
    face_scanning.class_ID = class_ID
    face_scanning.open_cam()
    video_label= tk.Label(face_checking_frame)
    video_label.pack(fill=tk.Y)
    video_label.place(width=640)
    face_scanning.scanning(class_ID)