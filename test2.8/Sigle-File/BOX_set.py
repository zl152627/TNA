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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def web_open_BOX():
    driver.get("http://www.a.com/")
    driver.maximize_window()
    time.sleep(1)
    
def BOX_set():
    element_BOX_init_Login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner")))
    element_BOX_init_Login.send_keys("123456")
    #driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("123456")
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
    pyautogui.moveTo(1111, 720, 1)
    pyautogui.click()
    time.sleep(5)#init step3 finished
    pyautogui.moveTo(950, 650, 1)
    pyautogui.click()#close alert of closing pc-WIFI
    pyautogui.click(950, 700)
   
driver = webdriver.Edge() 
time.sleep(5)
web_open_BOX()
BOX_set()