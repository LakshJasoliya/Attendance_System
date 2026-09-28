from tkinter import *
from PIL import Image, ImageTk
import os

class Devloper:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendence")
        self.root.wm_iconbitmap("face.ico")

        frame1 = Frame(root, bg="lightblue",bd=2,relief=SOLID)
        frame1.place(x=0, y=0, width=780, height=260)  # Position and size the frame
        
       

         # add lable
        label1 = Label(frame1, text='''ID                    
                       ''',font=("Arial", 14), bg="lightblue",bd=2,relief=SOLID)
        label1.place(x=300,y=30)


        

        
        # frame1_1
        frame1_1 = Frame(root, bg="lightblue",bd=2,relief=SOLID)
        frame1_1.place(x=0, y=215, width=780, height=230)

        label1 = Label(frame1_1, text='''ID                    
                       ''',font=("Arial", 14), bg="lightblue",bd=2,relief=SOLID)
        label1.place(x=300,y=30)

        
        # frame1_2
        frame1_2 = Frame(root, bg="lightblue",bd=2,relief=SOLID)
        frame1_2.place(x=0, y=415, width=780, height=230)

        label1 = Label(frame1_2, text='''ID                    
                       ''',font=("Arial", 14), bg="lightblue",bd=2,relief=SOLID)
        label1.place(x=300,y=30)

        # frame1_3
        frame1_3 = Frame(root, bg="lightblue",bd=2,relief=SOLID)
        frame1_3.place(x=0, y=615, width=780, height=230)

        label1 = Label(frame1_3, text='''ID                    
                       ''',font=("Arial", 14), bg="lightblue",bd=2,relief=SOLID)
        label1.place(x=300,y=30)

        # First GIF
        self.frames1 = self.load_gif(r"college_images/h.gif")  # Path to the first GIF
        self.gif_label1 = Label(frame1, bg="lightblue")
        self.gif_label1.place(x=0, y=4)
        self.animate_gif(self.frames1, self.gif_label1)

        # Second GIF
        self.frames2 = self.load_gif(r"college_images/h.gif")  # Path to the second GIF
        self.gif_label2 = Label(frame1_1, bg="lightblue")
        self.gif_label2.place(x=0, y=0)
        self.animate_gif(self.frames2, self.gif_label2)

        # Third GIF (can be added similarly)
        self.frames3 = self.load_gif(r"college_images/h.gif")  # Path to the third GIF
        self.gif_label3 = Label(frame1_2, bg="lightblue")
        self.gif_label3.place(x=0, y=0)
        self.animate_gif(self.frames3, self.gif_label3)

         # Fourth GIF (can be added similarly)
        self.frames3 = self.load_gif(r"college_images/h.gif")  # Path to the third GIF
        self.gif_label3 = Label(frame1_3, bg="lightblue")
        self.gif_label3.place(x=0, y=0)
        self.animate_gif(self.frames3, self.gif_label3)

        img3 = Image.open(r"college_images/BestFacialRecognition.jpg").resize((750, 790))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        frame2 = Frame(root, bg="lightblue", bd=2, relief=SOLID)
        frame2.place(x=780, y=0, width=750, height=790)

        img_label = Label(frame2, image=self.photoimg3, bg="lightblue")
        img_label.pack()

    def load_gif(self, gif_path):
        """Load frames from the GIF and return the frames list."""
        gif = Image.open(gif_path)
        frames = []
        try:
            while True:
                frames.append(ImageTk.PhotoImage(gif.copy()))
                gif.seek(len(frames))  # Load next frame
        except EOFError:
            pass  # End of GIF
        return frames

    def animate_gif(self, frames, gif_label, current_frame=0):
        """Animate GIF by looping through frames."""
        gif_label.config(image=frames[current_frame])
        current_frame = (current_frame + 1) % len(frames)  # Loop through frames
        self.root.after(100, self.animate_gif, frames, gif_label, current_frame)



    # Frame 2
        


        
    def open_img(self):
        os.startfile("data")

# Main Application
if __name__ == "__main__":
    root = Tk()
    obj = Devloper(root)
    root.mainloop()

