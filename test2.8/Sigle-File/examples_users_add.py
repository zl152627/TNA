'''
created at 2020.10.10 by zhanglei@tna.cn
use to set Center in adding Users
need to prepare python and pyautogui in this pc which is 1920x1080
way to install selenium: run "pip install selenium" in cmd after installing python
way to install pyautogui: run "pip install pyautogui" in cmd after installing python
'''

import os
import time
import random
import pyautogui
from sys import exit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def web_open_LAN2():
    driver.get("http://192.168.110.1:8092/#/main/index")
    driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(1)
    
def web_open_LAN1():
    driver.get("http://192.168.100.234:8092/#/main/index")
    driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(1)

def user_add(name, code):
    pyautogui.press('F5')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys(code)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button--primary > span").click()#确定
    
dict_user = {
    '李 四':101,
    '王  五':102,
    '诸葛猫蛋儿':103,
    '欧阳狗剩儿':104,
    '#@$DAF': 105,
    'sdk faj 1f5sd':106 
    }

def choice_way():
    way_openWeb = int(input("choice 1 or 2\n1:Control center via 192.168.110.1\n2:Control center via 192.168.100.234\n>"))
    if way_openWeb == 1:
        web_open_LAN2()
    elif way_openWeb == 2:
        web_open_LAN1()
    else:
        choice_way()

driver = webdriver.Edge()
driver.implicitly_wait(3)
driver.minimize_window()
choice_way()
for name, code in list(dict_user.items()):
    user_add(name, code)
driver.close()
pyautogui.hotkey('ctrl', 'c')
exit()