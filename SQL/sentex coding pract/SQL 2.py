# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:13:32 2021

@author: Rishabh

hERE WE ARE CREATING A DATABASE AND TRYING SOME BASIC COMMAND OF USING SQLITE3 IN PYTHON

"""
import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')
 
conn=sqlite3.connect("tutorial1.db")
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot( unix REAL, datestamp EXT,keyword TEXT, value REAL)")
    
def dynamic_table():
    unix =int(time.time())
    date= str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot(unix , datestamp ,keyword , value ) VALUES (?,?,?,?)",              
              (unix,date,keyword,value))
    
    conn.commit()

# create_table()

# for i in range(0,10):
#     dynamic_table()
#     time.sleep(2)
    
# c.close
# conn.close()

def read_data():
    #c.execute('SELECT * FROM stuffToPlot WHERE value=4')
    ## tochange the arrangement
    c.execute('SELECT keyword, value, unix, datestamp FROM stuffToPlot ')
    # data=c.fetchall()
    # print (data)
    for rows in c.fetchall():
        print(rows)
        
#read_data()

def graph_plot():
    c.execute("SELECT  unix , value FROM stuffToPlot")
    dates=[]
    values=[]
    #plt.figure(figsize=(50,50))
    for rows in c.fetchall():
        # print(rows[0])
       
        # print(datetime.datetime.fromtimestamp(rows[0]))
        # print()
        values.append(rows[1])
        dates.append(datetime.datetime.fromtimestamp(rows[0]))
       
        plt.plot_date(dates,values, '-')
        
        
             
#graph_plot()

def updating_del():
    
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]
    
    c.execute('UPDATE stuffToPlot SET value=10001 WHERE value= 4.0 ')
    conn.commit()
    c.execute("SELECT * FROM stuffToPlot")
    [print(rows)  for rows in c.fetchall()]


    c.execute("DELETE FROM stuffToPlot WHERE value = 10001")     
    conn.commit()  
    c.execute("SELECT * FROM stuffToPlot")
    [print(rows) for rows in c.fetchall()]                     


updating_del()


c.close
conn.close()
              
              
             


