# Packages
import os
import requests
import tkinter
from tkinter import ttk, messagebox
import subprocess


# Fonts
copyryt = u"\u00A9"
trademark = u"\u2122"
font4 = ('Times', 20)
font1 = ('Times', 18, 'bold')
font2 = ('Times', 15)
font3 = ('Times', 15, 'bold')

# tkinter main window
window = tkinter.Tk()
window.title("TEST CASE DOWNLOADER")
window.configure(background="#fff")
window.geometry("1000x390")
window.option_add("*tearOff", False)
window.resizable(False, False)
photo = tkinter.PhotoImage(file='images/xml.png')
window.iconphoto(False, photo)

# Global variables
global selected, envelope_headpath, envelope_footpath, client_link
global clients
clients = []
envelope_headpath = ""
envelope_footpath = ""
selected = False


def callback(addclient_str):
    if e2["state"] == "disabled":
        e2["state"] = "normal"
    if c1["state"] == "disabled":
        c1["state"] = "normal"
    if c2["state"] == "disabled":
        c2["state"] = "normal"
    newclient = addclient_str.get().upper().strip()
    flag1 = False
    flag2 = False
    file1 = os.path.join(os.getcwd(), 'envelopes', f'{newclient}_{library[0]}_Header.txt')
    file2 = os.path.join(os.getcwd(), 'envelopes', f'{newclient}_{library[1]}_Header.txt')
    if os.path.exists(file1):
        flag1 = True
        if c1["state"] == "normal" or c1["state"] == "active":
            c1["state"] = "disabled"
    if os.path.exists(file2):
        flag2 = True
        if c2["state"] == "normal" or c2["state"] == "active":
            c2["state"] = "disabled"
    if flag1 and flag2:
        if e2["state"] == "normal" or e2["state"] == "active":
            e2["state"] = "disabled"


def location():
    folderpath = os.path.join(os.getcwd(), 'xmls')
    os.startfile(folderpath)


def show_about_info():
    messagebox.showinfo(
        title="About",
        message=f'''Options:\n
        1. You Can Add Envelope Of Any Specific Client.\n
        2. Go To The XML File Location.\n
        3. Automate XML Envelope Addition.\n
        4. Download Any Specific Client Test Case.\n
        5. Add Any Client And Its Envelope In The Software.\n
        6. Delete Any Client From The Software.\n
        7. For Creating Multisource Test Case.\n
        8. Exit\n\n\t\t\t\t\t{brand}
        ''')


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


def quit_app():
    window.destroy()


def refreshClients():
    global clients
    clients = list()
    d1.set('')
    with open(client_path, 'r') as f:
        for line in f:
            clients.append(line.strip('\n'))
    d1['values'] = clients


def change_color(x):
    if x == 1:
        status_bar.config(bg="green2")
    elif x == 2:
        status_bar.config(bg="red2")
    elif x == 3:
        status_bar.config(bg="yellow")
        status_var.set(f"<Please Wait, Test Case Is Downloading...>")
    else:
        status_bar.config(bg="gray95")


def envelope():
    global envelope_headpath, envelope_footpath
    envelope_headpath = os.path.join(os.getcwd(), 'envelopes', f'{Clientstr.get().upper()}_{library[CheckVar1.get()-1]}_Header.txt')
    envelope_footpath = os.path.join(os.getcwd(), 'envelopes', f'{library[CheckVar1.get()-1]}_Footer.txt')


def clientlink():
    global client_link
    client_link = os.path.join(os.getcwd(), 'imp', 'downloadlinks',
                               f'{Clientstr.get().upper()}_{library[CheckVar1.get() - 1]}.txt')


