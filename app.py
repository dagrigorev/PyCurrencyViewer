from flask import Flask
from currency.controllers.PlotController import PlotController


app = Flask(__name__)
plot = PlotController()

@app.route("/")
def Index():
    return plot.Index()
