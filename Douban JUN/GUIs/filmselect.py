from tkinter import *
from PIL import ImageTk, Image
import pymysql


class filmsel():
    def __init__(self, master):
        mycolor = '#215297'
        filmselTk = master
        self.img = Image.open("Douban JUN/GUIs/background2.jpg")
        self.imgphoto = ImageTk.PhotoImage(self.img)
        self.imgtext = Text(filmselTk, width=800, height=650)
        self.imgtext.image_create(END, image=self.imgphoto)
        self.imgtext.place(x=0, y=0)
        self.filmentry = Entry(filmselTk, textvariable=StringVar(
        ), text='请输入电影名称：', font=('微软雅黑', 13), bg='white')  # Label“请输入电影名称”
        self.filmentry.place(x=220, y=40, width=300, height=35)
        self.filmselbt1 = Button(
            filmselTk, text='查询', command=self.etgetsel, bg='green', fg='white')  # 查询Button
        self.filmselbt1.place(x=560, y=40, width=100, height=35)

        mainloop()

    def directtocast(self):
        actornameCN = self.actorLabelCN.cget("text")
        print(actornameCN)
        import castpage
        castpage.castsel(actornameCN)

    def etgetsel(self):
        s = self.filmentry.get()
        # try:
        conn_info = pymysql.connect(
            "localhost", "test", "testnmb", "DOUBAN_JUN")
        curs = conn_info.cursor()
        # 连接数据库
        print("database chongya!!!")
        mycolor = '#215297'
        filmnameCN = '''SELECT  movieNameCN FROM movies   WHERE movieNameCN ='%s' ''' % s
        curs.execute(filmnameCN)
        nameCN = str(curs.fetchall()[0][0])
        self.filmnameCNLabel = Label(filmselTk, text=nameCN, font=(
            '百度综艺简体', 20), anchor=NW, bg=mycolor, fg='white')  # Label“标签”
        self.filmnameCNLabel.place(x=320, y=100, width=150, height=40)
        # 从SQL数据库中获取电影的中文名

        filmname = '''SELECT  movieName FROM movies   WHERE movieNameCN ='%s' ''' % s
        curs.execute(filmname)

        name = str(curs.fetchall()[0][0])
        self.filmnameLabel = Label(filmselTk, text=name, font=(
            'Times New Roman', 16), anchor=NW, bg=mycolor, fg='white')  # Label“标签”
        self.filmnameLabel.place(x=320, y=145, width=200, height=30)
        # 从SQL数据库中获取电影的英文名

        filmclass = '''SELECT  movieclass FROM movies   WHERE movieNameCN ='%s' ''' % s
        curs.execute(filmclass)
        fmclass = str(curs.fetchall()[
                      0][0])
        self.filmclassLabel = Label(filmselTk, text=fmclass, font=(
            'Times New Roman', 14), anchor=NW, bg=mycolor, fg='white')  # Label“标签”
        self.filmclassLabel.place(x=320, y=180, width=150, height=30)
        # 从SQL数据库中获取电影的类别

        filmdate = '''SELECT  movieDate FROM movies   WHERE movieNameCN ='%s' ''' % s
        curs.execute(filmdate)
        date = str(curs.fetchall()[0][0])
        self.filmdateLabel = Label(filmselTk, text=date, font=(
            'Times New Roman', 16), anchor=NW, bg=mycolor, fg='white')  # Label“标签”
        self.filmdateLabel.place(x=550, y=100, width=150, height=30)
        # 从SQL数据库中获取电影的时间

        actorCN = '''SELECT  casts.castNameCN FROM  castShow,casts,movies
                       WHERE castShow.castId = casts.castId and castShow.movieId = movies.movieId
                       and movieNameCN ='%s' ''' % s
        curs.execute(actorCN)
        resultactorCN = str(curs.fetchall()[
                            0][0])
        self.actorLabelCN = Label(filmselTk, text=resultactorCN, font=(
            '微软雅黑', 17), anchor=NW, bg=mycolor, fg='white')  # Label“标签”
        self.actorLabelCN.place(x=480, y=260, width=230, height=40)
        # 从SQL数据库中获取演员中文名

        actor = '''SELECT  casts.castName FROM  castShow,casts,movies
                    WHERE castShow.castId = casts.castId and castShow.movieId = movies.movieId
                    and movieNameCN ='%s' ''' % s
        curs.execute(actor)
        resultactor = str(curs.fetchall()[0][0])
        self.actorLabel = Label(filmselTk, text=resultactor, font=(
            'Times New Roman', 14), anchor=NW, bg=mycolor, fg='white')  # Label“标签”
        self.actorLabel.place(x=480, y=290, width=230, height=40)
        # 从SQL数据库中获取演员英文名

        score = '''SELECT  movies.movieRate FROM  movies
                                    WHERE movieNameCN ='%s' ''' % s
        curs.execute(score)
        resultscore = curs.fetchall()
        # 从SQL数据库中获取电影的评分

        self.scoreCN = Label(filmselTk, text='豆瓣评分',
                             font=('微软雅黑', 25), bg=mycolor, fg='white')  # Label“标签”
        self.scoreCN.place(x=120, y=430, width=140, height=41)
        self.score = Label(filmselTk, text='0.0',
                           font=('微软雅黑', 34), bg=mycolor, fg='white')  # Label 电影评分
        self.score.place(x=130, y=480, width=81, height=81)
        self.scoreCN = Label(filmselTk, text='我的评分',
                             font=('微软雅黑', 25), bg=mycolor, fg='white')  # Label“标签”
        self.scoreCN.place(x=610, y=420, width=140, height=41)
        self.scoreentry = Entry(filmselTk, textvariable=StringVar(), text='0.0',
                                font=('Times New Roman', 34), bg=mycolor, fg='white')  # entry 输入评分
        self.scoreentry.place(x=630, y=480, width=80, height=70)
        self.scoresubmit = Button(
            filmselTk, text='提交', bg='red', fg='white')  # 查询Button
        self.scoresubmit.place(x=625, y=570, width=90, height=28)
        self.filmact = Label(filmselTk, text='主演', font=(
            '百度综艺简体', 17), anchor=NW, bg=mycolor, fg='white')  # Label“主演”
        self.filmact.place(x=320, y=215, width=70, height=40)

        self.castpagebt = Button(
            filmselTk, text='演员表跳转', command=self.directtocast, bg='green', fg='white')  # 查询Button
        self.castpagebt.place(x=480, y=350, width=100, height=35)
        #######
        img = '''SELECT imgURL FROM movies  WHERE movieNameCN ='%s' ''' % s
        curs.execute(img)
        resultimg = curs.fetchone()[0]
        print(resultimg)
        self.pilImage = Image.open(resultimg)
        self.img_png = ImageTk.PhotoImage(self.pilImage)

        self.filmimage = Label(filmselTk,
                               height=280, width=210, image=self.img_png)
        self.filmimage.place(x=80, y=110)
        # self.filmimage.pack()
        # 从SQL数据库中获取电影的图片URL地址

        actimg1 = '''SELECT castURL FROM casts,castShow,movies  WHERE casts.castId = castShow.castId and castShow.movieId = movies.movieId and movieNameCN ='%s' ''' % s
        curs.execute(actimg1)
        actimg1 = curs.fetchone()[0]
        print(actimg1)
        self.castimage = Image.open(actimg1)
        self.cast_png = ImageTk.PhotoImage(self.castimage)
        self.castimg = Label(filmselTk,
                             height=130, width=130, image=self.cast_png)
        self.castimg.place(x=320, y=260)
        # self.actimage.pack()
        # 从SQL数据库中获取演员的图片URL地址

        conn_info.close()
        # except:
        # print("lljbd")
        # self.filmnameCNLabel.delete(0.0, END)
        # self.filmnameCNLabel.insert(1.0, '连接数据库失败')

        return resultactorCN


filmselTk = Toplevel()
filmselTk.title('电影查询')  # 设置窗口标题
filmselTk.geometry('800x650')
filmselapp = filmsel(filmselTk)
filmselTk.mainloop()
