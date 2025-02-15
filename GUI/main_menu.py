import tkinter as tk
from PIL import Image, ImageTk
# from back_end import face_scanning
from . import add_student, face_check, select_class
from back_end import face_scanning

root = tk.Tk()
root.title("Attendance checking software")
root.geometry("1080x750")
root.resizable(False, False)

class_ID = '154016'
#icon
toggle_icon = tk.PhotoImage(file="GUI/Icon/web.png")
switch_class_icon = tk.PhotoImage(file="GUI/Icon/change.png")
add_std_icon = tk.PhotoImage(file="GUI/Icon/plus.png")
show_list_icon = tk.PhotoImage(file="GUI/Icon/list.png")
face_check_icon = tk.PhotoImage(file="GUI/Icon/camera.png")

def switch_indication(indicator_label, page):
    switch_class_btn_indicator.config(bg=menu_bar_color)
    add_std_btn_indicator.config(bg=menu_bar_color)
    show_list_btn_indicator.config(bg=menu_bar_color)
    face_check_btn_indicator.config(bg=menu_bar_color)
    indicator_label.config(bg='white')
    if menu_bar_frame.winfo_width() > 45:
        fold_menu_bar()
        
    face_scanning.close_cam()
    for frame in page_frame.winfo_children():
        frame.destroy()
        
    page()
    
def extending_animation():
    current_width = menu_bar_frame.winfo_width()
    if current_width < 235:
        current_width += 10
        menu_bar_frame.config(width=current_width)
        root.after(ms=5, func= extending_animation)

def folding_animation():
    current_width = menu_bar_frame.winfo_width()
    if current_width > 45:
        current_width -= 10
        menu_bar_frame.config(width=current_width)
        root.after(ms=5, func= folding_animation)

def extend_menu_bar():
    extending_animation()
    toggle_menu_btn.config(command=fold_menu_bar)
    
def fold_menu_bar():
    folding_animation()
    toggle_menu_btn.config(command=extend_menu_bar)

def switch_class():
    switch_class_frame = tk.Frame(page_frame)
    select_class.window(switch_class_frame)
    switch_class_frame.pack(fill=tk.BOTH, expand=True)

def add_std():
    add_std_frame = tk.Frame(page_frame)
    add_student.window(add_std_frame, class_ID)
    add_std_frame.pack(fill=tk.BOTH, expand=True)
    
def show_list():
    show_list_frame = tk.Frame(page_frame,)
    
    show_list_frame.pack(fill=tk.BOTH, expand=True)

def face_checking():
    face_check_frame = tk.Frame(page_frame)
    face_check.window(face_check_frame, class_ID)
    face_check_frame.pack(fill=tk.BOTH, expand=True)

page_frame = tk.Frame(root)
page_frame.place(relheight=1.0, relwidth=1.0, x=50)
switch_class()

menu_bar_color = '#383838'
menu_bar_frame = tk.Frame(root, bg=menu_bar_color)

toggle_menu_btn = tk.Button(menu_bar_frame, image=toggle_icon, bg=menu_bar_color, bd=0, 
                            activebackground=menu_bar_color,
                            command=extend_menu_bar)
toggle_menu_btn.place(x=2, y=10)

switch_class_btn = tk.Button(menu_bar_frame, image=switch_class_icon, bg=menu_bar_color, bd=0, 
                             activebackground=menu_bar_color, 
                             command=lambda: switch_indication(switch_class_btn_indicator, switch_class))
switch_class_btn.place(x=3, y=130, width=40, height=40)
switch_class_btn_indicator = tk.Label(menu_bar_frame, bg='white')
switch_class_btn_indicator.place(x=1, y=130, height=40, width=3)
switch_class_lb = tk.Label(menu_bar_frame, text = "Switch class", bg=menu_bar_color, fg='white',
                           font=('Bold', 15), anchor=tk.W)
switch_class_lb.place(x=45, y=130, width=200, height=40)
switch_class_lb.bind('<Button-1>', lambda e: switch_indication(switch_class_btn_indicator, switch_class))

add_std_btn = tk.Button(menu_bar_frame, image=add_std_icon, bg=menu_bar_color, bd=0,
                        activebackground=menu_bar_color,
                        command=lambda: switch_indication(add_std_btn_indicator, add_std))
add_std_btn.place(x=3, y=190, width=40, height=40)
add_std_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
add_std_btn_indicator.place(x=1, y=190, height=40, width=3)
add_std_lb = tk.Label(menu_bar_frame, text = "Add student", bg=menu_bar_color, fg='white',
                           font=('Bold', 15), anchor=tk.W)
add_std_lb.place(x=45, y=190, width=200, height=40)
add_std_lb.bind('<Button-1>', lambda e : switch_indication(add_std_btn_indicator, add_std))

show_list_btn = tk.Button(menu_bar_frame, image=show_list_icon, bg=menu_bar_color, bd=0, 
                          activebackground=menu_bar_color,
                          command=lambda: switch_indication(show_list_btn_indicator, show_list))
show_list_btn.place(x=3, y=250, width=40, height=40)
show_list_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
show_list_btn_indicator.place(x=1, y=250, height=40, width=3)
show_list_lb = tk.Label(menu_bar_frame, text = "Student information", bg=menu_bar_color, fg='white',
                           font=('Bold', 15), anchor=tk.W)
show_list_lb.place(x=45, y=250, width=200, height=40)
show_list_lb.bind('<Button-1>', lambda e : switch_indication(show_list_btn_indicator, show_list))

face_check_btn = tk.Button(menu_bar_frame, image=face_check_icon, bg=menu_bar_color, bd=0, 
                           activebackground=menu_bar_color, 
                           command=lambda: switch_indication(face_check_btn_indicator, face_checking))
face_check_btn.place(x=3, y=310, width=40, height=40)
face_check_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
face_check_btn_indicator.place(x=1, y=310, height=40, width=3)
face_check_lb = tk.Label(menu_bar_frame, text = "Attendance checking", bg=menu_bar_color, fg='white',
                           font=('Bold', 15), anchor=tk.W)
face_check_lb.place(x=45, y=310, width=200, height=40)
face_check_lb.bind('<Button-1>', lambda e : switch_indication(face_check_btn_indicator, face_checking))

menu_bar_frame.pack(side=tk.LEFT, fill=tk.Y)
menu_bar_frame.pack_propagate(flag=False)
menu_bar_frame.configure(width=45)



# scan_button = CTkButton(
#     menu_bar_frame, 
#     text="Quét mặt", 
#     corner_radius=35, 
#     font=("Arial", 30), 
#     fg_color="#4158D0", 
#     hover_color="red", 
#     command=lambda: face_scanning.scanning("153016"))
# scan_button.pack(pady=100, padx=100, fill=tk.X)

# add_button = CTkButton(
#     menu_bar_frame, 
#     text="Thêm sinh viên", 
#     corner_radius=35, 
#     font=("Arial", 30), 
#     fg_color="#4158D0", 
#     hover_color="red", 
#     command=lambda: add_student.window("153016"))
# add_button.pack(pady=100, padx=100, fill=tk.X)

# right_frame = tk.Frame(root, width=830, height=750)
# right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# right_frame.grid_propagate(False)
# right_frame.pack_propagate(False)

root.mainloop()