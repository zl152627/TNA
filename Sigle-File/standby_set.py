'''
created at 2020.10.07 by zhanglei@tna.cn
use to set standby device for Center and Nodes
need to prepare python and pyautogui in this pc
way to install selenium: run "pip install selenium" in cmd after installing python
way to install pyautogui: run "pip install pyautogui" in cmd after installing python
'''
import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()

def web_open_LAN2():
    driver.get("http://192.168.110.1/")
    driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(1)

def center_standby():
    driver.find_element(By.CSS_SELECTOR, ".el-submenu__title > span").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".nest-menu:nth-child(5) span").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("192.168.100.233/24")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("192.168.100.232/24")
    driver.find_element(By.CSS_SELECTOR, ".right:nth-child(2) > span").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(9) > span").click()
    time.sleep(1)

def resource_node_standby():
    driver.find_element(By.CSS_SELECTOR, ".el-submenu__title").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".nest-menu:nth-child(2) span").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("10.10.10.233/24")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("10.10.10.232/24")
    driver.find_element(By.CSS_SELECTOR, ".right:nth-child(2) > span").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(9) > span").click()
    time.sleep(1)
    
def user_node_standby():
    driver.find_element(By.CSS_SELECTOR, ".el-submenu__title").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".nest-menu:nth-child(2) span").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("10.10.20.233/24")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("10.10.20.232/24")
    driver.find_element(By.CSS_SELECTOR, ".right:nth-child(2) > span").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(9) > span").click()
    time.sleep(1)
    

pyautogui.alert('正确接入Center主备机网线后点击确定')
web_open_LAN2()
center_standby()

pyautogui.alert('正确接入资源Node主备机网线后点击确定')
web_open_LAN2()
resource_node_standby()

pyautogui.alert('正确接入用户Node主备机网线后点击确定')
web_open_LAN2()
user_node_standby()

driver.close()