def submitFunction():
    global envelope_headpath, envelope_footpath
    if Clientstr.get() != "" and Clientstr.get() in clients and FileNameStr.get() != "" and CheckVar1.get() != 0:
        try:
            envelope()
            file_path = os.path.join(os.getcwd(), 'xmls', f'{FileNameStr.get().upper().replace(" ","")}.xml')
            with open(envelope_headpath, "r") as f, open(envelope_footpath, "r") as f1:
                header = f.read()
                footer = f1.read()

            with open(file_path, "r") as f2:
                content = f2.read()
            checker = '<DocumentData>\n<DocumentProperties>\n<Language>\n<LCID>1033</LCID>\n</Language>\n<Template>'
            print(content.find(checker))
            if content.find(checker) == -1:
                content = content.replace('<?xml version="1.0" encoding="utf-8"?>', "")
                xml_data = header + content + footer
                with open(file_path, "w") as f:
                    f.write(xml_data)
                status_var.set(f"<Envelope has added in {FileNameStr.get()} For {Clientstr.get()}>")
                change_color(1)

            else:
                status_var.set(f"<{FileNameStr.get()} already have envelope for {Clientstr.get()}>")
                change_color(2)

            FileNameStr.set("")
            Clientstr.set("")
            CheckVar1.set(0)

        except (FileNotFoundError, UnboundLocalError, IOError):
            status_var.set("<File Not Found At Location!>")
            change_color(2)

    else:
        FileNameStr.set("")
        Clientstr.set("")
        CheckVar1.set(0)
        status_var.set(f"<Please Enter A Valid FileName Or ClientName & Select Anyone Library>")
        change_color(0)


def AutomateFunction():
    global envelope_headpath, envelope_footpath
    if Clientstr.get() != "" and Clientstr.get() in clients and CheckVar1.get() != 0:
        try:
            status_var.set("Please wait!, Test cases are downloading...")
            change_color(0)
            envelope()
            folder = os.path.join(os.getcwd(), 'xmls')
            list1 = []
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
                checker = '<DocumentData>\n<DocumentProperties>\n<Language>\n<LCID>1033</LCID>\n</Language>\n<Template>'
                if content.find(checker) == -1:
                    content = content.replace('<?xml version="1.0" encoding="utf-8"?>',"")
                    xml_data = header + content + footer
                    with open(file_path, "w") as f:
                        f.write(xml_data)
                else:
                    list1.append(filename)

            list1.clear()
            status_var.set("Envelope added successfully in all the test cases")
            change_color(1)
            b2.grid_remove()
            if b1.winfo_ismapped()==0:
                b1.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
            menubar.entryconfig("Options", state="normal")
            messagebox.showinfo(title="Task Completed", message="Envelope Added Successfully")

        except(FileNotFoundError, IOError, UnboundLocalError):
            list1.clear()
            menubar.entryconfig("Options", state="normal")
            status_var.set("Please Select Client & Library, Then Press Automate!")
            change_color(0)

    else:
        Clientstr.set("")
        CheckVar1.set(0)
        status_var.set("Please Select Client & Library, Then Press Automate!")
        change_color(0)


def AddFunction():
    newclient = addclientstr.get().upper().strip()
    if newclient != "" and FileNameStr.get() != "" and CheckVar1.get() != 0:
        if newclient not in clients:
            with open(client_path, 'a') as f:
                f.write(f'{newclient}\n')
            refreshClients()
            status_var.set(f"<New Client Added Successfully>")
            change_color(1)
        else:
            status_var.set(f"<Client Already Exist>")
            change_color(2)

        file_path = os.path.join(os.getcwd(), 'envelopes', f'{newclient}_{library[CheckVar1.get()-1]}_Header.txt')
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(FileNameStr.get())
            status_var.set(f"<New Client Added Successfully>")
            change_color(1)
            b3.grid_remove()
            e1.grid_remove()
            l5.grid_remove()
            if b1.winfo_ismapped() == 0:
                b1.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
            if d1.winfo_ismapped() == 0:
                d1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
            if l3.winfo_ismapped() == 0:
                l3.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
            menubar.entryconfig("Options", state="normal")
        else:
            status_var.set(f"<{newclient}_{library[CheckVar1.get()-1]} Already Exist!, Select Another Library>")
            change_color(2)
        FileNameStr.set("")
        addclientstr.set("")
        Clientstr.set("")
        CheckVar1.set(0)
        if e2["state"] == "disabled":
            e2["state"] = "normal"
        if c1["state"] == "disabled":
            c1["state"] = "normal"
        if c2["state"] == "disabled":
            c2["state"] = "normal"

    elif newclient != "" and e2["state"] == "disabled":
        if newclient not in clients:
            with open(client_path, 'a') as f:
                f.write(f'{newclient}\n')
            refreshClients()
            status_var.set(f"<New Client Added Successfully>")
            change_color(1)
            b3.grid_remove()
            e1.grid_remove()
            l5.grid_remove()
            if b1.winfo_ismapped() == 0:
                b1.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
            if d1.winfo_ismapped() == 0:
                d1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
            if l3.winfo_ismapped() == 0:
                l3.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
            menubar.entryconfig("Options", state="normal")
        else:
            status_var.set(f"<Client Already Exist>")
            change_color(2)
        FileNameStr.set("")
        addclientstr.set("")
        Clientstr.set("")
        CheckVar1.set(0)
        if e2["state"] == "disabled":
            e2["state"] = "normal"
        if c1["state"] == "disabled":
            c1["state"] = "normal"
        if c2["state"] == "disabled":
            c2["state"] = "normal"

    else:
        status_var.set(f"<Please Type Client Name, Envelope & Select any library>")
        if e2["state"] == "disabled":
            e2["state"] = "normal"
        if c1["state"] == "disabled":
            c1["state"] = "normal"
        if c2["state"] == "disabled":
            c2["state"] = "normal"
        change_color(0)


