import pyautogui
import time
time.sleep(5)
pyautogui.click()
l=200
a=4
x,y=pyautogui.position()
while (a):
    pyautogui.dragRel(200, 0, 0.2)
    x1,y1=pyautogui.position()
    a-=1
    pyautogui.dragRel(0, 200, 0.2)
    a-=1
    pyautogui.dragRel(-200, 0, 0.2)
    a-=1
    pyautogui.dragRel(0, -200, 0.2)
    a-=1
pyautogui.click(x,y)
pyautogui.dragRel(100, -100, 0.2)
pyautogui.click(x1,y1)
pyautogui.dragRel(-100, -100, 0.2)
pyautogui.dragRel(350, 0, 0.2)
pyautogui.dragRel(0, 300, 0.2)
pyautogui.dragRel(-290, 0, 0.2)

pyautogui.click(x1,y1)
pyautogui.dragRel(250, 0, 0.2)