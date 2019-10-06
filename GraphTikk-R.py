import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style



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
    for line in lines:
        if len(line) > 1:
           x, y, y2, y3 = line.split(',')
           xs.append(x[1:-1])
           ys.append(y)
           ys1.append(y2)
           ys2.append(y3)
    ax1.clear()
    ax1.plot( xs, ys, label='Bid')
    ax1.plot( ys1, label='Last ')
    ax1.plot( ys2, label='Ask ' )
    plt.tick_params(axis='x', which='both', bottom=False,top=False,labelbottom=False)
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Price')
    
    #time, bid (gren triangles), last (blue line), Ask (Read Square)    
    


ani = animation.FuncAnimation(fig, animate, interval=100)
plt.title("Crypto Price Graph")
plt.show()
