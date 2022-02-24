from tkinter import *
from tkinter import font
from pytube import YouTube
import requests

def URLCheck(url):
    try:
        r = requests.get(url)
    except requests.exceptions.MissingSchema as exception:
        notice.set("Not an URL")
        return False
    except requests.exceptions.ConnectionError:
        notice.set("Not an URL")
        return False
    return True

def download():
    if URLCheck(link.get()):
        try:
            url = YouTube(str(link.get()))
            video = url.streams.first()
            video.download()
            notice.set("DOWNLOADED")
        except:
            notice.set("Video No Available")

window = Tk()
window.geometry("500x300")
window.resizable(0, 0)
window.title("YouTube Downloader")
Label(window, text="Enter Link Here:", font=("arial", 15, "bold")).place(x=160, y=60)
link = StringVar()
enteredText = Entry(window, textvariable=link, width=70).place(x=32, y=90)
notice = StringVar()
notice.set("")
temp = Label(window, textvariable=notice, font=("arial", 15)).place(x=180, y=210)
Button(window, text="DOWNLOAD", font=("arial", 15, "bold"), bg="pale violet red", padx=2, command=download).place(x=180, y=150)
mainloop()