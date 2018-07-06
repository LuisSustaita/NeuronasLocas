# Evolucion Diferencial
from evolucion import Evolucion

WeightInf=-100
WeightSup=100
DelayInf=0.1
DelaySup=16
C1TargetTime=20
C2TargetTime=10

Poblacion=30
Iteraciones=500
CapaEntrada=2
CapaOculta=5
CapaSalida=1

evo=Evolucion(WeightInf=WeightInf,WeightSup=WeightSup,DelaySup=DelaySup,DelayInf=DelayInf,TargetTime=C1TargetTime,
              Poblacion=Poblacion,Iteraciones=Iteraciones,CapaEntrada=CapaEntrada,CapaOculta=CapaOculta)

for i in range(24):
    evo.init(i)


