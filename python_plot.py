# For machine with no display environment
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# For machine with no display environment
from pylab import plt

# Begin plotting ..
fig = plt.figure(figsize=(12, 8))
plt.plot(x,y)
plt.plot(x2,y2)

plt.legend(['l1', 'l2'],  loc=0,fontsize=20)
plt.gca().grid()
plt.gca().set_xlim((0, 55))
plt.xticks(fontsize=20)
#gca().set_ylim((0, 2000))
plt.yticks(fontsize=20)
plt.xlabel("x variable", fontsize=30)
plt.ylabel("y variable", fontsize=30)
plt.savefig('sample.pdf') 
plt.show()

#The following is used when set figure window to some fixed locations
mngr = plt.get_current_fig_manager()
mngr.window.setGeometry(0,0,500, 500)

# color list for distinct plots
from matplotlib.pyplot import cm 
color_list=cm.rainbow(np.linspace(0,1,len(algos)))


# Name and auto rotate the x-ticks
plt.legend(handles=legend_handles,  scatterpoints=1, loc='lower left', fontsize=15)
plt.xticks(range(5)), ['names']*5, fontsize=15)
plt.yticks(fontsize=15)
fig.autofmt_xdate()
