import json
import os


def create_mobilephone_json():
    # 文件路径
    json_file = "mobilephone.json"

    # 检查文件是否存在，如果不存在则创建
    if not os.path.exists(json_file):
        # 创建一个空的字典结构
        mobilephone_data = {
            "username": "",
            "password": "",
            "mobile": ""
        }

        # 提醒用户补全信息
        print("mobilephone.json has been created successfully, and the content is as follows:")
        print(json.dumps(mobilephone_data, indent=4))

        # 将字典写入到 JSON 文件
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(mobilephone_data, f, ensure_ascii=False, indent=4)
        print(f"\n[NOTICE] Please complete the 'username', 'password', and 'mobile' fields in the {json_file} file.")
    else:
        print(f"[NOTICE] {json_file} is exist, you can now edit this file。")


# 调用函数
create_mobilephone_json()
