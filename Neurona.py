class neurona:
    def __init__(self,FiringTime=[],Weigh,Delay,Tau):
        self.FiringTime=FiringTime[:]
        self.Weigh=Weigh
        self.Delay=Delay
        self.Tau=Tau

    def Eargs(self,ActualTime):
        for FiTi in FiringTime:
            Yj+=ActualTime-self.FiTi-self.Delay
        return Yj if Yj>0 else 0

    def Ye(self,ActualTime):
        import numpy as np
        op=self.Eargs(ActualTime)/self.Tau
        return op*np.exp(1-op)

    def Ui(self,ActualTime):
        return self.Ye(ActualTime)*self.Weigh
