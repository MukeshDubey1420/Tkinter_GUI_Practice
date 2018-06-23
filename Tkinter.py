from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("<-- Mukesh Dubey -->")

        self.label = Label(master, text="Welcome To My First GUI !!")
        self.label.pack()

        self.greet_button = Button(master, text="Hi User ,, I am Mukesh Dubey ...", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()