from pymongo import MongoClient
from tkinter import *
from . import main_menu

def chosed(class_ID):
    main_menu.class_ID = class_ID
    main_menu.show_list()

def window(switch_class_frame: Frame):
    db = MongoClient()['basicdb']
    class_list = db.list_collection_names()
    for class_ID in class_list:
        i = 0
        class_btn = Button(switch_class_frame, text=class_ID, bd=1, 
                            activebackground="#FFFFFF",
                            command=lambda: chosed(class_ID))
        class_btn.place(x=50, y=50*i, width=200, height=50)
        class_btn.pack(pady=5)
        i += 1

