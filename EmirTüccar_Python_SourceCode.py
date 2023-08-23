import cv2
import imutils
import serial
import time
  
def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=540,
    display_height=4800,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink drop=True"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

arduino = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout= .1)

gun_cascade = cv2.CascadeClassifier('cas.xml')
body_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)
   
firstFrame = None
gun_exist = False

servo_degree = 90
def write_read(x):
    arduino.write(bytes(x))
    time.sleep(0.25)
    data = arduino.readline()
    return data


while True:
      
    ret, frame = camera.read()
   
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       
    guns = gun_cascade.detectMultiScale(gray,
                                       1.1, 5,
                                       minSize = (50, 50))
    
    body = body_cascade.detectMultiScale(gray,
                                       1.1, 5)
       
    if len(guns) > 0:
        gun_exist = True
           
    for i, (x, y, w, h) in enumerate(guns):
          
        frame = cv2.rectangle(frame,
                              (x, y),
                              (x + w, y + h),
                              (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]    

        # Write the index and location of the gun on the frame
        cv2.putText(frame, "Gun {}: ({}, {})".format(i,x,y), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

        #xd = (x//6) +45
        #arduino.write(xd)
        
        if (0 < x < 60):
            arduino.write(b'1')

        elif (60<=x<120):

           arduino.write(b'2')

        elif (120 <=x < 180):
            arduino.write(b'3')

        elif (180<=x<240):

            arduino.write(b'4')

        elif (240<=x<300):
            arduino.write(b'5')

        elif (300<=x<360):

           arduino.write(b'6')

        elif (360 <=x < 420):
            arduino.write(b'7')

        elif (420<=x<480):

            arduino.write(b'8')

        elif (480<=x<540):
            arduino.write(b'9')

        
        # Break after the first gun is detected
        if i == 0:
            break

    for (x, y, w, h) in body:

        for (gx, gy, gw, gh) in guns:

            if gx + 500 > x and gy +500 > y and gx + gw < x + w +1000 and gy + gh < y + h + 1000:

                color = (0,0,255)
                break

        else:
            color = (0,255,0)

        cv2.rectangle(frame, (x,y), (x + w, y+h), color, 2)





#    if (color == (0,0,255)):
        # Gun is detected near the face
  #      arduino.write(b'L')  # Send 'L' to Arduino to turn the servo left
 #   else:
        # Gun is not detected near the face
   #     arduino.write(b'R')  # Send 'R' to Arduino to turn the servo right

    
    #if (color == (0,0,255)):

        #cv2.putText(frame, "Gun detected", cv2.FONT_HERSHEY_SIMPLEX)
        
   
    if firstFrame is None:
        firstFrame = gray
        continue
   
    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF
      
    if key == ord('q'):
        break
  
    if gun_exist:
        print("guns detected")
    else:
        print("guns NOT detected")
  
camera.release()
cv2.destroyAllWindows()
