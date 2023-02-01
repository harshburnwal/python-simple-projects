from tkinter import *
from tkinter import dialog
from pytube import YouTube

box = Tk()
box.geometry('600x350')
box.title("Youtube video downloader by $adhu")

label_1 = Label(box, text="Youtube Video Downloader",
                font="arial 24 bold").pack()
link = StringVar()
label_2 = Label(box, text="Paste link here:",
                font="arial 15 bold").place(x=225, y=95)
Entry(box, width=70, textvariable=link).place(x=80, y=125)


def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    # Please provide the download path
    video.download('D:\VS Code\YT Downloader')
    # video.download('Enter here your desireable path')
    label_3 = Label(box, text="Successfully Downloaded",
                    font='arial 15').place(x=190, y=230)
    label_4 = Label(box, text="at "+video.download(),
                    font='arial 12').place(x=25, y=260)


btn = Button(box, text="Download", font='arial 15 bold',
             bg='violet red', padx=2, command=downloader).place(x=225, y=170)
box.mainloop()
