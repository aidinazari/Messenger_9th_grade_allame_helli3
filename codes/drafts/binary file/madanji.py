#be name khoda

import csv
import matplotlib.pyplot as plt

#setoza flowers info
setoza_tool_kas=[]
setoza_arz_kas=[]
setoza_tool_gol=[]
setoza_arz_gol=[]

#versocolor flowers info
ver_tool_kas=[]
ver_arz_kas=[]
ver_tool_gol=[]
ver_arz_gol=[]

#virginia flowers info
vir_tool_kas=[]
vir_arz_kas=[]
vir_tool_gol=[]
vir_arz_gol=[]

#flowers distance
setoza_kas_distance=[]
ver_kas_distance=[]
vir_kas_distance=[]
setoza_gol_distance=[]
ver_gol_distance=[]
vir_gol_distance=[]

#inputs
tool_kas=float(input('tool kasbarg:     '))
arz_kas=float(input('arz kasbarg:     '))
tool_gol=float(input('tool golbarg:     '))
arz_gol=float(input('arz golbarg:     '))

#oghlidosi distance
def distance(y1,y2,x1,x2):
    c=0
    if y1>y2:
        c=y1
        y1=y2
        y2=c
        c=0
    elif x1>x2:
        c=x1
        x1=x2
        x2=c
        c=0
    ans=(y2-y1)**2+(x2-x1)**2
    ans=ans**(0.5)
    if ans<0:
        ans=ans*-1
    return ans

with open("iris22.csv","r") as infofile:
    inforeader=csv.reader(infofile)
    for row in inforeader:
        if row[4]=='Iris-setosa':
            setoza_tool_kas.append(float(row[0]))
            setoza_arz_kas.append(float(row[1]))
            setoza_tool_gol.append(float(row[2]))
            setoza_arz_gol.append(float(row[3]))
        elif row[4]=='Iris-versicolor':
            ver_tool_kas.append(float(row[0]))
            ver_arz_kas.append(float(row[1]))
            ver_tool_gol.append(float(row[2]))
            ver_arz_gol.append(float(row[3]))
        elif row[4]=='Iris-virginica':
            vir_tool_kas.append(float(row[0]))
            vir_arz_kas.append(float(row[1]))
            vir_tool_gol.append(float(row[2]))
            vir_arz_gol.append(float(row[3]))
    #set moteghaier
    setoza_num=[]
    ver_num=[]
    vir_num=[]
    for i in range(1,51):
        setoza_num+=[i]
    for i in range(51,101):
        ver_num+=[i]
    for i in range(101,151):
        vir_num+=[i]
    #drawing chart
    f1=plt.figure('tool va arz kasbarg')
    plt.plot(setoza_tool_kas,setoza_arz_kas,marker='*',linestyle='',color='r',label='setoza')
    plt.plot(ver_tool_kas,ver_arz_kas,marker='o',linestyle='',color='b',label='versicolor')
    plt.plot(vir_tool_kas,vir_arz_kas,marker='p',linestyle='',color='y',label='virginica')
    plt.plot(tool_kas,arz_kas,marker='D',linestyle='',color='m',label='majhol')
    plt.title('tool va arz kasbarg giyahan')
    plt.xlabel('tool kasbarg')
    plt.ylabel('arz kasbarg')
    plt.legend()
    f1.show()
    #drawing chart
    f2=plt.figure('tool va arz golbarg')
    plt.plot(setoza_tool_gol,setoza_arz_gol,marker='*',linestyle='',color='r',label='setoza')
    plt.plot(ver_tool_gol,ver_arz_gol,marker='o',linestyle='',color='b',label='versicolor')
    plt.plot(vir_tool_gol,vir_arz_gol,marker='p',linestyle='',color='y',label='virginica')
    plt.plot(tool_gol,arz_gol,marker='D',linestyle='',color='m',label='majhol')
    plt.title('tool va arz golbarg giyahan')
    plt.xlabel('tool golbarg')
    plt.ylabel('arz golbarg')
    plt.legend()
    f2.show()
    #distance in kasbarg
    for i in range(50):
        setoza_kas_distance+=[(distance(float(setoza_arz_kas[i]),arz_kas,float(setoza_tool_kas[i]),tool_kas))]
        ver_kas_distance+=[(distance(float(ver_arz_kas[i]),arz_kas,float(ver_tool_kas[i]),tool_kas))]
        vir_kas_distance+=[(distance(float(vir_arz_kas[i]),arz_kas,float(vir_tool_kas[i]),tool_kas))]
    #distance in golbarg
    for i in range(50):
        setoza_gol_distance+=[(distance(float(setoza_arz_gol[i]),arz_gol,float(setoza_tool_gol[i]),tool_gol))]
        ver_gol_distance+=[(distance(float(ver_arz_gol[i]),arz_gol,float(ver_tool_gol[i]),tool_gol))]
        vir_gol_distance+=[(distance(float(vir_arz_gol[i]),arz_gol,float(vir_tool_gol[i]),tool_gol))]
    #sorting
    setoza_kas_distance.sort()
    ver_kas_distance.sort()
    vir_kas_distance.sort()
    setoza_gol_distance.sort()
    ver_gol_distance.sort()
    vir_gol_distance.sort()
    #knn algoritm
    setoza_kas_m=0
    ver_kas_m=0
    vir_kas_m=0
    setoza_gol_m=0
    ver_gol_m=0
    vir_gol_m=0
    for i in range(50):
        setoza_kas_m+=float(setoza_kas_distance[i])
        ver_kas_m+=float(ver_kas_distance[i])
        vir_kas_m+=float(vir_kas_distance[i])
        setoza_gol_m+=float(setoza_gol_distance[i])
        ver_gol_m+=float(ver_gol_distance[i])
        vir_gol_m+=float(vir_gol_distance[i])
    setoza_kas_m=setoza_kas_m/50
    ver_kas_m=ver_kas_m/50
    vir_kas_m=vir_kas_m/50
    setoza_gol_m=setoza_gol_m/50
    ver_gol_m=ver_gol_m/50
    vir_gol_m=vir_gol_m/50
    print('\n','etelaate kasbarg ha\n')
    print(setoza_kas_distance,'\n')
    print(setoza_kas_m,'\n')
    print(ver_kas_distance,'\n')
    print(ver_kas_m,'\n')
    print(vir_kas_distance,'\n')
    print(vir_kas_m,'\n')
    print('etelaate golbarg ha\n')
    print(setoza_gol_distance,'\n')
    print(setoza_gol_m,'\n')
    print(ver_gol_distance,'\n')
    print(ver_gol_m,'\n')
    print(vir_gol_distance,'\n')
    print(vir_gol_m,'\n')
    #answer kasbarg
    if setoza_kas_m<ver_kas_m and setoza_kas_m<vir_kas_m:
        print('by kasbargs=Iris setoza')
    elif ver_kas_m<setoza_kas_m and ver_kas_m<vir_kas_m:
        print('by kasbarg=Iris versicolor')
    elif vir_kas_m<setoza_kas_m and vir_kas_m<ver_kas_m:
        print('by kasbarg=Iris virginica')
    #answer golbarg
    if setoza_gol_m<ver_gol_m and setoza_gol_m<vir_gol_m:
        print('by golbargs=Iris setoza')
    elif ver_gol_m<setoza_gol_m and ver_gol_m<vir_gol_m:
        print('by golbarg=Iris versicolor')
    elif vir_gol_m<setoza_gol_m and vir_gol_m<ver_gol_m:
        print('by golbarg=Iris virginica')
    
        
    
    

        
        
   
