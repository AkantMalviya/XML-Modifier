import tkinter
from tkinter import ttk, messagebox

# main window
window = tkinter.Tk()
window.title("TEST CASE DOWNLOADER")
window.configure(background="#fff")
window.geometry("950x380")
window.option_add("*tearOff", False)
# window.resizable(False, False)

global selected
my_text = tkinter.Text(window, selectbackground="Yellow", selectforeground="black",undo=True)


def show_about_info():
    messagebox.showinfo(
        title="About",
        message="Tkinter is GUI for Python programing language."
    )


def quit_app():
    window.destroy()


def New():
    print("Example")


def example():
    print("Example")


def submitFunction():
    print(CheckVar1.get())
    print('Submit button is clicked.')


def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


def cut_text(e):
    pass


def copy_text(e):
    pass


def paste_text(e):
    pass


def delete_text(e):
    pass


# Status Bar
status_var = tkinter.StringVar()
status_var.set("Welcome to test case downloader!")
status_bar = tkinter.Label(window, textvariable=status_var, anchor=tkinter.N)

# Fonts and variables
copyryt = u"\u00A9"
trademark = u"\u2122"
font1 = ('Times', 20)
font2 = ('Times', 15)
CheckVar1 = tkinter.IntVar()
FileNameStr = tkinter.StringVar()
Clientstr = tkinter.StringVar()

# Labels and Entry
l1 = tkinter.Label(window, text=copyryt + 'AkantMalviya')
l4 = tkinter.Label(window, text='LifeWorks'+trademark)
l2 = tkinter.Label(window, text="CLIENT NAME:", font=font1, borderwidth=1, relief="solid")
l3 = tkinter.Label(window, text="TEST FILE NAME:", font=font1, borderwidth=1, relief="solid")
e2 = tkinter.Entry(window, width=31, font=font1, borderwidth=1, relief="solid",textvariable=FileNameStr)

# Combobox and Client Name list
d1 = ttk.Combobox(window, width=30, font=font1, textvariable=Clientstr )
window.option_add("*TCombobox*Listbox*Font", font2)
clients = ('OPF', 'IMRF', 'HOOPP', 'PIBA')
d1['values'] = clients

# Radio Buttons and Submit
c1 = tkinter.Radiobutton(window, text="Ariel360", variable=CheckVar1, value=1, font=font2)
c2 = tkinter.Radiobutton(window, text="ArielDB", variable=CheckVar1, value=2, font=font2)
b1 = tkinter.Button(window, text="SUBMIT", command=submitFunction, font=font1)
b1.config(width=20, height=2)

# Menubar Options Help
menubar = tkinter.Menu()
window.config(menu=menubar)

options_menu = tkinter.Menu(menubar)
help_menu = tkinter.Menu(menubar)

menubar.add_cascade(menu=options_menu, label="Options")
menubar.add_cascade(menu=help_menu, label="Help")

options_menu.add_command(label="New", command=example)
options_menu.add_command(label="Location", command=example)
options_menu.add_command(label="Add Client", command=example)
options_menu.add_command(label="Exit", command=quit_app)
help_menu.add_command(label="About", command=show_about_info)

# Right Click Menu
m = tkinter.Menu(window, tearoff=0)
m.add_command(label="Cut", command=lambda: cut_text(False))
m.add_separator()
m.add_command(label="Copy", command=lambda: copy_text(False))
m.add_separator()
m.add_command(label="Paste", command=lambda: paste_text(False))
m.add_separator()
m.add_command(label="Delete", command=lambda: delete_text(False))
window.bind("<Button-3>", do_popup)

# Grid
l4.grid(sticky=tkinter.NW, row=0, column=0, padx=10, pady=12, ipadx=2, ipady=2)
l2.grid(row=1, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
d1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
l3.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
e2.grid(row=2, column=2, padx=10, pady=10, ipadx=2, ipady=2)
c1.grid(row=3, column=1, ipadx=2, ipady=2, rowspan=1, columnspan=2)
c2.grid(row=3, column=2, ipadx=2, ipady=2, rowspan=1, columnspan=2)
b1.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
status_bar.grid(row=45, column=1, columnspan=2, sticky="ew")
l1.grid(sticky=tkinter.SE, row=100, column=500, padx=10, pady=12, ipadx=2, ipady=2)

window.mainloop()
