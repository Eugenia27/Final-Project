import numpy as np
import glob
import matplotlib.pyplot as plt
import math as mt
from matplotlib.ticker import NullFormatter,MultipleLocator, FormatStrFormatter
from matplotlib.offsetbox import AnchoredText


def scat_mas_gradiente(d,t,labels,c1,text1,limx,limy,tbin,statistics,c2,text2,psave,slab,sleg,lwd):
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

    fig = plt.figure(figsize=(14,7))

    ax1 = fig.add_subplot(121)
    ax1.scatter(d[0],t[0],marker='.',color=c1[0],s=0.1,label=text1[0])
    ax1.scatter(d[1],t[1],marker='.',color=c1[1],s=0.1,label=text1[1])
    ax1.scatter(d[2],t[2],marker='.',color=c1[2],s=0.1,label=text1[2])   
    ax1.set_xlim(limx[0],limx[1])
    ax1.set_ylim(limy[0],limy[1])
    lgnd=ax1.legend(loc='lower right', frameon=False, scatterpoints=1,borderpad=0.1, labelspacing=0.2,handletextpad=0.1)
    lgnd.legendHandles[0]._sizes = [500]
    lgnd.legendHandles[1]._sizes = [500]
    lgnd.legendHandles[2]._sizes = [500]
    ax1.set_xlabel(labels[0])
    ax1.set_ylabel(labels[1])
    y1t = ax1.yaxis.get_major_ticks()
    y1t[-1].label1.set_visible(False)
    x1t = ax1.xaxis.get_major_ticks()
    x1t[-1].label1.set_visible(False)
    ax1.minorticks_on()
    for t in range(len(x1t)):
        if t%2==0:
            x1t[t].label1.set_visible(False)

    ax2 = fig.add_subplot(122)
    ax2.plot(tbin,statistics[0],color=c2[0], label=text2[0])
    ax2.plot(tbin,statistics[1],color=c2[1], label=text2[1])
    ax2.set_xlabel(labels[0])
    ax2.yaxis.set_major_formatter(NullFormatter())
    ax2.set_xlim(limx[0],limx[1])
    ax2.set_ylim(limy[0],limy[1])
    ax2.legend(loc='lower left', frameon=False, scatterpoints=1,borderpad=0.1, labelspacing=0.2,handletextpad=0.1)
    ax2.minorticks_on()
    x2t = ax2.xaxis.get_major_ticks()
    x2t[-1].label1.set_visible(False)
    for t in range(len(x2t)):
        if t%2==0:
            x2t[t].label1.set_visible(False)
            
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.savefig(psave, format='pdf', dpi=100,bbox_inches='tight')
    plt.show()


def gradiente(limx,limy,labels,tbin,statistics,c2,text2,psave,slab,sleg,lwd):
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

    fig = plt.figure(figsize=(7,7))

    ax1 = fig.add_subplot(111)
    ax1.plot(tbin,statistics[0],color=c2[0], label=text2[0])
    ax1.plot(tbin,statistics[1],color=c2[1], label=text2[1])
    ax1.set_xlim(limx[0],limx[1])
    ax1.set_ylim(limy[0],limy[1])
    ax1.minorticks_on()
    ax1.set_xlabel(labels[0])
    ax1.set_ylabel(labels[1])

    ax1.legend(loc='lower left', frameon=False, scatterpoints=1,borderpad=0.1, labelspacing=0.2,handletextpad=0.1)
    x1t = ax1.xaxis.get_major_ticks()
    x1t[-1].label1.set_visible(False)
    for t in range(len(x1t)):
        if t%2==0:
            x1t[t].label1.set_visible(False)
            
    plt.savefig(psave, format='pdf', dpi=100,bbox_inches='tight')
    plt.show()


def gradiente_evolucion(limx,limy,labels,tbin,statistics1,c1,text1,statistics2,c2,text2,plotz1,plotmedianas,plotcomparacion,cmed1,cmed2,psave,slab,sleg,lwd):
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

    fig = plt.figure(figsize=(7,7))

    ax1 = fig.add_subplot(111)
    ax1.plot(tbin,statistics1[0],color=c1[0], label=text1[0])
    if plotz1=='true':
        ax1.plot(tbin,statistics2[0],color=c2[0], label=text2[0])
    if plotmedianas=='true':
        ax1.plot(tbin,statistics1[1],color=c1[1], label=text1[1],ls='--')
        ax1.plot(tbin,statistics2[1],color=c2[1], label=text2[1],ls='--')
        if plotcomparacion=='true':
            delta2=statistics1[1][0]-statistics2[1][0]
            medias2=statistics2[1]+delta2
            ax1.plot(tbin,medias2,color=cmed2,ls=':',label=text2[1]+'$+$'+str(round(delta2,5))) 
    if plotcomparacion=='true':
        delta1=statistics1[0][0]-statistics2[0][0]
        medias1=statistics2[0]+delta1
        ax1.plot(tbin,medias1,color=cmed1,ls=':',label=text2[0]+'$+$'+str(round(delta1,5))) 

    ax1.set_xlim(limx[0],limx[1])
    ax1.set_ylim(limy[0],limy[1])

    ax1.set_xlabel(labels[0])
    ax1.set_ylabel(labels[1])
    ax1.minorticks_on() 
    ax1.legend(loc='lower left', frameon=False, scatterpoints=1,borderpad=0.1, labelspacing=0.2,handletextpad=0.1)
    x1t = ax1.xaxis.get_major_ticks()
    x1t[-1].label1.set_visible(False)
    for t in range(len(x1t)):
        if t%2==0:
            x1t[t].label1.set_visible(False)
            
    plt.savefig(psave, format='pdf', dpi=100,bbox_inches='tight')
    plt.show()
