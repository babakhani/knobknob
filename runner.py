import pyautogui
import osascript
import serial


currentVolume = 100

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

handlers = [handleScroll, handleMoveDesktop, handleVolume, handleVideo]

handlerIndex = 0

def nextHandler():
    global handlerIndex
    if (handlerIndex == (len(handlers) - 1)):
       handlerIndex = 0
    else:
       handlerIndex += 1
    print(handlers[handlerIndex])

while(1):
    if(serialPort.in_waiting > 0):

        # Get serial input
        serialString = serialPort.readline()
        direction = serialString.decode('Ascii').strip()

        print(direction)

        if (direction == "SW"):
            nextHandler()
        
        # handle CCW and CW
        currentHandler = handlers[handlerIndex]
        currentHandler(direction)

