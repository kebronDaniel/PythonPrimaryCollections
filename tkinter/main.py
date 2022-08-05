from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

label = Label(text="Sample Text")
label.pack()


def change_label():
    label["text"] = get_user_input()


def get_user_input():
    return user_input.get()


user_input = Entry(width=20)
user_input.pack()
user_input.insert(END, string="Type your header here")

button = Button(text="Click", command=change_label)
button.pack()

my_text = Text(width=30, height=5)
my_text.pack()
my_text.focus()
my_text.insert(END, "Type your email here")
my_text.get("1.0", END)


def get_spin_value():
    print(spin.get())


spin = Spinbox(from_=0, to_=10, width=5, command=get_spin_value)
spin.pack()


def get_scale(value):
    print(value)


scale = Scale(from_=0, to_=10,command=get_scale)
scale.pack()


def get_checkbox():
    print(check_state.get())


check_state = IntVar()
check_box = Checkbutton(text="Above age", variable=check_state,command=get_checkbox)
check_box.pack()


def get_radio():
    print(radio_state.get())


radio_state = IntVar()
radio_one = Radiobutton(text="option 1", value=1,variable=radio_state,command=get_radio)
radio_two = Radiobutton(text="option 2", value=2,variable=radio_state,command=get_radio)
radio_one.pack()
radio_two.pack()


def get_list_box(event):
    print(list_box.get(list_box.curselection()))


list_box = Listbox(height=4)
names = ["Kebron","sivan","Daniel","Naomi"]
for name in names:
    list_box.insert(names.index(name), name)

list_box.bind("<<ListboxSelect>>", get_list_box)
list_box.pack()



window.mainloop()
