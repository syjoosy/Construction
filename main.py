from tkinter import *
window = Tk()
window.title("Ремонт от детей маминой подруги")
window.geometry('800x450')

Room_ID = 0
Rooms = []

#Функция преобразования введенных значений в список
def RoomStructureCreate(AddRoomWindow, RoomNameEntry, RoomLength, RoomWidthEntry, RoomHeightEntry):
    global Room_ID
    Room = []
    Room.append(Room_ID)
    Room.append(RoomNameEntry)
    Room.append(RoomLength)
    Room.append(RoomWidthEntry)
    Room.append(RoomHeightEntry)
    Room_ID += 1
    Rooms.append(Room)
    print(Rooms)
    #AddRoomWindow.quit()
    
# Окно ввода данных о комнате
def AddRoom():
    AddRoomWindow = Toplevel(window)
    AddRoomWindow.title("Добавление комнаты")
    AddRoomWindow.geometry('200x260')
    RoomName = Label(AddRoomWindow, text="Имя комнаты")
    RoomNameEntry = Entry(AddRoomWindow)
    RoomLengthLabel = Label(AddRoomWindow, text="Длина комнаты в см")
    RoomLengthEntry = Entry(AddRoomWindow)
    RoomWidthLabel = Label(AddRoomWindow, text="Ширина комнаты в см")
    RoomWidthEntry = Entry(AddRoomWindow)
    RoomHeightLabel = Label(AddRoomWindow, text="Высота комнаты в см")
    RoomHeightEntry = Entry(AddRoomWindow)
    RoomName.grid(padx=10, pady=5)
    RoomNameEntry.grid(padx=10)
    RoomLengthLabel.grid(padx=10, pady=5)
    RoomLengthEntry.grid(padx=10)
    RoomWidthLabel.grid(padx=10, pady=5)
    RoomWidthEntry.grid(padx=10)
    RoomHeightLabel.grid(padx=10, pady=5)
    RoomHeightEntry.grid(padx=10)
    Add = Button(AddRoomWindow, text="Add Room", command=lambda: RoomStructureCreate(AddRoomWindow, RoomNameEntry.get(),RoomLengthEntry.get(),RoomWidthEntry.get(),RoomHeightEntry.get()))
    Add.grid(padx=10, pady=5)



room_frame = LabelFrame(text="Room")

#room_entry = Entry(room_frame, width=10)
#room_entry.grid()

room_frame.grid(row=0, column=0, sticky=N+S, padx=10)

add_room_button = Button(window, text="Add Room", command=AddRoom)
add_room_button.grid(row=1, column=0, padx=35)

txt_edit = Text(window)
txt_edit.grid(row=0, column=1)

window.mainloop()