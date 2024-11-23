import time

from config.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from config.logger import logger
from scripts import resethandle


def search_test():
    try:
        # 根据类名定位输入框（确保唯一性）
        input_box = driver.find_element(By.CLASS_NAME, "nav-search-input")
        # 输入内容
        input_box.clear()
        input_box.send_keys("UID39750208")
        # 定位搜索按钮并点击
        search_button = driver.find_element(By.CLASS_NAME, "nav-search-btn")
        ActionChains(driver).move_to_element(search_button).click(search_button).perform()
        logger.info("搜索功能测试成功完成！")

    except Exception as e:
        logger.error(f"搜索测试功能出现错误: {e}")

    time.sleep(2)  # 等待页面加载

    # 获取所有标签页的句柄
    window_handles = driver.window_handles
    logger.info(f"当前所有标签页句柄: {window_handles}")

    if len(window_handles) > 1:
        # 切换到新打开的标签页（假设新标签页是最后一个）
        driver.switch_to.window(window_handles[-1])
        logger.info("切换到新标签页！")

        # 获取新标签页的 URL
        current_url = driver.current_url
        logger.info(f"获取到当前网址: {current_url}")

        # 修改 URL 中的 "all" 为 "upuser"
        new_url = current_url.replace("all", "upuser")
        logger.info(f"获取到修改后的网址: {new_url}")

        # 访问新网址
        driver.get(new_url)
        logger.info("已成功访问新网页！")

        time.sleep(2)

        # 点击目标链接
        user_link = driver.find_element(By.XPATH, "//a[@title='Jason_Stephen']")
        user_link.click()
        logger.info("发现了Jason_Stephen！")

        # 等待页面加载
        time.sleep(10)

        resethandle.reset_window()

        # 完成任务提示
        logger.info("欧耶！任务1完成啦！如果有任务，5秒后继续执行")
        time.sleep(5)

    else:
        logger.error("没有找到新的标签页！")
