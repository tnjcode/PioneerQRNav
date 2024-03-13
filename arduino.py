import numpy as np
import serial
import time
import threading

# initializing serial port and its properties
ser = serial.Serial('COM4',115200,bytesize=8,parity="N",stopbits=1,timeout=None)

# delay 1 second to prepare arduino
time.sleep(1)

# the buffer data to be sent to arduino
data = np.zeros(6, dtype=np.uint8)

# assigning values of each elements
data[0] = 0x73
data[1] = 1
data[2] = 0
data[3] = 0
data[4] = 0
data[5] = 0x64

# function to be called as a thread to write serial data
def writing():
    while True:
        ser.write(data)
        time.sleep(0.01)

# function to be called as a thread to read serial data
def read():
    while True:
        receivedData = ser.readline()
        print(receivedData)

# declaring threads
t1 = threading.Thread(target=writing)
t2 = threading.Thread(target=read)

# starting threads
t1.start()
t2.start()

t1.join()
t2.join()

