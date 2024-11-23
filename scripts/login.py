import json
import logging
import time

from config.driver import driver
from config.logger import logger

from selenium.webdriver.common.by import By


# 弹出验证码确认窗口(已废弃，因为未掌握线程管理相关的知识，使用Tkinter会导致线程阻塞)
# def show_verification_check():
#     """弹出 Tkinter 窗口，要求用户确认图形验证码是否完成，并填写验证码"""
#     root = tk.Tk()
#     root.title("图形验证码确认")
#
#     # 设置窗口大小
#     root.geometry("300x150")
#
#     # 创建提示标签
#     label = tk.Label(root, text="请确认图形验证码已完成")
#     label.pack(pady=10)
#
#     # 创建勾选框
#     var = tk.BooleanVar()
#     checkbox = tk.Checkbutton(root, text="已完成验证码", variable=var)
#     checkbox.pack()
#
#     # 创建确认按钮
#     def on_confirm():
#         if var.get():  # 如果勾选了已完成
#             root.quit()  # 关闭窗口
#             logger.info(f"手动确认验证通过")
#         else:
#             messagebox.showwarning("警告", "请完成图形验证码后再继续！")
#
#     button = tk.Button(root, text="确认", command=on_confirm)
#     button.pack(pady=10)
#
#     root.mainloop()


# 通过json获取手机号(需要提前填写手机号到mobilephone.json文件中)
def load_user_data():
    # 读取 mobilephone.json
    with open("./mobilephone.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    username = data.get("username", "")
    password = data.get("password", "")


    # 检查是否读取到手机号
    if not username or not password:
        logger.error("JSON中缺少账户信息！")
        exit()
    else:
        return username, password


# 尝试通过手机登录的操作
def try_pwd_login():
    # 登录操作（根据实际页面元素调整）
    login_button = driver.find_element(By.CLASS_NAME, "header-login-entry")
    login_button.click()
    time.sleep(2)  # 等待弹窗加载
    username, password = load_user_data()

    try:
        # 找到账号输入框并填入用户名
        username_input = driver.find_element(By.XPATH, '//input[@placeholder="请输入账号"]')
        username_input.clear()
        username_input.send_keys(username)
        logging.info(f"账号 {username} 已填充到输入框中！")

        # 找到密码输入框并填入密码
        password_input = driver.find_element(By.XPATH, '//input[@placeholder="请输入密码"]')
        password_input.clear()
        password_input.send_keys(password)
        logging.info("密码已填充到输入框中！")
    except Exception as e:
        logging.error(f"填写登录表单时发生错误: {e}")

    # 完成后执行登录按钮
    login_button = driver.find_element(By.CLASS_NAME, "btn_primary")
    login_button.click()
    time.sleep(1)
    # 检查是否存在图形验证码
    while True:
        try:
            # 查找geetest_panel元素
            geetest_panel = driver.find_element(By.CLASS_NAME, "geetest_panel")

            # 获取display属性
            display_style = geetest_panel.value_of_css_property("display")

            if display_style == "block":
                # 继续等待500毫秒后再检查
                time.sleep(0.5)
            else:
                break  # 退出循环，继续执行下一步

        except Exception as e:
            logger.warning("检查图形验证码时发生错误：%s", e)
            break  # 退出循环

    logger.info("成功点击了‘登录’按钮！")
    time.sleep(1)
    get_user_info()

# 获取用户信息，若未登录，尝试通过手机号登录
def get_user_info():
    url = "https://api.bilibili.com/x/space/v2/myinfo?"

    # 打开 URL
    driver.get(url)
    time.sleep(3)  # 等待网页加载

    try:
        # 获取网页中的 JSON 数据
        page_source = driver.page_source
        start_index = page_source.find("{")  # 查找 JSON 数据的开始位置
        end_index = page_source.rfind("}")  # 查找 JSON 数据的结束位置
        json_data = page_source[start_index:end_index + 1]  # 提取 JSON 数据

        # 解析 JSON 数据
        data = json.loads(json_data)

        # 检查返回的 message
        message = data.get("message", "未知状态")
        if message == "未登录":
            logger.warning("用户未登录，将开始尝试登录。")
            # 在这里可以添加登录操作
            return
        elif message == "OK":
            # 提取需要的条目
            user_data = data.get("data", {}).get("profile", {})
            mid = user_data.get("mid", "未知UID")
            name = user_data.get("name", "未知昵称")
            level = user_data.get("level", "未知等级")
            text = user_data.get("vip", {}).get("label", {}).get("text", "未知会员等级")

            # 格式化输出结果
            logger.info(f"尊敬的{text}{name}用户，欢迎登录小破站，您的UID是{mid}，您的等级是{level}. 接下来可以正式开始测试了！")
            driver.back()
        else:
            logger.error(f"接口返回未预料的状态：{message}")
    except Exception as e:
        logger.error(f"获取用户信息时发生错误：{e}")



 # 弹出验证码确认窗口
# def show_verification_sms():
#     """弹出 Tkinter 窗口，要求用户确认图形验证码是否完成，并填写验证码"""
#     root = tk.Tk()
#     root.title("图形验证码确认")
#
#     # 设置窗口大小
#     root.geometry("300x200")
#
#     # 创建提示标签
#     label = tk.Label(root, text="请确认图形验证码已完成，填写验证码并点击确认")
#     label.pack(pady=10)
#
#     # 创建验证码输入框
#     captcha_label = tk.Label(root, text="请输入验证码：")
#     captcha_label.pack(pady=5)
#     captcha_entry = tk.Entry(root)
#     captcha_entry.pack(pady=5)
#
#     # 创建确认按钮
#     def on_confirm():
#         captcha_code = captcha_entry.get().strip()
#         if captcha_code:
#             # 将验证码传递到目标输入框
#             captcha_input = driver.find_element(By.XPATH, '//input[@placeholder="请输入验证码"]')
#             captcha_input.clear()
#             captcha_input.send_keys(captcha_code)
#             logger.info(f"验证码 {captcha_code} 已填充到输入框中！")
#             root.quit()  # 关闭窗口
#         else:
#             messagebox.showwarning("警告", "请输入验证码！")
#
#     button = tk.Button(root, text="确认", command=on_confirm)
#     button.pack(pady=10)
#
#     root.mainloop()