def delFunction():
    with open(client_path,'r') as f:
        content = f.read()
    if Clientstr.get().upper().replace(" ","") in content and Clientstr.get() != "":
        new = content.replace(f'{Clientstr.get().upper().replace(" ","")}\n', "")
        with open(client_path, 'w') as f:
            f.write(new)
        refreshClients()
        status_var.set("Client deleted successfully!")
        change_color(1)
        FileNameStr.set("")
        Clientstr.set("")
        CheckVar1.set(0)
        if e2["state"] == "disabled":
            e2["state"] = "normal"
        if c1["state"] == "disabled":
            c1["state"] = "normal"
        if c2["state"] == "disabled":
            c2["state"] = "normal"
        b4.grid_remove()
        if b1.winfo_ismapped() == 0:
            b1.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
    else:
        status_var.set("<Client not found!>")
        change_color(2)


def downloadFunction():
    global client_link
    if Clientstr.get() != "" and Clientstr.get() in clients and FileNameStr.get() != "" and CheckVar1.get() == 1:
        folderpath = os.path.join(os.getcwd(), 'xmls', f'{FileNameStr.get().upper()}.xml')
        if not os.path.exists(folderpath):
            change_color(3)
            try:
                clientlink()
                with open(client_link, 'r') as f:
                    client_link = f.read()
                testcase = client_link[client_link.find("=") + 1:client_link.find("&")]
                filename = FileNameStr.get().upper().replace(" ","")
                myfile = requests.get(client_link.replace(testcase, filename))
                with open(folderpath, "wb") as f:
                    f.write(myfile.content)
                status_var.set(f"<{FileNameStr.get()} has been downloaded for {Clientstr.get().upper()}_{library[CheckVar1.get() - 1]}>")
                change_color(1)
                FileNameStr.set("")
                Clientstr.set("")
                CheckVar1.set(0)
                b5.grid_remove()
                if b1.winfo_ismapped() == 0:
                    b1.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
            except FileNotFoundError:
                status_var.set(f"<{Clientstr.get().upper()}_{library[CheckVar1.get() - 1]} Download link is not available>")
                change_color(2)
            except(IOError, UnboundLocalError):
                status_var.set(f"<Please Enter a valid FileName Or ClientName & Select anyone library>")
                change_color(0)
            except requests.exceptions.MissingSchema:
                status_var.set(f"Test case not found on the portal!")
                change_color(2)
        else:
            status_var.set(f"{FileNameStr.get().upper()} is already exist, click on Options/Location")
            change_color(2)

    else:
        FileNameStr.set("")
        Clientstr.set("")
        CheckVar1.set(0)
        status_var.set(f"<Please Enter a valid FileName Or ClientName & Select anyone library>")
        change_color(0)


