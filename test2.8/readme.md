----- preparing to run python file -----
file massage: created at 2020.11.03 by zhanglei@tna.cn
funtion: test TNA-devices-v2.7+
prepare: selenium and pyautogui have been installed in this pc which is 1920x1080
way to install selenium: run "pip install selenium" in cmd after installing python
way to install pyautogui: run "pip install pyautogui" in cmd after installing python
version: demo version v0.1, just finish a little easy functions with very easy python kownledge
prepare WebDriver:
	MicrosoftWebDriver.exe为Micosoft-Edge-85.0.564.68 (官方内部版本，64位，基于 Chromium开源项目及其他开源软件)原生驱动
	该驱动为Selenium相关Python脚本使用Edge自动化测试的前提，存放在Python安装目录下：C:\User\[用户名]\AppData\Local\Programs\Python\Python38-32\

----- git easy use -----
git init：初始化仓库 
git add: 添加文件 e.g. git add readme.md
git commit: 提交更改 e.g. git commit -m "add note"
git status: 察看文件状态
	若暂无需要提交的更改：nothing to commit, working tree clean
git diff: 察看文件修改的内容 e.g. git diff readme.md
git log: 察看历史记录
git log --pretty=oneline: 单行察看历史记录，会给出版本号（commit id）
git reset --hard HEAD^:  回退到上一个版本
	HEAD^^: 回退到上上一个版本
	HEAD~n: 回退到往前第n个版本
git reset --hard [commit id]: 恢复为指定版本，版本号不必写完
