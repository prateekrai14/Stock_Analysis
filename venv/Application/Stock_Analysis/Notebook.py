from tkinter import *
from tkinter import ttk
import tkinter as gui
import Home_Frame 
import Find_Stock_Frame_1
import Show_Data

from tkinter import messagebox

class hello:

        Main_window = Tk()
        Main_window.geometry("1300x800")
        Main_window.title("Main Window")
        
        temp_list = []
                
        #Notebook
        tab_control= ttk.Notebook(Main_window)

        def __init__(self):
                tab1 = Home_Frame.Welcome_Window(self.Main_window)
                tab2 = Find_Stock_Frame_1.Find_Stock(self.Main_window)
                
                self.Run_Time_Tabs(0, tab1, "Home")
                self.Run_Time_Tabs(1, tab2, "Find Stock")
                self.tab_control.select(0)
                
                self.tab_control.pack(expand = 0, fill = "both")
                
                #self.Main_window.mainloop()                              
                
        def Run_Time_Tabs(self,Frame_Id, frame, Company_Tab_Name):
                self.tab_control.add(frame, text=Company_Tab_Name)
                self.temp_list.append(Frame_Id)
  
                
                
                
                
                
                
                
                
                
      
