# !/usr/bin/python3
import values as v
from logging import shutdown
import tkinter as tk


def main():
    # root window
    root = tk.Tk()
    root.geometry(str(v.wwdw) + 'x' + str(v.hwdw))
    root.resizable(False, False)
    root.title("Shutdown menu")

    # create buttons and icons and pack
    for op in {"shutdown", "reboot", "hibernate"}:
        if op == "shutdown":
            shutdown_icon = v.icon("shutdown")
            shutdown_button = v.opbutton(root, "shutdown", shutdown_icon)
            v.pack(shutdown_button)
        elif op == "reboot":
            reboot_icon = v.icon("reboot")
            reboot_button = v.opbutton(root, "reboot", reboot_icon)
            v.pack(reboot_button)
        elif op == "hibernate":
            hibernate_icon = v.icon("hibernate")
            hibernate_button = v.opbutton(root, "hibernate", hibernate_icon)
            v.pack(hibernate_button)

    # screen width and height
    wscr = root.winfo_screenwidth()
    hscr = root.winfo_screenheight()

    # coordinates window
    pwidth = round(wscr/2 - v.wwdw/2)
    pheight = round(hscr/2 - v.hwdw/2)

    # no window manager decorations
    root.attributes('-toolwindow', True)

    # center window
    root.geometry(str(v.wwdw) + "x" + str(v.hwdw) + "+" + str(pwidth) + "+" +
                  str(pheight))

    root.mainloop()


if __name__ == "__main__":
    main()
