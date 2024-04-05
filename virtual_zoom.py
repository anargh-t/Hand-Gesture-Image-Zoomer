import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280) #width
cap.set(4,720)  #height

detector = HandDetector(detectionCon=0.8)
startDist = None
scale = 0
cx,cy = 500,500

while True:
    success,img = cap.read()
    img = cv2.flip(img, 1)
    hands,img = detector.findHands(img)
    #importing image
    img1 = cv2.imread("best-guard-dogs-1650302456.jpeg")
    img1 = cv2.resize(img1, (250, 250))

    if len(hands) == 2:
        #print(detector.fingersUp(hands[0]), detector.fingersUp(hands[1])) #shows values for both right and left hands
        if detector.fingersUp(hands[0])==[1,1,0,0,0] and detector.fingersUp(hands[1])==[1,1,0,0,0]:
            #print("Zoom Gesture")
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]

            #print(detector.findDistance(lmList1[8][:2],lmList2[8][:2],img))
            # point 8 is the tip of the index finger

            if startDist is None:
                length, info, img = detector.findDistance(lmList1[8][:2], lmList2[8][:2], img)
                #print("Distance between fingertips:", length)

                startDist = length
            
            length, info, img = detector.findDistance(lmList1[8][:2], lmList2[8][:2], img)
            scale = int(length - startDist) // 2
            cx,cy = info[4:]
            print(scale)

    else:
        startDist = None
        
    try:
        h1, w1, d1 = img1.shape
        newH, newW = ((h1+scale)//2)*2 , ((w1+scale)//2)*2
        img1 = cv2.resize(img1,(newW,newH))

        img[cy-newH//2:cy+newH//2, cx-newW//2:cx+newW//2] = img1
        # img[10:260,10:260] = img1
    except:
        pass
    
    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xFF==27:       #after video close and Asc character for esc button
        break