def multisourceFunction():
    global envelope_headpath, envelope_footpath, client_link
    success_count = 0
    if Clientstr.get() != "" and Clientstr.get() in clients and FileNameStr.get() != "" and CaseIDStr.get() != "":
        if CheckVar3.get() == 1 or CheckVar4.get() == 1 or CheckVar5.get() == 1:
            if len(FileNameStr.get())==11 and FileNameStr.get().isdigit():
                status_var.set(f"<Please wait, Multisource XML is downloading...>")
                change_color(3)
                Employee_ID = FileNameStr.get().upper().replace(" ","")
                Client_name = Clientstr.get().upper()
                CaseID = CaseIDStr.get().upper().replace(" ","")
                # Fetching Ariel Payroll XML
                if CheckVar3.get() == 1:
                    try:
                        scriptpath = os.path.join(os.getcwd(), "imp", "downloadlinks", f"{Client_name}_ArielPayroll.ps1")
                        with open(scriptpath, "r") as f:
                            commands = f.read()

                        commands = commands.replace("00000000000", Employee_ID)
                        result = subprocess.run(["powershell", "-command", commands], capture_output=True)
                        payrolldata = result.stdout
                        payrollxml = "<ArielPayroll>" + payrolldata.decode() + "</ArielPayroll>"
                        payrollxml = payrollxml.replace("\n", "")
                        payrollxmlpath = os.path.join(os.getcwd(),"xmls","multisource", f"{Employee_ID}PR.xml")
                        if Employee_ID in payrollxml:
                            with open(payrollxmlpath, "w") as f:
                                f.write(payrollxml)
                            success_count += 1
                        else:
                            messagebox.showerror(title="Abort", message="File not found at ArielPayroll portal")
                            status_var.set(f"<Employee ID is not available at ArielPayroll Portal...>")
                            change_color(2)

                    except(IOError, UnboundLocalError, FileNotFoundError):
                        status_var.set(f"<Please enter a valid client...>")
                        change_color(1)

                if CheckVar4.get() == 1 or CheckVar5.get() == 1:
                    try:
                        dbpath = os.path.join(os.getcwd(), "imp", "downloadlinks", f"{Client_name}_ArielDB.txt")
                        with open(dbpath) as f:
                            dbfilepath = f.read()
                        i = 0
                        inffile = ""
                        while i < len(Employee_ID) - 1:
                            i += 1
                            dbfilepath = dbfilepath + "\\" + Employee_ID[0:i]

                        for dbfilename in os.listdir(dbfilepath):
                            if dbfilename.endswith("INF.txt"):
                                with open(os.path.join(dbfilepath, dbfilename)) as f:
                                    infcontent = f.read()
                                    if Employee_ID in infcontent and CaseID in infcontent:
                                        inffile = dbfilename

                        dbfilename = inffile

                    except(IOError, UnboundLocalError, FileNotFoundError):
                        status_var.set(f"<Please enter a valid client & employee id>")
                        change_color(1)

                if CheckVar4.get() == 1:
                    # CRM TEST CASE ID Or Fetch Data for Ariel360 Case
                    try:
                        client_link = os.path.join(os.getcwd(), 'imp', 'downloadlinks', f'{Client_name}_Ariel360.txt')
                        with open(client_link, 'r') as f:
                            client_link = f.read()
                        testcase = client_link[client_link.find("=") + 1:client_link.find("&")]
                        client_link = client_link.replace(testcase, CaseID)
                        CRMfile = requests.get(client_link)
                        CRMfolderpath = os.path.join(os.getcwd(), "xmls", "multisource", f"{CaseID}.xml")
                        with open(CRMfolderpath, "wb") as f:
                            f.write(CRMfile.content)

                        with open(CRMfolderpath, "r") as f:
                            CRMfileContent = f.read()
                        CRMfileContent = "<Ariel360>" + CRMfileContent + "</Ariel360>"
                        CRMfileContent = CRMfileContent.replace('<?xml version="1.0" encoding="utf-8"?>', "")
                        with open(CRMfolderpath,"w") as f:
                            f.write(CRMfileContent)
                            success_count += 1
                        status_var.set(f"<{CaseID} has been downloaded for {Client_name}>")
                        change_color(1)

                    except(IOError, UnboundLocalError, FileNotFoundError):
                        status_var.set(f"<Please enter a valid client & employee id>")
                        change_color(0)

                    except requests.exceptions.MissingSchema:
                        status_var.set(f"Test case not found on the portal!")
                        messagebox.showerror(title="Abort", message="File not found at CRM portal")
                        change_color(2)

                if CheckVar5.get() == 1:
                    # fetching ArielDB XML
                    try:
                        dbfilename = dbfilename.replace("INF.txt", "STM.xml")
                        with open(os.path.join(dbfilepath, dbfilename), "r") as f:
                            ArielDBxml = f.read()
                            ArielDBxml = ArielDBxml.replace('<?xml version="1.0" encoding="utf-8"?>', "")
                            ArielDBxml = "<ArielDB>" + ArielDBxml + "</ArielDB>"

                        with open(os.path.join(os.getcwd(), "xmls", "multisource", f"{Employee_ID}STM.xml"), "w") as f:
                            f.write(ArielDBxml)
                            success_count += 1

                    except(IOError, UnboundLocalError, FileNotFoundError):
                        status_var.set(f"<Please enter a valid client & employee id>")
                        change_color(0)

                if success_count == 3 and payrollxml != "" and CRMfile != "" and ArielDBxml != "":
                    envelope_headpath = os.path.join(os.getcwd(), 'envelopes', f'{Client_name}_Multisource_Header.txt')
                    envelope_footpath = os.path.join(os.getcwd(), 'envelopes', f'Multisource_Footer.txt')
                    with open(envelope_headpath, "r") as f, open(envelope_footpath, "r") as f1:
                        header = f.read()
                        footer = f1.read()
                    multisourceXML = header + payrollxml + CRMfileContent + ArielDBxml + footer
                    with open(os.path.join(os.getcwd(), "xmls", "multisource", f"{Employee_ID}Multisource.xml"), "w") as f:
                        f.write(multisourceXML)
                    messagebox.showinfo(title="Task completed", message="Test case downloaded successfully")
                    status_var.set("Multisource XML has been downloaded successfully")
                    change_color(1)
                else:
                    messagebox.showwarning(title="Warning!", message="Something went wrong, please check location!")
                    status_var.set(f"<Please provide valid Employee ID & CASE ID>")
                    change_color(0)

            else:
                FileNameStr.set("")
                Clientstr.set("")
                CaseIDStr.set("")
                CheckVar3.set(1)
                CheckVar4.set(1)
                CheckVar5.set(1)
                status_var.set(f"<Please provide valid Employee ID & CASE ID>")
                change_color(0)

        else:
            FileNameStr.set("")
            Clientstr.set("")
            CaseIDStr.set("")
            CheckVar3.set(1)
            CheckVar4.set(1)
            CheckVar5.set(1)
            status_var.set(f"<Please Select Any Libraries>")
            change_color(0)

    else:
        FileNameStr.set("")
        Clientstr.set("")
        CaseIDStr.set("")
        CheckVar3.set(1)
        CheckVar4.set(1)
        CheckVar5.set(1)
        status_var.set(f"<Please Select Any Client & provide Employee ID & Case ID>")
        change_color(0)


