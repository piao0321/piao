# -*- coding: utf-8 -*-
"""
@Time :2022/11/20 0:28
@Author :Lai Xiangyuan
@Email :2936885192@qq.com
@File :try.py
@ID :12003990122
"""

import streamlit as st


def main():
    st.title("搜索引擎作业合集")
    # app = MultiPage()
    activities = ["实验一二", "实验三", "实验四", "实验五",
                  "实验六", "实验七", "实验八", "实验九"]

    choice = st.sidebar.selectbox("Select task", activities)
    st.success("当前选择：" + choice)

    # app.add_page('tea1', test1.app)
    # app.run()


main()
