#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-07-14 22:00:35
LastEditTime: 2021-07-14 22:58:57
Description: SDS 抑郁自评量表 GUI 页面(基于Tkinter框架)
'''
from tkinter import *
from tkinter import Frame
from tkinter import messagebox
from tkinter import scrolledtext


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        '''构造组件'''
        Label(self.master, text="SDS抑郁测评量表", font=(
            "宋体", 18), fg="red").pack(side=TOP)
        self.t = scrolledtext.ScrolledText(
            root, width=400, height=400, font=("宋体", 11))
        self.t.pack()
        defalt_information = "SAS采用4级评分，主要评定症状出现的频度，其标准为:\n" \
            "\"1\"表示没有或很少时间有\n" \
            "\"2\"表示有时有\n" \
            "\"3\"表示大部分时间有\n" \
            "\"4\"表示绝大部分时间或全部时间都有\n"

        self.t.insert(0.0, defalt_information)

        start_button = Button(self.t, text="开始测试", command=self.create_choice)
        self.t.window_create(INSERT, window=start_button)

    def create_choice(self):
        '''在文本框里面构造选项'''
        self.t.delete(0.0, INSERT)
        question_list = ['我感到沮丧，郁闷', '我感到早上心情最好', '我要哭或想哭', '我夜间睡眠不好', '我吃饭像平时一样多', '我的性功能正常', '我感到体重减轻', '我为便秘烦恼', '我的心跳比平时快', '我无故感到疲劳', '我的头脑像往常一样清楚',
                         '我做事情像平时一样不感到困难', '我坐卧不安,难以保持平静', '我对未来感到有希望', '我比平时更容易激怒', '我觉得决定什么事很容易', '我感觉自己是有用和不可缺少的人', '我的生活很有意义', '假若我死了别人会过的更好', '我仍旧喜爱自己平时喜爱的东西']

        v = IntVar()
        Radio_list = [
            Radiobutton(self.t, text='1.表示没有或很少时间', variable=v, value=1),
            Radiobutton(self.t, text='2.表示有时有', variable=v, value=2),
            Radiobutton(self.t, text='3.表示大部分时间有', variable=v, value=3),
            Radiobutton(self.t, text='4.表示绝大部分时间或全部时间都有', variable=v, value=4),
        ]
        x_list = [1, 2, 3]
        y_list = [1, 2, 3]
        xy = zip(x_list, y_list)
        xy_list = ["%s.%s" % (x, y) for x, y in xy]

        print(xy_list)
        for question in question_list:
            self.t.insert(INSERT, question+"\n")
            for radio in Radio_list:
                self.t.window_create(xy_list[0], window=radio)


if __name__ == "__main__":
    root = Tk()
    root.title("SDS抑郁测评量表")
    root.geometry("400x400+400+300")

    app = Application(root)
    root.mainloop()
