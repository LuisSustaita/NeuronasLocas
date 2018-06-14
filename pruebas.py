#http://webs.ucm.es/info/aocg/python/modulos_cientificos/matplotlib/index.html
#Librerias para graficar
import seaborn as sns
import matplotlib.pyplot as plt
#Clase Neurona
from Neurona import neurona

#Iniciamos 2 neuronas
n1=neurona(FiringTime=2,Weigh=0.5,Delay=1,Tau=3)
n2=neurona(FiringTime=5,Weigh=0.5,Delay=1.5,Tau=5)

#Las agregamos a una lista de neuronas
NeuronList=[n1,n2]

#Definimos una funcion para obtener Ui(t)
def TotalUi(NeuronList,ActualTime):
    result=0
    for neuron in NeuronList:
        result+=neuron.Ui(ActualTime)
    return result

#Definimos listas para graficar los resultados de cada neurona
UiN1List=[]
UiN2List=[]
#Definimos una lista para graficar Ui(t)
UiList=[]

#Iniciamos el 'tiempo'
for i in range(21):
    #Agregamos a las listas los totales de las operaciones
    UiList.append(TotalUi(NeuronList,i))
    UiN1List.append(n1.Ui(i))
    UiN2List.append(n2.Ui(i))

    '''
    print("Actual Time: "+str(i))
    print("Neurona 1:")
    print("Arg: "+str(n1.Eargs(i)))
    print("Y: "+str(n1.Ye(i)))
    print("Ui1: "+str(n1.Ui(i)))
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

plt.show()
