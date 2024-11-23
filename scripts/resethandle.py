import time

from config.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from config.logger import logger
def reset_window():
    # 回到第一个标签页
    first_tab = driver.window_handles[0]
    driver.switch_to.window(first_tab)
    logger.info("切换回第一个标签页！")

    # 关闭除了当前标签页外的其他标签页
    current_tab = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != current_tab:
            driver.switch_to.window(handle)
            driver.close()

    # 切换回当前标签页
    driver.switch_to.window(current_tab)

    # 刷新当前标签页（选择跳转是为了避免出现在同标签下操作）
    driver.get("https://www.bilibili.com")
    logger.info("已刷新当前标签页！")

