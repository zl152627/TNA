----- preparing to run python file -----
all files needed is in test2.8/Prepare-Tool/
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
git init:初始化仓库 
git add <file>:添加文件（到工作区）
    e.g. git add readme.md
git commit:提交更改（到库）
    e.g. git commit -m "add note"
git status:察看文件状态
    若暂无需要提交的更改:nothing to commit, working tree clean
git diff <file>:察看文件修改的内容
    e.g. git diff readme.md
git log:察看历史记录
git log --pretty=oneline:单行察看历史记录，会给出版本号（commit id）
git reset --hard HEAD^:回退到上一个版本
    HEAD^^:回退到上上一个版本
    HEAD~n:回退到往前第n个版本
git reset --hard <commit id>:恢复为指定版本，版本号不必写完
工作区（手动修改） ----- git add<file> ----- 暂存区 ----- git commit ----- 库 
git checkout -- <file>:撤销文件在工作区的修改，让文件回到最近一次git commit或git add时的状态
    e.g.git checkout -- readme.md
git restore <file>:撤销文件在工作区的修改
    e.g.git restore readme.md
git reset HEAD <file>:把暂存区的修改撤销掉
    e.g.git reset HEAD readme.md
git restore --staged <file>:把暂存区的修改撤销掉
    e.g.git reset HEAD readme.md
git rm <file>:删除库中的文件
    手动删除后，使用git rm <file>和git add <file>效果一样