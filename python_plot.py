from pylab import *
figure(figsize=(12, 8))

plot(x,y)
plot(x2,y2)

legend(['l1', 'l2'],  loc=0,fontsize=20)
grid()
gca().set_xlim((0, 55))
xticks(fontsize=20)
#gca().set_ylim((0, 2000))
yticks(fontsize=20)
xlabel("x variable", fontsize=30)
ylabel("y variable", fontsize=30)
pylab.savefig('sample.pdf')
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
