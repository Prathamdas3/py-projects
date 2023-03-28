import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishLable.configure(text="")
        video.download()
    except:
        finishLable.configure(text="Youtube link is invalid", text_color="red")
    finishLable.configure(text="Downloaded!", text_color="blue")


# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame(title, size)
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Download")


# Adding UI ELements
title = customtkinter.CTkLabel(app, text="Insert a Youtube link")
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# finished downloading
finishLable = customtkinter.CTkLabel(app, text='')
finishLable.pack()


# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=0, pady=10)

# run app(looping the app)
app.mainloop()
