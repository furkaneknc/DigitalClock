from tkinter import Label,Tk 
import time

app_windows = Tk() 
app_windows.title("Dijital Saat")
app_windows.geometry("460x210") 
app_windows.resizable(0,0) 
app_windows.configure(bg="black")

text_font = ("Boulder",36,'bold')
background = "black"
foreground = "blue"
border_width = 40

#SAAT ETİKETİ
label = Label(app_windows, font= text_font, bg=background, fg=foreground ) 
label.grid(row=0,column=1,padx=10,pady=10)


#TARİH ETİKETİ
date_label = Label(app_windows,font=text_font,bg=background,fg=foreground)
date_label.grid(row=1,column=1,padx=10,pady=10)


def digital_clock():
    time_live = time.strftime("%H:%M:%S") #değişkene anlık saat verisi cektim ve atadım . 
    label.config(text=time_live) 

    date_info = time.strftime("%d %B %Y")
    date_label.config(text=date_info)
    label.after(200,digital_clock)
digital_clock()

app_windows.mainloop()