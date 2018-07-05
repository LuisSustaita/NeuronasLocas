import random
import math
class individuo:
    def __init__(self, **kwargs):
        self.Fitness=1111
        if "TargetTime" in kwargs:
            self.TargetTime=kwargs["TargetTime"]
            self.ActualTime=kwargs["ActualTime"]
        else:
            self.TargetTime=111
            self.ActualTime=111

        if "Dimension" in kwargs:
            self.Dimension=kwargs["Dimension"]
        else:
            self.Dimension=2

        if "Elemento" in kwargs:
            self.Elemento = kwargs["Elemento"][:]
        else:
            self.Elemento = [random.uniform(kwargs["WeightInf"], kwargs["WeightSup"]) for x in range(self.Dimension/2)]
            self.Elemento.append(random.uniform(kwargs["DelayInf"], kwargs["DelaySup"]) for x in range(self.Dimension/2))

    def __add__(self, otro):
        val=[]
        if isinstance(otro, individuo):
            for i in range(2):
                val.append(self.Elemento[i]+otro.Elemento[i])
        elif isinstance(otro, float) or isinstance(otro, int):
            for i in range(2):
                val.append(self.Elemento[i]+otro)
        return individuo(Elemento=val)

    def __sub__(self, otro):
        val=[]
        if isinstance(otro, individuo):
            for i in range(2):
                val.append(self.Elemento[i]-otro.Elemento[i])
        elif isinstance(otro, float) or isinstance(otro, int):
            for i in range(2):
                val.append(self.Elemento[i]-otro)
        return individuo(Elemento=val)

    def __mul__(self, otro):
        val=[]
        if isinstance(otro, individuo):
            for i in range(2):
                val.append(self.Elemento[i]*otro.Elemento[i])
        elif isinstance(otro, float) or isinstance(otro, int):
            for i in range(2):
                val.append(self.Elemento[i]*otro)
        return individuo(Elemento=val)


    def __lt__(self, otro):
        return self.Fitness<otro.Fitness

    def __str__(self):
        return "Fitness: {} Individuo: {}".format(self.Fitness, self.Elemento)
