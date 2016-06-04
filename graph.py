import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from scipy import stats
from sklearn import datasets, linear_model
from mpl_toolkits.mplot3d.axes3d import Axes3D

def twoD(x,y1,y2):
    plt.plot(x,y1,color='r',ls=':',label='Flash Viewers')
    plt.plot(x,y2,color='b',label='Arrow Viewers')
    plt.xlabel('Episodes')
    plt.ylabel('viewers')
    plt.title('Prediction Of TV Serials')
    plt.legend()
    plt.show()

def threeD(x,y1,y2,z):
    fig = plt.figure(figsize=(14,6))
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.plot_surface(x, y1, z)
    ax.plot_surface(x, y2, z)


data = pd.read_csv('C:\Users\Parth\Downloads\data_science\open_data.csv')
f=[]
a=[]
e=[]
z=[1,2,3,4,5,6,7,8,9]
f=data['flash_us_viewers']
a=data['arrow_us_viewers']
e=data['flash_episode']

twoD(e,f,a)
#threeD(e,f,a,z)