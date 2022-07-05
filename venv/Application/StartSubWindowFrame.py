from tkinter import *
from tkinter import messagebox
import NoteBook as MyNoteBook
from InputLimits import *
from Processor import *
from math import *
from ShowStatsFrame import *

class StartSubWindowFrame(Frame):

    def __init__(self, master):
        Frame.__init__(self, master, height=40, width=70)
        self.pack(side="top", fill="y", expand=True)

        self.master = master
        self.Processor = Processor()
        self.criteriaSelectionEnumArray = []
        self.ListOfCriteriasCheckbox = []
        self.LastBackUpEntry = ['',''] #List of 1 pair of Acceptable and Not Acceptable Limits

        #self.PromotorShareHolding = ShareHolding(self)
        #self.PromotorPledgedShareHolding = PledgeShareHoldingLimits(self)
        #self.EquityCapitalLimits = EquityCapitalLimits(self)
        #self.ProfitGrowthLimits = ProfitGrowthLimits(self)
        #self.SalesGrowthLimits = SalesGrowthLimits(self)

        self.listOfStocksWithSelectedCriteria = []
        self.ListOfCriterias = [('Promotor ShareHolding(0-100) %\t\t\t:', 19, ShareHolding(self), self.Processor.getPromotorShareHolding), #SHAREHOLDINGS.PROMOTOR_HOLDINGS = 19
                                ('Promotor Pledge ShareHolding(0-100) %\t\t:', 20, PledgeShareHoldingLimits(self), self.Processor.getPledgedShareInfo), #SHAREHOLDINGS.PLEDGED = 20
                                ('Equity Capital Limit(1-1000) cr\t\t\t:', 3, EquityCapitalLimits(self), self.Processor.getEquityCapital), #ANNUALENTITIES.TOTAL_EQUITY
                                ('Profit Growth(0-100) %\t\t\t\t:', 6, ProfitGrowthLimits(self), self.Processor.getHistoricalProfitGrowth), #NET_PROFIT.NET_PROFIT
                                ('Sales Growth(0-100) %\t\t\t\t:', 5, SalesGrowthLimits(self), self.Processor.getHistoricalSalesGrowth)] #NET_PROFIT.SALES

        self.__creatSubWindowWeiget()

    def __creatSubWindowWeiget(self):
        Label(self, text="\t\t\t\t\t\n\n").grid(row=0, column=0, columnspan=3, rowspan=3)
        Label(self, text=" Acceptable", fg="green", font="Verdana 10 bold").grid(row=4, column=3, sticky='w')
        Label(self, text=" Not Acceptable", fg="red", font="Verdana 10 bold").grid(row=4, column=4, sticky='w')

        for index, value in enumerate(self.ListOfCriterias):
            self.criteriaSelectionEnumArray.append(IntVar())
            self.ListOfCriteriasCheckbox.append(Checkbutton(self, text=value[0], \
                                                            variable=self.criteriaSelectionEnumArray[index],
                                                            onvalue=value[1], offvalue=0).\
                                                            grid(row=5+index, column=2, sticky="w"))

        PSH_AcceptableEntry = Entry(self, textvariable=self.ListOfCriterias[0][2].AcceptableLimit, width=10)
        PSH_AcceptableEntry.grid(row=5, column=3)
        PSH_AcceptableEntry.bind('<FocusIn>', lambda event: self.__backupLastEntry(event, self.ListOfCriterias[0][2]))
        PSH_AcceptableEntry.bind('<FocusOut>', lambda event: self.__validateLimit(event, self.ListOfCriterias[0][2]))

        PSH_NotAcceptableEntry = Entry(self, textvariable=self.ListOfCriterias[0][2].NotAcceptableLimit, width=10)
        PSH_NotAcceptableEntry.grid(row=5, column=4)
        PSH_NotAcceptableEntry.bind('<FocusIn>', lambda event: self.__backupLastEntry(event, self.ListOfCriterias[0][2]))
        PSH_NotAcceptableEntry.bind('<FocusOut>', lambda event: self.__validateLimit(event, self.ListOfCriterias[0][2]))

        PPSH_AcceptableEntry = Entry(self, textvariable=self.ListOfCriterias[1][2].AcceptableLimit, width=10)
        PPSH_AcceptableEntry.grid(row=6, column=3)
        PPSH_AcceptableEntry.bind('<FocusIn>', lambda event: self.__backupLastEntry(event, self.ListOfCriterias[1][2]))
        PPSH_AcceptableEntry.bind('<FocusOut>', lambda event: self.__validateLimit(event, self.ListOfCriterias[1][2]))

        PPSH_NotAcceptableEntry = Entry(self, textvariable=self.ListOfCriterias[1][2].NotAcceptableLimit, width=10)
        PPSH_NotAcceptableEntry.grid(row=6, column=4)
        PPSH_NotAcceptableEntry.bind('<FocusIn>', lambda event: self.__backupLastEntry(event, self.ListOfCriterias[1][2]))
        PPSH_NotAcceptableEntry.bind('<FocusOut>', lambda event: self.__validateLimit(event, self.ListOfCriterias[1][2]))

        EC_AcceptableEntry = Entry(self, textvariable=self.ListOfCriterias[2][2].AcceptableLimit, width=10)
        EC_AcceptableEntry.grid(row=7, column=3)
        EC_AcceptableEntry.bind('<FocusIn>',lambda event: self.__backupLastEntry(event, self.ListOfCriterias[2][2]))
        EC_AcceptableEntry.bind('<FocusOut>',lambda event: self.__validateLimit(event, self.ListOfCriterias[2][2]))

        EC_NotAcceptableEntry = Entry(self, textvariable=self.ListOfCriterias[2][2].NotAcceptableLimit, width=10)
        EC_NotAcceptableEntry.grid(row=7, column=4)
        EC_NotAcceptableEntry.bind('<FocusIn>', lambda event: self.__backupLastEntry(event, self.ListOfCriterias[2][2]))
        EC_NotAcceptableEntry.bind('<FocusOut>', lambda event: self.__validateLimit(event, self.ListOfCriterias[2][2]))

        PG_AcceptableEntry = Entry(self, textvariable=self.ListOfCriterias[3][2].AcceptableLimit, width=10)
        PG_AcceptableEntry.grid(row=8, column=3)
        PG_AcceptableEntry.bind('<FocusIn>', lambda event: self.__backupLastEntry(event, self.ListOfCriterias[3][2]))
        PG_AcceptableEntry.bind('<FocusOut>', lambda event: self.__validateLimit(event, self.ListOfCriterias[3][2]))

        PG_NotAcceptableEntry = Entry(self, textvariable=self.ListOfCriterias[3][2].NotAcceptableLimit, width=10)
        PG_NotAcceptableEntry.grid(row=8, column=4)
        PG_NotAcceptableEntry.bind('<FocusIn>', lambda event: self.__backupLastEntry(event, self.ListOfCriterias[3][2]))
        PG_NotAcceptableEntry.bind('<FocusOut>', lambda event: self.__validateLimit(event, self.ListOfCriterias[3][2]))

        SG_AcceptableEntry = Entry(self, textvariable=self.ListOfCriterias[4][2].AcceptableLimit, width=10)
        SG_AcceptableEntry.grid(row=9, column=3)
        SG_AcceptableEntry.bind('<FocusIn>', lambda event: self.__backupLastEntry(event, self.ListOfCriterias[4][2]))
        SG_AcceptableEntry.bind('<FocusOut>', lambda event: self.__validateLimit(event, self.ListOfCriterias[4][2]))

        SG_NotAcceptableEntry = Entry(self, textvariable=self.ListOfCriterias[4][2].NotAcceptableLimit, width=10)
        SG_NotAcceptableEntry.grid(row=9, column=4)
        SG_NotAcceptableEntry.bind('<FocusIn>', lambda event: self.__backupLastEntry(event, self.ListOfCriterias[4][2]))
        SG_NotAcceptableEntry.bind('<FocusOut>', lambda event: self.__validateLimit(event, self.ListOfCriterias[4][2]))

        Label(self, text=" ").grid(row=10, column=0, rowspan=2)
        Button(self, text = "Show Stocks", command=self.__showSelection).grid(row=12, column=2)

        Button(self, text="Go To Home", command=self.__GotoHome).grid(row=12, column=4, columnspan=1)

        Label(self, text=" ").grid(row=13, column=0, rowspan=2)
        yScroll = Scrollbar(self, orient=VERTICAL)
        yScroll.grid(row=15, column=7, sticky=N + S)

        self.listbox = Listbox(self, width=100, height=10, bd=1, state=DISABLED, yscrollcommand=yScroll.set)
        self.listbox.grid(row=15, column=2, columnspan=5,sticky=N + S + E + W)
        yScroll['command'] = self.listbox.yview
        self.listbox.bind('<<ListboxSelect>>', self.__onSelectlistItem)

    def __backupLastEntry(self, event, object):
        self.LastBackUpEntry[0] = object.AcceptableLimit.get()
        self.LastBackUpEntry[1] = object.NotAcceptableLimit.get()

    def __validateLimit(self, event, object):
        validEntry, ErrorMessage = object.isValidLimits()
        if not validEntry:
            object.AcceptableLimit.set(self.LastBackUpEntry[0])
            object.NotAcceptableLimit.set(self.LastBackUpEntry[1])
            messagebox.showerror("Error", ("Invalid Entry!" + ErrorMessage))


    def __showSelection(self):

        isAnySelected = False
        index=0
        self.listOfStocksWithSelectedCriteria.clear()
        self.listbox.delete(0, END)
        self.listbox['state'] = DISABLED

        for criteria in self.criteriaSelectionEnumArray:

            if criteria.get() != 0  :
                isAnySelected = True
                if len(self.listOfStocksWithSelectedCriteria) == 0:
                    # Trace CurrentYearCompanyData and fill listOfStocksWithSelectedCriteria for first criteria
                    for BseSymbol in self.Processor.companiesCurrentYearData.keys():

                        if round(float(self.ListOfCriterias[index][3](BseSymbol))) > int(self.ListOfCriterias[index][2].AcceptableLimit.get()):
                            self.listOfStocksWithSelectedCriteria.insert(0, BseSymbol)
                        else:
                            if round(float(self.ListOfCriterias[index][3](BseSymbol))) > int(self.ListOfCriterias[index][2].NotAcceptableLimit.get()):
                                self.listOfStocksWithSelectedCriteria.append(BseSymbol)
                else:
                    # Trace listOfStocksWithSelectedCriteria for 1st criteria onward and remove not fulfilling stocks
                    for pos, BseSymbol in enumerate(self.listOfStocksWithSelectedCriteria):

                        if self.ListOfCriterias[index][1] == 20 or self.ListOfCriterias[index][1] == 3:
                            if round(float(self.ListOfCriterias[index][3](BseSymbol))) > int(self.ListOfCriterias[index][2].NotAcceptableLimit.get()):
                                self.listOfStocksWithSelectedCriteria.pop(pos)
                        else:
                            if round(float(self.ListOfCriterias[index][3](BseSymbol))) < int(self.ListOfCriterias[index][2].NotAcceptableLimit.get()):
                                self.listOfStocksWithSelectedCriteria.pop(pos)
            index+=1

        if isAnySelected == False:
            messagebox.showerror("Error", "Minimum 1 checkbox should be selected.")
        else:
            self.__printListOfStocksWithSelectedCriteria()

    def __printListOfStocksWithSelectedCriteria(self):
        self.listbox['state'] = NORMAL
        for each in self.listOfStocksWithSelectedCriteria:
            entry = str(each)
            entry += ' :    ' + self.Processor.getCompanyName(each).strip()
            self.listbox.insert(END, entry)

    def __onSelectlistItem(self, event):
        w1 = event.widget

        if w1.curselection() :
            value = w1.get(int(w1.curselection()[0]))
            BseSymbol = int(value.split(':')[0].strip())

            if BseSymbol in MyNoteBook.NoteBookHandler.notebookTabslist:
                MyNoteBook.NoteBookHandler.notebook.select(MyNoteBook.NoteBookHandler.notebookTabslist.index(BseSymbol))
            else:
                # make a frame
                StatsFrame = ShowStatsFrame(self.master, BseSymbol)

                # add this to notebook
                MyNoteBook.NoteBookHandler.notebookTabslist.append(BseSymbol)
                MyNoteBook.NoteBookHandler.notebook.add(StatsFrame, text=self.Processor.getCompanyName(BseSymbol).strip())

                # make it current tab
                MyNoteBook.NoteBookHandler.notebook.select(len(MyNoteBook.NoteBookHandler.notebookTabslist) - 1)

            self.listbox.selection_clear(0, END)

    def __GotoHome(self):
        MyNoteBook.NoteBookHandler.notebook.select(0) # Home window is always first window in application