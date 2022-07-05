import pandas
import tkinter as gui
from tkinter import *
from tkinter import ttk
import Notebook
import Show_Data

from tkinter import messagebox

class Welcome_Window(Frame):
    
    Data = pandas.read_csv("DataBank.csv.csv")
    Frame_Id = 2

    def __init__(self,master):
        Frame.__init__(self,master)

        #list
        self.bsb = list(self.Data["BSE Symbol"])
        self.option = list(self.Data["Company Name"])

        #gui design
        free_lable=gui.Label(self,text="").grid(padx=100,pady=25,row=1,column=1)

        #bsb_Design     
        self.bsb_label=gui.Label(self,text="BSB Symbol").grid(row=2,column=2)
        self.bsb_symbol=gui.Entry(self,text="")
        self.bsb_symbol.bind("<KeyRelease>",self.__pressed)
        self.bsb_symbol.grid(row=2,column=3)
        self.bsb_list = Listbox(self,bg='Grey94',height=6,bd=0,selectmode=SINGLE,takefocus = "off",highlightcolor="Grey94")

        self.bsb_list.bind("<<ListboxSelect>>",lambda x:self.__select(self.bsb_list,self.bsb,self.option))

        self.bsb_list.grid(row=3,column=3)

        #Company_Name_Design
        self.name=gui.Label(self,text="Company Name").grid(row=2,column=5)
        self.Company_Name = gui.Entry(self,text="")
        self.Company_Name.bind("<KeyRelease>",self.__released)
        self.Company_Name.grid(row=2,column=6)
        self.Company_n=Listbox(self,bg='Grey94',height=6,bd=0,selectmode=SINGLE,takefocus = "off",highlightcolor="Grey94")
        self.Company_n.bind("<<ListboxSelect>>",lambda x:self.__select(self.Company_n,self.option,self.bsb))
        self.Company_n.grid(row=3,column=6)

        self.show=gui.Button(self,text="Show",command = lambda : self.__Show(self.bsb_symbol.get(),self.Company_Name.get())).grid(padx=69,row=2,column=8)
        
        self.info_lable=gui.Label(self,text="                        Click to find Via Criteria => ",fg="red",font ="ShowcardGotic").grid(pady=200,row=5,column=4)    
        self.criterai=gui.Button(self,text="Search",command = lambda : self.__SwitchButton() )
        self.criterai.grid(row=5,column=5)
        
    #def __Key_Using_Value(self,Framee_Name):
    #    Tab_ID = list(Notebook.hello.Frame_Id_List.keys())
    #    Tab_Values = list(Notebook.hello.Frame_Id_List.values())
    #    tab = Tab_ID[Tab_Values.index(Framee_Name)]
    #    return(tab)

    def __Show(self,Temp_Bsb_Symbol,Framee_Name):
        Available_Tab = "False"
        Frame = Show_Data.Temp_Frame(Notebook.hello.Main_window,Temp_Bsb_Symbol)
            
        for Index in range(1,len(Notebook.hello.temp_list)): 
            if (Temp_Bsb_Symbol == Notebook.hello.temp_list[Index]):
                Notebook.hello.tab_control.select(Index)
                Available_Tab = "True"

        if(Available_Tab == "False"):
            Notebook.hello.Run_Time_Tabs(Notebook.hello, Temp_Bsb_Symbol, Frame, Framee_Name)
            Notebook.hello.tab_control.select(Frame)

    def __SwitchButton(self):
        Notebook.hello.tab_control.select(1)
    
    def __search(self,list,n,box):
        li = []
        for i in range(0,len(list)):
            if n in list[i]:
                li.append(list[i])
            else:
                box.delete(0,END)
        return(li)
              
    def __pressed(self,event):
        key = self.bsb_symbol.get()
        
        if(len(str(key)) > 6):
            messagebox.showinfo("Information","Maximum 6 Digit Allowed")
        try :
            int(key)
            n = []
            for i in range(0,len(self.bsb)):
                n.append(str(self.bsb[i]))
                
            new = self.__search(n,str(key),self.bsb_list)
            
            if (len(new) == 0):
                messagebox.showinfo("Information","Not Found")
            else:
                self.bsb_list.insert(0,*new)  
        except :
            if(len(str(key)) == 0):
                self.l=gui.Label(self,text="                                   ").grid(row=1,column=3)
                self.bsb_list.delete(0,END) 
            else:
                self.l=gui.Label(self,text="Numeric Digit Only !",fg="blue").grid(row=1,column=3)
            

    def __released(self,event):
        key=self.Company_Name.get()
        waste = self.__search(self.option,key,self.Company_n)
        if (len(waste) == 0):
            messagebox.showinfo("Information","Not Found")
        else:
            self.Company_n.insert(0,*waste)
            if(len(key) == 0):
                self.Company_n.delete(0,END)

    def __select(self,list,mainlist,list1):
        try :
            tupple=list.curselection()
            value=list.get(tupple)
            if (mainlist == self.bsb):
                self.bsb_symbol.delete(0,END)
                self.bsb_symbol.insert(0,str(value))
                for i in range(0,len(mainlist)):
                    if (value == str(mainlist[i])):
                        self.Company_Name.delete(0,END)
                        self.Company_Name.insert(0,list1[i])
                        self.bsb_list.delete(0,END)
                        self.Company_n.delete(0,END)
            else:
                self.Company_Name.delete(0,END)
                self.Company_Name.insert(0,str(value))
                for i in range(0,len(mainlist)):
                    if (value == mainlist[i]):
                        self.bsb_symbol.delete(0,END)
                        self.bsb_symbol.insert(0,list1[i])
                        self.bsb_list.delete(0,END)
                        self.Company_n.delete(0,END)
        except(TclError):
            Pass
