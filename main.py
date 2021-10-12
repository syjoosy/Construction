from tkinter import *
window = Tk()
window.title("Ремонт от детей маминой подруги")
window.geometry('800x450')

room_frame = LabelFrame(text="Room")

room_entry = Entry(room_frame, width=10)
room_entry.grid()

room_frame.grid(row=0, column=0, sticky=N+S, padx=10)

add_room_button = Button(window, text="Add Room")
add_room_button.grid(row=1, column=0, padx=35)

txt_edit = Text(window)
txt_edit.grid(row=0, column=1)

window.mainloop()
