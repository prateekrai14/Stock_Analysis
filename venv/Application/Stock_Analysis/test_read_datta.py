import pandas


class Data():

    def __init__(self,Tab_Id):
        companiesCurrentYearData= pandas.read_csv("StocksInputData-0.csv")
        #companiesLastYearData = pandas.read_csv("StocksInputData-1.csv")

        print(companiesCurrentYearData.loc[companiesCurrentYearData.BSEIndex == str(Tab_Id)])

        
=
companiesCurrentYearData= pandas.read_csv("StocksInputData-0.csv")
companiesLastYearData = pandas.read_csv("StocksInputData-1.csv")

print(companiesCurrentYearData)

#print(companiesCurrentYearData.loc[companiesCurrentYearData.BSEIndex==513375])



Promotor ShareHolding = 20 
Pledged ShareHolding = 21 
Market Capitalization = 23
Equity Capital = 4 
Book Value = 5
P/E Ratio = 26 
Divident = 9
EPS = 8
Last FY Sales= 6  
Last FY Profit= 7 
Last Quater Sales = 13 
Last Quater Profit = 14 
52Week Low/High = 25



