import numpy as np


class neurona:
    def __init__(self, Threshold, Tau):
        #Spike
        self.FiringTime = None
        self.Tau = Tau
        #Umbral-Limite
        self.Threshold = Threshold
        #Matriz de pesos - synapses
        self.WeightAndDelay = {"Weight": [], "Delay": []}

    #Estado de la neurona
    def Ye(self, ActualTime, FiringTime, Delay):
        FiringTime =-1 if FiringTime is None else ActualTime-FiringTime-Delay
        if FiringTime > 0:
            return (FiringTime/self.Tau)*np.exp(1-FiringTime/self.Tau)
        return 0

    #Potencial de la membrana
    def Simular(self, ActualTime, FiringTimes):
        x = 0
        if self.FiringTime is None:
            for i in range(len(self.WeightAndDelay["Delay"])):
                x += self.WeightAndDelay["Delay"][i] * self.Ye(ActualTime, FiringTimes[i], self.WeightAndDelay["Weight"][i])
            if x >= self.Threshold:
                self.FiringTime = ActualTime

    #Resetear neurona
    def ResetNeuron(self):
        self.FiringTime = None
