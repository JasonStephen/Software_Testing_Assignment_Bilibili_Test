from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import threading

# 定义四个网站的URL
urls = [
    "https://www.bilibili.com",  # 哔哩哔哩
    "https://www.youku.com",  # 优酷
    "https://www.iqiyi.com",  # 爱奇艺
    "https://www.douyin.com"  # 抖音
]


# 执行页面滚动操作的函数
def scroll_page(driver):
    for _ in range(10):
        body = driver.find_element("tag name", "body")
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        body.send_keys(Keys.PAGE_UP)
        time.sleep(1)


# 打开并控制浏览器窗口的函数
def open_window(url):
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")  # 启动时最大化窗口

    # 创建Edge WebDriver实例
    driver = webdriver.Edge(options=options)
    driver.get(url)

    # 执行滚动操作
    scroll_page(driver)

    # 关闭浏览器
    driver.quit()


# 使用线程并行启动四个窗口
threads = []
for url in urls:
    t = threading.Thread(target=open_window, args=(url,))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

print("所有浏览器窗口操作完成。")
