class neurona:
    def __init__(self,FiringTime,Weigh,Delay,Tau):
        self.FiringTime=FiringTime[:]
        self.Weigh=Weigh
        self.Delay=Delay
        self.Tau=Tau        

    def Eargs(self,ActualTime,i):
        Yj=ActualTime-self.FiringTime[i]-self.Delay
        return Yj if Yj>0 else 0

    def Ye(self,ActualTime,i):
        import numpy as np
        op=self.Eargs(ActualTime,i)/self.Tau
        return op*np.exp(1-op)*self.Weigh

    def SumaY(listaY):
        sy=0
        for y in listaY:
            sy+=y
        return sy

    def Ui(self,ActualTime,i):
        return self.Ye(ActualTime,i)*self.Weigh
