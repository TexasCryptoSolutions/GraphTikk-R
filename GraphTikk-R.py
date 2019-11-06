import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np
import math
import statistics as st
from matplotlib import style
from datetime import datetime as dt



style.use('fivethirtyeight')

fig = plt.figure()
fig.autofmt_xdate()

ax1 = fig.add_subplot(1,1,1)


def animate(i):
    graph_data = open('Tikk-RData.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    ys1 = []
    ys2 = []
    sys1 = []
    line_num = 0
    for line in lines:
        
        if len(line) > 1:
           x, y, y2, y3 = line.split(',')
           xTime = (x)
           dObj = dt.strptime( xTime[1:-1] , '%H:%M:%S')
           xs.append(str(dObj))
           ys.append(float(y))
           ys1.append(float(y2))
           ys2.append(float(y3))
           yyy = float(y)
           yyyy = float(y2)
           yyyyy = float(y3)
           
           line_num += 1
           data = [yyy, yyyyy, yyyyy]
           xdata = st.mean(data)
           sys1.append(xdata)
           print(line_num)
          
           
    
    ax1.clear()
    ax1.plot( xs, ys, label='Bid')
    ax1.plot( xs, ys1, label='Last ')
    ax1.plot( xs, ys2, label='Ask ' )
    ax1.plot( sys1, label='Computation')
    ax1.grid(b=True, which='major', color='w', linewidth=1.5)
    ax1.grid(b=True, which='minor', color='w', linewidth=0.75)
    plt.rcParams.update({'font.size': 8})
    plt.subplots_adjust(bottom=0.30)
    plt.legend()
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Time')
    plt.ylabel('Price')
   
    plt.tight_layout()

    
    #time, bid (gren triangles), last (blue line), Ask (Read Square)    
    

fig.tight_layout()
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.title("Crypto Price Graph")
plt.show()
