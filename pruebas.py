#http://webs.ucm.es/info/aocg/python/modulos_cientificos/matplotlib/index.html
#Librerias para graficar
import matplotlib.pyplot as plt

#Clase Neurona
from Neurona import neurona

#Iniciamos 2 neuronas
n1=neurona(FiringTime=[2,5],Weigh=0.5,Delay=1,Tau=3)
n2=neurona(FiringTime=[5,6],Weigh=0.5,Delay=1.5,Tau=5)

Threshold=0.8

#Las agregamos a una lista de neuronas
NeuronList=[n1,n2]

#Definimos una funcion para obtener Ui(t)
def TotalUi(NeuronList,ActualTime):
    result=0
    for neuron in NeuronList:
        for i in range(len(neuron.FiringTime)):
            result+=neuron.Ui(ActualTime,i)
    return result

#Definimos listas para graficar los resultados de cada neurona
UiN1List=[]
UiN2List=[]
#Definimos una lista para graficar Ui(t)
UiList=[]
#Iniciamos el 'tiempo'
for i in range(21):
'''
    if i == 2:
        n1.FiringTime.append(i)
    if i == 5:
        n1.FiringTime.append(i)
        n2.FiringTime.append(i)
    if i == 6:
        n2.FiringTime.append(i)
'''


    if TotalUi(NeuronList,i)>Threshold:
        i=0
    else:
        #Agregamos a las listas los totales de las operaciones
        UiList.append(TotalUi(NeuronList,i))
        for j in range(len(n1.FiringTime)):
            UiN1List.append(n1.Ui(i,j))
        for j in range(len(n2.FiringTime)):
            UiN2List.append(n2.Ui(i,j))


        print("Actual Time: "+str(i))
        print("Neurona 1:")
        print("Arg 2: "+str(n1.Eargs(i)))
        print("Y: "+str(n1.Ye(i)))
        print("Ui1: "+str(n1.Ui(i)))
        '''
        print("Neurona 2:")
        print("Arg: "+str(n2.Eargs(i)))
        print("Y: "+str(n2.Ye(i)))
        print("Ui2: "+str(n2.Ui(i)))
        '''

#Graficamos
plt.figure()
plt.plot(UiN1List,label="Ui de Neurona 1")
plt.plot(UiN2List,label="Ui de Neurona 2")
plt.plot(UiList,label="Ui")
plt.title('Spikes')

plt.show()
