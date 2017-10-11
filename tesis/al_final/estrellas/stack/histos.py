import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import plotly.plotly as py

def histograma(h1,h2,bines,ylim,xlim1,xlim2,save,labelx,labely,leg1,leg2,color,ticks,anotacion,m1,m2,t1,t2):
    fig = plt.figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(111)
    if len(h2)!=0:
        bins = np.histogram(np.hstack((h1,h2)), bins=bines)[1]
        ax.hist(h1, bins=bins, color=color,facecolor='none',histtype='stepfilled',linewidth=1, label=leg1)
        ax.hist(h2, bins=bins,color=color,facecolor='none',histtype='stepfilled', hatch='//', label=leg2)
    else:
        bins = bines
        ax.hist(h1, bins=bins, color=color,facecolor='none',histtype='stepfilled',hatch='xx',linewidth=1, label=leg1)
        
    if m1!='none':
        plt.axvline(x=m1,color='red',label=t1+'= '+str(round(m1,2)),ls='--',lw=2)
    if m2!='none':    
        plt.axvline(x=m2,color='blue',label=t2+'= '+str(round(m2,2)),ls=':',lw=2)

    plt.xlim(xlim1,xlim2)
    plt.ylim(0,ylim)
    xticks1 = ax.xaxis.get_major_ticks()
    xticks1[0].label1.set_visible(False)
    if ticks:
        for i in range(len(xticks1)):
            if i%2!=0:
                xticks1[i].label1.set_visible(False)

    yticks1 = ax.yaxis.get_major_ticks()
    for i in range(len(yticks1)):
            if i%2==0:
                yticks1[i].label1.set_visible(False)    
                
    yticks1[0].label1.set_visible(False)
    plt.legend(loc='upper left', frameon=False,scatterpoints=1,borderpad=0.2,
        labelspacing=0.3,handlelength=2,handletextpad=0.5,borderaxespad=1)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.minorticks_on()
    
    ax.annotate(anotacion, xy=(1, 1),color='gray', xytext=(-70, -130), fontsize=30,
                 xycoords='axes fraction', textcoords='offset points',
                 horizontalalignment='left', verticalalignment='bottom') 
    
    
    plt.savefig(save, format='pdf', dpi=1300,bbox_inches='tight')
    plt.show()
