import numpy as np
import math as mt

def bineado(x,entity,bins,init,end):
    step=(end-init)/bins
    nelements  =np.zeros(bins)
    bin_entity =np.zeros(bins)
    xbin       =np.zeros(bins)
    medians    =np.zeros(bins)

    matrixbin  = []
    
    for j in range(bins):
        matrixbin.append([])    
    
    for i in range(len(entity)):
        ibin = int(mt.floor((x[i]-init/step)))
        if ibin>=bins:
            continue
        else:
            nelements[ibin] += 1
            bin_entity[ibin] = bin_entity[ibin] + entity[i]
            matrixbin[ibin].append(entity[i])
            
    for k in range(bins):
        medians[k]=np.median(matrixbin[k])
        
    xbin=[init+0.5*(2*i+1)*step for i in range(bins)]    
    return nelements,xbin,bin_entity,medians,matrixbin
