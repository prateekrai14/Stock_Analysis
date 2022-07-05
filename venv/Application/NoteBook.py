from tkinter import *
from tkinter import ttk
from StartWindowFrame import StartWindowFrame
from StartSubWindowFrame import StartSubWindowFrame

class NoteBookHandler:

    root = Tk('Analyzer', baseName=None, className='Tk', useTk=1)
    notebook = ttk.Notebook(root)
    notebookTabslist = []

    def __init__(self):
        MainFrame = StartWindowFrame(self.root)
        self.__AddTabToApplication(MainFrame, 0, "Home")
        SubWindowFrame = StartSubWindowFrame(self.root)
        self.__AddTabToApplication(SubWindowFrame, 1, "Find Stocks")
        self.notebook.pack(expand=1, fill="both")
        self.root.geometry("{}x{}".format(900, 500))
        MainFrame.mainloop()

    def __AddTabToApplication(self, frame, tabBseIndex, tabName):
        self.notebookTabslist.append(tabBseIndex)
        self.notebook.add(frame, text=tabName)