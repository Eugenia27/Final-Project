import numpy as np
import cython
import glob
import matplotlib.pyplot as plt
import plot as po
import bineado as bi
#import matplotlib.ticker import NullFormatter,MultipleLocator, FormatStrFormatter
from matplotlib.offsetbox import AnchoredText



def stack(snap):
    stack=[0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1]
    rall = np.array([])
    metall = np.array([])
    ageall = np.array([])
    first='true'

    for reg in range(30):
        sreg  = str(reg) 
        if reg==0 or stack[reg]==0 or reg==30 or reg>9:
    #if reg==0 or reg>2:
            continue

        #prefijo_inputs='/home/mferraro/inputs/D'+str(reg)+'_LR_minpot3_rmmax_'+snap+'_'
        prefijo_inputs='/home/meugenia/0/LR/inputs_grupo0/D'+str(reg)+'_LR_minpot3_rmmax_'+snap+'_'

        file_mass=''
        for fm in glob.glob(prefijo_inputs+'*NoDust.dat'):  
            file_mass = fm

        print file_mass
   
        #file_obs='/home/mferraro/Dropbox/tesis/al_final/LR/tablas/LR_minpot3_rmmax_'+snap+'_band125_nodust_grupo0.txt'
        file_obs='/home/meugenia/Dropbox/tesis/al_final/LR/tablas/LR_minpot3_rmmax_'+snap+'_band125_nodust_grupo0.txt'
        r24=np.loadtxt(file_obs, usecols=[3],unpack=True)

        pt    =np.array([])
        x     =np.array([])
        y     =np.array([])
        met   =np.array([])
        age   =np.array([])
        rnorm =np.zeros(x)

        pt,x,y,age,met=np.loadtxt(file_mass,usecols=[0,1,2,4,5],unpack=True,skiprows=1)
        r=np.sqrt(x**2+y**2)
        rnorm=[value/float(r24[reg-1]) for value in r]
        #print 'RNORM: ',rnorm[0:10]
        if first=='false':  
            rall   =np.concatenate((rall,rnorm),axis=0) 
            metall =np.concatenate((metall,met),axis=0) 
            ageall =np.concatenate((ageall,age),axis=0) 
            #print len(rall),'  ', len(rnorm)
        if first=='true':
            rall   =rnorm
            metall =met 
            ageall =age 
            first='false'
            #print len(rall),'  ', len(rnorm)

        print 'PASE POR '+str(reg)
    return [rall],[ageall],[metall]


dist1 ,stars1 ,met1=stack('091')
zdist1,zstars1,zmet1=stack('041')


print dist1[:10],'\n',stars1[:10],'\n',met1[:10],'\n',dist1[:10],'\n',stars1[:10],'\n',met1[:10],

myfile0 = open('stackz0.txt','a')
for d in range(len(dist1)):
    myfile0.write('{:10.5g} {:10.5g} {:10.5g} \n'.format(dist1[d],stars1[d],met1[d]))
myfile0.close()

#myfile1 = open('stackz1.txt','a')
#myfile1.write('{:10.5g} {:10.5g} {:10.5g} \n'.format(zdist1,zstars1,m=zmet1))
#myfile1.close()



if 1==0:
    cmg='#92602E'
    cmc='black'
    cag='tomato'
    cac='#0066CC'

    anb  ,axbin  ,abe  ,amedians  ,amatriz   = bi.bineado(dist1,stars1,60,0,np.max(dist1)+5)
    zanb ,zaxbin ,zabe ,zamedians ,zamatriz  = bi.bineado(zdist1,zstars1,60,0,np.max(dist1)+5)
    mnb  ,mxbin  ,mbe  ,mmedians  ,mmatriz   = bi.bineado(dist1,met1,60,0,np.max(dist1)+5)
    zmnb ,zmxbin ,zmbe ,zmmedians ,zmmatriz  = bi.bineado(zdist1,zmet1,60,0,np.max(dist1)+5)

    plt.rc('text', usetex=True)
    font = {'family': 'serif', 'size': 25, 'serif': ['computer modern roman']}
    plt.rc('font', **font)
    plt.rc('legend', **{'fontsize': 17})
    plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']
    plt.rcParams['axes.linewidth'] = 1.0
    plt.rcParams['xtick.major.size'] = 8
    plt.rcParams['xtick.minor.size'] = 4
    plt.rcParams['ytick.major.size'] = 6
    plt.rcParams['ytick.minor.size'] = 3
    plt.rc('lines', linewidth=3)

    amedias=np.array([])
    asigmas=np.array([])
    for k in range(len(axbin)):
        amedias=np.append(amedias,np.mean(amatriz[k]))
        asigmas=np.append(asigmas,np.std(amatriz[k]))

    zamedias=np.array([])
    zasigmas=np.array([])
    for k in range(len(zaxbin)):
        zamedias=np.append(zamedias,np.mean(zamatriz[k]))
        zasigmas=np.append(zasigmas,np.std(zamatriz[k]))


    mmedias=np.array([])
    msigmas=np.array([])
    for k in range(len(mxbin)):
        mmedias=np.append(mmedias,np.mean(mmatriz[k]))
        msigmas=np.append(msigmas,np.std(mmatriz[k]))

    zmmedias=np.array([])
    zmsigmas=np.array([])
    for k in range(len(zmxbin)):
        zmmedias=np.append(zmmedias,np.mean(zmmatriz[k]))
        zmsigmas=np.append(zmsigmas,np.std(zmmatriz[k]))    



    po.gradientes_barras_evolucion([axbin,zaxbin],[amedias,zamedias],[asigmas,zasigmas],
                         [0,1.5],[-1,16],['R [Kpc]','Age [Gyr]'],['Edades-Medias\n z=0','Edades-Medias\n z=1'],
                         '',[cag,cac],[cag,cac],['black','black'],0,
                         'stack_edades.pdf')



    po.gradientes_barras_evolucion([mxbin,zmxbin],[mmedias,zmmedias],[msigmas,zmsigmas],
                         [0,1.5],[-0.01,0.05],['R [Kpc]','Z'],['Z-Medias\n z=0','Z-Medias\n z=1'],
                         '',[cmg,'gray'],[cmg,'gray'],['black','black'],0,
                         'stack_metalicidades.pdf')
