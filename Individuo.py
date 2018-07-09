import random


class individuo:
    def __init__(self, **kwargs):
        self.WeightInf=kwargs["WeightInf"]
        self.WeightSup=kwargs["WeightSup"]
        self.DelayInf=kwargs["DelayInf"]
        self.DelaySup=kwargs["DelaySup"]
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

    def __add__(self, otro):
        val={"Weight":[],"Delay":[]}

        #Si es instancia de Individuo
        if isinstance(otro, individuo):
            #Regreso toroidal para Weight
            for i in range(len(self.Elemento["Weight"])):
                r = self.Elemento["Weight"][i] + otro.Elemento["Weight"][i]
                while(r<self.WeightInf):
                    r=r+self.WeightSup-self.WeightInf
                while(r>self.WeightSup):
                    r=r-self.WeightSup+self.WeightInf
                val["Weight"].append(r)

            # Regreso toroidal para Delay
            for i in range(len(self.Elemento["Delay"])):
                r = self.Elemento["Delay"][i] + otro.Elemento["Delay"][i]
                while (r < self.DelayInf):
                    r = r + self.DelaySup - self.DelayInf
                while (r > self.DelaySup):
                    r = r - self.DelaySup + self.DelayInf
                val["Delay"].append(r)

        #Si es instancia de Flotante o Entero
        elif isinstance(otro, float) or isinstance(otro, int):
            # Regreso toroidal para Weight
            for i in range(len(self.Elemento["Weight"])):
                r=self.Elemento["Weight"][i] + otro
                while (r < self.WeightInf):
                    r = r + self.WeightSup - self.WeightInf
                while (r > self.WeightSup):
                    r = r - self.WeightSup + self.WeightInf
                val["Weight"].append(r)

            #Regreso toroidal para Delay
            for i in range(len(self.Elemento["Delay"])):
                r=self.Elemento["Delay"][i] + otro
                while (r < self.DelayInf):
                    r = r + self.DelaySup - self.DelayInf
                while (r > self.DelaySup):
                    r = r - self.DelaySup + self.DelayInf
                val["Delay"].append(r)

        return individuo(Elemento=val)

    def __sub__(self, otro):
        val = {"Weight": [], "Delay": []}

        # Si es instancia de Individuo
        if isinstance(otro, individuo):
            # Regreso toroidal para Weight
            for i in range(len(self.Elemento["Weight"])):
                r = self.Elemento["Weight"][i] - otro.Elemento["Weight"][i]
                while (r < self.WeightInf):
                    r = r + self.WeightSup - self.WeightInf
                while (r > self.WeightSup):
                    r = r - self.WeightSup + self.WeightInf
                val["Weight"].append(r)

            # Regreso toroidal para Delay
            for i in range(len(self.Elemento["Delay"])):
                r = self.Elemento["Delay"][i] - otro.Elemento["Delay"][i]
                while (r < self.DelayInf):
                    r = r + self.DelaySup - self.DelayInf
                while (r > self.DelaySup):
                    r = r - self.DelaySup + self.DelayInf
                val["Delay"].append(r)

        # Si es instancia de Flotante o Entero
        elif isinstance(otro, float) or isinstance(otro, int):
            # Regreso toroidal para Weight
            for i in range(len(self.Elemento["Weight"])):
                r = self.Elemento["Weight"][i] - otro
                while (r < self.WeightInf):
                    r = r + self.WeightSup - self.WeightInf
                while (r > self.WeightSup):
                    r = r - self.WeightSup + self.WeightInf
                val["Weight"].append(r)

            # Regreso toroidal para Delay
            for i in range(len(self.Elemento["Delay"])):
                r = self.Elemento["Delay"][i] - otro
                while (r < self.DelayInf):
                    r = r + self.DelaySup - self.DelayInf
                while (r > self.DelaySup):
                    r = r - self.DelaySup + self.DelayInf
                val["Delay"].append(r)

        return individuo(Elemento=val)

    def __mul__(self, otro):
        val = {"Weight": [], "Delay": []}

        # Si es instancia de Individuo
        if isinstance(otro, individuo):
            # Regreso toroidal para Weight
            for i in range(len(self.Elemento["Weight"])):
                r = self.Elemento["Weight"][i] * otro.Elemento["Weight"][i]
                while (r < self.WeightInf):
                    r = r + self.WeightSup - self.WeightInf
                while (r > self.WeightSup):
                    r = r - self.WeightSup + self.WeightInf
                val["Weight"].append(r)

            # Regreso toroidal para Delay
            for i in range(len(self.Elemento["Delay"])):
                r = self.Elemento["Delay"][i] * otro.Elemento["Delay"][i]
                while (r < self.DelayInf):
                    r = r + self.DelaySup - self.DelayInf
                while (r > self.DelaySup):
                    r = r - self.DelaySup + self.DelayInf
                val["Delay"].append(r)

        # Si es instancia de Flotante o Entero
        elif isinstance(otro, float) or isinstance(otro, int):
            # Regreso toroidal para Weight
            for i in range(len(self.Elemento["Weight"])):
                r = self.Elemento["Weight"][i] * otro
                while (r < self.WeightInf):
                    r = r + self.WeightSup - self.WeightInf
                while (r > self.WeightSup):
                    r = r - self.WeightSup + self.WeightInf
                val["Weight"].append(r)

            # Regreso toroidal para Delay
            for i in range(len(self.Elemento["Delay"])):
                r = self.Elemento["Delay"][i] * otro
                while (r < self.DelayInf):
                    r = r + self.DelaySup - self.DelayInf
                while (r > self.DelaySup):
                    r = r - self.DelaySup + self.DelayInf
                val["Delay"].append(r)

        return individuo(Elemento=val)

    def __lt__(self, otro):
        return self.Fitness < otro.Fitness

    def __str__(self):
        return "Fitness: {} Individuo: {}".format(self.Fitness, self.Elemento)
