'''
created at 2020.10.07 by zhanglei@tna.cn
use to set Center in Net, Node, Resource, Users and so on
need to prepare python and pyautogui in this pc which is 1920x1080 and 100%-scale
way to install selenium: run "pip install selenium" in cmd after installing python
way to install pyautogui: run "pip install pyautogui" in cmd after installing python
'''

import time
import pyautogui
from sys import exit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def web_open():
    driver.get("http://192.168.110.1/#/advanced/index")
    driver.maximize_window()
    #driver.set_window_size(1366, 768)
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(1)
	
def gateway_reset():
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button > span").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-input__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("RESET")
    driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys(Keys.ENTER)
    time.sleep(3)

def web_open_BOX():
    driver.get("http://www.a.com/")
    driver.maximize_window()
    #driver.set_window_size(1366, 768)
    time.sleep(2)

def BOX_reset():
    pyautogui.moveTo(30, 150, 1)
    pyautogui.click()
    pyautogui.moveTo(30, 270, 2)
    pyautogui.click()
    pyautogui.moveTo(888, 380, 1)
    pyautogui.click()
    pyautogui.typewrite('7758521')
    pyautogui.moveTo(1030, 440, 1)
    pyautogui.click()
    time.sleep(1)

def way_choice():
    way_choice = int(input("choice 1 or 2:\n1: reset BOX\n2: reset Gateway\n>"))
    if way_choice == 1:
        web_open_BOX()
        BOX_reset()
    elif way_choice == 2:
        web_open()
        gateway_reset()
    else:
        way_choice()
    
driver = webdriver.Edge()
driver.minimize_window()
way_choice()
driver.close()
pyautogui.hotkey('ctrl', 'c')
exit()