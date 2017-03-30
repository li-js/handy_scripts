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
