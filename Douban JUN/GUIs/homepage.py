# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql


class homesel():
    def __init__(self, master):
        homeselTk = master
        self.img = Image.open("Douban JUN/GUIs/background2.jpg")
        self.imgphoto = ImageTk.PhotoImage(self.img)
        self.imgtext = Text(homeselTk, width=800, height=650)
        self.imgtext.image_create(END, image=self.imgphoto)
        self.imgtext.place(x=0, y=0)
        # 菜单栏
        self.menubar = Menu(homeselTk)
        # 创建下拉菜单我的主页
        self.infomenu = Menu(self.menubar, tearoff=0)
        #self.infomenu.add_command(label='个人主页', command=self.directtouser)
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
        mycolor = '#215297'
        self.titleLabel = Label(
            homeselTk, text='简易豆瓣', font=('百度综艺简体', 48), anchor=NW, bg=mycolor, fg='white')
        #bg = RGB(31, 81, 150)
        self.titleLabel.place(x=270, y=90, width=260, height=74)

        self.userLabel = Label(
            homeselTk, text='用户名：', font=('微软雅黑', 20), anchor=NW, bg=mycolor, fg='white')
        self.userLabel.place(x=180, y=260, width=100, height=44)

        self.nameEntry = Entry(homeselTk, textvariable=StringVar(), text='',
                               font=('Helvetica', 20))
        self.nameEntry.place(x=330, y=260, width=250, height=44)

        self.pwLabel = Label(
            homeselTk, text='密码：', font=('微软雅黑', 20), anchor=NW, bg=mycolor, fg='white')
        self.pwLabel.place(x=200, y=340, width=80, height=44)

        self.pwentry = Entry(homeselTk, textvariable=StringVar(),
                             font=('Helvetica', 20), show='*')
        self.pwentry.place(x=330, y=340, width=250, height=44)

        self.loginbt = Button(
            homeselTk, text='登录', command=self.directtouser, bg='green', fg='white')  # 查询Button
        self.loginbt.place(x=300, y=460, width=210, height=40)

        mainloop()

    def directtouser(self):
        conn_info = pymysql.connect(
            "localhost", "test", "testnmb", "DOUBAN_JUN")
        curs = conn_info.cursor()
        s = self.nameEntry.get()
        sql = '''select userpassword from users where userName = '%s' ''' % s
        curs.execute(sql)
        realpw = curs.fetchone()[0]
        print(realpw)
        if self.pwentry.get() == realpw:
            from UserPage import usersel
        else:
            self.nameEntry.select_clear()
            self.pwentry.select_clear()
            r = messagebox.showerror('消息框', '密码错误，请重新输入')

    def directtocast(self):
        from castselect import castsel

    def directtofilm(self):
        from filmselect import filmsel

    def directtodeveloper(self):

        from developerpage import developsel

    def directtodeveloper(self):
        supinfTk = Tk(className='开发者信息')
        supinfTk.geometry('500x500')
        mycolor = '#215297'
        backlb = Label(supinfTk, text='', bg=mycolor)
        backlb.place(x=0, y=0, width=500, height=500)
        supinflb2 = Label(supinfTk, text='简易豆瓣开发者名单', font=(
            '百度综艺简体', 30), bg=mycolor, fg='white')
        supinflb2.place(x=50, y=100, width=400, height=80)  # 产生文本
        supinflb3 = Label(supinfTk, text='信计160班 柳士俊', font=(
            '微软雅黑', 17), bg=mycolor, fg='white')
        supinflb3.place(x=100, y=200, width=300, height=40)  # 产生文本
        supinflb4 = Label(supinfTk, text='应数162班 潘俊汝', font=(
            '微软雅黑', 17), bg=mycolor, fg='white')
        supinflb4.place(x=100, y=260, width=300, height=40)  # 产生文本
        mainloop()


homeselTk = Toplevel()
homeselTk.title('用户主页')  # 设置窗口标题
homeselTk.geometry('800x650')
homeapp = homesel(homeselTk)
homeselTk.mainloop()
