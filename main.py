# Load From Config
# Tkinter
import time
import tkinter as tk
from tkinter import messagebox

from config.driver import driver
from config.logger import logger
# Custom Features
from scripts import login
import scripts.autosearch
import scripts.hottopicsearch
import scripts.sanlian
import scripts.unsubscribe


# 登陆场景
def test_logged_in():
    try:
        # 打开B站主页
        driver.get("https://www.bilibili.com")
        driver.maximize_window()
        # 尝试获取用户信息

        login.try_pwd_login()
    except Exception as e:
        print(f"测试失败：{e}")


def search_test():
    logger.info("您已选择执行搜索功能测试，搜搜我自己吧！！！")
    scripts.autosearch.search_test()


def popular_terms_access():
    logger.info("执行热门词条访问，看看今天发生了什么！！！")
    scripts.hottopicsearch.hot_search()


def video_triple_stats():
    logger.info("执行视频三连数量统计，Jason的视频必须要三连！！！")
    scripts.sanlian.sanlian()

def cancel_follow_test():
    logger.info("您已选择执行一键取消关注功能测试，我要取消子慷的关注，欧耶！！！")
    scripts.unsubscribe.unsubscribe()


def execute_selected_functions(var_search, var_popular, var_video_triple, var_cancel_follow):
    # 获取用户选中的功能
    selected_functions = []
    print(var_search.get(), var_popular.get(), var_video_triple.get(), var_cancel_follow.get())  # 调试输出
    if var_search.get():
        selected_functions.append(search_test)
    if var_popular.get():
        selected_functions.append(popular_terms_access)
    if var_video_triple.get():
        selected_functions.append(video_triple_stats)
    if var_cancel_follow.get():
        selected_functions.append(cancel_follow_test)

    # 按顺序执行选中的功能
    if selected_functions:
        for func in selected_functions:
            func()  # 执行功能
            print("功能已执行")
    else:
        messagebox.showwarning("警告", "请至少选择一个功能执行！")


def check_windows():
    # 创建主窗口
    root = tk.Tk()
    root.title("功能选择")
    root.geometry("400x300")

    # 创建功能选择的勾选框
    var_search = tk.BooleanVar()
    var_popular = tk.BooleanVar()
    var_video_triple = tk.BooleanVar()
    var_cancel_follow = tk.BooleanVar()

    checkbox_search = tk.Checkbutton(root, text="搜索功能测试", variable=var_search)
    checkbox_popular = tk.Checkbutton(root, text="热门词条访问", variable=var_popular)
    checkbox_video_triple = tk.Checkbutton(root, text="视频三连数量统计", variable=var_video_triple)
    checkbox_cancel_follow = tk.Checkbutton(root, text="一键取消关注功能测试", variable=var_cancel_follow)

    checkbox_search.pack(anchor="w", padx=20)
    checkbox_popular.pack(anchor="w", padx=20)
    checkbox_video_triple.pack(anchor="w", padx=20)
    checkbox_cancel_follow.pack(anchor="w", padx=20)

    # 创建执行按钮
    button_execute = tk.Button(root, text="开始执行", command=lambda: execute_selected_functions(var_search, var_popular, var_video_triple, var_cancel_follow))
    button_execute.pack(pady=20)

    # 运行主事件循环
    root.mainloop()


# 测试日志输出
logger.info("Copyright (c) 2024 Jason_Stephen")
test_logged_in() # 登录
check_windows() # 功能选择
logger.info("耶！所有的任务都完成啦，下班下班！")
time.sleep(3)
driver.quit()

"""
Copyright (c) 2024 Jason_Stephen

This software is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
"""
