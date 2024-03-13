import qrscanner
import serial
import time
import threading

ser = serial.Serial('COM4',9600,timeout=.1) 

op = qrscanner.qr_detect()

def moveMotor(speed1,speed2):
    speed = str(speed1)+","+str(speed2)+"\n"
    ser.write(bytes(speed,  'utf-8'))

def detectCam():
    while True:
        qrscanner.open_window()

def cetakHasil():
    global op
    while True:
        op = qrscanner.qr_detect()
        print(op)
        if op == "kanan":
            moveMotor(200,0)
            time.sleep(1)
        
        elif op == "kiri":
            moveMotor(0,200)
            time.sleep(0.1)

        elif op == "mundur":
            moveMotor(-200,-200)
            time.sleep(1)
        
        elif op == "maju":
            moveMotor(200,200)
            time.sleep(1)
        
        else:
            moveMotor(0, 0)
            time.sleep(1)


# while True:

    
#     detectCam()
#     cetakHasil()

detect_thread = threading.Thread(target=detectCam)
cetak_thread = threading.Thread(target=cetakHasil)

detect_thread.start()
cetak_thread.start()

detect_thread.join()
cetak_thread.join()
  