from Individuo import individuo
from RedNeuronalPulsante import Pulsante
import random
import math


class Evolucion:
    def __init__(self, **kwargs):
        self.Poblacion = kwargs["Poblacion"]
        self.Dimension = kwargs["Dimension"]
        self.F = kwargs["F"]
        self.Cr = kwargs["Cr"]
        self.Llamadas = kwargs["Iteraciones"]
        self.WeightInf = kwargs["WeightInf"]
        self.WeightSup = kwargs["WeightSup"]
        self.DelayInf = kwargs["DelayInf"]
        self.DelaySup = kwargs["DelaySup"]
        self.Patrones = kwargs["Patrones"]
        self.TiempoFin = kwargs["TiempoFin"]
        self.Entradas = kwargs["CapaEntrada"]
        self.Ocultas = kwargs["CapaOculta"]

        self.RedPulsante = Pulsante(self.Ocultas, kwargs["Threshold"],
                                    kwargs["Tau"], kwargs["TiempoInicio"], self.TiempoFin)
        self.PoblacionList = []

        # Llenar arreglo de poblacion
        for i in range(self.Poblacion):
            s = individuo(WeightInf=self.WeightInf, WeightSup=self.WeightSup,
                         DelayInf=self.DelayInf, DelaySup=self.DelaySup,
                         Dimension=self.Dimension)

            s.Fitness = self.CalculoFitness(s)
            self.PoblacionList.append(s)


    def evolucionar(self):
        # Llamadas a funcion
        for i in range(self.Llamadas):
            # Paso 1: Mutacion
            # Lista tabu para evitar tener aleatorios iguales
            indexes=[]
            for j in range(self.Poblacion):
                #Se agrega la posicion a la lista
                indexes.append(j)
                while len(indexes)<4:
                    # Se seleccionan 3 individuos aleatoriamente
                    index = random.randint(0, len(self.PoblacionList) - 1)
                    while indexes.__contains__(index):
                        index = random.randint(0, len(self.PoblacionList) - 1)
                    indexes.append(index)
                indexes.pop(0)

                R1 = self.PoblacionList[indexes[0]]
                R2 = self.PoblacionList[indexes[1]]
                R3 = self.PoblacionList[indexes[2]]

                # Se aplican operaciones al individuo y se agrega a la poblacion
                mutado = individuo(Elemento=(R2.__sub__(R3)).Elemento,
                                   WeightSup=self.WeightSup, WeightInf=self.WeightInf,
                                   DelaySup=self.DelaySup, DelayInf=self.DelayInf)
                mutado = mutado.__mul__(self.F)
                mutado = R1.__add__(mutado)

                #Paso 2: Cruza
                Cruzado = {"Weight": [], "Delay": []}
                for k in mutado.Elemento:
                    # Para cada componente del arreglo
                    if random.random() <= self.Cr:
                        # Si el aleatorio es menor que Cr tomamos el componente del arreglo de la nueva poblacion
                        Cruzado[k] = mutado.Elemento[k]
                    else:
                        # Si no es menor tomamos el componente del arreglo de la poblacion original
                        Cruzado[k] = self.PoblacionList[j].Elemento[k]

                Cruzado = individuo(Elemento=Cruzado,
                                    WeightSup=self.WeightSup, WeightInf=self.WeightInf,
                                    DelaySup=self.DelaySup, DelayInf=self.DelayInf)

                Cruzado.Fitness = self.CalculoFitness(Cruzado)
                # Paso 3: Reemplazo
                if Cruzado.__lt__(self.PoblacionList[j]):
                    # Si el cruzado es menor (mejor) que el original se reemplaza
                    self.PoblacionList[j] = Cruzado
                else:
                    # Si no es mejor se queda el original
                    pass

            #print(self.PoblacionList[0])

        #Ordenar PoblacionList
        self.PoblacionList = sorted(self.PoblacionList, key=lambda obj: obj.Fitness)

        return self.PoblacionList[0]

    def CalculoFitness(self, individuo):
        fitness = 0
        synapses = []

        for i in range(self.Ocultas):
            s = {"Weight": [], "Delay": []}
            for j in range(self.Entradas):
                s["Weight"].append(individuo.Elemento["Weight"][i+j])
                s["Delay"].append(individuo.Elemento["Delay"][i+j])
            synapses.append(s)

        s = {"Weight": [], "Delay": []}
        inicio = len(individuo.Elemento["Delay"])+len(individuo.Elemento["Weight"])-(self.Ocultas*2)
        fin = len(individuo.Elemento["Delay"])+len(individuo.Elemento["Weight"])

        for i in range(int(inicio/2), int(fin/2)):
            s["Weight"].append(individuo.Elemento["Weight"][i])
            s["Delay"].append(individuo.Elemento["Delay"][i])

        synapses.append(s)

        self.RedPulsante.setWeightAndDelay(synapses)
        FiringTime = None
        for key in self.Patrones:
            spikes = self.Patrones[key]
            for p in spikes:
                FiringTime = self.RedPulsante.Simular(p)
                fitness += self.TiempoFin ** 2 if FiringTime is None else (key - FiringTime) ** 2
                self.RedPulsante.ResetPulsante()

        return fitness

    def getSNN(self):
        # Ordenar PoblacionList
        self.PoblacionList = sorted(self.PoblacionList, key=lambda obj: obj.Fitness)

        x = self.PoblacionList[0].Elemento
        synapses = []

        for i in range(self.Ocultas):
            s = {"Weight": [], "Delay": []}

            for j in range(self.Entradas):
                pos=(i * self.Entradas) + j
                s["Weight"].append(x["Weight"][pos])
                s["Delay"].append(x["Delay"][(i * self.Entradas) + j])
            synapses.append(s)

        s = {"Weight": [], "Delay": []}

        inicio = len(x["Delay"]) + len(x["Weight"]) - (self.Ocultas * 2)
        fin = len(x["Delay"]) + len(x["Weight"])

        for i in range(int(inicio / 2), int(fin / 2)):
            s["Weight"].append(x["Weight"][i])
            s["Delay"].append(x["Delay"][i])

        synapses.append(s)
        self.RedPulsante.setWeightAndDelay(synapses)

        return self.RedPulsante





