from Tkinter import *
from Database.db_mongo import DB
from functools import partial


class TrainGUI:

    TOTAL_TRAINED_DATA = 0
    LABEL_TEXT = None
    WARNING_TEXT = None

    def __init__(self, *args):
        self.root = Tk()
        TrainGUI.LABEL_TEXT = StringVar()
        TrainGUI.LABEL_TEXT.set("TOTAL TRAINED DATA: %d" %
                                TrainGUI.TOTAL_TRAINED_DATA)
        TrainGUI.WARNING_TEXT = StringVar()
        self.root.geometry("300x200+500+200")
        self.entry = Entry(self.root, bd=5)
        self.label = Label(self.root, textvariable=TrainGUI.LABEL_TEXT)
        self.warning_label = Label(
            self.root, textvariable=TrainGUI.WARNING_TEXT, bg='Red')
        self.submit = Button(self.root, text="Submit",
                             command=partial(self.label_submitted, args))
        self.db = DB()
        self.init_UI()

    def label_submitted(self, args):
        label = self.entry.get()
        if len(label) != 1 or not label.isalpha():
            TrainGUI.WARNING_TEXT.set("Please enter a valid label !")
            self.root.update_idletasks()
            return
        TrainGUI.WARNING_TEXT.set('')
        TrainGUI.TOTAL_TRAINED_DATA += 1
        TrainGUI.LABEL_TEXT.set("TOTAL TRAINED DATA: %d" %
                                TrainGUI.TOTAL_TRAINED_DATA)
        self.root.update_idletasks()
        args['label'] = label
        self.db.insert_train_data(args)
        self.quit()

    def change_train_data(self, args):
        self.submit.config(command=partial(self.label_submitted, args))
        self.root.update_idletasks()

    def init_UI(self):
        self.label.pack()
        self.warning_label.pack()
        self.entry.pack()
        self.submit.pack(side=BOTTOM)

    def run(self, args):

        self.change_train_data(args)
        self.root.mainloop()

    def quit(self):
        self.root.quit()


# if __name__ == '__main__':
#    train_gui = TrainGUI()
#    train_gui.run('k','k','j')
#    train_gui.quit()
#    train_gui.run('ka','ff','asd')
#    print train_gui.TOTAL_TRAINED_DATA
