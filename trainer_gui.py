from Tkinter import *



class TrainGUI:

    def __init__(self):
        self.root = Tk()
        self.label = Label(self.root, text="LABEL")
        self.entry = Entry(self.root, bd = 5)
        self.submit = Button(self.root, text ="Submit", command=self.label_submitted)


    def label_submitted(self):
        print self.entry.get()

    def run(self):
        self.label.pack()
        self.entry.pack()
        self.submit.pack(side =BOTTOM) 
        self.root.mainloop()


# if __name__ == '__main__':
#     train_gui = TrainGUI()
#     train_gui.run()