import cv2
import imutils

lower=(136,40,100)
higher=(179,255,255)

#starting the camera

cam=cv2.VideoCapture(0)

while True:
    (grabbed,frame)=cam.read()
    farme=imutils.resize(frame,width=400)
    #smooth making

    blurred=cv2.GaussianBlur(frame,(11,11),0)
    #converting BDR to HSV

    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)

    #take mak
    mask=cv2.inRange(hsv,lower,higher)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center=None
    if len(cnts)>0:
        c=max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center=(int (M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
        if radius>10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
            #coloring dark dot
            cv2.circle(frame,center,5,(0,0,255),-1)
            if radius >250:
                print("stop")
            else:
                if(center[0]<150):
                    print("left")
                elif(center[0]>450):
                    print("Right")
                elif(radius<250):
                    print("Front")
                else:
                    print("stop")
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)&0xFF
    if key==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
                    
                
            
        
    
    

