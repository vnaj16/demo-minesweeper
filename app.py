from tkinter import *
import settings

root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("VNAJ Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="red", #change to black
    width=settings.WIDTH,
    height=settings.TOP_FRAME_HEIGHT
)
top_frame.place(x=0,y=0)

left_frame = Frame(
    bg="blue",
    width=settings.LEFT_FRAME_WIDTH,
    height=settings.HEIGHT - settings.TOP_FRAME_HEIGHT
)
left_frame.place(x=0, y=settings.TOP_FRAME_HEIGHT)


# Run the window
root.mainloop()