# !/usr/bin/python3
from tkinter import Tk, messagebox, END, Label, Entry, Text, Button
from functools import partial
import sender as s


def send(receiverField, subjectField, bodyMessageField):
    if receiverField.get() == "":
        print("Please insert receiver mail")
    elif subjectField.get() == "" or bodyMessageField.get("1.0", END) == "":
        print("Please fill fields to send mail")
    else:
        s.send(receiverField.get(), subjectField.get(),
               bodyMessageField.get("1.0", END))
        receiverField.delete(0, END)
        subjectField.delete(0, END)
        bodyMessageField.delete("1.0", END)
        messagebox.showinfo("Success", "Message sent")


def main():
    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    root.configure(background='light gray')

    # set the title of GUI window
    root.title("Email sender")

    # set the configuration of GUI window
    root.geometry("500x300")

    # create a Form label
    heading = Label(root, text="Email sender", bg="light gray")

    # create a Name label
    receiver = Label(root, text="CC", bg="light gray")

    # create a Course label
    subject = Label(root, text="Subject", bg="light gray")

    # create a Semester label
    bodyMessage = Label(root, text="Message", bg="light gray")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    receiver.grid(row=1, column=0)
    subject.grid(row=2, column=0)
    bodyMessage.grid(row=3, column=1)

    # create a text entry box
    # for typing the information
    receiverField = Entry(root)
    subjectField = Entry(root)
    bodyMessageField = Text(root, height=10, width=50)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    receiverField.grid(row=1, column=1, ipadx="100")
    subjectField.grid(row=2, column=1, ipadx="100")
    bodyMessageField.grid(row=4, column=1)

    # create a Submit Button and place into the root window
    submit = Button(root, text="Submit", fg="Black", bg="Grey",
                    command=partial(send, receiverField, subjectField,
                                    bodyMessageField))
    submit.grid(row=8, column=1)

    # start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()
