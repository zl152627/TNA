# -*- coding:utf-8 -*-
'''
file massage: created at 2020.10.22 by zhanglei@tna.cn
funtion: test TNA-devices-v2.7+
prepare1: selenium and pyautogui have been installed in this pc
prepare2: C:\Putty.exe and C:\iperf3\iperf3.exe
version: demo version v0.1, just finish a little easy functions with very easy python kownledge
'''

import os
import time
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Function_TNA_set(object):
    def __init__(self):
        self.CenterSet = Setup_Center()
        self.BOXSet = Setup_BOX()
        self.NodeSet = Setup_Node()
        self.AddNodesExample = Add_nodes_examples()
        self.AddResourcesExample = Add_resources_example()
        self.AddUsersExample = Add_users_example()
        self.Reset = Reset_devices()
        self.StandbySet = Setup_standby()
        self.Easytest = Easy_test()
        
    def select_run(self):
        os.system("cls")
        print('''
            ------------TNA-set v0.1--------------
            |      select a function num         |
            |      1.setup Center                |
            |      2.setup BOX                   |
            |      3.setup Node                  |
            |      4.add test-examples           |
            |      5.reset devices               |
            |      6.set standby devices         |
            |      7.devices easy test           |
            |      0.exit                        |
            --------------------------------------
            ''')
        select_input = input("input num:\n>")
        if select_input.isdigit():
            select_num = int(select_input)
        else:
            print("input a number from 0 to 7")
            time.sleep(1)
            self.select_run()
        
        if select_num == 1:
            print("-----setup Center-----")
            time.sleep(1)
            self.CenterSet.center_set()
            self.select_run()
        elif select_num == 2:
            print("-----setup BOX-----")
            time.sleep(1)
            self.BOXSet.BOX_set_run()
            self.select_run()
        elif select_num == 3:
            print("-----setup Node-----")
            self.NodeSet.Node_set_run()
            self.select_run()
        elif select_num == 4:
            print("-----add test-examples-----")
            print('''
            1.add node-examples
            2.add resource-examples
            3.add user-examples
            0.back to main menu
                ''')
            add_examples_input = input("input example num:\n>")
            if add_examples_input.isdigit() and 0 <= int(add_examples_input) <= 3:
                add_examples_num = int(add_examples_input)
            else:
                print("not from 0 to 3\nbacking to main menu...")
                time.sleep(0.5)
                self.select_run()
            if add_examples_num == 1:
                self.AddNodesExample.node_add_examples_run()
                print("add node-examples finished")
                time.sleep(1)
                self.select_run()
            elif add_examples_num == 2:
                self.AddResourcesExample.resource_add_examples_run()
                print("add resource-examples finished")
                time.sleep(1)
                self.select_run()
            elif add_examples_num == 3:
                self.AddUsersExample.user_add_example_run()
                print("add user-examples finished")
                time.sleep(1)
                self.select_run()
            else:
                self.select_run()
        elif select_num == 5:
            print("-----reset devices-----")
            self.Reset.way_choice()
            self.select_run()
        elif select_num == 6:
            print("-----set standby devices-----")
            self.StandbySet.standby_set_run()
            self.select_run()
        elif select_num == 7:
            print("-----devices easy test-----")
            #pyautogui.confirm returns "OK" or "Cancel"
            if pyautogui.confirm('用于寄出设备前的简要测试,若设备已配置请点击取消') == "OK":
                time.sleep(1)
                self.Easytest.easy_test_run()
            else:
                print("cancelling...")
                time.sleep(0.5)
            self.select_run()
        elif select_num == 0:
            print("exiting...")
            driver.quit()
            exit()
        else:
            print("input a number from 0 to 7")
            time.sleep(1)
            self.select_run()

