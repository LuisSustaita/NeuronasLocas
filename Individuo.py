import random


class individuo:
    def __init__(self, **kwargs):
        self.WeightInf = kwargs["WeightInf"]
        self.WeightSup = kwargs["WeightSup"]
        self.DelayInf = kwargs["DelayInf"]
        self.DelaySup = kwargs["DelaySup"]

        self.Fitness = 111111

        if "Elemento" in kwargs:
            self.Elemento = kwargs["Elemento"]
        else:
            #self.Elemento={"Weight": [random.uniform(kwargs["WeightInf"], kwargs["WeightSup"])
            #                         for x in range(int(kwargs["Dimension"]/2))],
            #              "Delay": [random.uniform(kwargs["DelayInf"], kwargs["DelaySup"])
            #                       for x in range(int(kwargs["Dimension"]/2))]}

            self.Elemento = {"Weight": [2
                                        for x in range(int(kwargs["Dimension"] / 2))],
                             "Delay": [2
                                       for x in range(int(kwargs["Dimension"] / 2))]}

    def RegresoToroidal(self, LimiteInferior, LimiteSuperior, Valor):
        import math
        if Valor < LimiteInferior:
            li=(LimiteSuperior - LimiteInferior)
            if li is 0:
                print("")
            Valor = LimiteSuperior - (math.fabs(Valor - LimiteInferior) % (LimiteSuperior - LimiteInferior))
        else:
            Valor = LimiteInferior + (math.fabs(Valor + LimiteInferior) % (LimiteSuperior - LimiteInferior))
        return Valor

    def __add__(self, otro):
        val = {"Weight": [], "Delay": []}

        # Si es instancia de Individuo
        if isinstance(otro, individuo):
            for i in range(len(self.Elemento["Weight"])):
                r = self.Elemento["Weight"][i] + otro.Elemento["Weight"][i]

                # Regreso toroidal para Weight
                r = self.RegresoToroidal(self.WeightInf, self.WeightSup, r)

                val["Weight"].append(r)

            for i in range(len(self.Elemento["Delay"])):
                r = self.Elemento["Delay"][i] + otro.Elemento["Delay"][i]

                # Regreso toroidal para Delay
                r = self.RegresoToroidal(self.DelayInf, self.DelaySup, r)

                val["Delay"].append(r)

        # Si es instancia de Flotante o Entero
        elif isinstance(otro, float) or isinstance(otro, int):
            for i in range(len(self.Elemento["Weight"])):
                r = self.Elemento["Weight"][i] + otro

                # Regreso toroidal para Weight
                r = self.RegresoToroidal(self.WeightInf, self.WeightSup, r)

                val["Weight"].append(r)

            for i in range(len(self.Elemento["Delay"])):
                r = self.Elemento["Delay"][i] + otro

                # Regreso toroidal para Delay
                r = self.RegresoToroidal(self.DelayInf, self.DelaySup, r)

                val["Delay"].append(r)

        return individuo(Elemento=val,
                         WeightInf=self.WeightInf, WeightSup=self.WeightSup,
                         DelayInf=self.DelayInf, DelaySup=self.DelaySup)

    def __sub__(self, otro):
        val = {"Weight": [], "Delay": []}

        # Si es instancia de Individuo
        if isinstance(otro, individuo):
            for i in range(len(self.Elemento["Weight"])):
                r = self.Elemento["Weight"][i] - otro.Elemento["Weight"][i]

                # Regreso toroidal para Weight
                r = self.RegresoToroidal(self.WeightInf,self.WeightSup,r)

                val["Weight"].append(r)

            for i in range(len(self.Elemento["Delay"])):
                r = self.Elemento["Delay"][i] - otro.Elemento["Delay"][i]

                # Regreso toroidal para Delay
                r = self.RegresoToroidal(self.DelayInf, self.DelaySup, r)

                val["Delay"].append(r)

        # Si es instancia de Flotante o Entero
        elif isinstance(otro, float) or isinstance(otro, int):
            for i in range(len(self.Elemento["Weight"])):
                r = self.Elemento["Weight"][i] - otro

                # Regreso toroidal para Weight
                r = self.RegresoToroidal(self.WeightInf, self.WeightSup, r)

                val["Weight"].append(r)

            for i in range(len(self.Elemento["Delay"])):
                r = self.Elemento["Delay"][i] - otro

                # Regreso toroidal para Delay
                r = self.RegresoToroidal(self.DelayInf, self.DelaySup, r)

                val["Delay"].append(r)
        return individuo(Elemento=val,
                         WeightInf=self.WeightInf,WeightSup=self.WeightSup,
                         DelayInf=self.DelayInf,DelaySup=self.DelaySup)

    def __mul__(self, otro):
        val = {"Weight": [], "Delay": []}

        # Si es instancia de Individuo
        if isinstance(otro, individuo):
            for i in range(len(self.Elemento["Weight"])):
                r = self.Elemento["Weight"][i] * otro.Elemento["Weight"][i]

                # Regreso toroidal para Weight
                r = self.RegresoToroidal(self.WeightInf, self.WeightSup, r)

                val["Weight"].append(r)

            for i in range(len(self.Elemento["Delay"])):
                r = self.Elemento["Delay"][i] * otro.Elemento["Delay"][i]

                # Regreso toroidal para Delay
                r = self.RegresoToroidal(self.DelayInf, self.DelaySup, r)

                val["Delay"].append(r)

        # Si es instancia de Flotante o Entero
        elif isinstance(otro, float) or isinstance(otro, int):
            for i in range(len(self.Elemento["Weight"])):
                r = self.Elemento["Weight"][i] * otro

                # Regreso toroidal para Weight
                r = self.RegresoToroidal(self.WeightInf, self.WeightSup, r)

                val["Weight"].append(r)

            # Regreso toroidal para Delay
            for i in range(len(self.Elemento["Delay"])):
                r = self.Elemento["Delay"][i] * otro

                # Regreso toroidal para Delay
                r = self.RegresoToroidal(self.DelayInf, self.DelaySup, r)

                val["Delay"].append(r)

        return individuo(Elemento=val,
                         WeightInf=self.WeightInf, WeightSup=self.WeightSup,
                         DelayInf=self.DelayInf, DelaySup=self.DelaySup)

    def __lt__(self, otro):
        return self.Fitness < otro.Fitness

    def __str__(self):
        return "Fitness: {} Individuo: {}".format(self.Fitness, self.Elemento)
