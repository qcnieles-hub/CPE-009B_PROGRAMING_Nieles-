from tkinter import *

class MidtermExam:
    def __init__(self, root):
        self.root = root
        self.root.title("Special Midterm Exam in OOP")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        self.button = Button(
            self.root,
            text="Click to Change Color",
            font=("Arial", 12, "bold"),
            command=self.change_color
        )
        self.button.place(relx=0.5, rely=0.5, anchor=CENTER)

    def change_color(self):
        self.button.configure(bg="yellow")

root = Tk()
app = MidtermExam(root)
root.mainloop()
