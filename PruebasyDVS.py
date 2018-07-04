#Librerias para graficar
import matplotlib.pyplot as plt
# Clase Neurona
from Neurona import neurona

#Listas
FiringList=[]
NeuronList=[]
#Lista para picos
listaYs1 = []
listaYs2 = []
#Listas para graficar
Ulist=[]
sumaYsList=[]

# Limite de disparo
Threshold = 1

#Abrimos el archivo con los datos del DVS
data = open('blinking.data')

#Leemos el archivo
for line in self.data.readlines():
    #Separamos los datos en diferentes variables
    x, y, sign, t = line.strip().split()
    #Convertimos las variables en enteros y flotante
    y = int(y)
    x = int(x)
    sign = int(sign)
    t = float(t)

    # Iniciamos un neurona por cada pixel activo
    neuron = neurona(FiringTime=FiringList.append(t), Weigh=0.75, Delay=1, Tau=3)
    # Agregamos la neurona a una lista
    NeuronList.append(neuron)

    print("Actual Time: " + str(t))
    print("Neurona {},{}".format(x,y))
    listaYs1 = []
    for j in range(len(n1.FiringTime)):

    time.sleep(1)


# Definimos una funcion para obtener Ui(t)
def SumaY(listaYs, ActualTime):
    result = 0
    for y in listaYs:
        result += y
    return result

def Ui(SumaYs,Threshold):
    return SumaYs if SumaYs<=Threshold else 0


############################################
# Iniciamos el 'tiempo'
for i in range(21):
    #print("Actual Time: " + str(i))
    #print("Neurona 1")
    #listaYs1 = []
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
