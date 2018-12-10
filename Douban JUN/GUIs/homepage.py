# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
import pymysql


class homesel():
    def __init__(self, master):
        homeselTk = master
        # 菜单栏
        self.menubar = Menu(homeselTk)
        # 创建下拉菜单我的主页
        self.infomenu = Menu(self.menubar, tearoff=0)
        self.infomenu.add_command(label='个人主页', command=self.directtouser)
        self.menubar.add_cascade(label='个人信息', menu=self.infomenu)

        # 创建下拉菜单信息查询
        self.slmenu = Menu(self.menubar, tearoff=0)
        self.slmenu.add_command(label='电影查询', command=self.directtofilm)
        self.slmenu.add_command(label='演员查询', command=self.directtocast)
        self.menubar.add_cascade(label='信息查询', menu=self.slmenu)

        # 创建下拉菜单
        self.abmenu = Menu(self.menubar, tearoff=0)
        self.abmenu.add_command(label='开发者信息', command=self.directtodeveloper)
        self.abmenu.add_separator()
        self.abmenu.add_command(label='退出系统', command=homeselTk.quit)
        self.menubar.add_cascade(label='关于我们', menu=self.abmenu)
        homeselTk.config(menu=self.menubar)
        mainloop()

    def directtouser(self):
        from UserPage import usersel

    def directtocast(self):
        from castselect import castsel

    def directtofilm(self):
        from filmselect import filmsel

    def directtodeveloper(self):
        from developerpage import developsel


homeselTk = Toplevel()
homeselTk.title('用户主页')  # 设置窗口标题
homeselTk.geometry('800x650')
homeapp = homesel(homeselTk)
homeselTk.mainloop()
