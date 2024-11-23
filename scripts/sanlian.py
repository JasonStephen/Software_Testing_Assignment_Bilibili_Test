import time

import requests

from config.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from config.logger import logger
from scripts import resethandle


def sanlian():
    # 访问 API 获取数据
    global view
    api_url = "https://api.bilibili.com/x/space/masterpiece?vmid=39750208"

    # 设置请求头，模拟正常浏览器的请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'application/json',
        'Connection': 'keep-alive'
    }

    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()  # 解析 JSON 数据

            max_view_video = None  # 用于存储最大播放量的视频
            max_view_count = 0  # 初始最大播放量

            # 获取所有视频的相关信息
            for video in data['data']:
                title = video['title']  # 视频标题
                view = video['stat']['view']  # 播放量
                danmaku = video['stat']['danmaku']  # 弹幕数
                reply = video['stat']['reply']  # 回复数
                like = video['stat']['like']  # 点赞数
                coin = video['stat']['coin']  # 硬币数
                share = video['stat']['share']  # 分享数
                short_link_v2 = video['short_link_v2']  # 视频链接（短链接）

                # 输出视频的统计信息
                logger.info(
                    f"代表作“{title}”拥有{view}播放，共有{like}个点赞，观众们发送了{danmaku}个弹幕以及{reply}个回复。最主要的是，观众们还总共投了{coin}个币，并且有{share}个人分享了他的视频。")

                # 更新最大播放量的视频
                if view > max_view_count:
                    max_view_count = view
                    max_view_video = short_link_v2

            # 如果找到最大播放量的视频，使用 Selenium 打开视频链接
            if max_view_video:
                logger.info(f"播放量最大的影片链接是: {max_view_video}, 播放量为{view}")
                driver.get(max_view_video)  # 使用 Selenium 打开视频链接
            else:
                logger.error("没有找到视频数据。")
    except requests.exceptions.RequestException as e:
        logger.error(f"请求发生异常: {e}")

    # 等待页面加载完成
    time.sleep(5)  # 或者使用 WebDriverWait 来确保元素加载

    # 定位点赞按钮
    like_button = driver.find_element(By.CSS_SELECTOR, ".video-like")

    # 使用 ActionChains 模拟长按操作
    action = ActionChains(driver)
    action.click_and_hold(like_button).perform()  # 长按按钮

    # 持续一段时间模拟“长按”
    time.sleep(3)  # 长按 3 秒，可以根据需要调整时间

    # 释放按键
    action.release().perform()

    time.sleep(20)
    resethandle.reset_window()

    # 完成任务提示
    logger.info("欧耶！任务3完成啦！如果有任务，5秒后继续执行")
    time.sleep(5)
