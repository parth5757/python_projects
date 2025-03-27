from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=YDnQvxhldvE"
# yt = YouTube(url, on_progress_callback=on_progress)
yt = YouTube(url, on_progress_callback=on_progress)

print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()