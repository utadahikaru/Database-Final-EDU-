from tkinter import *
from PIL import ImageTk,Image
import pyodbc
import pymysql


class homesel():
    def __init__(self,master):
        homeselTk=master
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

        # self.filmentry = Entry(castselTk,textvariable=StringVar(),text='请输入电影名称：',font=('Times New Roman', 12)) #Label“请输入电影名称”
        # self.filmentry.place(x=220, y=50, width=300, height=35)
        # self.filmselbt1 = Button(castselTk, text='查询', command=self.etgetsel,bg='green', fg='white') #查询Button
        # self.filmselbt1.place(x=560, y=50, width=100, height=35)
        mainloop()

    def directtouser(self):
        from UserPage import usersel

    def directtocast(self):
        from castselect import castsel

    def directtofilm(self):
        from filmselect import filmsel

    def directtodeveloper(self):
        from developerpage import developsel
    # def etgetsel(self):
    #     s="盖尔加朵"
    #     #s = self.filmentry.get() #输入已知的castNameCN演员中文名
    #     # try:
    #     conn_info = pyodbc.connect(
    #                 'DRIVER={SQL Server};server=localhost;PORT=1433;database=DoubanJUN;user=sa;password=Junrupan9393')
    #     curs = conn_info.cursor()
    #     #连接数据库
    #     print("database chongya!!!")
    #
    #     self.filmnameCNLabel = Label(castselTk, text=s, font=('微软雅黑', 20), anchor=NW)
    #     self.filmnameCNLabel.place(x=370, y=70, width=350, height=41)
    #     # 从显示演员的中文名
    #
    #     castname = '''SELECT  castName FROM casts   WHERE castNameCN ='%s' ''' % s
    #     resultname = str(curs.execute(castname).fetchall()[0]).replace("('", "").replace("', )", "")
    #     self.filmnameLabel = Label(castselTk, text=resultname, font=('微软雅黑', 12), anchor=NW)
    #     self.filmnameLabel.place(x=370, y=120, width=230, height=30)
    #     #从SQL数据库中获取演员的英文名
    #
    #     castcountry = '''SELECT  castCountry FROM casts   WHERE castNameCN ='%s' ''' % s
    #     resultcountry = str(curs.execute(castcountry).fetchall()[0]).replace("('", "").replace("', )", "")
    #     self.countryLabel = Label(castselTk, text=resultcountry, font=('微软雅黑', 12), anchor=NW)
    #     self.countryLabel.place(x=370, y=170, width=370, height=40)
    #     # 从SQL数据库中获取演员的国家
    #
    #     castbirth = '''SELECT  castBirthday FROM casts   WHERE castNameCN ='%s' ''' % s
    #     resultbirth = str(curs.execute(castbirth).fetchall()[0]).replace("('", "").replace("', )", "")
    #     self.birthLabel = Label(castselTk, text=resultbirth, font=('微软雅黑', 12), anchor=NW)
    #     self.birthLabel.place(x=370, y=210, width=370, height=40)
    #     # 从SQL数据库中获取演员的生日
    #
    #     img = '''SELECT castURL FROM casts  WHERE castNameCN ='%s' '''%s
    #     resultimg = str(curs.execute(img).fetchall()[0]).replace("('", "").replace("', )", "")
    #     print(resultimg)
    #     img_open = Image.open(resultimg)
    #     img_png = ImageTk.PhotoImage(img_open)
    #     self.castimage = Label(castselTk, bg='white', height=200, width=200, image=img_png)
    #     self.castimage.place(x=110, y=70)
    #     # 从SQL数据库中获取演员的图片URL地址
    #
    #     self.sclabel = Label(castselTk, text='评分', font=('微软雅黑', 20), anchor=NW)
    #     self.sclabel.place(x=480, y=340, width=71, height=41)
    #     # Label“评分”
    #
    #     castscore = '''SELECT  castRate FROM  casts  WHERE castNameCN ='%s' ''' % s
    #     resultscore = str(curs.execute(castscore).fetchall()[0]).replace("(", "").replace(", )", "")
    #     print(resultscore)
    #     self.scoreLabel = Label(castselTk, text=resultscore, font=('Times New Roman', 34), anchor=NW)
    #     self.scoreLabel.place(x=490, y=390, width=80, height=80)
    #     # 从SQL数据库中获取演员的评分
    #
    #     self.sclabel = Label(castselTk, text='我的评分', font=('微软雅黑', 20), anchor=NW)
    #     self.sclabel.place(x=620, y=340, width=131, height=41)
    #     # Label“我的评分”
    #
    #     self.scoreentry = Entry(castselTk, textvariable=StringVar(), text='0.0',
    #                             font=('Times New Roman', 34))  # entry 输入评分
    #     self.scoreentry.place(x=630, y=400, width=80, height=70)
    #
    #     self.scoresubmit = Button(castselTk, text='提交', bg='red', fg='white')  # 查询Button
    #     self.scoresubmit.place(x=630, y=490, width=93, height=28)
    #
    #
    #     self.filmlabel = Label(castselTk, text='出演电影', font=('微软雅黑', 16))
    #     self.filmlabel.place(x=110, y=300, width=121, height=41)
    #     # Label“出演电影”
    #
    #     mvimg = '''SELECT imgURL FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
    #     and castNameCN ='%s' ''' % s
    #     resultmvimg = str(curs.execute(mvimg).fetchall()[0]).replace("('", "").replace("', )", "")
    #     print(resultmvimg)
    #     mvimg_open = Image.open(resultmvimg)
    #     mvimg_png = ImageTk.PhotoImage(mvimg_open)
    #     self.movieimage = Label(castselTk, bg='white', height=140, width=120, image=mvimg_png)
    #     self.movieimage.place(x=110, y=360)
    #     # 从SQL数据库中获取电影的图片URL地址
    #
    #     filmnameCN = '''SELECT  movieNameCN FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
    #     and castNameCN ='%s' ''' % s
    #     nameCN = str(curs.execute(filmnameCN).fetchall()[0]).replace("('", "").replace("', )", "")
    #     self.filmnameCNLabel = Label(castselTk, text=nameCN, font=('微软雅黑', 18), anchor=NW)  # Label“标签”
    #     self.filmnameCNLabel.place(x=250, y=360, width=130, height=40)
    #     # 从SQL数据库中获取电影的中文名
    #
    #     filmname = '''SELECT  movieName FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
    #     and castNameCN ='%s' ''' % s
    #     name = str(curs.execute(filmname).fetchall()[0]).replace("('", "").replace("', )", "")
    #     self.filmnameLabel = Label(castselTk, text=name, font=('Times New Roman', 12), anchor=NW)  # Label“标签”
    #     self.filmnameLabel.place(x=250, y=400, width=160, height=20)
    #     # 从SQL数据库中获取电影的英文名
    #
    #     filmdate = '''SELECT  movieDate FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
    #            and castNameCN ='%s' ''' % s
    #     date = str(curs.execute(filmdate).fetchall()[0]).replace("('", "").replace("', )", "")
    #     self.filmdateLabel = Label(castselTk, text=date, font=('Times New Roman', 12), anchor=NW)  # Label“标签”
    #     self.filmdateLabel.place(x=250, y=430, width=130, height=40)
    #     # 从SQL数据库中获取电影的日期
    #
    #     if nameCN==[]:
    #         self.castseltx1.delete(0.0, END)
    #         self.castseltx1.insert(1.0, '没有该电影信息')
    #         conn_info.close()
    #     else:
    #         print(1)
    #         self.castseltx1.delete(0.0, END)
    #         self.castseltx1.insert(1.0, filmnameCN)   # 插入该电影的中文名字
    #         # self.filmname.delete(0.0, END)
    #         # self.filmname.insert(1.0, filmname)         # 插入该电影的名字
    #         # self.actname.delete(0.0, END)
    #         # self.actname.insert(1.0, resultactor)       #插入演员的名字
    #         # self.score.delete(0.0, END)
    #         # self.score.insert(1.0, resultscore)       #插入该电影的评分
    #
    #
    #         conn_info.close()
    #     # except:
    #     #         print("lljbd")
    #             # self.filmnameCN.delete(0.0,END)
    #             # self.filmnameCN.insert(1.0,'连接数据库失败')


homeselTk=Toplevel()
homeselTk.title('用户主页') #设置窗口标题
homeselTk.geometry('800x650')
homeapp=homesel(homeselTk)
homeselTk.mainloop()