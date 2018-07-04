from Individuo import individuo
import random

#Valores iniciales
poblacion=10
F=0.9
Cr=0.8

WeightInf=-1
WeightSup=1
DelayInf=0.01
DelaySup=2
EquisTargetTime=1.324295
TeTargetTime=6
Patron1=[
    [72, 87, 0, 1.087529],
    [37, 28, 1, 1.090818],
    [54, 86, 1, 1.091283],
    [31, 72, 1, 1.092883],
    [75, 79, 0, 1.112324],
    [75, 79, 0, 1.112444],
    [118, 113, 0, 1.112970],
    [89, 109, 1, 1.115653],
    [96, 110, 1, 1.116520],
    [1, 45, 0, 1.117583],
    [1, 45, 0, 1.117670],
    [44, 68, 0, 1.118594],
    [29, 68, 1, 1.119664],
    [70, 93, 1, 1.119834],
    [70, 93, 1, 1.119922],
    [18, 45, 0, 1.120710]]
Patron2=[
    [47, 85, 1, 1.122432],
    [13, 64, 1, 1.124018],
    [50, 84, 1, 1.124311],
    [52, 87, 1, 1.124956],
    [80, 102, 1, 1.125907],
    [6, 63, 0, 1.126278],
    [6, 63, 0, 1.126397],
    [3, 46, 0, 1.127347],
    [3, 46, 0, 1.127445],
    [3, 46, 0, 1.127529],
    [17, 67, 1, 1.127755],
    [111, 116, 1, 1.128078],
    [98, 104, 0, 1.128588],
    [98, 104, 0, 1.128681],
    [7, 45, 0, 1.129999],
    [47, 13, 1, 1.130110]]
Patron3=[
    [47,13,1,1.130110],
    [93,100,0,1.130875],
    [24,63,1,1.132204],
    [69,81,0,1.132464],
    [31,36,1,1.132827],
    [7,80,1,1.133378],
    [51,86,1,1.133588],
    [31,43,1,1.133908],
    [76,101,1,1.134047],
    [55,6,1,1.134871],
    [41,25,1,1.135067],
    [6,78,1,1.136107],
    [3,56,1,1.136359],
    [4,78,1,1.136527],
    [12,67,1,1.138785],
    [113,112,0,1.140325]]
Patron4=[
    [49,83,1,1.171032],
    [33,61,0,1.174067],
    [0,73,0,1.176453],
    [107,119,1,1.289455],
    [99,114,1,1.290945],
    [117,111,0,1.291785],
    [28,71,1,1.292236],
    [17,63,1,1.293128],
    [103,94,0,1.293495],
    [103,94,0,1.293557],
    [2,57,1,1.295445],
    [50,86,1,1.296491],
    [105,118,1,1.296649],
    [12,72,1,1.298313],
    [61,92,1,1.298642],
    [18,66,1,1.299668]]
Patron5=[
    [85,92,0,1.299864],
    [3,57,1,1.300388],
    [3,57,1,1.300443],
    [47,3,0,1.300973],
    [97,113,1,1.301129],
    [69,96,1,1.301356],
    [8,75,1,1.301816],
    [48,8,1,1.302747],
    [118,113,0,1.303725],
    [42,81,1,1.309141],
    [1,115,0,1.309288],
    [13,70,1,1.309839],
    [71,92,1,1.310247],
    [93,102,0,1.310320],
    [1,45,0,1.310681],
    [12,65,1,1.310755]]
Patron6=[
    [59,85,1,1.311639],
    [31,70,1,1.312000],
    [88,100,0,1.312171],
    [48,10,1,1.312390],
    [51,88,1,1.312608],
    [30,68,1,1.312730],
    [30,68,1,1.312803],
    [36,71,1,1.312926],
    [36,71,1,1.312999],
    [6,85,1,1.313123],
    [20,60,1,1.313246],
    [20,60,1,1.313318],
    [4,56,1,1.313441],
    [49,81,1,1.313724],
    [1,93,1,1.314047],
    [36,73,1,1.314505]]
Patron7=[
    [81,107,1,1.314821],
    [81,107,1,1.314894],
    [57,86,1,1.315019],
    [43,18,1,1.315191],
    [14,68,1,1.315314],
    [110,116,1,1.315486],
    [116,122,1,1.315662],
    [47,10,1,1.315865],
    [55,90,1,1.316086],
    [30,72,1,1.316209],
    [42,74,1,1.316332],
    [100,112,1,1.316599],
    [46,12,1,1.316865],
    [46,12,1,1.316939],
    [102,112,1,1.317350],
    [18,60,1,1.317625]]
Patron8=[
    [49,79,1,1.317756],
    [44,76,1,1.317975],
    [41,77,1,1.318306],
    [52,83,1,1.319409],
    [52,83,1,1.319488],
    [82,102,1,1.319678],
    [10,64,1,1.319863],
    [26,70,1,1.319993],
    [35,74,1,1.320223],
    [10,65,1,1.320501],
    [30,67,1,1.320640],
    [39,73,1,1.320774],
    [82,110,1,1.320954],
    [51,83,1,1.321136],
    [41,75,1,1.321266],
    [41,75,1,1.321343]]
