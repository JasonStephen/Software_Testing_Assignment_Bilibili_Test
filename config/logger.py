import logging
import os

# 设置日志文件路径
log_file = os.path.abspath("log.log")  # 使用绝对路径

# 如果日志文件不存在，则创建该文件
if not os.path.exists(log_file):
    with open(log_file, "w", encoding="utf-8"):
        pass  # 创建文件

# 创建日志记录器
logger = logging.getLogger("user_info_logger")
logger.setLevel(logging.DEBUG)  # 设置记录器的级别为DEBUG

# 文件处理器：写入日志文件
file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)  # 设置文件处理器的级别为DEBUG

# 控制台处理器：输出到屏幕
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # 设置控制台处理器的级别为DEBUG

# 日志格式
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)
