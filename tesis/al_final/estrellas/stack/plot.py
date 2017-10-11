import numpy as np
import glob
import matplotlib.pyplot as plt
import math as mt
from matplotlib.ticker import NullFormatter,MultipleLocator, FormatStrFormatter
from matplotlib.offsetbox import AnchoredText


def gradientes_barras_evolucion(axbin,amedias,asigmas,limx,limy,labels,legends,title,cl,ce,cm,comparar,psave):
    fig=plt.figure(1, figsize=(7, 7))
    ax1 = fig.add_subplot(111)
    ax1.minorticks_on()
    plt.errorbar(axbin[0], 
        amedias[0], 
        asigmas[0], 
        capsize=1, 
        elinewidth=1.,
        markeredgewidth=1,ecolor=ce[0],color=cl[0],marker='o',mec=cm[0],lw=2,label=legends[0])
    if comparar==1:
        delta=amedias[0][0]-amedias[1][0]
        comp=amedias[1]+delta
        plt.errorbar(axbin[1], 
        comp, 
        asigmas[1], 
        capsize=1, 
        elinewidth=1.,
        markeredgewidth=1,ecolor=ce[1],color=cl[1],marker='o',mec=cm[1],lw=2,label=legends[1]+'(+'+str(round(delta,5))+')')                
    else:
        plt.errorbar(axbin[1], 
        amedias[1], 
        asigmas[1], 
        capsize=1, 
        elinewidth=1.,
        markeredgewidth=1,ecolor=ce[1],color=cl[1],marker='o',mec=cm[1],lw=2,label=legends[1])
    
    plt.legend(loc='lower right', frameon=False, scatterpoints=1,borderpad=0.5,handletextpad=1,ncol=2)
    plt.xlim(limx[0],limx[1])
    plt.ylim(limy[0],limy[1])
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.savefig(psave, format='pdf', dpi=100,bbox_inches='tight')
    plt.show()