Patron9=[
    [3,85,1,1.321474],
    [3,85,1,1.321597],
    [108,115,1,1.321737],
    [108,115,1,1.321816],
    [69,92,1,1.321947],
    [69,92,1,1.322024],
    [0,83,1,1.322206],
    [0,83,1,1.322283],
    [17,59,1,1.322465],
    [17,59,1,1.322543],
    [55,1,1,1.322875],
    [55,1,1,1.322952],
    [25,62,1,1.323183],
    [2,83,1,1.323415],
    [2,83,1,1.323492],
    [102,111,1,1.323723]]
Patron10=[
    [102,111,1,1.323800],
    [102,111,1,1.323879],
    [79,100,1,1.324009],
    [79,100,1,1.324087],
    [49,82,1,1.324218],
    [49,82,1,1.324295],
    [116,118,1,1.324509],
    [116,118,1,1.324572],
    [6,58,1,1.324709],
    [23,60,1,1.324840],
    [23,60,1,1.324918],
    [0,52,1,1.325131],
    [104,111,1,1.325425],
    [20,61,1,1.325760],
    [76,103,1,1.326092],
    [50,87,1,1.326221]]

#Llenar arreglo de poblacion
PoblacionList=[]
PoblacionList.append(individuo(TargetTime=EquisTargetTime,WeightInf=WeightInf,WeightSup=WeightSup,DelayInf=DelayInf,DelaySup=DelaySup,Patrones=Patron1))
PoblacionList.append(individuo(TargetTime=EquisTargetTime,WeightInf=WeightInf,WeightSup=WeightSup,DelayInf=DelayInf,DelaySup=DelaySup,Patrones=Patron2))
PoblacionList.append(individuo(TargetTime=EquisTargetTime,WeightInf=WeightInf,WeightSup=WeightSup,DelayInf=DelayInf,DelaySup=DelaySup,Patrones=Patron3))
PoblacionList.append(individuo(TargetTime=EquisTargetTime,WeightInf=WeightInf,WeightSup=WeightSup,DelayInf=DelayInf,DelaySup=DelaySup,Patrones=Patron4))
PoblacionList.append(individuo(TargetTime=EquisTargetTime,WeightInf=WeightInf,WeightSup=WeightSup,DelayInf=DelayInf,DelaySup=DelaySup,Patrones=Patron5))
PoblacionList.append(individuo(TargetTime=EquisTargetTime,WeightInf=WeightInf,WeightSup=WeightSup,DelayInf=DelayInf,DelaySup=DelaySup,Patrones=Patron6))
PoblacionList.append(individuo(TargetTime=EquisTargetTime,WeightInf=WeightInf,WeightSup=WeightSup,DelayInf=DelayInf,DelaySup=DelaySup,Patrones=Patron7))
PoblacionList.append(individuo(TargetTime=EquisTargetTime,WeightInf=WeightInf,WeightSup=WeightSup,DelayInf=DelayInf,DelaySup=DelaySup,Patrones=Patron8))
PoblacionList.append(individuo(TargetTime=EquisTargetTime,WeightInf=WeightInf,WeightSup=WeightSup,DelayInf=DelayInf,DelaySup=DelaySup,Patrones=Patron9))
PoblacionList.append(individuo(TargetTime=EquisTargetTime,WeightInf=WeightInf,WeightSup=WeightSup,DelayInf=DelayInf,DelaySup=DelaySup,Patrones=Patron10))

#Iteraciones
for i in range(1000):

    #Paso 1: Mutacion
    #Nueva poblacion de individuos
    NewPoblacionList=[]
    for j in range(poblacion):
        #Se seleccionan 3 individuos aleatoriamente
        R1=PoblacionList[random.randint(0, len(PoblacionList)-1)]
        R2=PoblacionList[random.randint(0, len(PoblacionList)-1)]
        R3=PoblacionList[random.randint(0, len(PoblacionList)-1)]

        #Se aplican operaciones al individuo y se agrega a la poblacion
        #TEMPORAL: SE AGREGA LA LISTA DE PATRONES DE LA POSICION EN LA QUE ESTÁ
        NewPoblacionList.append(individuo(
            TargetTime=EquisTargetTime,
            Elemento=(R1.__add__(R2.__sub__(R3).__mul__(F))).Elemento,
            Patrones=PoblacionList[j].Patrones))


    #Paso 2: Cruza
    for j in range(poblacion):
        VectorTemp=[]
        for k in range(2):
            #Para cada componente del arreglo
            if random.random()<=Cr:
                #Si el aleatorio es menor que Cr tomamos el componente del arreglo de la nueva poblacion
                VectorTemp.append(NewPoblacionList[j].Elemento[k])
            else:
                #Si no es menor tomamos el componente del arreglo de la poblacion original
                VectorTemp.append(PoblacionList[j].Elemento[k])

        # ¿QUE PATRONES LE DOY AL NUEVO INDIVIDUO?
        #TEMPORAL: LE PASAMOS LOS PATRONES DE LA POSICION EN LA QUE ESTÁ
        individuoCruzado = individuo(TargetTime=EquisTargetTime,
                                     Elemento=VectorTemp,
                                     Patrones=PoblacionList[j].Patrones)

        #Paso 3: Reemplazo
        if individuoCruzado.__lt__(PoblacionList[j]):
            # Si el cruzado es menor (mejor) que el original se reemplaza
            PoblacionList[j]=individuoCruzado
        else:
            # Si no es mejor se queda el original
            pass
    print(PoblacionList[0].__str__())







