'''
created at 2020.10.10 by zhanglei@tna.cn
use to set Center in adding Nodes
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
    driver.maximize_window()
    driver.get("http://192.168.110.1:8092/#/gateway/index")
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(1)
	
def web_open_LAN1():
    driver.get("http://192.168.100.234:8092/#/gateway/index")
    driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(1)
    
def node_add_resource(resource_node_name, resource_node_net):
    pyautogui.press('F5')
    driver.find_element(By.CSS_SELECTOR, ".el-button-group > .el-button:nth-child(1)").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".name > .el-input__inner").send_keys(resource_node_name)
    driver.find_element(By.CSS_SELECTOR, "select:nth-child(1)").click()#省
    pyautogui.press('down', random.randint(1,34))
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, "select:nth-child(2)").click()#市
    pyautogui.press('down',random.randint(1,10))
    pyautogui.press('enter')
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content:nth-child(1) .el-input__inner").send_keys(resource_node_net)
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()#确定
    time.sleep(1)
    
def node_add_user(user_node_name):
    pyautogui.press('F5')
    driver.find_element(By.CSS_SELECTOR, ".el-button-group > .el-button:nth-child(1)").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".name > .el-input__inner").send_keys(user_node_name)
    driver.find_element(By.CSS_SELECTOR, "select:nth-child(1)").click()#省
    pyautogui.press('down', random.randint(1,34))
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, "select:nth-child(2)").click()#市
    pyautogui.press('down',random.randint(1,10))
    pyautogui.press('enter')
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".el-radio:nth-child(2) > .el-radio__label").click()#用户模式
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)

dict_resource_node = {
    'Resc-Node': '10.10.12.0/24',
    '一二三四五六七八九十一二三四五六七八九廿': '10.10.13.0/24',
    '@#$%资源 网关@#$^': '10.10.14.0/24'
    }
list_user_node_name = ['user-Node1', '1237894', '一二三四五六七八九十一二三四五六七八九廿', '@#$ 用户 网 关1%@#$^']

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
for resource_node_name, resource_node_net in list(dict_resource_node.items()):
    node_add_resource(resource_node_name, resource_node_net)
for user_node_name in list_user_node_name:
    node_add_user(user_node_name)
print("-----add nodes finished-----")
driver.close()
pyautogui.hotkey('ctrl', 'c')
exit()