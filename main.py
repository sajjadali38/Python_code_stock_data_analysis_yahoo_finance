from flask import Flask
from flask import request
from flask import render_template
from pandas_datareader import data as pdr
import tkinter
from tkinter import messagebox

import datetime as dt
import fix_yahoo_finance as yf
import numpy as np
from numpy.lib.function_base import average
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def my_form():   
    return render_template("my-form.html")


@app.route('/chart', methods=['POST'])
#Method "def chart()" display one month data for Corn, Gasoline and Nasdaq in a chart
def chart():
    symbols = ['CORN', 'UGA', 'NDAQ']  # defining stock value for each stock
    data = yf.download(symbols,'2018-01-01','2018-01-31') # download data from yahoo finance api
    data.Close.plot() # plot the data
    plt.show()  # show the data
    return render_template("my-form.html") 

@app.route('/my_form_post', methods=['POST'])
 #Method "my_form_post()" display the average of three days
def my_form_post():
    
    yf.pdr_override() #takes value from yahoo finance 
    start = '2018-1-29' # specify the start period
    #end = '2018-1-31'
    end = dt.datetime(2018, 2, 1) # specify the end period
    #end=dt.datetime.today()
    result=pdr.get_data_yahoo("CORN", start, end) # getting the corn data and stored in variable "result"
    [numofDays, numOfAttributes]=np.shape(result)  #shape attribute for numpy arrays returns the dimensions of the array in rows(numofDays) and columns(numOfAttributes)
    averageStatistics=np.sum(result, axis=0)  # np.sum sum up the values
    averageOpeningVal=averageStatistics[0]/3 # getting average of the opening value by array index
    averageHighVal=averageStatistics[1]/3  # getting average of the High value by array index
    averageLowVal=averageStatistics[2]/3  # getting average of the Low value by array index
    averageClosingVal=averageStatistics[3]/3 # getting average of the closing value by array index
    averageAdjVal=averageStatistics[4]/3 # getting average of the adj value by array index
    averageVolVal=averageStatistics[5]/3 # getting average of the volume  by array index
    root = tkinter.Tk()  
    root.withdraw() # hide Python tkinter root window
    # messagebox showing the forecast value of CORN
    messagebox.showinfo('Forecast Value: Teucrium Corn ETF (CORN)', "\n".join(["CORN", "\n","Average opening value is: " + str(averageOpeningVal), "Average high value is:" + str(averageHighVal),"Average low value is:" + str(averageLowVal), "Average closing value is:" + str(averageClosingVal), "Average Adj value is:" + str(averageAdjVal), "Average Volume value is:" + str(averageVolVal)]))
    result1=pdr.get_data_yahoo("UGA", start, end) # getting the UGA data and stored in variable "result"
    [numofDays, numOfAttributes]=np.shape(result1) #shape attribute for numpy arrays returns the dimensions of the array in rows(numofDays) and columns(numOfAttributes)
    averageStatistics=np.sum(result1, axis=0)  # np.sum sum up the values
    averageOpeningVal=averageStatistics[0]/3 # getting average of the opening value by array index
    averageHighVal=averageStatistics[1]/3 # getting average of the High value by array index
    averageLowVal=averageStatistics[2]/3  # getting average of the Low value by array index
    averageClosingVal=averageStatistics[3]/3  # getting average of the closing value by array index
    averageAdjVal=averageStatistics[4]/3  # getting average of the adj value by array index
    averageVolVal=averageStatistics[5]/3  # getting average of the volume  by array index
    # messagebox showing the forecast value of Gasoline
    messagebox.showinfo('Forecast Value: United States Gasoline (UGA)', "\n".join(["Gasoline", "\n","Average opening value is: " + str(averageOpeningVal), "Average high value is:" + str(averageHighVal),"Average low value is:" + str(averageLowVal), "Average closing value is:" + str(averageClosingVal), "Average Adj value is:" + str(averageAdjVal), "Average Volume value is:" + str(averageVolVal)]))
    result2=pdr.get_data_yahoo("NDAQ", start, end) # getting the NDAQ data and stored in variable "result"
    [numofDays, numOfAttributes]=np.shape(result2)  #shape attribute for numpy arrays returns the dimensions of the array in rows(numofDays) and columns(numOfAttributes)
    averageStatistics=np.sum(result2, axis=0)   # np.sum sum up the values
    averageOpeningVal=averageStatistics[0]/3  # getting average of the opening value by array index
    averageHighVal=averageStatistics[1]/3   # getting average of the High value by array index
    averageLowVal=averageStatistics[2]/3   # getting average of the Low value by array index
    averageClosingVal=averageStatistics[3]/3  # getting average of the closing value by array index
    averageAdjVal=averageStatistics[4]/3  # getting average of the adj value by array index
    averageVolVal=averageStatistics[5]/3   # getting average of the volume  by array index
    # messagebox showing the forecast value of Nasdaq
    messagebox.showinfo('Forecast Value: Nasdaq, Inc. (NDAQ)', "\n".join(["Nasdaq", "\n","Average opening value is: " + str(averageOpeningVal), "Average high value is:" + str(averageHighVal),"Average low value is:" + str(averageLowVal), "Average closing value is:" + str(averageClosingVal), "Average Adj value is:" + str(averageAdjVal), "Average Volume value is:" + str(averageVolVal)]))
    root.deiconify() # make the window visible again
    root.destroy() # destroy the root window along with all other tkinter widgets
    
    return render_template("my-form.html") 

if __name__ == '__main__':
    app.run()


