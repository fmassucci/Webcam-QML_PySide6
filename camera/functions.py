import cv2

def colorSelection (imageBGR, lower, upper):
    hsv = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2HSV)
    masked = cv2.inRange(hsv, (lower,0,0), (upper,255,255))
    result = cv2.bitwise_and(imageBGR, imageBGR, mask = masked) 
    result= cv2.cvtColor(result, cv2.COLOR_BGR2RGB)  
    return result