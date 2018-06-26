class neurona:
    def __init__(self,FiringTime,Weigh,Delay,Tau):
        self.FiringTime=FiringTime[:]
        self.Weigh=Weigh
        self.Delay=Delay
        self.Tau=Tau        

    def Eargs(self,ActualTime,i):
        arg=ActualTime-self.FiringTime[i]-self.Delay
        return arg if arg>0 else 0

    def Ye(self,ActualTime,i):
        import numpy as np
        op=self.Eargs(ActualTime,i)/self.Tau
        ex=np.exp(1-op)
        op=op*ex
        op=op*self.Weigh
        return op