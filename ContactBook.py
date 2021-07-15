import tkinter
from tkinter import messagebox
from tkinter import Tk
from tkinter import *

#1. Button Add
def addFun():
    if contactName.get() != "" and PhoneNumber.get() != "":
        with open("contactBook.txt" , "a") as file:
            file.write("\n" + contactName.get() + " : ")
            file.write(PhoneNumber.get())
        messagebox.showinfo("result","\nYour phone number added in contact book")

#2. Button remove
def removeFun():
    phoneNum = ""
    remove = False
    result = False
    with open("contactBook.txt" , "r") as ReadMode:
        reader = ReadMode.readlines()
    for data in reader:
        data = data.split(" : ")
        if data[0] == contactName.get() :
            phoneNum = data[1]
            pop_data = contactName.get() + " : " + phoneNum.rstrip("\n")
            result = messagebox.askyesno("result",pop_data+"\nDo you want remove it ?")
            remove = True
            break
    if remove == False:
        messagebox.showerror("Error" ,"Name not found")

    if result == True :
        with open("contactBook.txt" , "w") as WriteMode:
            for data in reader:
                if data.strip("\n") != pop_data :
                    WriteMode.write(data)
        messagebox.showinfo( " result ",pop_data + " is remove.")

#3. Button search
def searchFun():
    phoneNum = ""
    find = False
    with open("contactBook.txt" , "r") as ReadMode:
        reader = ReadMode.readlines()
    for data in reader:
        data = data.split(" : ")
        if data[0] == contactName.get() :
            phoneNum = data[1]
            find_data = contactName.get() + " : " + phoneNum.rstrip("\n")
            messagebox.showinfo("Search",find_data)
            find = True
            break
    if find != True:
        messagebox.showerror("Error" ,"Name not found")

#4. Button show
def showFun():
    with open("contactBook.txt" , "r") as ReadMode:
        FileWithEmptyLines =  ReadMode.read()
        lines = FileWithEmptyLines.split("\n")
        NonEmptyLines = [line for line in lines if line.strip() != ""]
        Final_file = "" #without empty lines
        for line in NonEmptyLines:
              Final_file += line + "\n"

        messagebox.showinfo("Phone number list",Final_file)

#5. Button Exit
def ExitFun():
    main.destroy()

#Main program
main = Tk()
main.title("Contact book")
main.geometry("370x200")
main.resizable(width = False, height = False)
main['bg'] = '#ffb997'

#Variable
contactName = StringVar()
PhoneNumber = StringVar()

# name and phone number Entry
name = Label(main , text = "Name" , width = 15)
name['bg'] = '#621940'
name['fg'] = 'white'
nameFild = Entry(main , textvariable = contactName)
name.pack()
nameFild.pack()
name.place(x = 10 , y = 10 )
nameFild.place(x = 130 , y = 10)

phoneNum = Label(main , text = "Phone number" , width = 15)
phoneNum['bg'] = '#621940'
phoneNum['fg'] = 'white'
phoneNumFild = Entry(main , textvariable = PhoneNumber)
phoneNum.pack()
phoneNumFild.pack()
phoneNum.place(x = 10 , y = 40)
phoneNumFild.place(x = 130 , y = 40)

#add Button
add = tkinter.Button(main , text = "add phone number" , width = 20 , command = addFun)
add['bg'] = '#f67e7d'
add.pack()
add.place(x = 10 , y = 80)

#remove Button
remove = tkinter.Button(main , text = "remove phone number" , width = 20 , command = removeFun)
remove['bg'] = '#f67e7d'
remove.pack()
remove.place(x = 200 , y = 80)

#search Button
search = tkinter.Button(main , text = "search phone number" , width = 20 , command = searchFun)
search['bg'] = '#f67e7d'
search.pack()
search.place(x = 10 , y = 110)

#show Button
Show = tkinter.Button(main , text = "show phone number" , width = 20 , command = showFun)
Show['bg'] = '#f67e7d'
Show.pack()
Show.place(x = 200 , y = 110)

#exit Button
Exit = tkinter.Button(main , text = "Exit" , width = 10 , command = ExitFun)
Exit['bg'] = '#843b62'
Exit.pack()
Exit.place(x = 140 , y = 150)

main.mainloop()
