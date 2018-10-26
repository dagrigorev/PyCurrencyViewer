from ..models.CurrencyModel import CurrencyModel
from flask import render_template


class PlotController():
    def __init__(self):
        self.model = CurrencyModel()
        self.title = "Plot"

    def details(self):
        self.title = "Detailed plot view"

    def Index(self):
        return render_template('layout.html')
