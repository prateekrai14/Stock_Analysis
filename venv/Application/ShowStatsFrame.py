from tkinter import *
from tkinter import ttk
from Processor import *
import NoteBook as MyNoteBook

class ShowStatsFrame(Frame):

    def __init__(self, master, symbol):
        Frame.__init__(self, master, height=40, width=70)
        self.Processor = Processor()
        self.BseSymbol = symbol
        self.pack(side="top", fill="y", expand=True)
        self.__creatShowStatsWeiget()

    def __creatShowStatsWeiget(self):
        EmptyLabel = Label(self, text="\t\t\t\t\n\n").grid(row=0, column=0, columnspan=3, rowspan=3)

        shareHoldingLabel = Label(self, text="Promotor ShareHolding\t:").grid(row=3, column=3, padx=4, pady=3)
        shareHoldingEntryLable = Label(self, text=self.Processor.getPromotorShareHolding(self.BseSymbol) + " %", width=15,anchor="se")
        shareHoldingEntryLable.grid(row=3, column=4, padx=4, pady=3)

        shareHoldingHistoricalLabel = Label(self, text="\tHistorical :").grid(row=3, column=5, padx=4, pady=3)
        shareHoldingHistoricalEntryLable = Label(self, text=self.Processor.getHistoricalPromotorShare(self.BseSymbol) + " %", width=10, anchor="se")
        shareHoldingHistoricalEntryLable.grid(row=3, column=6, padx=4, pady=3)

        pledgedShareHoldingLabel = Label(self, text="Pledged ShareHolding\t:").grid(row=4, column=3, padx=4, pady=3)
        pledgedShareHoldingEntryLabel = Label(self, text=self.Processor.getPledgedShareInfo(self.BseSymbol) + " %", width=15,anchor="se")
        pledgedShareHoldingEntryLabel.grid(row=4, column=4, padx=4, pady=3)

        marketCapitalizationLabel = Label(self, text="Market Capitalization\t:").grid(row=5, column=3, padx=4, pady=3)
        marketCapitalizationEntry = Label(self, text=self.Processor.getMarketCapital(self.BseSymbol) + " Cr", width=15,anchor="se")
        marketCapitalizationEntry.grid(row=5, column=4, padx=4, pady=3)

        equityCapitalLabel =  Label(self, text="Equity Capital\t\t:").grid(row=6, column=3, padx=4, pady=3)
        equityCapitalLabelEntry = Label(self, text=self.Processor.getEquityCapital(self.BseSymbol) + " Cr", width=15,anchor="se")
        equityCapitalLabelEntry.grid(row=6, column=4, padx=4, pady=3)

        equityCapitalHisLabel = Label(self, text="\tHistorical :").grid(row=6, column=5, padx=4, pady=3)
        equityCapitalHisLabelEntry = Label(self, text=self.Processor.getHistoricalEquityCapital(self.BseSymbol) + " Cr", width=10, anchor="se")
        equityCapitalHisLabelEntry.grid(row=6, column=6, padx=4, pady=3)

        bookValueLabel = Label(self, text="Book Value\t\t:").grid(row=7, column=3, padx=4, pady=3)
        bookValueEntry = Label(self, text=self.Processor.getBookValue(self.BseSymbol) + " Rs", width=15,anchor="se")
        bookValueEntry.grid(row=7, column=4, padx=4, pady=3)

        PELabel  = Label(self, text="P/E Ratio\t\t:").grid(row=8, column=3, padx=4, pady=3)
        PELabelEntry = Label(self, text=self.Processor.getPEInfo(self.BseSymbol), width=15,anchor="se")
        PELabelEntry.grid(row=8, column=4, padx=4, pady=3)

        PEHistoricalLabel = Label(self, text="\tHistorical :").grid(row=8, column=5, padx=4, pady=3)
        PEHistoricalEntry = Label(self, text=self.Processor.getHistoricalPE(self.BseSymbol), width=10, anchor="se")
        PEHistoricalEntry.grid(row=8, column=6, padx=4, pady=3)

        dividentLabel = Label(self, text="Divident\t\t\t:").grid(row=9, column=3, padx=4, pady=3)
        dividentLabelEntry = Label(self, text=self.Processor.getDividentData(self.BseSymbol) + " Rs", width=15,anchor="se")
        dividentLabelEntry.grid(row=9, column=4, padx=4, pady=3)

        epsLabel = Label(self, text="EPS\t\t\t:").grid(row=10, column=3, padx=4, pady=3)
        epsLabelEntry = Label(self, text=self.Processor.getEPS(self.BseSymbol) + " Rs", width=15,anchor="se")
        epsLabelEntry.grid(row=10, column=4, padx=4, pady=3)

        saleLabel = Label(self, text="Last FY Sales\t\t:").grid(row=11, column=3, padx=4, pady=3)
        saleLabelEntry = Label(self, text=self.Processor.getSaleData(self.BseSymbol) + " Cr", width=15,anchor="se")
        saleLabelEntry.grid(row=11, column=4, padx=4, pady=3)

        saleHistoricalLabel = Label(self, text="\tHistorical :").grid(row=11, column=5, padx=4, pady=3)
        saleHistoricalLabelEntry = Label(self, text=self.Processor.getHistoricalSales(self.BseSymbol) + " Cr", width=10, anchor="se")
        saleHistoricalLabelEntry.grid(row=11, column=6, padx=4, pady=3)

        profitLabel = Label(self, text="Last FY Profit\t\t:").grid(row=12, column=3, padx=4, pady=3)
        profitLabelEntry = Label(self, text=self.Processor.getNetProfitData(self.BseSymbol) + " Cr", width=15,anchor="se")
        profitLabelEntry.grid(row=12, column=4, padx=4, pady=3)

        profitHistoricalLabel = Label(self, text="\tHistorical :").grid(row=12, column=5, padx=4, pady=3)
        profitHistoricalLabelEntry = Label(self, text=self.Processor.getHistoricalProfit(self.BseSymbol) + " Cr", width=10, anchor="se")
        profitHistoricalLabelEntry.grid(row=12, column=6, padx=4, pady=3)

        quarterSaleLabel = Label(self, text="Last Quarter Sales\t\t:").grid(row=13, column=3, padx=4, pady=3)
        quarterSaleLabelEntry = Label(self, text=self.Processor.getLastQuarterSaleData(self.BseSymbol) + " Cr", width=15,anchor="se")
        quarterSaleLabelEntry.grid(row=13, column=4, padx=4, pady=3)

        quarterProfitLabel = Label(self, text="Last Quarter Profit\t:").grid(row=14, column=3, padx=4, pady=3)
        quarterProfitLabelEntry = Label(self, text=self.Processor.getLastQuarterProfit(self.BseSymbol) + " Cr", width=15,anchor="se")
        quarterProfitLabelEntry.grid(row=14, column=4, padx=4, pady=3)

        LowHigLabel = Label(self, text="52Week Low/High\t:").grid(row=15, column=3, padx=4, pady=3)
        lowHighString = self.Processor.get52WeekLow(self.BseSymbol) + "/" + self.Processor.get52WeekHigh(self.BseSymbol)
        LowHigLabelEntry = Label(self, text=lowHighString, width=15,anchor="se")
        LowHigLabelEntry.grid(row=15, column=4, padx=4, pady=3)

        EmptyLabel2 = Label(self, text="\n\n\n\n\n\n").grid(row=16, column=0, columnspan=3, rowspan=3)
        exitButton = Button(self, text="Close Tab", command= self.__closeTab, width=8, height=2).grid(row=16,column=3, columnspan=2)

    def __closeTab(self):

        MyNoteBook.NoteBookHandler.notebookTabslist.remove(self.BseSymbol)
        #MyNoteBook.NoteBookHandler.notebook.select(0)
        self.destroy()