# -*- coding:utf-8 -*-
'''
created at 2020.10.21 by zhanglei@tna.cn
use to set Center in Net, Node, Resource, Users and so on
need to prepare python and pyautogui in this pc which is 1920x1080 and 100%-scale
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

#网络配置 http://192.168.110.1:8092/#/config/network
#主备管理 http://192.168.110.1:8092/#/config/standby
#添加网关 http://192.168.110.1:8092/#/gateway/index
#添加资源 http://192.168.110.1:8092/#/policy/index
#添加用户 http://192.168.110.1:8092/#/main/index

def web_open_LAN2():
    driver.get("http://192.168.110.1/")
    driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(1)

def mode_choice_center():
    driver.find_element(By.CSS_SELECTOR, ".admin > .img").click()
    time.sleep(1)

def center_set():
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys("笛卡尔盾科技有限公司")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("192.168.3.200/24")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("192.168.3.1")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-input__inner").send_keys("192.168.100.234/24")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(5) .el-input__inner").send_keys("192.168.100.101")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(6) .el-input__inner").send_keys("192.168.3.200:32749")
    driver.find_element(By.CSS_SELECTOR, ".right").click()
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(5) .el-dialog__close").click()
    time.sleep(1)

def resource_add_Center():
    driver.get("http://192.168.110.1:8092/#/policy/index")
    #driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > a > .submenu-title-noDropdown > span").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys("Center")
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys("192.168.100.234:8092")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
    time.sleep(0.2)
    pyautogui.press('down', 3)
    pyautogui.press('enter')#全通
    driver.find_element(By.CSS_SELECTOR, ".el-button--success").click() #加服务地址
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(3) .el-input-group__prepend .el-input__inner").click()
    time.sleep(0.2)
    pyautogui.press('down', 3)
    pyautogui.press('enter')#全通
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(3) .ep > .el-input__inner").send_keys("192.168.100.101")
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)
    #-------add Center-Route-------
    pyautogui.press('F5')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys("Center-Route")
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys("192.168.101.101:8092")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
    pyautogui.press('down', 3)
    pyautogui.press('enter')#全通
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)
    
def node_add_resource():
    driver.get("http://192.168.110.1:8092/#/gateway/index")
    #driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) .submenu-title-noDropdown").click()
    time.sleep(1)
    #add Resource-Node
    driver.find_element(By.CSS_SELECTOR, ".el-button-group > .el-button:nth-child(1)").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".name > .el-input__inner").send_keys("Resource-Node")
    driver.find_element(By.CSS_SELECTOR, "select:nth-child(1)").click()#省
    pyautogui.press('down', random.randint(1,34))
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, "select:nth-child(2)").click()#市
    pyautogui.press('down',random.randint(1,10))
    pyautogui.press('enter')
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content:nth-child(1) .el-input__inner").send_keys("10.10.0.0/16")
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()#确定
    time.sleep(1)
    #add Resource-Node2
    pyautogui.press('F5')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button-group > .el-button:nth-child(1)").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".name > .el-input__inner").send_keys("Resource-Node2")
    driver.find_element(By.CSS_SELECTOR, "select:nth-child(1)").click()#省
    pyautogui.press('down', random.randint(1,34))
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, "select:nth-child(2)").click()#市
    pyautogui.press('down',random.randint(1,10))
    pyautogui.press('enter')
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".el-button--success").click()
    time.sleep(0.5)#点击加号后框的元素名发生了变化，不要改动位置
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input__inner").send_keys("10.10.30.0/24")
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(3) .el-input__inner").send_keys("10.10.31.0/24")
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()#确定
    time.sleep(1)
    
def node_add_user():
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) .submenu-title-noDropdown").click()
    time.sleep(1)
    #add User-Node
    driver.find_element(By.CSS_SELECTOR, ".el-button-group > .el-button:nth-child(1)").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".name > .el-input__inner").send_keys("User-Node")
    driver.find_element(By.CSS_SELECTOR, "select:nth-child(1)").click()#省
    pyautogui.press('down', random.randint(1,34))
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, "select:nth-child(2)").click()#市
    pyautogui.press('down',random.randint(1,10))
    pyautogui.press('enter')
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".el-radio:nth-child(2) > .el-radio__label").click()#用户模式
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".app-name").click()#添加资源
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(1) > .el-checkbox__label").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(2) > .el-checkbox__label").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(3) > .el-checkbox__label").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(4) > .el-checkbox__label").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(5) > .el-checkbox__label").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(6) > .el-checkbox__label").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(7) > .el-checkbox__label").click()
    pyautogui.moveTo(1288, 484, 1)
    pyautogui.click()
    #driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(2) .el-button--primary > span").click()
    #error：selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
    time.sleep(1)
    
def resource_add_Resource():
    driver.get("http://192.168.110.1:8092/#/policy/index")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()#资源-添加
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys("Resource_Node")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-select .el-input__inner").click()#接入网关
    pyautogui.press('down', 2)
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys("10.10.10.1:8092")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
    time.sleep(0.2)
    pyautogui.press('down', 3)
    pyautogui.press('enter')#全通
    driver.find_element(By.CSS_SELECTOR, ".el-button--success").click() #加服务地址
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(3) .el-input-group__prepend .el-input__inner").click()
    time.sleep(0.2)
    pyautogui.press('down', 3)
    pyautogui.press('enter')#全通
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(3) .ep > .el-input__inner").send_keys("10.10.10.2")
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)
    #-------add Resource-Route-------
    pyautogui.press('F5')
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys("Resource-Route")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-select .el-input__inner").click()#接入网关
    pyautogui.press('down', 2)
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys("10.10.11.1:8092")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
    pyautogui.press('down', 3)#全通
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)
    #-------add Resource-PC-------
    pyautogui.press('F5')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys("R-PC-for-speedtest")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-select .el-input__inner").click()#接入网关
    pyautogui.press('down', 2)
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys("10.10.10.101")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
    pyautogui.press('down', 3)#全通
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)
    
def resource_add_Resource2():
    pyautogui.press('F5')
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()#资源-添加
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys("Resource_Node2")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-select .el-input__inner").click()#接入网关
    pyautogui.press('down', 3)
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys("10.10.30.1:8092")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
    time.sleep(0.2)
    pyautogui.press('down', 3)
    pyautogui.press('enter')#全通
    driver.find_element(By.CSS_SELECTOR, ".el-button--success").click() #加服务地址
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(3) .el-input-group__prepend .el-input__inner").click()
    time.sleep(0.2)
    pyautogui.press('down', 3)
    pyautogui.press('enter')#全通
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(3) .ep > .el-input__inner").send_keys("10.10.30.2")
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)
    #-------add Resource2-Route-------
    pyautogui.press('F5')
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys("Resource2-Route")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-select .el-input__inner").click()#接入网关
    pyautogui.press('down', 3)
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys("10.10.31.1:8092")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
    pyautogui.press('down', 3)#全通
    pyautogui.press('enter')
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
    time.sleep(1)

def user_add():
	#driver.get(http://192.168.110.1:8092/#/main/index)
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > a > .submenu-title-noDropdown").click()
    time.sleep(1)
    #add user zl
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("zl")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("zl")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-input__inner").send_keys("15010821222")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(5) .el-input__inner").send_keys("zhanglei@tna.cn")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(6) .el-input__inner").send_keys("昆仑-华夏")
    #add resources
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(1) .el-checkbox__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(2) .el-checkbox__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(3) .el-checkbox__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(4) .el-checkbox__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(5) .el-checkbox__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(6) .el-checkbox__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(7) .el-checkbox__inner").click()
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button--primary > span").click()#确定
    time.sleep(1)
    #add more box resources
    driver.find_element(By.CSS_SELECTOR, ".icon-add-offline").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-message-box__btns > .el-button--primary > span").click()
    time.sleep(0.5)
    #add user 1
    pyautogui.press('F5')
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("100")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("张三")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(5) .el-input__inner").send_keys("TNA-test@tna.cn")
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button--primary > span").click()
    time.sleep(1)
    #add more box resources
    driver.find_element(By.CSS_SELECTOR, ".icon-add-offline").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-message-box__btns > .el-button--primary > span").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".icon-add-offline").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-message-box__btns > .el-button--primary > span").click()
    time.sleep(1)

driver = webdriver.Edge()
driver.implicitly_wait(10)

web_open_LAN2()
mode_choice_center()
center_set()
node_add_resource()
resource_add_Center()
resource_add_Resource()
resource_add_Resource2()
node_add_user()
user_add()
driver.close()
pyautogui.hotkey('ctrl', 'c')
exit()