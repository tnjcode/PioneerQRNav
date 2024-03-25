import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3, 160)
cap.set(4, 120)
in1 = 4
in2 = 17
in3 = 27
in4 = 22
en1 = 23
en2 = 24
qcd = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()
    forqr = frame.copy()
    cv2.normalize(frame, frame, 0, 80, cv2.NORM_MINMAX)
    low_b = np.array([5,0,0])
    high_b = np.array([49,49,239])
    mask = cv2.inRange(frame, low_b, high_b)
    contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0 :
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] !=0 :
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            # print("CX : "+str(cx)+"  CY : "+str(cy))
            if cx >= 120 :
                # print("Turn Right")
                pass
            if cx < 120 and cx > 40 :
                # print("On Track!")
                pass
            if cx <=40 :
                # print("Turn Left")
                pass
            cv2.circle(frame, (cx,cy), 5, (255,255,255), -1)
            cv2.drawContours(frame, c, -1, (0,255,0), 1)
    else :
        # print("I don't see the line")
        pass
    

    retval, points, straight_code = qcd.detectAndDecode(forqr)
    if retval != "":
        print(retval)


    cv2.imshow("Mask",mask)
    cv2.imshow("Frame",frame)
    cv2.imshow("QR Detect", forqr)
    if cv2.waitKey(1) & 0xff == ord('q'):   # 1 is the time in ms
        break
cap.release()
cv2.destroyAllWindows()