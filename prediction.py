import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from scipy import stats
from sklearn import datasets, linear_model

def get_data(open_data):
 data = pd.read_csv(open_data)
 flash_x_parameter = []
 flash_y_parameter = []
 arrow_x_parameter = []
 arrow_y_parameter = []
 
 #print data['flash_episode'] 
 #print data['flash_us_viewers']
 #print data['arrow_episode']
 #print data['arrow_us_viewers']
 
 for x1,y1,x2,y2 in zip(data['flash_episode'],data['flash_us_viewers'],data['arrow_episode'],data['arrow_us_viewers']):
     flash_x_parameter.append([float(x1)])
     flash_y_parameter.append(float(y1))
     arrow_x_parameter.append([float(x2)])
     arrow_y_parameter.append(float(y2))
     return flash_x_parameter,flash_y_parameter,arrow_x_parameter,arrow_y_parameter
     

def more_viewers(x1,y1,x2,y2):
 regr1 = linear_model.LinearRegression()
 regr1.fit(x1, y1)
 predicted_value1 = regr1.predict(9)
 print predicted_value1
 
 regr2 = linear_model.LinearRegression()
 regr2.fit(x2, y2)
 predicted_value2 = regr2.predict(9)
 print predicted_value2
 
 if predicted_value1 > predicted_value2:
  print "The Flash Tv Show will have more viewers for next week"
 else:
  print "Arrow Tv Show will have more viewers for next week"
  
x1,y1,x2,y2 = get_data('C:\Users\Parth\Downloads\data_science\open_data.csv')
print x1
more_viewers(x1,y1,x2,y2)