class Setup_Center(object):
    def web_open_LAN2(self):
        driver.get("http://192.168.110.1/")
        driver.maximize_window()
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        time.sleep(1)

    def mode_choice_center(self):
        driver.find_element(By.CSS_SELECTOR, ".admin > .img").click()
        time.sleep(1)

    def center_net_set(self):
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys("北京笛卡尔盾科技有限公司")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("192.168.3.200/24")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("192.168.3.1")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-input__inner").send_keys("192.168.100.234/24")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(5) .el-input__inner").send_keys("192.168.100.101")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(6) .el-input__inner").send_keys("192.168.3.200:32749")
        driver.find_element(By.CSS_SELECTOR, ".right").click()
        driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        try:
            #WebDriverWait(driver, 12, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(5) .el-dialog__close"))).click()
            #弹窗一直存在于页面，只是被隐藏，显示等待不可用!
            time.sleep(4)
            driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(5) .el-dialog__close").click()
        except:
            pyautogui.press('tab', 2)
            pyautogui.press('enter')
            pyautogui.alert(text = "检查连线和网络", title = "配置失败", button = "继续运行")
        time.sleep(1)

    def resource_add_Center(self):
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
        driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
        driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys("Center-Route")
        driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys("192.168.101.101:8092")
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
        pyautogui.press('down', 3)
        pyautogui.press('enter')#全通
        driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
        time.sleep(1)
        #-------add Resource-Node-------
        pyautogui.press('F5')
        driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
        driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys("R-Node-C")
        driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys("172.31.128.12:8092")
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
        pyautogui.press('down', 3)
        pyautogui.press('enter')#全通
        driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
        time.sleep(1)
        pyautogui.press('F5')
        driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
        driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys("U-Node-C")
        driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys("172.31.128.14:8092")
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input-group__prepend .el-input__inner").click()
        pyautogui.press('down', 3)
        pyautogui.press('enter')#全通
        driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
        time.sleep(1)

    def node_add_resource(self):
        driver.get("http://192.168.110.1:8092/#/gateway/index")
        #driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) .submenu-title-noDropdown").click()
        time.sleep(1)
        #add Resource-Node
        driver.find_element(By.CSS_SELECTOR, ".el-button-group > .el-button:nth-child(1)").click()
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".name > .el-input__inner").send_keys("Resource-Node")
        driver.find_element(By.CSS_SELECTOR, "select:nth-child(1)").click()#省
        time.sleep(0.5)
        pyautogui.press('down', random.randint(1,34))
        pyautogui.press('enter')
        driver.find_element(By.CSS_SELECTOR, "select:nth-child(2)").click()#市
        time.sleep(0.5)
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
        time.sleep(0.5)
        pyautogui.press('down', random.randint(1,34))
        pyautogui.press('enter')
        driver.find_element(By.CSS_SELECTOR, "select:nth-child(2)").click()#市
        time.sleep(0.5)
        pyautogui.press('down',random.randint(1,10))
        pyautogui.press('enter')
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, ".el-button--success").click()
        time.sleep(0.5)#点击加号后框的元素名发生了变化，不要改动位置
        driver.find_element(By.CSS_SELECTOR, ".box:nth-child(2) .el-input__inner").send_keys("10.10.30.0/24")
        driver.find_element(By.CSS_SELECTOR, ".box:nth-child(3) .el-input__inner").send_keys("10.10.31.0/24")
        driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()#确定
        time.sleep(1)

    def node_add_user(self):
        driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) .submenu-title-noDropdown").click()
        time.sleep(1)
        #add User-Node
        driver.find_element(By.CSS_SELECTOR, ".el-button-group > .el-button:nth-child(1)").click()
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".name > .el-input__inner").send_keys("User-Node")
        driver.find_element(By.CSS_SELECTOR, "select:nth-child(1)").click()#省
        time.sleep(0.5)
        pyautogui.press('down', random.randint(1,34))
        pyautogui.press('enter')
        driver.find_element(By.CSS_SELECTOR, "select:nth-child(2)").click()#市
        time.sleep(0.5)
        pyautogui.press('down',random.randint(1,10))
        pyautogui.press('enter')
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, ".el-radio:nth-child(2) > .el-radio__label").click()#用户模式
        driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".app-name").click()#添加资源
        time.sleep(0.5)
        for resource_num in range(1,11):
            try:
                driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(%d) > .el-checkbox__label" %resource_num).click()
            except:
                pyautogui.press('tab', 2)
                pyautogui.press('enter')
                break
        time.sleep(1)

    def resource_add_Resource(self):
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

    def resource_add_Resource2(self):
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

    def user_add(self):
        driver.get("http://192.168.110.1:8092/#/main/index")
        #driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > a > .submenu-title-noDropdown").click()
        time.sleep(1)
        #add user zl
        driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("1")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("1")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-input__inner").send_keys("15010821222")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(5) .el-input__inner").send_keys("zhanglei@tna.cn")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(6) .el-input__inner").send_keys("昆仑-华夏")
        #add resources
        for resource_num in range(1,11):
            try:
                driver.find_element(By.CSS_SELECTOR, ".el-checkbox:nth-child(%d) .el-checkbox__inner" %resource_num).click()
            except:
                driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button--primary > span").click()#确定
                break
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
    
    def center_set(self):
        self.web_open_LAN2()
        self.mode_choice_center()
        self.center_net_set()
        self.node_add_resource()
        self.resource_add_Center()
        self.resource_add_Resource()
        self.resource_add_Resource2()
        self.node_add_user()
        self.user_add()
        driver.minimize_window()

class Setup_BOX(object):
    def web_open_BOX(self):
        driver.get("http://www.a.com/")
        driver.maximize_window()
        time.sleep(1)
        
    def BOX_set(self):
        element_BOX_init_Login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner")))
        element_BOX_init_Login.send_keys("123456")
        #driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-input__inner").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, "#login > span").click()
        pyautogui.alert('BOX 连接有线或WIFI后点击「确定」')
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1.5)
        driver.find_element(By.CSS_SELECTOR, ".next > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys("笛卡尔盾测试")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("1")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("1")
        pyautogui.press('enter')
        time.sleep(6)#init step2 finished
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)#init step3 finished
        
    def BOX_set_run(self):
        self.web_open_BOX()
        self.BOX_set()
        driver.minimize_window()
        print("BOX set finsihed")
        time.sleep(1)

