import tkinter as gui
from tkinter import *
import Home_Frame
import Notebook
import pandas

class Temp_Frame(Frame):
    
    def __init__(self,master,Tab_Id):
        Frame.__init__(self,master)

        companiesCurrentYearData= pandas.read_csv("StocksInputData-0.csv")
        li = (companiesCurrentYearData.loc[companiesCurrentYearData.BSEIndex == str(Tab_Id)].iloc[0])
        

        l1=gui.Label(self,text="Promotor ShareHolding               :").grid(padx=30,row=1,column=1)
        l2=gui.Label(self,text="Pledged ShareHolding                :").grid(row=2,column=1)
        l3=gui.Label(self,text="Market Capitalization               :").grid(row=3,column=1)
        l4=gui.Label(self,text="Equity Capital                      :").grid(row=4,column=1)
        l5=gui.Label(self,text="Book Value                          :").grid(row=5,column=1)
        l6=gui.Label(self,text="P/E Ratio                           :").grid(row=6,column=1)
        l7=gui.Label(self,text="Divident                            :").grid(row=7,column=1)
        l8=gui.Label(self,text="EPS                                 :").grid(row=8,column=1)
        l9=gui.Label(self,text="Last FY Sales                       :").grid(row=9,column=1)
        l10=gui.Label(self,text="Last FY Profit                    :").grid(row=10,column=1)
        l11=gui.Label(self,text="Last Quater Sales                 :").grid(row=11,column=1)
        l12=gui.Label(self,text="Last Quater Profit                :").grid(row=12,column=1)
        l13=gui.Label(self,text="52Week Low/High                    :").grid(row=13,column=1)

        e1=gui.Label(self,text=li[20],bg='Grey94',bd=0).grid(row=1,column=2)
        e2=gui.Label(self,text=li[21],bg='Grey94',bd=0).grid(row=2,column=2)
        e3=gui.Label(self,text=li[23],bg='Grey94',bd=0).grid(row=3,column=2)
        e4=gui.Label(self,text=li[4],bg='Grey94',bd=0).grid(row=4,column=2)
        e5=gui.Label(self,text=li[5],bg='Grey94',bd=0).grid(row=5,column=2)
        e6=gui.Label(self,text=li[26],bg='Grey94',bd=0).grid(row=6,column=2)
        e7=gui.Label(self,text=li[9],bg='Grey94',bd=0).grid(row=7,column=2)
        e8=gui.Label(self,text=li[8],bg='Grey94',bd=0).grid(row=8,column=2)
        e9=gui.Label(self,text=li[6],bg='Grey94',bd=0).grid(row=9,column=2)
        e10=gui.Label(self,text=li[7],bg='Grey94',bd=0).grid(row=10,column=2)
        e11=gui.Label(self,text=li[13],bg='Grey94',bd=0).grid(row=11,column=2)
        e12=gui.Label(self,text=li[14],bg='Grey94',bd=0).grid(row=12,column=2)
        e13=gui.Label(self,text=li[25],bg='Grey94',bd=0).grid(row=13,column=2)

        

        closebutton=gui.Button(self,text="Close Tab",command = lambda : __Destroy_Tab()).grid(pady=50,row=14,column=2)
        
        def __Destroy_Tab():
            self.destroy()
            Notebook.hello.temp_list.remove(Tab_Id)

