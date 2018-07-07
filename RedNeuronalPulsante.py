from Neurona import neurona

class Pulsante:
    def __init__(self,CapaOculta,Threshold,Tau,TiempoInicio,TiempoFin):
        self.TiempoInicio=TiempoInicio
        self.TiempoFin=TiempoFin
        self.NeuronasOcultas=[neurona(Threshold,Tau) for i in range(CapaOculta)]
        self.NeuronaSalida=neurona(Threshold,Tau)

    def ResetPulsante(self):
        for s in self.NeuronasOcultas:
            s.ResetNeuron()
        self.NeuronaSalida.ResetNeuron()

    def setWeightAndDelay(self,WeightAndDelay):
        for i in range(len(self.NeuronasOcultas)):
            self.NeuronasOcultas[i].WeightAndDelay.__setitem__(
                "Weight",WeightAndDelay[i]["Weight"])
            self.NeuronasOcultas[i].WeightAndDelay.__setitem__(
                "Delay", WeightAndDelay[i]["Delay"])
        self.NeuronaSalida.WeightAndDelay.__setitem__(
            "Weight", WeightAndDelay[len(self.NeuronasOcultas)]["Weight"])
        self.NeuronaSalida.WeightAndDelay.__setitem__(
            "Delay", WeightAndDelay[len(self.NeuronasOcultas)]["Delay"])

    def Simular(self,FiringTimes):
        SalidasOcultas=[]
        for t in range(self.TiempoInicio,self.TiempoFin,1):
            for i in range(len(self.NeuronasOcultas)):
                self.NeuronasOcultas[i].Simular(t,FiringTimes)
                SalidasOcultas.append(self.NeuronasOcultas[i].FiringTime)
            self.NeuronaSalida.Simular(t,SalidasOcultas)
        
        return self.NeuronaSalida.FiringTime