def New():
    FileNameStr.set("")
    Clientstr.set("")
    addclientstr.set("")
    CheckVar1.set(0)
    l5.grid_remove()
    e1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    b4.grid_remove()
    b5.grid_remove()
    b6.grid_remove()
    c3.grid_remove()
    c4.grid_remove()
    c5.grid_remove()
    l4.grid_remove()
    l6.grid_remove()
    e3.grid_remove()
    e2.config(width=31)
    if e2["state"] == "disabled":
        e2["state"] = "normal"
    if c1["state"] == "disabled":
        c1["state"] = "normal"
    if c2["state"] == "disabled":
        c2["state"] = "normal"
    if e2.winfo_ismapped() == 0:
        e2.grid(row=2, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    if c1.winfo_ismapped() == 0:
        c1.grid(row=3, column=1, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    if c2.winfo_ismapped() == 0:
        c2.grid(row=3, column=2, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    if d1.winfo_ismapped() == 0:
        d1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    if b1.winfo_ismapped() == 0:
        b1.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
    if l3.winfo_ismapped() == 0:
        l3.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)

    status_var.set("Welcome to test case downloader!")
    change_color(0)


def auto_mate():
    FileNameStr.set("")
    Clientstr.set("")
    CheckVar1.set(0)
    e1.grid_remove()
    b1.grid_remove()
    b3.grid_remove()
    b4.grid_remove()
    b5.grid_remove()
    b6.grid_remove()
    l5.grid_remove()
    c3.grid_remove()
    c4.grid_remove()
    c5.grid_remove()
    l4.grid_remove()
    l6.grid_remove()
    e3.grid_remove()
    e2.config(width=31)
    if e2["state"] == "normal" or e2["state"] == "active":
        e2["state"] = "disabled"
    if e2.winfo_ismapped() == 0:
        e2.grid(row=2, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    if c1.winfo_ismapped() == 0:
        c1.grid(row=3, column=1, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    if c2.winfo_ismapped() == 0:
        c2.grid(row=3, column=2, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    if d1.winfo_ismapped() == 0:
        d1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    if b2.winfo_ismapped()==0:
        b2.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
    if l3.winfo_ismapped()==0:
        l3.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)

    status_var.set("Please Select Client & Library, Then Press Automate!")
    change_color(0)


def addClient():
    FileNameStr.set("")
    addclientstr.set("")
    Clientstr.set("")
    CheckVar1.set(0)
    d1.grid_remove()
    l3.grid_remove()
    b1.grid_remove()
    b2.grid_remove()
    b4.grid_remove()
    b5.grid_remove()
    b6.grid_remove()
    c3.grid_remove()
    c4.grid_remove()
    c5.grid_remove()
    l4.grid_remove()
    l6.grid_remove()
    e3.grid_remove()
    e2.config(width=31)
    if e2["state"] == "disabled":
        e2["state"] = "normal"
    if c1["state"] == "disabled":
        c1["state"] = "normal"
    if c2["state"] == "disabled":
        c2["state"] = "normal"
    if e2.winfo_ismapped() == 0:
        e2.grid(row=2, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    if c1.winfo_ismapped() == 0:
        c1.grid(row=3, column=1, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    if c2.winfo_ismapped() == 0:
        c2.grid(row=3, column=2, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    if e1.winfo_ismapped() == 0:
        e1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    if l5.winfo_ismapped() == 0:
        l5.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
    if b3.winfo_ismapped() == 0:
        b3.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)

    status_var.set("Please Type Client, Paste Envelope, Select Library, then press ADD!")
    change_color(0)


def delClient():
    FileNameStr.set("")
    Clientstr.set("")
    CheckVar1.set(0)
    e1.grid_remove()
    l5.grid_remove()
    b1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    b5.grid_remove()
    b6.grid_remove()
    c3.grid_remove()
    c4.grid_remove()
    c5.grid_remove()
    l4.grid_remove()
    l6.grid_remove()
    e3.grid_remove()
    e2.config(width=31)
    if e2.winfo_ismapped() == 0:
        e2.grid(row=2, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    if e2["state"] == "normal" or e2["state"] == "active":
        e2["state"] = "disabled"
    if c1["state"] == "normal" or c1["state"] == "active":
        c1["state"] = "disabled"
    if c2["state"] == "normal" or c2["state"] == "active":
        c2["state"] = "disabled"
    if c1.winfo_ismapped() == 0:
        c1.grid(row=3, column=1, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    if c2.winfo_ismapped() == 0:
        c2.grid(row=3, column=2, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    if d1.winfo_ismapped() == 0:
        d1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    if l3.winfo_ismapped() == 0:
        l3.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
    if b4.winfo_ismapped() == 0:
        b4.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)

    status_var.set("Please Select Client, Then Press Delete!")
    change_color(0)


def download():
    FileNameStr.set("")
    Clientstr.set("")
    CheckVar1.set(0)
    e1.grid_remove()
    b1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    b4.grid_remove()
    l5.grid_remove()
    b6.grid_remove()
    c3.grid_remove()
    c4.grid_remove()
    c5.grid_remove()
    l4.grid_remove()
    l6.grid_remove()
    e3.grid_remove()
    e2.config(width=31)
    if e2["state"] == "disabled":
        e2["state"] = "normal"
    if c1["state"] == "disabled":
        c1["state"] = "normal"
    if c2["state"] == "disabled":
        c2["state"] = "normal"
    if e2.winfo_ismapped() == 0:
        e2.grid(row=2, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    if d1.winfo_ismapped() == 0:
        d1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    if c1.winfo_ismapped() == 0:
        c1.grid(row=3, column=1, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    if c2.winfo_ismapped() == 0:
        c2.grid(row=3, column=2, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    if l3.winfo_ismapped() == 0:
        l3.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
    if b5.winfo_ismapped() == 0:
        b5.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)

    status_var.set("Welcome to test case downloader!")
    change_color(0)


def multisource():
    FileNameStr.set("")
    Clientstr.set("")
    CaseIDStr.set("")
    CheckVar1.set(0)
    CheckVar3.set(1)
    CheckVar4.set(1)
    CheckVar5.set(1)
    b1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    b4.grid_remove()
    b5.grid_remove()
    c1.grid_remove()
    c2.grid_remove()
    l3.grid_remove()
    l5.grid_remove()
    e1.grid_remove()
    e2.config(width=13)
    if e2.winfo_ismapped() != 0:
        e2.grid(row=2, column=2, padx=10, pady=10, ipadx=2, ipady=2, sticky=tkinter.W)
    if e2["state"] == "disabled":
        e2["state"] = "normal"
    if l4.winfo_ismapped() == 0:
        l4.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
    if l6.winfo_ismapped() == 0:
        l6.grid(row=2, column=3, padx=10, pady=10, ipadx=2, ipady=2)
    if e2.winfo_ismapped() == 0:
        e2.grid(row=2, column=2, padx=10, pady=10, ipadx=2, ipady=2, sticky=tkinter.W)
    if e3.winfo_ismapped() == 0:
        e3.grid(row=2, column=4, padx=10, pady=10, ipadx=2, ipady=2)
    if d1.winfo_ismapped() == 0:
        d1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    if b6.winfo_ismapped() == 0:
        b6.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
    if c3.winfo_ismapped() == 0:
        c3.grid(row=3, column=1, ipadx=2, ipady=2, sticky=tkinter.EW)
    if c4.winfo_ismapped() == 0:
        c4.grid(row=3, column=2, ipadx=2, ipady=2, sticky=tkinter.EW)
    if c5.winfo_ismapped() == 0:
        c5.grid(row=3, column=3, ipadx=2, ipady=2, sticky=tkinter.EW)

    status_var.set("Welcome to test case downloader!")
    change_color(0)


# Multisource Variables
CheckVar3 = tkinter.IntVar()
CheckVar4 = tkinter.IntVar()
CheckVar5 = tkinter.IntVar()
c3 = tkinter.Checkbutton(window, text="ArielPayroll", variable=CheckVar3, font=font3)
c4 = tkinter.Checkbutton(window, text="Ariel360", variable=CheckVar4, font=font3)
c5 = tkinter.Checkbutton(window, text="ArielDB", variable=CheckVar5, font=font3)

# Status Bar
status_var = tkinter.StringVar()
status_var.set("Welcome to test case downloader!")
status_bar = tkinter.Label(window, textvariable=status_var, anchor=tkinter.N, font=('Helvetica', 12, 'bold'))

# variables
Clientstr = tkinter.StringVar()
FileNameStr = tkinter.StringVar()
CaseIDStr = tkinter.StringVar()
CheckVar1 = tkinter.IntVar()
addclientstr = tkinter.StringVar()
addclientstr.trace("w", lambda name, index,mode, addclientstr=addclientstr: callback(addclientstr))
client_path = os.path.join(os.getcwd(), 'imp', 'Clients.txt')
library = ['Ariel360', 'ArielDB']
brand = copyryt + 'AkantMalviya'

# image logo
img = tkinter.PhotoImage(master=window, file="images/logo.png")
img = img.subsample(4,4)
logo = tkinter.Label(master=window, image=img, background='white')
# Labels and Entry
l1 = tkinter.Label(window, text=brand, background='white')
l2 = tkinter.Label(window, text="CLIENT NAME :", font=font1, borderwidth=0, relief="solid")
l3 = tkinter.Label(window, text="TEST CASE NAME :", font=font1, borderwidth=0, relief="solid")
l4 = tkinter.Label(window, text="EMPLOYEE ID :", font=font1, borderwidth=0, relief="solid")
l5 = tkinter.Label(window, text="ENVELOPE HEADER :", font=font1, borderwidth=0, relief="solid")
l6 = tkinter.Label(window, text="CASE ID :", font=font1, borderwidth=0, relief="solid")
e1 = tkinter.Entry(window, width=31, font=font4, borderwidth=1, relief="solid",textvariable=addclientstr, selectbackground="Yellow", selectforeground="black")
e2 = tkinter.Entry(window, width=31, font=font4, borderwidth=1, relief="solid",textvariable=FileNameStr, selectbackground="Yellow", selectforeground="black")
e3 = tkinter.Entry(window, width=16, font= font4, borderwidth=1, relief="solid",textvariable=CaseIDStr, selectbackground="Yellow", selectforeground="black")
# Combobox and Client Name list
d1 = ttk.Combobox(window, width=30, font=font4, textvariable=Clientstr)
window.option_add("*TCombobox*Listbox*Font", font2)
refreshClients()

# Radio Buttons and Action Buttons
c1 = tkinter.Radiobutton(window, text="Ariel360", variable=CheckVar1, value=1, font=font3)
c2 = tkinter.Radiobutton(window, text="ArielDB", variable=CheckVar1, value=2, font=font3)

b1 = tkinter.Button(window, text="ENVELOPE", command=submitFunction, font=font1)
b1.config(width=15, height=1)
b2 = tkinter.Button(window, text="AUTOMATE", command=AutomateFunction, font=font1)
b2.config(width=15, height=1)
b3 = tkinter.Button(window, text="ADD", command=AddFunction, font=font1)
b3.config(width=15, height=1)
b4 = tkinter.Button(window, text="DELETE", command=delFunction, font=font1)
b4.config(width=15, height=1)
b5 = tkinter.Button(window, text="DOWNLOAD", command=downloadFunction, font=font1)
b5.config(width=15, height=1)
b6 = tkinter.Button(window, text="MULTISOURCE", command=multisourceFunction, font=font1)
b6.config(width=15, height=1)

# Menubar Options Help
font5 = ('Times', 12, 'bold')
menubar = tkinter.Menu()
window.config(menu=menubar)
options_menu = tkinter.Menu(menubar)
help_menu = tkinter.Menu(menubar)

menubar.add_cascade(menu=options_menu, label="Options")
menubar.add_cascade(menu=help_menu, label="Help")

options_menu.add_command(label="New",font=font5, command=lambda: New())
options_menu.add_command(label="Location",font=font5, command=lambda:location())
options_menu.add_command(label="Automate",font=font5, command=lambda: auto_mate())
options_menu.add_command(label="Download",font=font5, command=lambda: download())
options_menu.add_command(label="Add Client",font=font5, command=lambda:addClient())
options_menu.add_command(label="Delete Client",font=font5, command=lambda:delClient())
options_menu.add_command(label="MultisourceXML",font=font5, command=lambda:multisource())
options_menu.add_command(label="Exit",font=font5, command=lambda:quit_app())
help_menu.add_command(label="About",font=font5, command=lambda:show_about_info())

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


# Grid Function
def gridFunction():
    logo.grid(sticky=tkinter.NW, row=0, column=0, padx=10, pady=10, ipadx=2, ipady=2)
    l2.grid(row=1, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
    d1.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2, columnspan=3, sticky=tkinter.W)
    l3.grid(row=2, column=1, sticky=tkinter.W, padx=10, pady=10, ipadx=2, ipady=2)
    e2.grid(row=2, column=2, padx=10, pady=10, ipadx=2, ipady=2)
    c1.grid(row=3, column=1, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    c2.grid(row=3, column=2, ipadx=2, ipady=2, rowspan=1, columnspan=2)
    b1.grid(row=4, column=1, padx=10, pady=10, rowspan=3, columnspan=3)
    status_bar.grid(row=45, column=1, columnspan=3, sticky="ew",padx=10, pady=20)


gridFunction()
window.mainloop()
# Code Written by Akant Malviya
