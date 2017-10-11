import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from matplotlib.ticker import NullFormatter#,MultipleLocator, FormatStrFormatter
from matplotlib.offsetbox import AnchoredText
import os
import math as mt

def superplot(x,y,c,text,psave,slab,sleg,lwd):

    plt.rc('text', usetex=True)
    font = {'family': 'serif', 'size': slab, 'serif': ['computer modern roman']}
    plt.rc('font', **font)
    plt.rc('legend', **{'fontsize': sleg}) 
    plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

    plt.rcParams['axes.linewidth'] = 1.0
    plt.rcParams['xtick.major.size'] = 8
    plt.rcParams['xtick.minor.size'] = 4
    plt.rcParams['ytick.major.size'] = 6
    plt.rcParams['ytick.minor.size'] = 3
    plt.rc('lines', linewidth=lwd)


    nullfmt = NullFormatter()  
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    plt.figure(1, figsize=(8, 8))

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)

    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    axScatter.scatter(x[0],y[0],marker='.',s=0.1,color=c[0],label=text[0]) 
    axScatter.scatter(x[1],y[1],marker='.',s=0.1,color=c[1],label=text[1])
    axScatter.minorticks_on() 
    binwidth = 0.25
    xymax = np.max([np.max(np.fabs(x[0])), np.max(np.fabs(y[0]))])
    lim = (int(xymax/binwidth) + 1) * binwidth

    axScatter.set_xlim((-lim, lim))
    axScatter.set_ylim((-lim, lim))

    axScatter.set_xlabel('X [Kpc]') 
    axScatter.set_ylabel('Y [Kpc]')

    lgnd=axScatter.legend(loc='upper right', frameon=False, scatterpoints=1,borderpad=0.1,handletextpad=0.001)
    
    lgnd.legendHandles[0]._sizes = [500]
    lgnd.legendHandles[1]._sizes = [500]

    bins = np.histogram(np.hstack((x[0],x[1])), bins=50)[1]
    axHistx.hist(x[0], bins=bins,edgecolor=c[0],color='white',facecolor='none',histtype='stepfilled')
    axHistx.hist(x[1], bins=bins,edgecolor=c[1], color='white',facecolor='none',histtype='stepfilled',hatch='//',linewidth=1)
    axHistx.set_ylabel('N')

    bins = np.histogram(np.hstack((y[0],y[1])), bins=50)[1]
    axHisty.hist(y[0], bins=bins,edgecolor=c[0],color='white',facecolor='none',histtype='stepfilled',
             orientation='horizontal')
    axHisty.hist(y[1], bins=bins,edgecolor=c[1], color='white',facecolor='none',histtype='stepfilled',hatch='//',linewidth=1,
             orientation='horizontal')
    axHisty.set_xlabel('N')

    yticksv = axHisty.xaxis.get_major_ticks()
    for t in range(len(yticksv)):
        if t%3!=0:
            yticksv[t].label1.set_visible(False)

    yticksh = axHistx.yaxis.get_major_ticks()
    for t in range(len(yticksh)):
        if t%5!=0:
            yticksh[t].label1.set_visible(False)
       
    axHistx.set_xlim(axScatter.get_xlim())
    axHisty.set_ylim(axScatter.get_ylim())

    plt.savefig(psave, format='pdf', dpi=100,bbox_inches='tight')
    plt.show()
