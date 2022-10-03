from tkinter import Label, Tk 
import time
clk_window = Tk() 
clk_window.title("Data Liness Clock") 
clk_window.geometry("570x180") 
clk_window.resizable(0,0)
txt_font= ("Arial", 102, 'bold')
bg_color = "#08044C"
foreground= "#F4FF05"
border = 15
label = Label(clk_window, font=txt_font, bg=bg_color, fg=foreground, bd=border) 
label.grid(row=0, column=1)
def dataliness_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(500, dataliness_clock)
dataliness_clock()
clk_window.mainloop()