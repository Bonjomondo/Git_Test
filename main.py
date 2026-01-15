#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Git 测试项目的主程序
"""

from utils import add_numbers, greet_user

def main():
    print("欢迎使用 Git 测试项目！")
    print("这是一个简单的 Python 程序，用于测试 Git 功能。")
    print("now,I'm currently testing cloud synchronization")
    # 调用工具函数
    result = add_numbers(100, 3)
    print(f"100 + 3 = {result}")

    # 更多功能可以在这里添加
    greet_user("Git 用户")

if __name__ == "__main__":
    main()
