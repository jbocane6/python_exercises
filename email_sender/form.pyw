# !/usr/bin/python3
from tkinter import Tk, messagebox, END, Label, Entry, Text, Button
from email_validator import validate_email, EmailNotValidError
from functools import partial
import sender as s


def validate(lst):
    for mail in lst:
        try:
            # Check that the email address is valid.
            validation = validate_email(mail, check_deliverability=True)
        except EmailNotValidError:
            # Email is not valid.
            return False
    return True


# Validates all fields are filled and send args to send mail
def send(receiverField, subjectField, bodyMessageField):
    receivers = receiverField.get()
    lst = receivers.split(',')
    if receivers == "":
        messagebox.showinfo("Error", "Please insert receiver mail")
    elif not validate(lst):
        messagebox.showinfo("Error", "Verify email format")
    elif subjectField.get() == "" or bodyMessageField.get("1.0", END) == "":
        messagebox.showinfo("Error", "Please fill fields to send mail")
    else:
        s.sendmail(lst, subjectField.get(), bodyMessageField.get("1.0", END))
        receiverField.delete(0, END)
        subjectField.delete(0, END)
        bodyMessageField.delete("1.0", END)
        messagebox.showinfo("Success", "Message sent")


def main():
    root = Tk()
    root.configure(background='light gray')
    root.title("Email sender")
    root.geometry("500x300")

    # Labels
    heading = Label(root, text="Email sender", bg="light gray")
    receiver = Label(root, text="CC", bg="light gray")
    subject = Label(root, text="Subject", bg="light gray")
    bodyMessage = Label(root, text="Message", bg="light gray")

    # Align labels
    heading.grid(row=0, column=1)
    receiver.grid(row=1, column=0)
    subject.grid(row=2, column=0)
    bodyMessage.grid(row=3, column=1)

    # Entry boxes for typing the information
    receiverField = Entry(root)
    subjectField = Entry(root)
    bodyMessageField = Text(root, height=10, width=50)

    # Align fields
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
