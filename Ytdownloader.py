from tkinter import *
from PIL import Image, ImageTk
import urllib.request
import io
import re
from urllib.parse import urlparse
import pytube
from tkinter import messagebox








root = Tk()
root.geometry('+%d+%d'%(150,10))
root.title("Youtube video downloader")

url=""

def focus_out_entry_box(widget, widget_text):
    if widget['fg'] == 'Black' and len(widget.get()) == 0:
        widget.delete(0, END)
        widget['fg'] = 'Grey'
        widget.insert(0, widget_text)


def focus_in_entry_box(widget):
    if widget['fg'] == 'Grey':
        widget['fg'] = 'Black'
        widget.delete(0, END)


def resize_image(img):
    width, height = int(img.size[0]), int(img.size[1])
    if width > height:
        height = int(300/width*height)
        width = 300
    elif height > width:
        width = int(250/height*width)
        height = 250
    else:
        width, height = 250,250
    img = img.resize((width, height))
    return img
def display_images(img):
    img = resize_image(img)
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="white")
    img_label.image = img
    img_label.grid(row=4, column=2, rowspan=2)
    return img_label

def downloadv(video):
    video.download('/Downloads')
    messagebox.showinfo("Success", "finishid")

def search():
    url=my_entry.get()
    url_data = urlparse(url)
    print(url_data.query[2::])
    it=url_data.query[2::]
    imgUrl = f"https://img.youtube.com/vi/{it}/maxresdefault.jpg"
    print(imgUrl)
    raw_data = urllib.request.urlopen(imgUrl).read()
    
    im = Image.open(io.BytesIO(raw_data))
    display_images(im)
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    lab=Label(text=video.title,bg="#fff")
    lab.grid( row=4,column=0)
    btn2 = Button( text = 'Download !',  command= lambda: downloadv(video))
    btn2.grid(row=5,column=0)


header = Frame(root, width=800, height=150, bg="#FF0000")
header.grid(columnspan=3, rowspan=2, row=0)


main_content = Frame(root, width=800, height=250, bg="white")
main_content.grid(columnspan=3, rowspan=2, row=4)
header.grid_propagate(False)
header.pack_propagate(False)
logo = Label(header, text='Youtube Downloader', font='Helvetica 18 bold',bg="#ff0000",fg="#fff")
logo.pack()

entry_text = 'Youtube video Url'
my_entry = Entry(header,font='Arial 18', fg='Grey',width=40)
my_entry.insert(0, entry_text)
my_entry.bind("<FocusIn>", lambda args: focus_in_entry_box(my_entry))
my_entry.bind("<FocusOut>", lambda args: focus_out_entry_box(my_entry, entry_text))
my_entry.pack()

btn1 = Button(header, text = 'Search !',
                
             command = search)

btn1.pack(padx=20, pady=20)             
root.mainloop()