#http://webs.ucm.es/info/aocg/python/modulos_cientificos/matplotlib/index.html
#Librerias para graficar
import matplotlib.pyplot as plt

#Clase Neurona
from Neurona import neurona

#Limite para disparo
Threshold=1

#Iniciamos 2 neuronas
n1=neurona(FiringTime=[2,5],Weigh=0.75,Delay=1,Tau=3)
n2=neurona(FiringTime=[5,6],Weigh=0.25,Delay=1.75,Tau=3)


#Las agregamos a una lista de neuronas
NeuronList=[n1,n2]

#Definimos una funcion para obtener Ui(t)
def TotalUi(listaYs,ActualTime):
    result=0
    for y in listaYs:
        result+=y
    return result

#Definimos listas para graficar los resultados de cada neurona
UiN1List=[]
UiN2List=[]
#Definimos una lista para graficar Ui(t)
UiList=[]

listaYs=[]
#Iniciamos el 'tiempo'
for i in range(21):

    if TotalUi(listaYs,i)>Threshold:
        i=0
        UiList.append(0)
    else:
        #Agregamos a las listas los totales de las operaciones
        UiList.append(TotalUi(listaYs,i))
        for j in range(len(n1.FiringTime)):
            UiN1List.append(n1.Ui(i,j))
        for j in range(len(n2.FiringTime)):
            UiN2List.append(n2.Ui(i,j))


        print("Actual Time: "+str(i))
        '''
        print("Neurona 1:")
        for j in range(len(n1.FiringTime)):
            print("Arg 2: "+str(n1.Eargs(i,j)))
            print("Y: "+str(n1.Ye(i,j)))
            print("Ui1: "+str(n1.Ui(i,j)))
        '''
        #print("Neurona 1:")
        for j in range(len(n1.FiringTime)):
            print("Arg "+str(n1.FiringTime[j])+": "+str(n1.Eargs(i,j))+" | Y: " + str(n1.Ye(i,j)))
            #print("Ui: "+str(n1.Ui(i,j)))


#Graficamos
plt.figure()
plt.plot(UiN1List,label="Ui de Neurona 1")
#plt.plot(UiN2List,label="Ui de Neurona 2")
#plt.plot(UiList,label="Ui")
plt.title('Spikes')

#plt.show()
