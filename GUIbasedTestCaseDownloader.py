import os
import webbrowser
import tkinter
from tkinter import ttk, messagebox


# main window
window = tkinter.Tk()
window.title("TEST CASE DOWNLOADER")
window.configure(background="#fff")
window.geometry("950x420")
window.option_add("*tearOff", False)
window.resizable(False, False)

global selected, envelope_headpath, envelope_footpath
envelope_headpath = ""
envelope_footpath = ""
selected = False


def AutomateFunction():
    global envelope_headpath, envelope_footpath
    if Clientstr.get() != "" and Clientstr.get() in clients and CheckVar1.get() != 0:
        try:
            status_var.set("Please wait!, Test cases are downloading...")
            envelope()
            folder = os.path.join(os.getcwd(), 'xmls')
            list1 = []
            b2["state"] = "disabled"
            menubar.entryconfig("Options", state="disabled")
            for filename in os.listdir(folder):
                if not filename.endswith('.xml'):
                    continue
                if filename in list1:
                    continue
                file_path = os.path.join(folder, filename)
                with open(envelope_headpath, "r") as f, open(envelope_footpath, "r") as f1, open(file_path, "r") as f2:
                    header = f.read()
                    footer = f1.read()
                    content = f2.read()

                if "</LCID>" not in content:
                    content = content.removeprefix('<?xml version="1.0" encoding="utf-8"?>')
                    xml_data = header + content + footer
                    with open(file_path, "w") as f:
                        f.write(xml_data)
                else:
                    list1.append(filename)

            list1.clear()
            status_var.set("Envelope added successfully in all the test cases")
            b2.grid_remove()
            menubar.entryconfig("Options", state="normal")

        except(FileNotFoundError, IOError, UnboundLocalError):
            b2["state"] = "normal"
            list1.clear()
            menubar.entryconfig("Options", state="normal")
            status_var.set("Please Select Client & Library, Then Press Automate!")

    else:
        status_var.set("Please Select Client & Library, Then Press Automate!")


def location():
    pass


def auto_mate():
    b2["state"] = "normal"
    FileNameStr.set("")
    Clientstr.set("")
    CheckVar1.set(0)
    b2.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
    if b1["state"] == "normal" or b1["state"] == "active":
        b1["state"] = "disabled"
    if e2["state"] == "normal" or e2["state"] == "active":
        e2["state"] = "disabled"
    status_var.set("Please Select Client & Library, Then Press Automate!")


def show_about_info():
    messagebox.showinfo(
        title="About",
        message="By this software\n1. you can download any test case.\n2. you can add envelope of any specific client."
    )


def quit_app():
    window.destroy()


def New():
    FileNameStr.set("")
    Clientstr.set("")
    CheckVar1.set(0)
    b2.grid_remove()
    if b1["state"] == "disabled":
        b1["state"] = "normal"
    if e2["state"] == "disabled":
        e2["state"] = "normal"
    if c1["state"] == "disabled":
        c1["state"] = "normal"
    if c2["state"] == "disabled":
        c2["state"] = "normal"

    status_var.set("Welcome to test case downloader!")


def envelope():
    global envelope_headpath, envelope_footpath
    envelope_headpath = os.path.join(os.getcwd(), 'envelopes', f'{Clientstr.get()}_{library[CheckVar1.get()-1]}_Header.txt')
    envelope_footpath = os.path.join(os.getcwd(), 'envelopes', f'{library[CheckVar1.get()-1]}_Footer.txt')


def submitFunction():
    # webbrowser.open('http://example.com')
    global envelope_headpath, envelope_footpath
    if Clientstr.get() != "" and Clientstr.get() in clients and FileNameStr.get() != "" and CheckVar1.get() != 0:
        try:
            envelope()
            file_path = os.path.join(os.getcwd(), 'xmls', f'{FileNameStr.get()}.xml')
            with open(envelope_headpath, "r") as f, open(envelope_footpath, "r") as f1, open(file_path, "r") as f2:
                header = f.read()
                footer = f1.read()
                content = f2.read()

            if "</LCID>" not in content:
                content = content.removeprefix('<?xml version="1.0" encoding="utf-8"?>')
                xml_data = header + content + footer
                with open(file_path, "w") as f:
                    f.write(xml_data)

            status_var.set(f"<{FileNameStr.get()} has been downloaded for {Clientstr.get()}>")

        except(FileNotFoundError, IOError, UnboundLocalError):
            status_var.set(f"<Please Enter a valid FileName Or ClientName & Select anyone library>")

    else:
        FileNameStr.set("")
        Clientstr.set("")
        CheckVar1.set(0)
        status_var.set(f"<Please Enter a valid FileName Or ClientName & Select anyone library>")


def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


def cut_text():
    global selected
    if e2.select_present():
        selected = e2.selection_get()
        e2.delete('sel.first', 'sel.last')


def copy_text():
    global selected
    if e2.select_present():
        selected = e2.selection_get()


def paste_text():
    global selected
    if e2.select_present():
        e2.delete('sel.first', 'sel.last')
        e2.insert(1, selected)
    else:
        e2.insert(1, selected)


def delete_text():
    if e2.select_present():
        e2.delete('sel.first', 'sel.last')


def refreshClients():
    clients.clear()
    with open(client_path, 'r') as f:
        for line in f:
            clients.append(line.strip())
    d1['values'] = clients


def delFunction():
    pass