class Setup_Node(object):
    def web_open_LAN2(self):
        driver.get("http://192.168.110.1/")
        driver.maximize_window()
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        time.sleep(1)
    def mode_choice_node(self):
        driver.find_element(By.CSS_SELECTOR, ".gateway > .img").click()
        time.sleep(1)

    def Node_Resource_set(self, outer_net, inner_net, innner_gateway):
        pyautogui.press('Tab')
        pyautogui.typewrite(outer_net)
        time.sleep(0.2)
        pyautogui.press('Tab')
        pyautogui.typewrite('192.168.3.1')
        time.sleep(0.2)
        pyautogui.press('Tab')
        pyautogui.typewrite('192.168.3.200:32749')
        time.sleep(0.2)
        driver.find_element(By.CSS_SELECTOR, ".lan > .el-button > span").click()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, ".next > span").click()
        time.sleep(1)
        pyautogui.alert("1.输入口令\n2.如图将网线从LAN1口更换到WAN口上\n3.点击确定")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".wan > .el-button > span").click()
        time.sleep(9)
        driver.find_element(By.CSS_SELECTOR, ".next > span").click()
        time.sleep(1)
        pyautogui.press('Tab')
        pyautogui.typewrite(inner_net)
        time.sleep(0.2)
        pyautogui.press('Tab')
        pyautogui.typewrite(innner_gateway)
        time.sleep(0.2)
        driver.find_element(By.CSS_SELECTOR, ".inner > .el-button > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".next > span").click()
    def Node_User_set(self, outer_net, inner_net):
        pyautogui.press('Tab')
        pyautogui.typewrite(outer_net)
        time.sleep(0.2)
        pyautogui.press('Tab')
        pyautogui.typewrite('192.168.3.1')
        time.sleep(0.2)
        pyautogui.press('Tab')
        pyautogui.typewrite('192.168.3.200:32749')
        time.sleep(0.2)
        driver.find_element(By.CSS_SELECTOR, ".lan > .el-button > span").click()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, ".next > span").click()
        time.sleep(1)
        pyautogui.alert("1.输入口令\n2.如图将网线从LAN1口更换到WAN口上")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".wan > .el-button > span").click()
        time.sleep(9)
        driver.find_element(By.CSS_SELECTOR, ".next > span").click()
        time.sleep(1)
        pyautogui.press('Tab')
        pyautogui.typewrite(inner_net)
        time.sleep(0.2)
        driver.find_element(By.CSS_SELECTOR, ".inner > .el-button > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".next > span").click()
    
    def Node_set_run(self):
        way_net_input = input("select net for node\n1.resource_node:192.168.3.201\n2.user_node:192.168.3.202\n3.resource_node2:192.168.3.203\n>")
        time.sleep(1)
        if way_net_input.isdigit() and 1 <= int(way_net_input) <= 3:
            way_net_num = int(way_net_input)
        else:
            self.choice_way()
            
        pyautogui.alert("1.将互联网连接至待配置设备LAN1口\n2.将本电脑连接至待配置设备LAN2口\n3.切换至英式键盘")
        self.web_open_LAN2()
        self.mode_choice_node()
                    
        if way_net_num == 1:
            self.Node_Resource_set("192.168.3.201/24", "10.10.10.1/24", "10.10.10.2")
        elif way_net_num == 2:
            self.Node_User_set("192.168.3.202/24", "10.10.20.1/24")
        elif way_net_num == 3:
            self.Node_Resource_set("192.168.3.203/24", "10.10.30.1/24", "10.10.30.2")
        else:
            self.Node_set_run()
        print("node set finished")
        time.sleep(1)
        driver.minimize_window()
    
class Add_nodes_examples(object):
    def web_open_LAN2(self):
        driver.maximize_window()
        driver.get("http://192.168.110.1:8092/#/gateway/index")
        try:
            driver.find_element(By.NAME, "username").send_keys("admin")
            driver.find_element(By.NAME, "password").send_keys("123456")
            driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)
    def web_open_LAN1(self):
        driver.get("http://192.168.100.234:8092/#/gateway/index")
        driver.maximize_window()
        try:
            driver.find_element(By.NAME, "username").send_keys("admin")
            driver.find_element(By.NAME, "password").send_keys("123456")
            driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)
    def choice_way(self):
        way_openWeb_input = input("choice 1 or 2\n1:Control center via 192.168.110.1\n2:Control center via 192.168.100.234\n>")
        if way_openWeb_input.isdigit() and 1 <= int(way_openWeb_input) <= 2:
            way_openWeb_num = int(way_openWeb_input)
        else:
            self.choice_way()
        if way_openWeb_num == 1:
            self.web_open_LAN2()
        elif way_openWeb_num == 2:
            self.web_open_LAN1()
        else:
            self.choice_way()
            
    def node_add_resource(self, resource_node_name, resource_node_net):
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
        
    def node_add_user(self, user_node_name):
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
    
    def node_add_examples_run(self):
        dict_resource_node = {
            'Resc-Node': '10.10.12.0/24',
            '一二三四五六七八九十一二三四五六七八九廿': '10.10.13.0/24',
            '@#$%资源 网关@#$^': '10.10.14.0/24'
            }
        list_user_node_name = ['user-Node1', '1237894', '一二三四五六七八九十一二三四五六七八九廿', '@#$ 用户 网 关1%@#$^']
        self.choice_way()
        for resource_node_name, resource_node_net in list(dict_resource_node.items()):
            self.node_add_resource(resource_node_name, resource_node_net)
        for user_node_name in list_user_node_name:
            self.node_add_user(user_node_name)
        driver.minimize_window()

