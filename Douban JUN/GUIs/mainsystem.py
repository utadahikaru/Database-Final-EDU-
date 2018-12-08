from tkinter import *
from PIL import ImageTk, Image

class mainsys():
    def __init__(self, master):
        tl = master
        self.img = Image.open('C:\Database-Final-EDU-\Douban JUN\GUIs\image')
        self.imgphoto = ImageTk.PhotoImage(self.img)
        self.imgtext=Text(tl,width=800,height=650)
        self.imgtext.image_create(END,image=self.imgphoto)
        self.imgtext.place(x=0, y=0)

        # 菜单栏
        self.menubar = Menu(tl)
        # 创建下拉菜单信息查询
        self.slmenu = Menu(self.menubar, tearoff=0)
        self.slmenu.add_command(label='电影查询', command=self.filmsc)
        self.slmenu.add_command(label='演员查询', command=self.colsel)
        #self.slmenu.add_command(label='课程查询', command=self.cousel)
        #self.slmenu.add_command(label='职位查询', command=self.possel)
        #self.slmenu.add_command(label='综合查询', command=self.comsel)
        #self.menubar.add_cascade(label='信息查询', menu=self.slmenu)

        # 创建下拉菜单编辑管理
        #self.editmenu = Menu(self.menubar, tearoff=0)
        #self.editmenu.add_command(label='新增信息', command=self.insinf)
        #self.editmenu.add_command(label='修改信息', command=self.altinf)
        #self.editmenu.add_command(label='删除信息', command=self.delinf)
        #self.menubar.add_cascade(label='编辑管理', menu=self.editmenu)


        # 创建下拉菜单社团信息
        #infomenu = Menu(self.menubar, tearoff=0)
        #infomenu.add_command(label='部门信息', command=self.secinf)
        #infomenu.add_command(label='课程信息', command=self.couinf)
        #self.menubar.add_cascade(label='社团信息', menu=infomenu)

        # 创建下拉菜单file ctrl+/加注释
        self.abmenu = Menu(self.menubar, tearoff=0)
        self.abmenu.add_command(label='开发者信息', command=self.supinf)
        self.abmenu.add_separator()
        self.abmenu.add_command(label='退出系统', command=tl.quit)
        self.menubar.add_cascade(label='关于我们', menu=self.abmenu)
        tl.config(menu=self.menubar)

        #self.loginsys = Button(tl, text='综合查询', command=self.comsel,bg='green', fg='white')
        self.search=Button(tl,text='搜索',command=tl.serach,bg='grey',fg='white')
        self.quitsys = Button(tl, text='退出系统', command=tl.quit,
                              bg='red', fg='white')
        self.search.place(x=475, y=100, width=100, height=40)
        self.quitsys.place(x=475, y=410, width=100, height=40)  # 退出按钮可省略


    def filmsc(self):
        from sectionselect import sectionsel

    def colsel(self):
        from collegeselect import collegesel

    def cousel(self):
        from courseselect import coursesel

    def possel(self):
        from positionselect import positionsel

    def comsel(self):
        from filmselect import filmsel

    def insinf(self):
        from insertinfo import insertinfomation

    def altinf(self):
        from alterinfo import alterinfomation

    def delinf(self):
        from deleteinfo import deleteinfomation

    def secinf(self):
        secinfTk = Tk(className='部门信息')
        secinfTk.geometry('500x400')
        secinflb1 = Label(secinfTk, text='数学与智能科技协会下设8个部门：', font=('Times New Roman', 14))
        secinflb1.place(x=100, y=20, width=300, height=40)
        secinflb0 = Label(secinfTk, text='(以及行政管理部门：会长层）', font=('Times New Roman', 14))
        secinflb0.place(x=100, y=70, width=300, height=40)
        secinflb2 = Label(secinfTk, text='秘书处', font=('Times New Roman', 12))
        secinflb2.place(x=150, y=120, width=100, height=40)
        secinflb3 = Label(secinfTk, text='宣传部', font=('Times New Roman', 12))
        secinflb3.place(x=250, y=120, width=100, height=40)
        secinflb4 = Label(secinfTk, text='外联部', font=('Times New Roman', 12))
        secinflb4.place(x=150, y=170, width=100, height=40)
        secinflb5 = Label(secinfTk, text='科技部', font=('Times New Roman', 12))
        secinflb5.place(x=250, y=170, width=100, height=40)
        secinflb6 = Label(secinfTk, text='信息技术部', font=('Times New Roman', 12))
        secinflb6.place(x=150, y=220, width=100, height=40)
        secinflb7 = Label(secinfTk, text='基础学科部', font=('Times New Roman', 12))
        secinflb7.place(x=250, y=220, width=100, height=40)
        secinflb8 = Label(secinfTk, text='数据部', font=('Times New Roman', 12))
        secinflb8.place(x=150, y=270, width=100, height=40)
        secinflb9 = Label(secinfTk, text='数模部', font=('Times New Roman', 12))
        secinflb9.place(x=250, y=270, width=100, height=40)
        mainloop()

    def couinf(self):
        couinfTk = Tk(className='课程信息')
        couinfTk.geometry('500x400')
        couinflb1 = Label(couinfTk, text='数学与智能科技协会2017学年开设两门课程：', font=('Times New Roman', 14))
        couinflb1.place(x=50, y=50, width=400, height=40)
        couinflb2 = Label(couinfTk, text='Matlab', font=('Times New Roman', 16))
        couinflb2.place(x=80, y=120, width=100, height=40)
        couinflb3 = Label(couinfTk, text='Python', font=('Times New Roman', 16))
        couinflb3.place(x=80, y=240, width=100, height=40)
        couinflb4 = Label(couinfTk, text='开课部门：信息技术部', font=('Times New Roman', 12))
        couinflb4.place(x=200, y=100, width=200, height=40)
        couinflb5 = Label(couinfTk, text='开课部门：信息技术部', font=('Times New Roman', 12))
        couinflb5.place(x=200, y=220, width=200, height=40)
        couinflb6 = Label(couinfTk, text='主讲人：应物160 牛泽宇', font=('Times New Roman', 12))
        couinflb6.place(x=200, y=140, width=200, height=40)
        couinflb7 = Label(couinfTk, text='主讲人：应数152 李明辰', font=('Times New Roman', 12))
        couinflb7.place(x=200, y=260, width=200, height=40)
        mainloop()

    def supinf(self):
        supinfTk = Tk(className='开发者信息')
        supinfTk.geometry('500x500')
        supinflb1 = Label(supinfTk, text='MITA社团信息管理系统', font=('Times New Roman', 14))
        supinflb1.place(x=150, y=70, width=200, height=40)  # 产生文本
        supinflb2 = Label(supinfTk, text='开发者名单', font=('Times New Roman', 14))
        supinflb2.place(x=150, y=120, width=200, height=40)  # 产生文本
        supinflb3 = Label(supinfTk, text='应数152班 陆鹏皓', font=('Times New Roman', 12))
        supinflb3.place(x=150, y=180, width=200, height=40)  # 产生文本
        supinflb4 = Label(supinfTk, text='应数152班 高昊', font=('Times New Roman', 12))
        supinflb4.place(x=150, y=220, width=200, height=40)  # 产生文本
        supinflb5 = Label(supinfTk, text='应数152班 胡光', font=('Times New Roman', 12))
        supinflb5.place(x=150, y=260, width=200, height=40)  # 产生文本
        supinflb6 = Label(supinfTk, text='对于本信息管理系统有任何问题或建议可联系', font=('Times New Roman', 11))
        supinflb6.place(x=50, y=340, width=400, height=40)  # 产生文本
        supinflb7 = Label(supinfTk, text='数学与智能科技协会官方大群：QQ 625341373', font=('Times New Roman', 11))
        supinflb7.place(x=50, y=370, width=400, height=40)  # 产生文本
        mainloop()


tl=Toplevel()
tl.title('数学与智能科技协会社团管理系统')
tl.geometry('750x500')
mainapp = mainsys(tl)
tl.mainloop()
