from tkinter import *
from tkinter.ttk import Combobox
window = Tk()
window.title("Ремонт от детей маминой подруги")
window.geometry('800x450')

Room_ID = 0
Rooms = {}


# Функция преобразования введенных значений в словарь
# Используется два словаря: внутренний содержит в себе непосредственно комнату (все ее параметры), внешний нужен для присвоения комнатам уникального идентификатора
def RoomStructureCreate(AddRoomWindow, RoomNameEntry, RoomLength, RoomWidthEntry, RoomHeightEntry, RoomFloorMaterial):
    global Room_ID
    Room = {"RoomName":RoomNameEntry, "RoomLength":RoomLength, "RoomWidth":RoomWidthEntry, "RoomHeight":RoomHeightEntry, "RoomFloorMaterial":RoomFloorMaterial}
    Room_ID += 1
    Rooms[Room_ID] = Room
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
    # Выпадающий список для материалов
    material_picker = Combobox(AddRoomWindow)
    material_picker["values"] = ("Плитка", "Паркет", "Ламинат")
    material_picker.current(0)
    #
    RoomName.grid(padx=10, pady=5)
    RoomNameEntry.grid(padx=10)
    RoomLengthLabel.grid(padx=10, pady=5)
    RoomLengthEntry.grid(padx=10)
    RoomWidthLabel.grid(padx=10, pady=5)
    RoomWidthEntry.grid(padx=10)
    RoomHeightLabel.grid(padx=10, pady=5)
    RoomHeightEntry.grid(padx=10)
    material_picker.grid(padx=10, pady=5)
    Add = Button(AddRoomWindow, text="Add Room", command=lambda: RoomStructureCreate(AddRoomWindow, RoomNameEntry.get(),RoomLengthEntry.get(),RoomWidthEntry.get(),RoomHeightEntry.get(), material_picker.get()))
    Add.grid(padx=10, pady=5)

# Расчет краски
def CalculatePaint(LayerCount, SurfaceLength, SurfaceWidth, PaintConsumption, CanVolume):
    return (LayerCount*(SurfaceWidth*SurfaceLength+(SurfaceWidth*SurfaceLength)/10)/(PaintConsumption*CanVolume))

# Расчет настенной плитки
def CalculateWallTiles(RoomHeight, RoomLength, RoomWidth, WindowHeight, WindowWidth, DoorHeight, DoorWidth, SquareInPackage):
    return (2*RoomHeight*(RoomLength+RoomWidth)+(2*RoomHeight*(RoomLength+RoomWidth)/10-WindowWidth*WindowHeight-DoorWidth*DoorHeight)/SquareInPackage)

# Расчет напольного материала (плитка/ламинат/паркет)
def CalculateFloorMaterial(RoomLength, RoomWidth, SquareInPackage):
    return ((RoomLength*RoomWidth+RoomLength*RoomWidth/10)/SquareInPackage)

# Расчет обоев
def CalculateWallpaper(RoomHeight, RoomLength, RoomWidth, WindowHeight, WindowWidth, DoorHeight, DoorWidth, RollWidth, RollHeight):
    return (2*RoomHeight*(RoomLength+RoomWidth)+(2*RoomHeight*(RoomLength+RoomWidth)/10-WindowWidth*WindowHeight-DoorWidth*DoorHeight)/(RollWidth*RollHeight))

# Расчет клея
def CalculateGlue(SurfaceWidth, SurfaceLength, GlueConsumption, Packing):
    return (SurfaceWidth*SurfaceLength+(SurfaceWidth*SurfaceLength)/10*GlueConsumption/Packing)

#room_entry = Entry(room_frame, width=10)
#room_entry.grid()
room_frame = LabelFrame(text="Room")
room_frame.grid(row=0, column=0, sticky=N+S, padx=10)

add_room_button = Button(window, text="Add Room", command=AddRoom)
add_room_button.grid(row=1, column=0, padx=35)

txt_edit = Text(window)
txt_edit.grid(row=0, column=1)

window.mainloop()