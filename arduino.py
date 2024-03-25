# import numpy as np
# import serial
# import time
# import threading
# # import qrscanner

# # initializing serial port and its properties
# ser = serial.Serial('COM4',115200,bytesize=8,parity="N",stopbits=1,timeout=None)

# # op = qrscanner.qr_detect()

# # delay 1 second to prepare arduino
# time.sleep(1)

# # the buffer data to be sent to arduino
# data = np.zeros(6, dtype=np.uint8)

# # assigning values of each elements
# data[0] = 0x73
# data[1] = 1
# data[2] = 200
# data[3] = 0
# data[4] = 200
# data[5] = 0x64

# # function to be called as a thread to write serial data
# def writing():
#     global data 
#     while True:
#         ser.write(data)
#         time.sleep(0.01)

# # function to be called as a thread to read serial data
# # def open_window():
# #     while True:
# #         qrscanner.open_window()

# # function to read qr value
# def read():
#     while True:
#             data[1] = 1
#             data[2] = 200
#             data[3] = 0
#             data[4] = 200
        
#         elif op == "kiri":
#             data[1] = 0
#             data[2] = 200
#             data[3] = 1
#             data[4] = 200

#         elif op == "mundur":
#             data[1] = 1
#             data[2] = 200
#             data[3] = 1
#             data[4] = 200
        
#         elif op == "maju":
#             data[1] = 0
#             data[2] = 200
#             data[3] = 0
#             data[4] = 200
        
#         else:
#             data[1] = 0
#             data[2] = 0
#             data[3] = 0
#             data[4] = 0

# # declaring threads
# t1 = threading.Thread(target=writing)
# t2 = threading.Thread(target=read)
# t3 = threading.Thread(target=motor)

# # starting threads
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
