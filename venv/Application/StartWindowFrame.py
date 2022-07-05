from tkinter import *
from FileParser import FileParser
from SupportLib import HelperFunctions
from ShowStatsFrame import *
import NoteBook as MyNoteBook

SuggestionListSizeControler = 5

class StartWindowFrame(Frame):

    def __init__(self, master):
        Frame.__init__(self, master, height=30, width=30)
        self.master.title("Market Trading Analysis")
        self.companyNameIndexDic = FileParser().createIndexNameDic("StocksList.csv")
        self.BseSymbol = StringVar()
        self.isBseSymbolFinal = False
        self.CompanyName = StringVar()
        self.isCompanyNameFinal = False
        self.pack(side="top", fill="y", expand=True)
        self.__createMainWeiget()

    def __createMainWeiget(self):
        self.__CreateBseSymbolEntry()
        self.__CreateCompanyNameEntry()
        self.__CreateGetStatsButton()
        self.__CreateShowSubWindowButton()

    def __CreateBseSymbolEntry(self):
        self.BseSymbolErrorLabel = Label(self, text="", fg="red")
        self.BseSymbolErrorLabel.grid(row=0, column=1, padx=4, pady=3)

        self.BseSymbolLabel = Label(self, text="BSE Symbol")
        self.BseSymbolLabel.grid(row=1, column=0, padx=4, pady=3)

        self.BseSymbolEntry = Entry(self, textvariable=self.BseSymbol)
        self.BseSymbolEntry.grid(row=1, column=1, padx=4, pady=3)
        self.BseSymbolEntry.insert(0,next(iter(self.companyNameIndexDic)))
        self.BseSymbolEntry.bind('<KeyRelease>', self.__pollBseSymbol)

        self.BseSymbollBox = Listbox(self, width=20, height=5, bg="Gray94", bd=0, highlightcolor="Gray94", state=DISABLED)
        self.BseSymbollBox.bind('<<ListboxSelect>>', self.__onSelectBseSymbol)
        self.BseSymbollBox.grid(row=2, column=1, padx=4, pady=3)

    def __CreateCompanyNameEntry(self):

        self.CompanyNameErrorLabel = Label(self, text="", fg="red")
        self.CompanyNameErrorLabel.grid(row=0, column=3, padx=4, pady=3)

        self.CompanyNameLabel = Label(self, text="Company Name")
        self.CompanyNameLabel.grid(row=1, column=2, padx=4, pady=3)

        self.CompanyNameEntry = Entry(self, textvariable=self.CompanyName)
        self.CompanyNameEntry.insert (0,next(iter(self.companyNameIndexDic.values())))
        self.CompanyNameEntry.grid(row=1, column=3, padx=4, pady=3)
        self.CompanyNameEntry.bind('<KeyRelease>', self.__pollCompanyName)

        self.CompanyNamelBox = Listbox(self, width=20, height=5, bg="Gray94", bd=0, highlightcolor="Gray94", state=DISABLED)
        self.CompanyNamelBox.bind('<<ListboxSelect>>', self.__onSelectCompanyName)
        self.CompanyNamelBox.grid(row=2, column=3, padx=4, pady=3)

    def __CreateGetStatsButton(self):
        LocalEmpatyLabel = Label(self, text="     ").grid(row=1, column=4)
        self.GetStatesButton = Button(self, text="Get Stats", state=ACTIVE, command= self.__showStats)
        self.GetStatesButton.grid(row=1, column=5, padx=0, pady=1)

    def __CreateShowSubWindowButton(self):

        Label(self, text="Click Button To Find Criteria Based Stocks ->", fg="blue", font="Verdana 8 bold").\
            grid(row=7, column=2, columnspan=2, sticky="se")
        self.GetSubWindowButton = Button(self, text="Click Here", state=ACTIVE, command=self.__showSubWindow)
        self.GetSubWindowButton.grid(row=7, column=5, padx=0, pady=1)

    def __pollBseSymbol(self, event):
        self.GetStatesButton['state'] =DISABLED
        tempvar = self.BseSymbolEntry.get()
        if tempvar.isdigit():
            if len(tempvar) < 6:
                self.__listNearestBseSymbol(tempvar)
            else:
                if int(tempvar) in self.companyNameIndexDic.keys():
                    self.__fillCompanyNameEntryForKey(int(tempvar))
                else:
                    if len(tempvar) == 6:
                        self.BseSymbolErrorLabel.config(text="Invalid BSE Symbol")
                    else:
                        self.BseSymbolErrorLabel.config(text="Max 6 Digits Allowed")
        else:
            self.BseSymbolErrorLabel.config(text="Only Numric Input")

    def __pollCompanyName(self, event):
        self.GetStatesButton['state'] = DISABLED
        self.__listNearestCompanyName(self.CompanyNameEntry.get())

    def __onSelectCompanyName(self, event):
        w1=event.widget
        value = w1.get(int(w1.curselection()[0]))
        for BseSymbol, companyName in self.companyNameIndexDic.items():
            if (value == companyName):
                self.__fillCompanyNameEntryForKey(BseSymbol)
                break

    def __onSelectBseSymbol(self, event):
        w1=event.widget
        value = w1.get(int(w1.curselection()[0]))
        self.__fillCompanyNameEntryForKey(int(value))

    def __fillCompanyNameEntryForKey(self, key):
        self.BseSymbolEntry.delete(0,END)
        self.BseSymbolEntry.insert(0, str(key))
        self.CompanyNameEntry.delete(0, END)
        self.CompanyNameEntry.insert(0, self.companyNameIndexDic.get(key))
        self.BseSymbolErrorLabel.config(text="")
        self.CompanyNameErrorLabel.config(text="")
        self.BseSymbollBox.delete(0, END)
        self.BseSymbollBox['state'] = DISABLED
        self.CompanyNamelBox.delete(0, END)
        self.CompanyNamelBox['state'] = DISABLED
        self.GetStatesButton['state'] = ACTIVE

    def  __listNearestBseSymbol(self, key):
        index = 0
        self.BseSymbollBox['state']=NORMAL
        self.BseSymbollBox.delete(0,END)
        for item in self.companyNameIndexDic.keys():
            #SuggestionListSizeControler : Global Variable
            if (index < SuggestionListSizeControler) and (key in str(item)):
                self.BseSymbollBox.insert(END, item)
                index= index + 1

    def __listNearestCompanyName(self, companyNameSubStr):
        index = 0
        self.CompanyNamelBox['state'] = NORMAL
        self.CompanyNamelBox.delete(0, END)
        self.CompanyNameErrorLabel.config(text="")
        for item in self.companyNameIndexDic.values():
            # SuggestionListSizeControler : Global Variable
            if (index < SuggestionListSizeControler) and (str(companyNameSubStr).lower() in str(item).lower()):
                self.CompanyNamelBox.insert(END, item)
                index = index + 1

        if self.CompanyNamelBox.size() == 0:
            self.CompanyNameErrorLabel.config(text="No match found")

    def __showStats(self):

        isTabAvailable = False
        tabId = 0
        for tabText in MyNoteBook.NoteBookHandler.notebookTabslist:
            if (tabText == int(self.BseSymbolEntry.get())):
                isTabAvailable = True
                MyNoteBook.NoteBookHandler.notebook.select(tabId)

            tabId += 1

        if isTabAvailable == False:
            #make a frame
            StatsFrame = ShowStatsFrame(self.master, int(self.BseSymbolEntry.get()))

            #add this to notebook
            MyNoteBook.NoteBookHandler.notebookTabslist.append(int(self.BseSymbolEntry.get()))
            MyNoteBook.NoteBookHandler.notebook.add(StatsFrame, text=self.CompanyNameEntry.get())

            #make it current tab
            MyNoteBook.NoteBookHandler.notebook.select(len(MyNoteBook.NoteBookHandler.notebookTabslist) - 1)

    def __showSubWindow(self):
        MyNoteBook.NoteBookHandler.notebook.select(1) # subwindow is always second window to home


#######################################################################################################
