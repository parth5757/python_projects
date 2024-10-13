from moviepy.editor import VideoFileClip
from tkinter import Tk
from tkinter import filedialog

# Hide the root tkinter window
Tk().withdraw()

# Take input MP4 video file

input_file = filedialog.askopenfilename(
    title="Select MP4 Videos",
    filetype = [("MP4 file", "*.mp4")]
)

if input_file:
    # Take input where gif file will store with the name
    output_file = filedialog.asksaveasfilename(
        title="Save File as...",
        defaultextension=".gif",
        filetypes=[("GIF files", "*gif")]
    )

    if output_file:
        # load the MP4 file
        clip = VideoFileClip(input_file)
        # save the file at selected place
        clip.write_gif(output_file)

        print(f"GIF has been saved at{output_file}")
    else:
        print("No path selected to save")
else:
    print("No input path selected")