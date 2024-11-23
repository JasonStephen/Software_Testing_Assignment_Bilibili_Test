import time

import requests

from config.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from config.logger import logger
from scripts import resethandle


def hot_search():
    # 访问 API 获取热搜数据
    api_url = "https://api.bilibili.com/x/web-interface/wbi/search/square?limit=10"

    # 设置请求头，模拟正常浏览器的请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'application/json',
        'Connection': 'keep-alive'
    }

    try:
        response = requests.get(api_url, headers=headers)

        # 确保请求成功
        if response.status_code == 200:
            data = response.json()  # 解析 JSON 数据

            # 获取第一个 keyword
            keyword = data['data']['trending']['list'][0]['show_name']
            logger.info(f"获取到的第一个关键词为: {keyword}")

            # 等待网页加载
            time.sleep(2)

            # 定位输入框并填充关键词
            input_box = driver.find_element(By.CLASS_NAME, "nav-search-input")
            input_box.clear()
            input_box.send_keys(keyword)
            logger.info(f"已将关键词 '{keyword}' 填入搜索框")

            # 定位搜索按钮并点击
            search_button = driver.find_element(By.CLASS_NAME, "nav-search-btn")
            ActionChains(driver).move_to_element(search_button).click(search_button).perform()

        else:
            logger.error(f"API 请求失败，状态码: {response.status_code}")
            logger.error(f"响应内容: {response.text}")

    except requests.exceptions.RequestException as e:
        logger.error(f"请求发生异常: {e}")

    # 等待页面加载并检查搜索结果
    time.sleep(10)

    resethandle.reset_window()

    # 完成任务提示
    logger.info("欧耶！任务2完成啦！如果有任务，5秒后继续执行")
    time.sleep(5)