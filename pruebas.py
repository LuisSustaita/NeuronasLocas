
from Neurona import neurona

n1=neurona(2,0.5,1,3)
n2=neurona(5,0.5,1.5,5)

NeuronList=[n1,n2]

def TotalUi(NeuronList,ActualTime):
    result=0
    for neuron in NeuronList:
        result+=neuron.Ui(ActualTime)
    return result

for i in range(21):
    print("Ui: "+str(TotalUi(NeuronList,i)))
    
    '''
    print("Actual Time: "+str(i))
    print("Neurona 1:")
    print("Arg: "+str(n1.Eargs(i)))
    print("Y: "+str(n1.Ye(i)))
    print("Ui1: "+str(n1.Ui(i)))
    print("Neurona 2:")
    print("Arg: "+str(n2.Eargs(i)))
    print("Y: "+str(n2.Ye(i)))
    print("Ui2: "+str(n2.Ui(i)))
    '''
