'''
created at 2020.10.10 by zhanglei@tna.cn
use to set Center in adding Resources
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
    driver.get("http://192.168.110.1:8092/#/policy/index")
    driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > a > .submenu-title-noDropdown > span").click()
    time.sleep(1)

def web_open_LAN1():
    driver.get("http://192.168.100.234:8092/#/policy/index")
    driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(1)

def resource_add_Center_TCP(center_name, center_net):
    pyautogui.press('F5')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys(center_name)
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys(center_net)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)

def resource_add_Center_UDP(center_name, center_net):
    pyautogui.press('F5')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys(center_name)
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys(center_net)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
    pyautogui.press('down', 2)#123:tcp udp 全通
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)

def resource_add_Center_ALL(center_name, center_net):
    pyautogui.press('F5')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys(center_name)
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys(center_net)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
    pyautogui.press('down', 3)#123:tcp udp 全通
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)

def resource_add_Node_TCP(resource_name, resource_net):
    pyautogui.press('F5')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys(resource_name)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-select .el-input__inner").click()#接入网关
    pyautogui.press('down', 2)
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys(resource_net)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)

def resource_add_Node_UDP(resource_name, resource_net):
    pyautogui.press('F5')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys(resource_name)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-select .el-input__inner").click()#接入网关
    pyautogui.press('down', 2)#Resource_Node, net_range_10.10.0.0/16
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys(resource_net)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
    pyautogui.press('down', 2)
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)

def resource_add_Node_ALL(resource_name, resource_net):
    pyautogui.press('F5')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys(resource_name)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-select .el-input__inner").click()#接入网关
    pyautogui.press('down', 2)
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys(resource_net)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
    pyautogui.press('down', 3)
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)
	
dict_center = {
    'TNA管理中心': '192.168.100.234',
    '#￥879… a中 s23管理…6': '192.168.100.234:8888',
    'TNA管理中心-10.10.10.1': '10.10.10.1',
    'TNA管理中心-10.10.10.2': '10.10.10.2',
    'TNA管理中心-10.10.20.1': '10.10.20.1'
    }
dict_node = {
    '改端口号限制10.1:8888': '10.10.10.1:8888',
    '一二三四五六七八九十一二三四五六七八九廿': '10.10.10.2',
    '一二三四五六七': '10.10.10.1'
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
for center_name, center_net in dict_center.items():
        resource_add_Center_ALL(center_name, center_net)
        
for resource_name, resource_net in dict_node.items():
    resource_add_Node_ALL(resource_name, resource_net)

resource_add_Center_UDP('UDP#￥… a中 s23管理…6', '192.168.100.234:8888')
resource_add_Node_UDP('UDP端口号10.1:8888', '10.10.10.1:8888')
#dict_center.get('TNA管理中心')

driver.close()
pyautogui.hotkey('ctrl', 'c')
exit()