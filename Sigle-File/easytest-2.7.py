'''
created at 2020.10.07 by zhanglei@tna.cn
using to test if the new device with ver2.7 could work easyly
need to prepare selenium and pyautogui in this pc which is 1920x1080
way to install selenium: run "pip install selenium" in cmd after installing python
way to install pyautogui: run "pip install pyautogui" in cmd after installing python
'''
import os
import time
import pyautogui
from sys import exit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def web_open_LAN2():
    driver.get("http://192.168.110.1/")
    driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(1)

def center_set():
    driver.find_element(By.CSS_SELECTOR, ".admin > .img").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys("cartesianshield")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("192.168.3.200/24")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("192.168.3.1")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-input__inner").send_keys("192.168.100.234/24")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(5) .el-input__inner").send_keys("192.168.100.101")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(6) .el-input__inner").send_keys("192.168.3.200:32749")
    driver.find_element(By.CSS_SELECTOR, ".right").click()
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(5) .el-dialog__close").click()
    
def route_check():
    os.startfile('C:\putty.exe')
    pyautogui.alert('设置输入法为英文后点击「确定」')
    pyautogui.typewrite('192.168.110.1')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.typewrite('tna')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.typewrite('123456')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.typewrite('ip route show table 4')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.typewrite('ip addr show dev enp6s0')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.typewrite('ip addr show dev enp1s0')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.alert('若网址信息无误且LED1闪烁则点击「确定」')
    time.sleep(1)
    pyautogui.typewrite('exit')
    pyautogui.press('enter')
    time.sleep(1)

def center_reset():
    driver.get("http://192.168.110.1/#/advanced/index")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button > span").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-input__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("RESET")
    driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys(Keys.ENTER)
    time.sleep(1)

driver = webdriver.Edge()
driver.implicitly_wait(10)
web_open_LAN2()
center_set()
route_check()
center_reset()
driver.close()
exit()