class Add_resources_example(object):
    def web_open_LAN2(self):
        driver.get("http://192.168.110.1:8092/#/policy/index")
        driver.maximize_window()
        try:
            driver.find_element(By.NAME, "username").send_keys("admin")
            driver.find_element(By.NAME, "password").send_keys("123456")
            driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > a > .submenu-title-noDropdown > span").click()
        time.sleep(1)
    def web_open_LAN1(self):
        driver.get("http://192.168.100.234:8092/#/policy/index")
        driver.maximize_window()
        try:
            driver.find_element(By.NAME, "username").send_keys("admin")
            driver.find_element(By.NAME, "password").send_keys("123456")
            driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)
    def choice_way(self):
        way_openWeb_input = input("choice 1 or 2\n1:Control center via 192.168.110.1\n2:Control center via 192.168.100.234\n>")
        if way_openWeb_input.isdigit() and 1<= int(way_openWeb_input) <= 2:
            way_openWeb_num = int(way_openWeb_input)
        else:
            self.choice_way()
        if way_openWeb_num == 1:
            self.web_open_LAN2()
        elif way_openWeb_num == 2:
            self.web_open_LAN1()
        else:
            self.choice_way()

    def resource_add_Center_TCP(self, center_name, center_net):
        pyautogui.press('F5')
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1) .op > use").click()
        driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys(center_name)
        driver.find_element(By.CSS_SELECTOR, ".box-item > .el-input__inner").send_keys(center_net)
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary").click()
        time.sleep(1)

    def resource_add_Center_UDP(self, center_name, center_net):
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

    def resource_add_Center_ALL(self, center_name, center_net):
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

    def resource_add_Node_TCP(self, resource_name, resource_net):
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

    def resource_add_Node_ALL(self, resource_name, resource_net):
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
        
    def resource_add_examples_run(self):
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

        self.choice_way()
        for center_name, center_net in dict_center.items():
            self.resource_add_Center_ALL(center_name, center_net)
        for resource_name, resource_net in dict_node.items():
            self.resource_add_Node_ALL(resource_name, resource_net)
        self.resource_add_Center_UDP('UDP#￥… a中 s23管理…6', '192.168.100.234:8888')
        self.resource_add_Node_UDP('UDP端口号10.1:8888', '10.10.10.1:8888')
        driver.minimize_window()

class Add_users_example(object):
    def web_open_LAN2(self):
        driver.get("http://192.168.110.1:8092/#/main/index")
        driver.maximize_window()
        try:
            driver.find_element(By.NAME, "username").send_keys("admin")
            driver.find_element(By.NAME, "password").send_keys("123456")
            driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)    
    def web_open_LAN1(self):
        driver.get("http://192.168.100.234:8092/#/main/index")
        driver.maximize_window()
        try:
            driver.find_element(By.NAME, "username").send_keys("admin")
            driver.find_element(By.NAME, "password").send_keys("123456")
            driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)
    def choice_way(self):
        way_openWeb_input = input("choice 1 or 2\n1:Control center via 192.168.110.1\n2:Control center via 192.168.100.234\n>")
        if way_openWeb_input.isdigit() and 1<= int(way_openWeb_input) <= 2:
            way_openWeb_num = int(way_openWeb_input)
        else:
            self.choice_way()
        if way_openWeb_num == 1:
            self.web_open_LAN2()
        elif way_openWeb_num == 2:
            self.web_open_LAN1()
        else:
            self.choice_way()
    
    def user_add(self, name, code):
        pyautogui.press('F5')
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys(code)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys(name)
        driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button--primary > span").click()#确定
        
    def user_add_example_run(self):
        dict_user = {
            '李 四':101,
            '王  五':102,
            '诸葛猫蛋儿':103,
            '欧阳狗剩儿':104,
            '#@$DAF': 105,
            'sdk faj 1f5sd':106 
            }
        self.choice_way()
        for name, code in list(dict_user.items()):
            self.user_add(name, code)
        driver.minimize_window()

