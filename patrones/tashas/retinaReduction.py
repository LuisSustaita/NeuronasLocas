'''
Vista del DVS con filtro de ruido
Modificar en el main para:
mostrar un archivo grabado (RetinaRecord)
grabar un archivo nuevo y mostrarlo en pantalla (Retina)
'''

import serial
import time
import thread
import numpy as np
import sys
import math

class Retina(object):
    def __init__(self, port='/dev/ttyUSB0', record=None):
        self.serial = serial.Serial(port, baudrate=4000000, rtscts=True)
        time.sleep(0.1)
        self.serial.write("E+\nZ+\n")
        self.image = np.zeros((128, 128), dtype=float)
        self.Tmap = np.zeros((128, 128), dtype=float)
        self.start_point = time.time()

        if record is not None:
            self.record = open(record, 'w')
        else:
            self.record = None
        thread.start_new_thread(self.update_loop, ())

    def clear_image(self):
        self.image *= 0.3

    def update_loop(self):
        cont = 0
        i=0

        while True:
            byte0 = ord(self.serial.read())
            if byte0 & 0x80 == 0:
                #print 'invalid byte', byte0, chr(byte0), 'good:', events
                continue

            byte0 = byte0 & 0x7F   # strip the top byte
            byte1 = ord(self.serial.read())
            sign = byte1 >= 0x7F
            byte1 = byte1 & 0x7F   # strip the top byte
            t = time.time() - self.start_point

            dif = t -float(self.Tmap[byte0,byte1])

            if (dif<0.8):
                self.image[math.ceil(byte1/4), math.ceil(byte0/4)] += 1 if sign else -1
                if self.record is not None:
                    self.record.write('%d %d %d %.6f\n' % (byte0, byte1, sign, t))

            self.Tmap[byte0,byte1]= t

class RetinaRecord(object):#Borrar la reduccion luego de actualizar los patrones de prueba
    def __init__(self, filename):
        self.data = open(filename)
        self.image = np.zeros((128, 128), dtype=float)
        thread.start_new_thread(self.update_loop, ())

    def clear_image(self):
        self.image *= 0.3

    def update_loop(self):
        offset = None

        for line in self.data.readlines():
            x, y, sign, t = line.strip().split()
            y = math.ceil(int(y)/4)
            x = math.ceil(int(x)/4)
            sign = int(sign)
            t = float(t)
            if offset is None:
                offset = time.time() - t

            #while time.time() < t + offset:
            time.sleep(0.000001)
                #pass

            self.image[y, x] += 1 if sign else -1

class RetinaView(object):
    def __init__(self, retina):
        self.retina = retina
        thread.start_new_thread(self.update_loop, ())
        self.start_point=time.time()

    def update_loop(self):
        import matplotlib.pyplot as plt
        plt.ion()
        #plt.grid(True)
        #plt.grid(color='red',linestyle='-',linewidth=1)
        #plt.axvspan(30,100,alpha=0.10,color='r')
        #plt.axhspan(80,120,alpha=0.10,color='r')
        vmin, vmax = -1, 1

        self.img = plt.imshow(self.retina.image, vmin=vmin, vmax=vmax,
                                cmap='gray', interpolation='none')

        while True:
            elapsed_time = time.time () - self.start_point
            plt.title('DVS OUTPUT. Time: '+str(elapsed_time))
            self.img.set_data(self.retina.image)
            self.retina.clear_image()
            plt.draw()
            time.sleep(0.01)



if __name__ == '__main__':
    #Grabar
    #retina = Retina(record='blinking.data')
    #Mostrar grabacion
    retina = RetinaRecord('blinking5.data')
    view = RetinaView(retina)

    while True:
        time.sleep(1)
        if sys.stdin.read(1)=='q':
            break


#https://pybonacci.es/2012/05/25/manual-de-introduccion-a-matplotlib-pyplot-iii-configuracion-del-grafico/#more-438
