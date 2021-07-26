import pyautogui
from PIL import Image,ImageGrab
import time
from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

def takess():
    image = ImageGrab.grab().convert('L')
    return image

if __name__ == "__main__":
    print("Dino game about to start")
    time.sleep(3)
    hit('up')
    cnt=0
    speed1 = 420
    speed2 = 400
    ac=speed1
    while True:
        speed1 = speed1 + ac*0.00032
        speed2 = speed2 + ac*0.00032
        image = takess()
        data = image.load()
            # if ismidbird(data):
            #     hit("down")
        print(str(speed1)+"\n")

        if iscolourchange(data,cnt):
            if isCollidedark(data,speed1,speed2):
                hit("up")
        else:
            if isCollide(data,speed1,speed2):
                hit("up")
        

    # print(asarray(data))
    draw(data,speed1)
    image.show()
    
    
    
    def iscolourchange(data,cnt):
    for i in range(80,81):
        for j in range(80,81):
            if (data[i,j]<(125) and cnt%2==0) or (data[i,j]>(125) and cnt%2!=0):
                cnt=cnt+1
    return cnt%2