class Reset_devices(object):
    def web_open_LAN2(self):
        driver.get("http://192.168.110.1/#/advanced/index")
        driver.maximize_window()
        pyautogui.press('F5')
        try:
            driver.find_element(By.NAME, "username").send_keys("admin")
            driver.find_element(By.NAME, "password").send_keys("123456")
            driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)
        
    def gateway_reset(self):
        driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".el-input__inner").click()
        driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("RESET")
        driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys(Keys.ENTER)
        time.sleep(2)

    def web_open_BOX(self):
        driver.get("http://www.a.com/")
        driver.maximize_window()
        pyautogui.press('F5')
        time.sleep(2)

    def BOX_reset(self):
        '''
        pyautogui.moveTo(30, 150, 1)
        pyautogui.click()
        pyautogui.moveTo(30, 270, 1)
        pyautogui.click()
        pyautogui.moveTo(888, 380, 1)
        pyautogui.click()
        pyautogui.typewrite('7758521')
        pyautogui.moveTo(1030, 440, 1)
        pyautogui.click()
        '''
        #pyautogui.hotkey('shift', 'tab', 2)
        #pyautogui.press('enter')
        driver.find_element(By.CSS_SELECTOR, ".el-dropdown:nth-child(1) .set").click()
        time.sleep(0.5)
        pyautogui.press('down', 3)
        pyautogui.press('enter')
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys("16349527")
        pyautogui.press('tab', 2)
        pyautogui.press('enter')
        time.sleep(2)

    def way_choice(self):
        way_choice_input = input("choice 1 or 2:\n1: reset BOX\n2: reset Gateway\n0:exit\n>")
        if way_choice_input.isdigit():
            way_choice_num = int(way_choice_input)
        else:
            self.way_choice()
        if way_choice_num == 1:
            self.web_open_BOX()
            self.BOX_reset()
        elif way_choice_num == 2:
            self.web_open_LAN2()
            self.gateway_reset()
        elif way_choice_num == 0:
            print("exiting reset-devices...")
            time.sleep(0.5)
        else:
            self.way_choice()
        driver.minimize_window()
        print("device reset finished")
        time.sleep(1)

class Setup_standby(object):
    def web_open_LAN2(self):
        driver.get("http://192.168.110.1:8092/#/config/standby")
        driver.maximize_window()
        try:
            driver.find_element(By.NAME, "username").send_keys("admin")
            driver.find_element(By.NAME, "password").send_keys("123456")
            driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)
        
    def center_standby(self):
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("192.168.100.233/24")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("192.168.100.232/24")
        driver.find_element(By.CSS_SELECTOR, ".right:nth-child(2) > span").click()
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(9) > span").click()
        time.sleep(1)

    def resource_node_standby(self):
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("10.10.10.233/24")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("10.10.10.232/24")
        driver.find_element(By.CSS_SELECTOR, ".right:nth-child(2) > span").click()
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(9) > span").click()
        time.sleep(1)
        
    def user_node_standby(self):
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("10.10.20.233/24")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("10.10.20.232/24")
        driver.find_element(By.CSS_SELECTOR, ".right:nth-child(2) > span").click()
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(9) > span").click()
        time.sleep(1)
    
    def standby_set_run(self):
        way_devices_input = input("select devices\n1.center\n2.resource-node\n3.user-node\n>")
        time.sleep(1)
        if way_devices_input.isdigit() and 1 <= int(way_devices_input) <= 3:
            way_devices_num = int(way_devices_input)
        else:
            self.standby_set_run()
            
        pyautogui.alert('注意是否只有一台空白设备')
        self.web_open_LAN2()
        if way_devices_num == 1:
            self.center_standby()
        elif way_devices_num == 2:
            self.resource_node_standby()
        elif way_devices_num == 3:
            self.user_node_standby()
        else:
            self.standby_set_run()
        driver.minimize_window()
        print("set standby device finished")
        time.sleep(1)

