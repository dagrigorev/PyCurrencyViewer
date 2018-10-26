# Import libraries
import requests
import pandas as pd


class IMFData():
    def __init__(self):
        self.startPeriod = 1976
        self.endPeriod = 2016
        self.url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/Q.AU.PXP_IX.?startPeriod={' \
              '0}&endPeriod={1}'

    def GetData(self, name):
        # Get data from the above URL using the requests package
        data = requests.get(self.url.format(self.startPeriod, self.endPeriod)).json()
        return pd.DataFrame(data['CompactData']['DataSet']['Series'][name])

    def GetOBS(self):
        return self.GetData(self, 'Obs')

    def GetDollarData(self):
        return self.GetData(self, 'Dollar')
