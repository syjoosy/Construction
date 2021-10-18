import tkinter
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog
from tkinter import commondialog

room_ID = 0

'''
class RoomParameters(object):
    def __init__(self, x, y, z, id):
        self.room_x=x
        self.room_y=y
        self.room_z=z
        self.room_ID = id

'''

class RoomAddDialog(simpledialog.Dialog):
    def __init__(self, parent, title):
        self.room_x = None
        self.room_y = None
        self.room_z = None
        self.room_id = None
        super().__init__(parent, title)

    def body(self, Frame):
        self.ask_room_name_label = Label(Frame, width=40, text="Введите название комнаты")
        self.ask_room_name_label.pack()
        self.ask_room_name_box = Entry(Frame, width=40)
        self.ask_room_name_box.pack()
        self.ask_room_x_label = Label(Frame, width=40, text="Введите длину комнаты в сантиметрах")
        self.ask_room_x_label.pack()
        self.ask_room_x_box = Entry(Frame,width=40)
        self.ask_room_x_box.pack()
        self.ask_room_y_label = Label(Frame, width=40, text="Введите ширину комнаты в сантиметрах")
        self.ask_room_y_label.pack()
        self.ask_room_y_box = Entry(Frame,width=40)
        self.ask_room_y_box.pack()
        self.ask_room_z_label = Label(Frame, width=40, text="Введите высоту комнаты в сантиметрах")
        self.ask_room_z_label.pack()
        self.ask_room_z_box = Entry(Frame,width=40)
        self.ask_room_z_box.pack()
        return Frame

    def ok_pressed(self):
        self.room_name = self.ask_room_name_box.get()
        self.room_x = self.ask_room_x_box.get()
        self.room_y = self.ask_room_y_box.get()
        self.room_z = self.ask_room_z_box.get()
        global room_ID
        room_ID += 1
        self.room_id = room_ID
        self.destroy()
        
    def cancel_pressed(self):
        self.destroy()

    def buttonbox(self):
        self.ok_button = Button(self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="left")
        cancel_button = Button(self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())

def roomAddDialog():
    dialog = RoomAddDialog(title="Добавление комнаты", parent=window)
    return dialog.room_name, dialog.room_x, dialog.room_y, dialog.room_z, dialog.room_id

x = 0
y = 0
room_table = [["" for j in range(x)] for i in range(y)]

def showRoomAddDialog():
    global room_table, x, y
    x += 1
    y += 1
    room_table += roomAddDialog()
    print(room_table)
'''
def addRoom():
    room_name = simpledialog.askstring(title="Добавление комнаты",
                                  prompt="Введите название комнаты:")
    room_list = []
    room_list.append(room_name)
    room_x = simpledialog.askinteger(title="Добавление комнаты",
                                  prompt="Введите длину комнаты в сантиметрах:")
    room_list.append(room_x)
    room_y = simpledialog.askinteger(title="Добавление комнаты",
                                  prompt="Введите ширину комнаты в сантиметрах:")
    room_list.append(room_y)
    room_z = simpledialog.askinteger(title="Добавление комнаты",
                                  prompt="Введите высоту комнаты в сантиметрах:")
    room_list.append(room_z)
    room_floorMaterial = simpledialog.askstring(title="Добавление комнаты",
                                  prompt="Введите материал пола:")
    room_list.append(room_floorMaterial)
    room_image = Label(master=txt_edit, text=room_name, fg="black", bg="white", height=room_x // 100,
                       width=room_y // 100)
    room_image.grid(row=0, column=0, sticky=N + S, padx=10)
    print(room_list)
'''
window = Tk()
window.title("Ремонт от детей маминой подруги")
window.geometry('800x450')

txt_edit = Text(window)
txt_edit.place(x=150, y=0)

room_frame = LabelFrame(text="Room")

'''
room_entry = Entry(room_frame, width=15)
room_entry.grid()
'''

room_frame.grid(row=0, column=0, sticky=N+S, padx=10)

add_room_message = Entry(room_frame, width=15)
add_room_button = Button(window, text="Add Room", command=showRoomAddDialog)
add_room_button.place(x=45, y=100)

def deleteRoom():
    print("Здесь должно быть удаление комнаты")

delete_room_button = Button(window, text="Delete Room", command=deleteRoom)
delete_room_button.place(x=45, y=140)

'''
room_id_test = RoomParameters(5,3.2,1.8,1)
print(room_id_test.room_ID)
'''

window.mainloop()