class Easy_test(object):
    def web_open_LAN2(self):
        driver.get("http://192.168.110.1/")
        driver.maximize_window()
        pyautogui.press('F5')
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        time.sleep(1)
   
    def center_set(self):
        driver.find_element(By.CSS_SELECTOR, ".admin > .img").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys("cartesianshield")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("192.168.3.205/24")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("192.168.3.1")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-input__inner").send_keys("192.168.100.235/24")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(5) .el-input__inner").send_keys("192.168.100.101")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(6) .el-input__inner").send_keys("192.168.3.205:32749")
        driver.find_element(By.CSS_SELECTOR, ".right").click()
        driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        time.sleep(5)
        net_set_finish = driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(5) .el-dialog__close")
        if net_set_finish:
            net_set_finish.click()
        else:
            driver.find_element(By.CSS_SELECTOR, ".el-button--small:nth-child(1) > span").click()
            #driver.find_element(By.CSS_SELECTOR, ".el-message-box__close").click()
        time.sleep(1)
        driver.get("http://192.168.110.1:8092/#/main/index")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("1")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("1")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(5) .el-input__inner").send_keys("TNA-test@tna.cn")
        driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button--primary > span").click()
        time.sleep(1)

    def route_check(self):
        os.startfile('C:\putty.exe')
        time.sleep(0.5)
        pyautogui.typewrite('192.168.110.1')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('tna')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('123456')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('ip route show table 5')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('ip addr show dev enp6s0')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('ip addr show dev enp1s0')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.alert('若网址信息无误且设备LED灯闪烁正常则点击「确定」')
        time.sleep(1)
        pyautogui.typewrite('exit')
        pyautogui.press('enter')
        time.sleep(1)

    def reboot_BOX(self):
        os.startfile('C:\putty.exe')
        time.sleep(0.5)
        pyautogui.typewrite('192.168.231.193')
        pyautogui.press('tab', 2)
        pyautogui.press('left', 2)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('root')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('admin12345')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('reboot')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        pyautogui.press('enter')
        time.sleep(1)

    def reset_BOX(self):
        driver.get("http://www.a.com/")
        driver.maximize_window()
        pyautogui.press('F5')
        time.sleep(1)
        
        driver.find_element(By.CSS_SELECTOR, ".el-dropdown:nth-child(1) .set").click()
        time.sleep(0.5)
        pyautogui.press('down', 3)
        pyautogui.press('enter')
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys("16349527")
        pyautogui.press('tab', 2)
        pyautogui.press('enter')
        time.sleep(2)

    def set_BOX(self):
        try:
            driver.get("http://www.a.com/")
        except:
            time.sleep(3)
            driver.get("http://www.a.com/")
        driver.maximize_window()
        time.sleep(1)
        element_BOX_init_Login = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner")))
        element_BOX_init_Login.send_keys("123456")
        #driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-input__inner").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, "#login > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".next > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys("192.168.3.205:32749")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("1")
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("1")
        pyautogui.press('enter')
        time.sleep(6)#init step2 finished
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)#init step3 finished

    def center_reset(self):
        driver.get("http://192.168.110.1/#/advanced/index")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button > span").click()
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".el-input__inner").click()
        driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("RESET")
        driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys(Keys.ENTER)
        time.sleep(1)

    def easy_test_run(self):
        pyautogui.alert('1.设置输入法为美式键盘\n2.将BOX连接有线后接入电脑\n3设备WAN口连接路由器')
        self.web_open_LAN2()
        self.center_set()
        self.route_check()
        self.reset_BOX()
        self.reboot_BOX()
        time.sleep(12)
        self.set_BOX()
        self.center_reset()
        self.reset_BOX()
        driver.minimize_window()

class Function_speedtest(object):
    def __init__(self):
        self.fun_b2c = b2c()
        self.fun_b2r = b2r()
        self.fun_b2c = u2c()
        self.fun_b2r = u2r()
        self.fun_b2c = r2c()
        self.fun_b2r = r2r()
    
    def select_run(self):
        os.system("cls")
        print('''
            ----------TCP-speedtest v0.1---------
            |      select a function num        |
            |      1.b2c                        |
            |      2.b2r                        |
            |      3.u2c                        |
            |      4.u2r                        |
            |      5.r2c                        |
            |      6.r2r                        |
            |      0.exit                       |
            -------------------------------------
            ''')
        select_input = input("input num:\n>")
        if select_input.isdigit():
            select_num = int(select_input)
        else:
            print("input a number from 0 to 6")
            time.sleep(1)
            self.select_run()
            
        if select_num == 1:
            print("-----speedtest between BOX and resource of Center-----")
            time.sleep(1)
            self.fun_b2c.b2c_run()
            self.select_run()
        elif select_num == 2:
            print("-----speedtest between BOX and resource of Resc-Node-----")
            time.sleep(1)
            self.fun_b2r.b2r_run()
            self.select_run()
        elif select_num == 3:
            print("-----speedtest between User-Node and resource of Center-----")
            time.sleep(1)
            self.fun_u2c.u2c_run()
            self.select_run()
        elif select_num == 4:
            print("-----speedtest between User-Node and resource of Resc-Node-----")
            time.sleep(1)
            self.fun_u2r.u2r_run()
            self.select_run()
        elif select_num == 5:
            print("-----speedtest between resource of Resc-Node and resource of Resc-Node-----")
            time.sleep(1)
            self.fun_r2c.r2c_run()
            self.select_run()
        elif select_num == 6:
            print("-----speedtest between two resources of Resc-Node-----")
            time.sleep(1)
            self.fun_r2r.r2r_run()
            self.select_run()
        elif select_num == 0:
            print("exiting...")
            exit()
        else:
            print("input a number from 0 to 6")
            time.sleep(1)
            self.select_run()
  
