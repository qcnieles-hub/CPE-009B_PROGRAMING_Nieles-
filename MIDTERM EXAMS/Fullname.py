from tkinter import *

class MidtermOOP:
    def __init__(self, root):
        self.root = root
        self.root.title("Midterm in OOP")
        self.root.geometry("800x450")

        # Fullname Label
        self.label = Label(self.root, text="Enter your fullname:",
                           font=("Arial", 12), fg="brown")
        self.label.place(x=100, y=150)

        # Input Textbox
        self.input_name = Entry(self.root, font=("Arial", 18), width=25)
        self.input_name.place(x=400, y=145)

        # Button
        self.button = Button(self.root, text="Click to display your fullname",
                             font=("Arial", 12), fg="brown",
                             command=self.display_name)
        self.button.place(x=100, y=220)

        # Output Textbox
        self.output_name = Entry(self.root, font=("Arial", 18), width=25)
        self.output_name.place(x=400, y=211)

    def display_name(self):
        fullname = self.input_name.get()
        self.output_name.delete(0, END)
        self.output_name.insert(0, fullname)

root = Tk()
app = MidtermOOP(root)
root.mainloop()
