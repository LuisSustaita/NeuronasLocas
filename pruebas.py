#http://webs.ucm.es/info/aocg/python/modulos_cientificos/matplotlib/index.html
#Librerias para graficar
import matplotlib.pyplot as plt

# Clase Neurona
from Neurona import neurona
# Evolucion Diferencial
from evolucion import Evolucion

WeightInf=-100
WeightSup=100
DelayInf=0.1
DelaySup=16
C1TargetTime=20
C2TargetTime=10

ArgsED={"Poblacion":30,"Iteraciones":500,"CapaEntrada":2,"CapaOculta":5,"CapaSalida":1,
        "WeightInf":WeightInf,"WeightSup":WeightSup,"DelayInf":DelayInf,"DelaySup":DelaySup}

# Limite de disparo
Threshold = 1

# Iniciamos 2 neuronas
n1 = neurona(FiringTime=[0, 0], Weigh=0.75, Delay=1, Tau=3)
n2 = neurona(FiringTime=[0, 6], Weigh=0.25, Delay=1.75, Tau=3)
n3 = neurona(FiringTime=[6, 0], Weigh=0.75, Delay=1, Tau=3)
n4 = neurona(FiringTime=[6, 6], Weigh=0.25, Delay=1.75, Tau=3)

# Las agregamos a una lista de neuronas
NeuronList = [n1, n2, n3, n4]

# Definimos una funcion para obtener Ui(t)
def SumaY(listaYs, ActualTime):
    result = 0
    for y in listaYs:
        result += y
    return result

def Ui(SumaYs,Threshold):
    return SumaYs if SumaYs<=Threshold else 0

#Lista para picos
listaYs1 = []
listaYs2 = []

#Listas para graficar
Ulist=[]
sumaYsList=[]

# Iniciamos el 'tiempo'
for i in range(24):
    print("Actual Time: " + str(i))
    print("Neurona 1")
    listaYs1 = []
    for j in range(len(n1.FiringTime)):
        y1 = n1.Ye(i,j)
        #print("Arg "+str(n1.FiringTime[j])+": "+str(n1.Eargs(i,j))+" | Y: "+str(y1))
        listaYs1.append(y1)
    print("Suma Y: "+str(SumaY(listaYs1,i)))

    print("Neurona 2")
    listaYs2 = []
    for j in range(len(n2.FiringTime)):
        y2 = n2.Ye(i,j)
        #print("Arg "+str(n2.FiringTime[j])+": "+str(n2.Eargs(i,j))+" | Y: "+str(y2))
        listaYs2.append(y2)
    print("Suma Y: "+str(SumaY(listaYs2,i)))

    sumays = SumaY(listaYs1, i) + SumaY(listaYs2, i)
    print("Suma Ys: "+str(sumays))
    sumaYsList.append(sumays)
    print("U: "+str(Ui(sumays,Threshold)))
    Ulist.append(Ui(sumays,Threshold))

# Graficamos
plt.figure()
plt.xlabel('Tiempo', fontsize = 20)
plt.ylabel('Potencial de la membrana', fontsize=20)
plt.plot(0,Threshold,'k--',label='Threshold')
plt.plot(Ulist,label='U')
plt.plot(sumaYsList,label='Suma Ys')
plt.title('Spikes')
plt.show()
