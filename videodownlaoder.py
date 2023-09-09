from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil

def get_path():
    path= filedialog.askdirectory()
    path_label.config(text='path')

def download():
    video_path=url_entry.get()
    file_path=path_label.cget("text")
    print("downloading...........")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip =VideoClip(mp4)

    audio_clip=video_clip.audio
    audio_clip.write_audiofile('audio.mp3')
    audio_clip.close()
    shutil.move(mp4,audio_clip)



    video_clip.close()
    shutil.move(mp4,file_path)
    print("downloaded")





root =Tk()


root.title('video downloader')
canvas = Canvas(root,width=400,height=300)
canvas.pack()


app_label=Label(root,text='Video Downloader',fg='blue',font=('Arial',30))
canvas.create_window(200,20,window=app_label)



url_label=Label(root,text="enter the video url")
url_entry=Entry(root)
canvas.create_window(200,80,window=url_label)
canvas.create_window(200,100,window=url_entry)
path_label=Label(root,text="select the path too save the video")
path_button=Button(root,text="Select",command=get_path)

canvas.create_window(200,150,window=path_label)
canvas.create_window(200,170,window=path_button)

download_button= Button(root,text="Download",command=download)
canvas.create_window(200,250,window=download_button)


root.mainloop()