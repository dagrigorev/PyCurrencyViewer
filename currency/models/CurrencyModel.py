from IMF import IMFData

class CurrencyModel():
    def __init__(self):
        self.currencyData = []
        self.imfData = IMFData.IMFData()

    def GetData(self, startDate, endDate):
        self.imfData.startPeriod = startDate
        self.imfData.endPeriod = endDate
        self.currencyData = self.imfData.GetDollarData()
