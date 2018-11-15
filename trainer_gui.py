from Tkinter import *
from Database.db_config import DB
from functools import partial


class TrainGUI:

    TOTAL_TRAINED_DATA = 0
    LABEL_TEXT = None
    
    
    def __init__(self,*args):
        self.root = Tk()
        TrainGUI.LABEL_TEXT = StringVar()
        TrainGUI.LABEL_TEXT.set("TOTAL TRAINED DATA: %d"%TrainGUI.TOTAL_TRAINED_DATA)
        self.root.geometry("300x200+500+200")
        self.entry = Entry(self.root, bd = 5)    
        self.label = Label(self.root, textvariable=TrainGUI.LABEL_TEXT)
        self.submit = Button(self.root, text ="Submit", command=partial(self.label_submitted, *args))
        self.db = DB('leapd')

    def label_submitted(self,*args):
        label = self.entry.get()
        if len(label) != 1 or not label.isalpha():
            print 'Please enter a valid label'
            return
        TrainGUI.TOTAL_TRAINED_DATA += 1
        TrainGUI.LABEL_TEXT.set("TOTAL TRAINED DATA: %d"%TrainGUI.TOTAL_TRAINED_DATA)
        self.root.update_idletasks()
        self.quit()
        for count, thing in enumerate(args):
            print( '{0}. {1}'.format(count, thing))

    def change_train_data(self,*args):
        self.submit.config(command=partial(self.label_submitted, *args))
        self.root.update_idletasks()

    def run(self,*args):
        self.label.pack()
        self.entry.pack()
        self.submit.pack(side = BOTTOM) 
        self.change_train_data(*args)
        self.root.mainloop()

    def quit(self):
        self.root.quit()


# if __name__ == '__main__':
#     train_gui = TrainGUI('apple', 'banana', 'cabbage')
#     train_gui.run('k','k','j')
#     train_gui.quit()
#     train_gui.run('ka','ff','asd')
#     print train_gui.TOTAL_TRAINED_DATA