class b2c(object):
    def Iperf_log_b2c(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('192.168.101.101')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('iperf3 -s -f m > ./speedtest/b2c.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def CPU_log_b2c_ctop(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('192.168.100.234')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/b2c-ctop.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
        
    def cmd_iperf(self):
        os.startfile('cmd.exe')
        time.sleep(1)
        pyautogui.typewrite('cd /d C:\iperf3')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 800 -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 1k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 1.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 2k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 2.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 3k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 3.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 4k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 6k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 8k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 10k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        time.sleep(10)
        pyautogui.alert('测试完成，日志保存在Center设备、路由设备、用户Node设备的speedtest文件夹内，下次运行本测试日志将被覆盖')
        time.sleep(0.1)
        
    def close_window(self):
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)

    def b2c_run(self):
        pyautogui.alert('该脚本只使用一台电脑，同时使用作为路由功能的TNA设备，对BOX与Center下属资源TCP速率进行测试')
        pyautogui.alert('点击确定后测试开始，预计65分钟后完成，以防干扰建议期间不要进行其他测试。完成后会有提示')
        self.Iperf_log_b2c()
        self.CPU_log_b2c_ctop()
        self.cmd_iperf()
        self.close_window()

class b2r(object):
    def Iperf_log_b2r(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('10.10.11.1')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('iperf3 -s -f m > ./speedtest/b2r.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def CPU_log_b2r_ctop(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('192.168.100.234')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/b2r-ctop.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def CPU_log_b2r_rtop(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('10.10.10.1')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/b2r-rtop.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)   
       
    def cmd_iperf(self):
        os.startfile('cmd.exe')
        time.sleep(1)
        pyautogui.typewrite('cd /d C:\iperf3')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 800 -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 1k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 1.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 2k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 2.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 3k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 3.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 4k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 6k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 8k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 10k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        time.sleep(10)
        pyautogui.alert('测试完成，日志保存在Center设备、资源Node设备、路由设备的speedtest文件夹内，下次运行本测试日志将被覆盖')
        time.sleep(0.1)
        
    def close_window(self):
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)

    def b2r_run(self):
        pyautogui.alert('该脚本只使用一台电脑，同时使用作为路由功能的TNA设备，对BOX与资源Node下属资源TCP速率进行测试')
        pyautogui.alert('点击确定后测试开始，预计65分钟后完成，以防干扰建议期间不要进行其他测试。完成后会有提示')
        self.Iperf_log_b2r()
        self.CPU_log_b2r_ctop()
        self.CPU_log_b2r_rtop()
        self.cmd_iperf()
        self.close_window()

class u2c(object):
    def Iperf_log_u2c(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('192.168.101.101')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('iperf3 -s -f m > ./speedtest/u2c.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def CPU_log_u2c_ctop(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('192.168.100.234')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/u2c-ctop.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
        
    def CPU_log_u2c_utop(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('10.10.20.1')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/u2c-utop.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)   
        
    def cmd_iperf(self):
        os.startfile('cmd.exe')
        time.sleep(1)
        #先确认电脑中iperf3.exe的位置
        pyautogui.typewrite('cd /d C:\iperf3')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 800 -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 1k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 1.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 2k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 2.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 3k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 3.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 4k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 6k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 8k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.101.101 -b 1000M -l 10k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        time.sleep(10)
        pyautogui.alert('测试完成，日志保存在Center设备、路由设备、用户Node设备的speedtest文件夹内，下次运行本测试日志将被覆盖')
        time.sleep(0.1)
        
    def close_window(self):
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)

    def u2c_run(self):
        pyautogui.alert('该脚本只使用一台电脑，同时使用作为路由功能的TNA设备，对用户Node与Center下属资源TCP速率进行测试')
        pyautogui.alert('本机为用户Node上位机，本机网址设置为10.10.20.101/24,网关10.10.20.1,禁用DELL带电脑进行测试')
        pyautogui.alert('点击确定后测试开始，预计65分钟后完成，以防干扰建议期间不要进行其他测试。完成后会有提示')
        self.Iperf_log_u2c()
        self.CPU_log_u2c_ctop()
        self.CPU_log_u2c_utop()
        self.cmd_iperf()
        self.close_window()

class u2r(object):
    def Iperf_log_u2r(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('10.10.11.1')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('iperf3 -s -f m > ./speedtest/u2r.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def CPU_log_u2r_ctop(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('192.168.100.234')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/u2r-ctop.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def CPU_log_u2r_utop(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('10.10.20.1')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/u2r-utop.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def CPU_log_u2r_rtop(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('10.10.10.1')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/u2r-rtop.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)   
       
    def cmd_iperf(self):
        os.startfile('cmd.exe')
        time.sleep(1)
        #先确认电脑中iperf3.exe的位置
        pyautogui.typewrite('cd /d C:\iperf3')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 800 -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 1k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 1.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 2k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 2.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 3k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 3.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 4k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 6k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 8k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.11.1 -b 1000M -l 10k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        time.sleep(10)
        pyautogui.alert('测试完成，日志保存在Center设备、用户Node设备、资源Node设备、路由设备的speedtest文件夹内，下次运行本测试日志将被覆盖')
        time.sleep(0.1)
        
    def close_window(self):
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)

    def u2r_run(self):
        pyautogui.alert('该脚本只使用一台电脑，同时使用作为路由功能的TNA设备，对用户Node与资源Node下属资源TCP速率进行测试')
        pyautogui.alert('本机为用户Node上位机，本机网址设置为10.10.20.101/24,网关10.10.20.1,禁用DELL带电脑进行测试')
        pyautogui.alert('点击确定后测试开始，预计65分钟后完成，以防干扰建议期间不要进行其他测试。完成后会有提示')
        self.Iperf_log_u2r()
        self.CPU_log_u2r_ctop()
        self.CPU_log_u2r_utop()
        self.CPU_log_u2r_rtop()
        self.cmd_iperf()
        self.close_window()

class r2c(object):
    def Iperf_log_r2c(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('192.168.100.101')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('iperf3 -s -f m > ./speedtest/r2c.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def CPU_log_r2c_ctop(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('192.168.100.101')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('ssh tna@192.168.100.234')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/r2c-ctop.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def CPU_log_r2c_rtop(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('10.10.10.1')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/r2c-rtop.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def cmd_iperf(self):
        os.startfile('cmd.exe')
        time.sleep(1)
        #先确认电脑中iperf3.exe的位置
        pyautogui.typewrite('cd /d C:\iperf3')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 800 -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 1k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 1.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 2k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 2.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 3k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 3.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 4k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 6k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 8k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 192.168.100.101 -b 1000M -l 10k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        time.sleep(10)
        pyautogui.alert('测试完成，日志保存在Center的路由设备的speedtest文件夹内，下次运行本测试日志将被覆盖')
        time.sleep(0.1)
        
    def close_window(self):
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)

    def r2c_run(self):
        pyautogui.alert('该脚本只使用一台电脑，同时使用作为路由功能的TNA设备，对资源Node下属资源与Center下属资源TCP速率进行测试')
        pyautogui.alert('本机为资源Node1上位机，本机网址设置为10.10.10.101/24,网关10.10.10.1,禁用DELL带电脑进行测试')
        pyautogui.alert('点击确定后测试开始，预计65分钟后完成，以防干扰建议期间不要进行其他测试。完成后会有提示')
        self.Iperf_log_r2c()
        self.CPU_log_r2c_rtop()
        self.CPU_log_r2c_ctop()
        self.cmd_iperf()
        self.close_window()

class r2r(object):
    def Iperf_log_r2r(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('10.10.30.2')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('iperf3 -s -f m > ./speedtest/r2r.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def CPU_log_r2r_ctop(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('192.168.100.101')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('ssh tna@192.168.100.234')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/r2r-ctop.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    
    def CPU_log_r2r_r1top(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('10.10.10.1')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/r2r-r1top.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    def CPU_log_r2r_r2top(self):
        os.startfile('C:\putty.exe')
        time.sleep(1)
        pyautogui.typewrite('10.10.30.2')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('tna')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('ssh tna@10.10.30.1')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('123456')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('top -b -d 10 -n 390 | grep "tna_main_proxy" > ./speedtest/r2r-r2top.log')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)   

    def cmd_iperf(self):
        os.startfile('cmd.exe')
        time.sleep(1)
        #先确认电脑中iperf3.exe的位置
        pyautogui.typewrite('cd /d C:\iperf3')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 800 -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 1k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 1.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 2k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 2.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 3k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 3.5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 4k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 5k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 6k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 8k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        pyautogui.typewrite('iperf3.exe -c 10.10.30.2 -b 1000M -l 10k -t 300')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(320)
        time.sleep(60)
        pyautogui.alert('测试完成，日志保存在Center设备、资源Node1设备、资源Node2设备、路由设备的speedtest文件夹内，下次运行本测试日志将被覆盖')
        time.sleep(0.1)
        
    def close_window(self):
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('exit')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)

    def r2r_run(self):
        pyautogui.alert('该脚本只使用一台电脑，同时使用作为路由功能的TNA设备，对两台资源Node下属资源TCP速率进行测试')
        pyautogui.alert('本机为资源Node1上位机，本机网址设置为10.10.10.101/24,网关10.10.10.1,禁用DELL带电脑进行测试')
        pyautogui.alert('点击确定后测试开始，预计65分钟后完成，以防干扰建议期间不要进行其他测试。完成后会有提示')
        self.Iperf_log_r2r()
        self.CPU_log_r2r_ctop()
        self.CPU_log_r2r_r1top()
        self.CPU_log_r2r_r2top()
        self.CPU_log_r2r_ctop()
        self.cmd_iperf()
        self.close_window()

os.system("cls")
print(r'''-----运行要求-----
    1.需在本电脑安装python3，默认路径即可
    2.安装python后依次在命令行窗口执行：
        pip install selenium
        pip install pyautogui
    3.脚本控制的浏览器为Edge-Chromium版，需将其原生驱动MicrosoftWebDriver.exe复制到Python安装目录下：
        C:\User[用户名]\AppData\Local\Programs\Python\Python38-32\ （此为默认安装路径）
    4.将PuTTY.exe与iperf3文件夹复制到C:\目录下（其中iperf3为测速必需）
        ''')
function_choice_input = input("select main function:\n1:TNA-set\n2:TCP-speedtest\n>")
if function_choice_input.isdigit() and int(function_choice_input) == 2:
    fun_TCP_speedtest = Function_speedtest()
    fun_TCP_speedtest.select_run()
else:
    pyautogui.FAILSAFE = True #mouse poiter at (0,0) to stop pyautogui
    driver = webdriver.Edge()
    driver.minimize_window()
    driver.implicitly_wait(3)
    fun_TNA_set = Function_TNA_set()
    fun_TNA_set.select_run()