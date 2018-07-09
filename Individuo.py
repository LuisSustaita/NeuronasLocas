import random


class individuo:
    def __init__(self, **kwargs):
        if "Fitness" in kwargs:
            self.Fitness = kwargs["Fitness"]
        else:
            self.Fitness = 1111

        if "Elemento" in kwargs:
            self.Elemento = kwargs["Elemento"]
        else:
            self.Elemento={"Weight": [random.uniform(kwargs["WeightInf"], kwargs["WeightSup"])
                                     for x in range(kwargs["Dimension"]/2)],
                          "Delay": [random.uniform(kwargs["DelayInf"], kwargs["DelaySup"])
                                   for x in range(kwargs["Dimension"]/2)]}

    #
    #Agregar regreso toroidal
    #
    def __add__(self, otro):
        val={}
        if isinstance(otro, individuo):
            for key in individuo.Elemento:
                for i in range(individuo.Elemento[key]):
                    val.__setitem__(key, self.Elemento[key:i]+otro.Elemento[key:i])
        elif isinstance(otro, float) or isinstance(otro, int):
            for key in individuo.Elemento:
                for i in range(individuo.Elemento[key]):
                    val.__setitem__(key, self.Elemento[key:i]+otro)
        return individuo(Elemento=val)

    #
    # Agregar regreso toroidal
    #
    def __sub__(self, otro):
        val={}
        if isinstance(otro, individuo):
            for key in individuo.Elemento:
                for i in range(individuo.Elemento[key]):
                    val.__setitem__(key, self.Elemento[key:i]-otro.Elemento[key:i])
        elif isinstance(otro, float) or isinstance(otro, int):
            for key in individuo.Elemento:
                for i in range(individuo.Elemento[key]):
                    val.__setitem__(key, self.Elemento[key:i]-otro)
        return individuo(Elemento=val)

    #
    # Agregar regreso toroidal
    #
    def __mul__(self, otro):
        val={}
        if isinstance(otro, individuo):
            for key in individuo.Elemento:
                for i in range(individuo.Elemento[key]):
                    val.__setitem__(key, self.Elemento[key:i]*otro.Elemento[key:i])
        elif isinstance(otro, float) or isinstance(otro, int):
            for key in individuo.Elemento:
                for i in range(individuo.Elemento[key]):
                    val.__setitem__(key, self.Elemento[key:i]*otro)
        return individuo(Elemento=val)

    def __lt__(self, otro):
        return self.Fitness < otro.Fitness

    def __str__(self):
        return "Fitness: {} Individuo: {}".format(self.Fitness, self.Elemento)
