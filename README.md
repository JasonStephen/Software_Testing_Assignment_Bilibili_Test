# README | 关于我们

![](./img/card.png)

## 一、我们的项目是什么？
我们的项目主要针对Bilibili网站的一些功能进行测试的测试脚本，以Python与Selenium为主的测试脚本。旨在测试一些网站的基本功能。

## 二、我的做这个项目的目的是什么？
首先除了学业目的外，这个项目也是对于Selenium扩展功能的一个探索。因为Selenium强大的自动化能力，我们可以做很多有趣的事情。除此之外由我总负责项目，我也尝试了项目封包的尝试，可以自动化部署到任何地方。

## 三、我们实现了什么功能？
### 1. 基础功能
- 自动登录（读取json中的账号密码进行自动填入登录）

### 2. 选择测试功能
通过tkinter实现复选框，可以选择4个测试项目的任意项，可重复测试已测试项目。

### 3. 测试项功能
- **a. 搜索功能**：搜索用户，查看用户个人主页
- **b. 检索top10热门**：选择最热门词条搜索
- **c. 检索代表作**：分析代表作播放最高的作品，提取并跳转URL，三连功能(长按控件)
- **d. 关注/取消关注功能**

## 四、如何使用？
您可以去 [GitHub](https://github.com/JasonStephen/Software_Testing_Assignment_Bilibili_Test/tree/master) 获取我们的项目。(需要手动搭建虚拟环境&安装依赖)

也可以通过我们的自动部署脚本部署项目(请先运行`RUN THIS FIRST.bat`进行一键部署，不再需要手动搭建虚拟环境以及安装依赖)。

自行配置`mobilephone.json`，在登录环节需要使用（否则无法运行项目）。

配置完成后请使用`run.bat`运行项目（`run.bat`会在检查`mobilephone.json`是否更改过后，自动进入虚拟环境运行`main.py`）。

## 五、其他
您可以通过我的[GitHub个人主页](https://github.com/JasonStephen) 获取更多我的项目，感谢你的支持，也欢迎参考。



----

## 1. What is our project?
Our project is a testing script aimed at some features of the Bilibili website, primarily using Python and Selenium. The goal is to test basic website functionalities.

## 2. What is the purpose of doing this project?
In addition to academic purposes, this project is also an exploration of Selenium's extended features. With Selenium's powerful automation capabilities, we can do many interesting things. Additionally, as I am in charge of the project, I also attempted to package the project, making it possible to automate the deployment anywhere.

## 3. What features have we implemented?
### 3.1. Basic Features
- Auto login (automatically fills in the login information by reading the account and password from a JSON file).

### 3.2. Feature Selection
Using tkinter, we implemented checkboxes where you can choose from four test items. You can repeatedly test the already tested items.

### 3.3. Test Features
- **a. Search Function**: Search for users and view their personal pages.
- **b. Retrieve Top 10 Hot Topics**: Select the most popular entry and search for it.
- **c. Retrieve Representative Works**: Analyze the works with the highest views, extract and jump to the URL, and three-click function (long-press the control).
- **d. Follow/Unfollow Function**

## 4. How to use it?
You can go to [GitHub](https://github.com/JasonStephen/Software_Testing_Assignment_Bilibili_Test/tree/master) to get our project. (Manual virtual environment setup and dependency installation required)

Alternatively, you can deploy the project using our auto-deployment script (run `RUN THIS FIRST.bat` to deploy it with one click, no need to manually set up the virtual environment or install dependencies).

Configure `mobilephone.json`, as it is required during the login step (otherwise, the project won't run).

After configuration, please run `run.bat` (it will check if `mobilephone.json` has been modified, then automatically enter the virtual environment and run `main.py`).

## 5. Other
You can find more of my projects on my [GitHub profile](https://github.com/JasonStephen). Thank you for your support, and feel free to refer to them.