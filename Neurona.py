import math

class neurona:
    def __init__(self, Threshold, Tau):
        #Spike
        self.FiringTime = None
        #Tau
        self.Tau = Tau
        #Umbral-Limite
        self.Threshold = Threshold
        #Matriz de pesos - synapses
        self.WeightAndDelay = {"Weight": [], "Delay": []}

    #Estado de la neurona
    def Ye(self, ActualTime, FiringTime, Delay):
        tinput=-1 if FiringTime is None else ActualTime-FiringTime-Delay
        if tinput > 0:
            r=(tinput / self.Tau) * math.exp(1 - tinput / self.Tau)
            return r
        return 0

    #Potencial de la membrana
    def Simular(self, ActualTime, FiringTimes):
        x = 0
        if self.FiringTime is None:
            for i in range(len(self.WeightAndDelay)):
                y=self.Ye(ActualTime, FiringTimes[i], self.WeightAndDelay["Weight"][i])
                x += self.WeightAndDelay["Delay"][i] * y
            if x >= self.Threshold:
                self.FiringTime = ActualTime

    #Resetear neurona
    def ResetNeuron(self):
        self.FiringTime = None
