'''
created at 2020.10.07 by zhanglei@tna.cn
using to test if the new device with ver2.7 could work easyly
need to prepare selenium and pyautogui in this pc which is 1920x1080
way to install selenium: run "pip install selenium" in cmd after installing python
way to install pyautogui: run "pip install pyautogui" in cmd after installing python
'''
import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
	
def web_open_BOX():
    driver.get("http://www.a.com/")
    driver.maximize_window()
    time.sleep(1)
    
def BOX_set():
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-input__inner").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "#login > span").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".next > span").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys("笛卡尔盾测试")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("1")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("1")
    pyautogui.press('enter')
    time.sleep(1)#init step2 finished
    pyautogui.moveTo(1111, 780, 1)
    pyautogui.click()
    driver.implicitly_wait(3)#init step3 finished
    pyautogui.moveTo(960, 840, 1)
    pyautogui.click()#close alert of closing pc-WIFI
   
driver = webdriver.Edge() 
driver.implicitly_wait(5)
web_open_BOX()
BOX_set()