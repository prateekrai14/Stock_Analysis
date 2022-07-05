import FileParser as FileHandler
import SupportEnum as Enums
import SupportLib as LibFunc

class Processor:

    HistoryController = 2

    def __init__(self):
        fileProcessor = FileHandler.FileParser()
        self.companiesCurrentYearData = fileProcessor.parseCompanyData("StocksInputData-0.csv")
        self.companiesLastYearData = fileProcessor.parseCompanyData("StocksInputData-1.csv")

    def getMarketCapital(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.MARKETDATA.MARKET_CAP].strip()

    def getBookValue(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.ANNUALENTITIES.BOOK_VALUE].strip()

    def getEquityCapital(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.ANNUALENTITIES.TOTAL_EQUITY].strip()

    def getCompanyName(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.ANNUALENTITIES.COMPANY_NAME].strip()

    def getDividentData(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.ANNUALENTITIES.ANUALIZED_DIVIDENT].strip()

    def getSaleData(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.ANNUALENTITIES.SALES].strip()

    def getNetProfitData(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.ANNUALENTITIES.NET_PROFIT].strip()

    def getEPS(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.ANNUALENTITIES.EPS].strip()

    def getLastQuarterSaleData(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.QUATERENTITIES.QSALES].strip()

    def getLastQuarterProfit(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.QUATERENTITIES.QNET_PROFIT].strip()

    def getYearToDateSalesData(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.YEAR2DATEENTITIES.YSALES].strip()

    def getYearToDateProfit(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.YEAR2DATEENTITIES.YNET_PROFIT].strip()

    def getPromotorShareHolding(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.SHAREHOLDINGS.PROMOTOR_HOLDINGS].strip()

    def getPledgedShareInfo(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.SHAREHOLDINGS.PLEDGED].strip()

    def getSectorName(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.MARKETDATA.SECTOR].strip()

    def get52WeekHigh(self, BSEIndex):
        #Get High from High/Low Data
        list = self.companiesCurrentYearData[BSEIndex][Enums.MARKETDATA.YEAR_HIGH_LOW].strip().split('/')
        return list[0]

    def get52WeekLow(self, BSEIndex):
        # Get Low from High/Low Data
        list = self.companiesCurrentYearData[BSEIndex][Enums.MARKETDATA.YEAR_HIGH_LOW].strip().split('/')
        return list[1]

    def getPrice(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.MARKETDATA.PRICES].strip()

    def getPEInfo(self, BSEIndex):
        return self.companiesCurrentYearData[BSEIndex][Enums.MARKETDATA.PE].strip()

    def getHighestIndustrialPE(self, BSEIndex):
        raise NotImplementedError("This functionaliy is not implemented yet")

    def getHistoricalPE(self, BSEIndex):
        if self.__wasStockPresent(BSEIndex):
            return self.companiesLastYearData[BSEIndex][Enums.MARKETDATA.PE].strip()
        else:
            return self.companiesCurrentYearData[BSEIndex][Enums.MARKETDATA.PE].strip()

    def getHistoricalEquityCapital(self, BSEIndex):
        if self.__wasStockPresent(BSEIndex):
            return self.companiesLastYearData[BSEIndex][Enums.ANNUALENTITIES.TOTAL_EQUITY].strip()
        else:
            return self.companiesCurrentYearData[BSEIndex][Enums.ANNUALENTITIES.TOTAL_EQUITY].strip()

    def getHistoricalSales(self, BSEIndex):
        if self.__wasStockPresent(BSEIndex):
            return self.companiesLastYearData[BSEIndex][Enums.ANNUALENTITIES.SALES].strip()
        else:
            return self.companiesCurrentYearData[BSEIndex][Enums.ANNUALENTITIES.SALES].strip()

    def getHistoricalSalesGrowth(self, BSEIndex):
        gowth = round(float(self.getSaleData(BSEIndex))) - round(float(self.getHistoricalSales(BSEIndex)))
        if gowth > 0:
            return str(round(float((gowth*100)/(round(float(self.getSaleData(BSEIndex)))))))
        else:
            return str(0)

    def getHistoricalPromotorShare(self, BSEIndex):
        if self.__wasStockPresent(BSEIndex):
            return self.companiesLastYearData[BSEIndex][Enums.SHAREHOLDINGS.PROMOTOR_HOLDINGS].strip()
        else:
            return self.companiesCurrentYearData[BSEIndex][Enums.SHAREHOLDINGS.PROMOTOR_HOLDINGS].strip()

    def getHistoricalProfit(self, BSEIndex):
        if self.__wasStockPresent(BSEIndex):
            return  self.companiesLastYearData[BSEIndex][Enums.ANNUALENTITIES.NET_PROFIT].strip()
        else:
            return self.companiesCurrentYearData[BSEIndex][Enums.ANNUALENTITIES.NET_PROFIT].strip()

    def getHistoricalProfitGrowth(self, BSEIndex):
        gowth = round(float(self.getNetProfitData(BSEIndex))) - round(float(self.getHistoricalProfit(BSEIndex)))
        if gowth > 0 and round(float(self.getNetProfitData(BSEIndex))) > 0:
            return str(round(float((gowth*100)/(round(float(self.getNetProfitData(BSEIndex)))))))
        else:
            return str(0)

    def __wasStockPresent(self, BSEIndex):
        return True if self.companiesLastYearData.get(BSEIndex) else False