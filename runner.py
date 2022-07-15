import pyautogui
import osascript
import serial

mode = "video"

currentVolume = 100

osascript.osascript("set volume output volume 100")

serialPort = serial.Serial(port = "/dev/cu.usbserial-1410", baudrate=9600)

serialString = "" 

def handleVideo (direction):
    if (direction == 'CW'):
        pyautogui.press('left')
    if (direction == 'CCW'):
        pyautogui.press('right')

def handleScroll (direction):
    if (direction == 'CW'):
        pyautogui.scroll(30)
    if (direction == 'CCW'):
        pyautogui.scroll(-30)

def handleMoveDesktop (direction):
    if (direction == 'CW'):
        pyautogui.keyDown('ctrl')
        pyautogui.press('right')
    if (direction == 'CCW'):
        pyautogui.keyDown('ctrl')
        pyautogui.press('left')

def handleVolume (direction):
    global currentVolume
    if (direction == 'CW'):
        if (currentVolume < 0):
           print("Volume UP")
           currentVolume = 0
        else:    
           currentVolume -= 5
    if (direction == 'CCW'):
        if (currentVolume > 100):
           print("Volume DOWN")
           currentVolume = 100
        else:    
           currentVolume += 5
    print(currentVolume)
    osascript.osascript("set volume output volume %s" % currentVolume)

while(1):
    if(serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        # print(serialString)
        direction = serialString.decode('Ascii').strip()
        print(direction)
        handleVolume(direction)
        # handleMoveDesktop(direction)
        # handleScroll(direction)
        # handleVideo(direction)
