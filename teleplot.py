import serial.tools.list_ports
from matplotlib import pyplot as plt
import time
import datetime

def userplot():
    serialInst = serial.Serial()

    portVar = "COM3"
    serialInst.baudrate = 9600
    serialInst.port = portVar
    serialInst.open()

    def throttle(x, max, min):
        max -= min
        x -= min
        return 100*(max - x)/(max) # This is to calculate % of throttle

    xlst = []
    ylst = []
    i = 0
    while True:
        if serialInst.in_waiting:
            try:
                packet = serialInst.readline()
                reading = int(packet.decode('utf').rstrip("\r\n")[:-1])
                status = int(packet.decode('utf').rstrip("\r\n")[-1])
            except ValueError:
                status = int(packet.decode('utf').rstrip("\r\n")[-1])

            if status == True:
                if i == 0:
                    start_time = time.time()
                xlst.append(time.time() - start_time)
                # print(xlst[-1])
                if reading > 8:
                    ylst.append(0)
                elif reading < 3:
                    ylst.append(100)
                else:
                    ylst.append(throttle(reading,8,3))

                print(ylst[-1], reading)
                i=1
            if len(xlst) > 0 and status == False:
                break


    for i in range(50,len(ylst)-50): # Smooth the graph out by taking the average of 50 entries on either side. Sensor is a bit erratic
        ylst[i] = sum(ylst[i-50:i+51])/100

    for x in xlst: # Converts the xlst values (which are in seconds) to minutes and seconds. Eg: 65 -> 1:05
        x = str(datetime.timedelta(seconds=x))


    plt.plot(xlst,ylst)
    plt.savefig("static\\usertelemetry.jpg")
    return True
