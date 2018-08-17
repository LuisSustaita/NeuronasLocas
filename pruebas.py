#http://webs.ucm.es/info/aocg/python/modulos_cientificos/matplotlib/index.html
#Librerias para graficar
import matplotlib.pyplot as plt

# Clase Neurona
from Neurona import neurona
# Evolucion Diferencial
from evolucion import Evolucion
# Red neuronal
from RedNeuronalPulsante import Pulsante

patron11 = [0, 0]
patron12 = [6, 6]
c1 = [patron11, patron12]
patron21 = [0, 6]
patron22 = [6, 0]
c2 = [patron21, patron22]

Patrones = {20: c1, 10: c2}

CapaEntrada = 2
CapaOculta = 10
CapaSalida = 1

WeightInf = -100
WeightSup = 100
DelayInf = 0.1
DelaySup = 16

Dimension = 2*(CapaOculta*CapaEntrada+CapaSalida*CapaOculta)
Poblacion = 30
Iteraciones = 200
TiempoInicio = 0
TiempoFin = 24
F = 0.9
Cr = 0.8
Threshold = 1
Tau = 7

de = Evolucion(Poblacion=Poblacion, Dimension=Dimension,
               F=F, Cr=Cr,
               Iteraciones=Iteraciones,
               WeightInf=WeightInf, WeightSup=WeightSup,
               DelayInf=DelayInf, DelaySup=DelaySup,
               Patrones=Patrones,
               CapaEntrada=CapaEntrada, CapaOculta=CapaOculta,
               Threshold=Threshold, Tau=Tau,
               TiempoInicio=TiempoInicio, TiempoFin=TiempoFin)

evolucion = de.evolucionar()
print("*"*20)
print("Solucion: {}".format(evolucion.Elemento))
print("Fitness: {}".format(evolucion.Fitness))

snn = de.getSNN()

for key in Patrones:
    spikes = Patrones[key]
    for p in spikes:
        FiringTime = snn.Simular(p)
        print("Patron: {} Clase: {} Prediccion: {}".format(p, key, FiringTime))
    snn.ResetPulsante()








