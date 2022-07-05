import tkinter as gui
from tkinter import *
import Notebook
import pandas
#from Home_Frame import Welcome_Window
import Home_Frame

class Find_Stock(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        
        self.List_Of_Criteria_Checkbox= []
        self.Check_Box_Inputs= [("promotor Shareholdor (%)\t\t",1),
                                ("promotor pledge Shareholdor (%)\t\t\t",2),
                                ("Equality Capital limit (cr)\t\t",3),
                                ("Book Value (cr)\t\t ",4),
                                ("P/E Ratio (%)\t\t",5)]
        

        '''1 = PromotorShareHoldings
        2 = PledgedShareHoldings
        3 = EquityCapital
        4 = BookValue
        5 = PERation
        '''
                
        #Calling Function
        self.__Create_Window_Design()

        

    def __Create_Window_Design(self):
        
        for Index,Value in enumerate(self.Check_Box_Inputs):
            self.List_Of_Criteria_Checkbox.append(Checkbutton(self,text=Value[0],\
                                                  onvalue=Value[1], offvalue=0).\
                                                  grid(row=4+Index, column=1, sticky="W"))

        self.Acceptable_l=gui.Label(self,text="Acceptable",fg="green",font ="ShowcardGotic").grid(padx=10,row=3,column=3)
        self.Non_Acceptable_l=gui.Label(self,text="Non Acceptable",fg="red",font="ShowcardGotic").grid(padx=10,row=3,column=4)


        self.Acc_1=gui.Entry(self,text = "",width = 6)
        self.Acc_1.insert(0,80)
        self.Acc_1.grid(row=4,column=3)

        self.Nacc_1=gui.Entry(self,text = "",width = 6)
        self.Nacc_1.insert(0,30)
        self.Nacc_1.grid(row=4,column=4)

        self.Acc_2=gui.Entry(self,text = "",width = 6)
        self.Acc_2.insert(0,0)
        self.Acc_2.grid(row=5,column=3)

        self.Nacc_2=gui.Entry(self,text = "",width = 6)
        self.Nacc_2.insert(0,6)
        self.Nacc_2.grid(row=5,column=4)

        self.Acc_3=gui.Entry(self,text = "",width = 6)
        self.Acc_3.insert(0,10)
        self.Acc_3.grid(row=6,column=3)

        self.Nacc_3=gui.Entry(self,text = "",width = 6)
        self.Nacc_3.insert(0,200)
        self.Nacc_3.grid(row=6,column=4)

        self.Acc_4=gui.Entry(self,text = "",width = 6)
        self.Acc_4.insert(0,10)
        self.Acc_4.grid(row=7,column=3)

        self.Nacc_4=gui.Entry(self,text = "",width = 6)
        self.Nacc_4.insert(0,0)
        self.Nacc_4.grid(row=7,column=4)

        self.Acc_5=gui.Entry(self,text = "",width = 6)
        self.Acc_5.insert(0,10)
        self.Acc_5.grid(row=8,column=3)

        self.Nacc_5=gui.Entry(self,text = "",width = 6)
        self.Nacc_5.insert(0,0)
        self.Nacc_5.grid(row=8,column=4)

        #Listbox
        self.ListBox1= gui.Listbox(self,height=20,width=80)
        
        self.ListBox1.bind("<<ListboxSelect>>",lambda x: self.__Show_Stats())
        
        self.ListBox1.grid(row=11, column=1,columnspan=4,sticky="W")

        ScrollBar = Scrollbar(self)
        ScrollBar.grid(row=11,column=3,rowspan=20)

        self.ListBox1.configure(yscrollcommand=ScrollBar.set)
        ScrollBar.configure(command = self.ListBox1.yview)

            
        self.Show_Stock_b = gui.Button(self,text="Show Stocks",command = lambda : self.__Show_Stock_Using_Criteria()).grid(pady=50,row=10,column=1)
        self.Clear_Button = gui.Button(self,text="Clear List Box",command= lambda : self.__Clear()).grid(row=10,column=2,sticky="W")
        self.Go_Home_b = gui.Button(self,text="Go To Home",command = lambda : self.__Switch() ).grid(row=10,column=4,sticky="W")

    def __Show_Stats(self):
        Index = self.ListBox1.curselection()[0]
        Bsb_Symbol_Selected= self.ListBox1.get(Index)[0]
        Company_Name_Selected= self.ListBox1.get(Index)[2]
        return(Bsb_Symbol_Selected,Company_Name_Selected)
        #Send To Home_Frame Both Values
        #Home_Frame.Welcome_Window.__Show(Home_Frame,Bsb_Symbol_Selected,Company_Name_Selected)

    def __Show_Stock_Using_Criteria(self):
        self.ListBox1.delete(0,END)
        
        for bsb,name in zip(Home_Frame.Welcome_Window.Data["BSE Symbol"],Home_Frame.Welcome_Window.Data["Company Name"]):
            self.ListBox1.insert(END,[bsb,":",name])
    def __Clear(self):
        self.ListBox1.delete(0,END)
        
    def __Switch(self):
        Notebook.hello.tab_control.select(0)
        

