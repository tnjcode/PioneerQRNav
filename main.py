import pioneer
import qrscanner
import time

pn = pioneer.Pioneer()

while True:
    qrscanner.open_window()
    op = qrscanner.qr_detect()
    print(op)

    if op == "kanan":
        pn.move_pioneer(3, 0)
        # time.sleep(1)
    
    elif op == "kiri":
        pn.move_pioneer(0, 3)
        # time.sleep(1)

    elif op == "mundur":
        pn.move_pioneer(-5, -5)
        # time.sleep(1)
    
    elif op == "maju":
        pn.move_pioneer(5,5)
        # time.sleep(1)
    
    else:
        pn.move_pioneer(0, 0)