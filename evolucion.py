from Individuo import individuo
from RedNeuronalPulsante import Pulsante
import random

class Evolucion:
    def __init__(self,**kwargs):
        self.Poblacion = kwargs["Poblacion"]
        self.F = 0.9
        self.Cr = 0.8
        self.Llamadas = kwargs["Iteraciones"]
        self.WeightInf = kwargs["WeightInf"]
        self.WeightSup = kwargs["WeightSup"]
        self.DelayInf = kwargs["DelayInf"]
        self.DelaySup = kwargs["DelaySup"]
        self.Patrones = kwargs["Patrones"]
        self.TiempoFin = kwargs["TiempoFin"]
        self.RedPulsante=Pulsante(kwargs["CapaOculta"],kwargs["Threshold"],
            kwargs["Tau"],kwargs["TiempoInicio"],self.TiempoFin)
        self.PoblacionList = []

        # Llenar arreglo de poblacion
        for i in range(self.Poblacion):
            PoblacionList.append(individuo(TargetTime=self.TargetTime,
                                           WeightInf=self.WeightInf, WeightSup=self.WeightSup,
                                           DelayInf=self.DelayInf, DelaySup=self.DelaySup,
                                           Dimension=self.Dimension))

    def init(self,TiempoActual):

        #Llamadas a funcion
        for i in range(self.Llamadas):

            #Paso 1: Mutacion
            #Nueva poblacion de individuos
            NewPoblacionList=[]
            for j in range(self.Poblacion):
                #Se seleccionan 3 individuos aleatoriamente
                R1=PoblacionList[random.randint(0, len(PoblacionList)-1)]
                R2=PoblacionList[random.randint(0, len(PoblacionList)-1)]
                R3=PoblacionList[random.randint(0, len(PoblacionList)-1)]

                #Se aplican operaciones al individuo y se agrega a la poblacion
                NewPoblacionList.append(individuo(
                    TargetTime=self.TargetTime,
                    Elemento=(R1.__add__(R2.__sub__(R3).__mul__(self.F))).Elemento))


            #Paso 2: Cruza
            for j in range(self.Poblacion):
                VectorTemp=[]
                for k in range(2):
                    #Para cada componente del arreglo
                    if random.random()<=Cr:
                        #Si el aleatorio es menor que Cr tomamos el componente del arreglo de la nueva poblacion
                        VectorTemp.append(NewPoblacionList[j].Elemento[k])
                    else:
                        #Si no es menor tomamos el componente del arreglo de la poblacion original
                        VectorTemp.append(PoblacionList[j].Elemento[k])

                individuoCruzado = individuo(TargetTime=self.TargetTime,
                                             Elemento=VectorTemp)

                #Paso 3: Reemplazo
                if individuoCruzado.__lt__(PoblacionList[j]):
                    # Si el cruzado es menor (mejor) que el original se reemplaza
                    PoblacionList[j]=individuoCruzado
                else:
                    # Si no es mejor se queda el original
                    pass
            print(PoblacionList[0].__str__())