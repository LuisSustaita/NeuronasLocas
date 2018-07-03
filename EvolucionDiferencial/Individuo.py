import random
import math
class individuo:
    def __init__(self, **kwargs):
        if "Patrones" in kwargs:
            self.Patrones = kwargs["Patrones"][:]
            self.Fitness = self.evaluar(self.Patrones)
        else:
            self.Patrones = None
            self.Fitness=None

        if "Elemento" in kwargs:
            self.Elemento = kwargs["Elemento"][:]
        else:
            self.Elemento = [random.uniform(kwargs["WeightInf"], kwargs["WeightSup"]),
                             random.uniform(kwargs["DelayInf"], kwargs["DelaySup"])]

        if "TargetTime" in kwargs:
            self.TargetTime=kwargs["TargetTime"]
        else:
            self.TargetTime=1

    def evaluar(self,PatternsInTrainingSet):
        result=0
        for pattern in PatternsInTrainingSet:
            result+=math.pow(pattern[3]-self.TargetTime,2)
        return result


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
        return "Fitness: {} Individuo (Weight,Delay): {}".format(self.Fitness, self.Elemento)
