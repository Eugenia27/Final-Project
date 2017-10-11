import numpy as np
import math as mt
import glob

def cargo_datos(reg,snap,lc,uc,lg,ug):  
    primeraparte='/home/meugenia/0/LR/inputs_grupo0/D'+str(reg)+'_LR_minpot3_rmmax_'+snap+'_'
    for path_mass in glob.glob(primeraparte + '*NoDust.dat'):     #*NoDust.dat para polvo *L500kpc.dat sin polvo
        path_mas = path_mass
    print path_mass
    pt    =np.array([])
    x     =np.array([])
    y     =np.array([])
    stars =np.array([])
    met   =np.array([])        
    xb    =np.array([])
    yb    =np.array([])    
    sb    =np.array([])   
    xr    =np.array([])
    yr    =np.array([])    
    sr    =np.array([])    
    pm    =np.array([])
    stars1=np.array([])
    met1  =np.array([])
    dist1 =np.array([])
    x1    =np.array([])
    y1    =np.array([])   
    pt,x,y,stars,met,pm=np.loadtxt(path_mass,usecols=[0,1,2,4,5,8],unpack=True,skiprows=1)
    dist=np.sqrt(x**2+y**2)   
    for i in range(len(stars)):
        if pt[i]!=-1 or met[i]==-666.67:
            continue
        if stars[i]>0 and stars[i]<50:
            stars1=np.append(stars1,stars[i])
            dist1=np.append(dist1,dist[i])
            met1=np.append(met1,met[i])
            x1=np.append(x1,x[i])
            y1=np.append(y1,y[i])
            if stars[i]>lc and stars[i]<=uc:
                xb=np.append(xb,x[i])
                yb=np.append(yb,y[i])
                sb=np.append(sb,stars[i])             
            if stars[i]>lg and stars[i]<ug:
                xr=np.append(xr,x[i])
                yr=np.append(yr,y[i])
                sr=np.append(sr,stars[i])
                
    return dist1,stars1,met1,x1,y1,xb,yb,sb,xr,yr,sr

def metalicidades_limit(x1,y1,met1,limr,limp):
    xmb  =np.array([])
    ymb  =np.array([])    
    z1   =np.array([])   
    xmr  =np.array([])
    ymr  =np.array([])    
    z2   =np.array([]) 
    for i in range(len(x1)):
        if met1[i]<=limr[1] and met1[i]>=limr[0]:
    	    z1 = np.append(z1,met1[i])
    	    xmb= np.append(xmb,x1[i])
    	    ymb= np.append(ymb,y1[i])
        elif met1[i]<=limp[1] and met1[i]>=limp[0]: 
            z2 = np.append(z2,met1[i])
    	    xmr= np.append(xmr,x1[i])
    	    ymr= np.append(ymr,y1[i])
    return z1,xmb,ymb,z2,xmr,ymr