def delClient():
    b4["state"] = "normal"
    FileNameStr.set("")
    Clientstr.set("")
    CheckVar1.set(0)
    b4.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
    if b1["state"] == "normal" or b1["state"] == "active":
        b1["state"] = "disabled"
    if e2["state"] == "normal" or e2["state"] == "active":
        e2["state"] = "disabled"
    if c1["state"] == "normal" or c1["state"] == "active":
        c1["state"] = "disabled"
    if c2["state"] == "normal" or c2["state"] == "active":
        c2["state"] = "disabled"
    status_var.set("Please Select Client, Then Press Delete!")
    # with open(client_path,'a+') as f:
    #     f.write(clients[])


def AddFunction():
    newclient = Clientstr.get().upper()
    if Clientstr.get() == "" or FileNameStr.get() == "":
        status_var.set(f"<Please Type Client Name and Envelope>")

    elif Clientstr.get() != "" and FileNameStr.get() != "" and CheckVar1.get() != 0:
        with open(client_path, 'a') as f:
            f.write(f'\n{newclient}')
        refreshClients()
        file_path = os.path.join(os.getcwd(), 'envelopes', f'{Clientstr.get()}_{library[CheckVar1.get()-1]}_Header.txt')
        with open(file_path, "w") as f:
            f.write(FileNameStr.get())

        b3.grid_remove()
        b1.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
        if b1["state"] == "disabled":
            b1["state"] = "normal"
        e1.grid_remove()
        d1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
        l5.grid_remove()
        l3.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
        FileNameStr.set("")
        Clientstr.set("")
        CheckVar1.set(0)
        status_var.set(f"<New Client Added Successfully>")
        menubar.entryconfig("Options", state="normal")

    else:
        status_var.set(f"<Client Already Exist>")


def addClient():
    menubar.entryconfig("Options", state="disabled")
    FileNameStr.set("")
    Clientstr.set("")
    CheckVar1.set(0)
    d1.grid_remove()
    e1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    l3.grid_remove()
    l5.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
    b1.grid_remove()
    b2.grid_remove()
    b3.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)


# Status Bar
status_var = tkinter.StringVar()
status_var.set("Welcome to test case downloader!")
status_bar = tkinter.Label(window, textvariable=status_var, anchor=tkinter.N, font=('Helvetica', 12, 'bold'))

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
l5 = tkinter.Label(window, text="ENVELOPE HEADER:", font=font1, borderwidth=1, relief="solid")
e2 = tkinter.Entry(window, width=31, font=font1, borderwidth=1, relief="solid",textvariable=FileNameStr, selectbackground="Yellow", selectforeground="black")
e1 = tkinter.Entry(window, width=31, font=font1, borderwidth=1, relief="solid",textvariable=Clientstr, selectbackground="Yellow", selectforeground="black")

# Combobox and Client Name list
d1 = ttk.Combobox(window, width=30, font=font1, textvariable=Clientstr)
window.option_add("*TCombobox*Listbox*Font", font2)
clients = []
client_path = os.path.join(os.getcwd(), 'imp', 'Clients.txt')
library = ['Ariel360', 'ArielDB']
refreshClients()

# Radio Buttons and Submit
c1 = tkinter.Radiobutton(window, text="Ariel360", variable=CheckVar1, value=1, font=font2)
c2 = tkinter.Radiobutton(window, text="ArielDB", variable=CheckVar1, value=2, font=font2)
b1 = tkinter.Button(window, text="SUBMIT", command=submitFunction, font=font1)
b1.config(width=20, height=2)
b2 = tkinter.Button(window, text="AUTOMATE", command=AutomateFunction, font=font1)
b2.config(width=20, height=2)
b3 = tkinter.Button(window, text="ADD", command=AddFunction, font=font1)
b3.config(width=20, height=2)
b4 = tkinter.Button(window, text="DELETE", command=delFunction, font=font1)
b4.config(width=20, height=2)

# Menubar Options Help
menubar = tkinter.Menu()
window.config(menu=menubar)

options_menu = tkinter.Menu(menubar)
help_menu = tkinter.Menu(menubar)

menubar.add_cascade(menu=options_menu, label="Options")
menubar.add_cascade(menu=help_menu, label="Help")

options_menu.add_command(label="New", command=lambda: New())
options_menu.add_command(label="Location", command=lambda:location())
options_menu.add_command(label="Add Client", command=lambda:addClient())
options_menu.add_command(label="Delete Client", command=lambda:delClient())
options_menu.add_command(label="Automate", command=lambda: auto_mate())
options_menu.add_command(label="Exit", command=lambda:quit_app())
help_menu.add_command(label="About", command=lambda:show_about_info())

# Right Click Menu
m = tkinter.Menu(window, tearoff=0)
m.add_command(label="Cut", command=lambda: cut_text())
m.add_separator()
m.add_command(label="Copy", command=lambda: copy_text())
m.add_separator()
m.add_command(label="Paste", command=lambda: paste_text())
m.add_separator()
m.add_command(label="Delete", command=lambda: delete_text())
window.bind("<Button-3>", do_popup)


# Grid
def gridFunction():
    l4.grid(sticky=tkinter.NW, row=0, column=0, padx=10, pady=12, ipadx=2, ipady=2)
    l2.grid(row=1, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
    d1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    l3.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
    e2.grid(row=2, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    c1.grid(row=3, column=1, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    c2.grid(row=3, column=2, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    b1.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
    status_bar.grid(row=45, column=1, columnspan=2, sticky="ew",padx=10, pady=20)
    l1.grid(sticky=tkinter.SE, row=100, column=500, padx=10, pady=3, ipadx=2, ipady=2)


gridFunction()
window.mainloop()
