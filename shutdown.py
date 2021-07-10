import pywhatkit 
import pyautogui
def shutdownsystem(time):
    pywhatkit.shutdown(time)

def takescreenshot(sname):
    image = pyautogui.screenshot()
    image.save(sname+".PNG")
    n=int(input("enter 1 to show the image"))
    if(n==1):
        image.show()
