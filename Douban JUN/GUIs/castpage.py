from tkinter import *
from PIL import ImageTk, Image
import pymysql
import pyodbc

class castsel():
    def __init__(self, master):
        castselTk = master
        self.img = Image.open('C:\Database-Final-EDU-\Douban JUN\GUIs\\background2.jpg')
        self.imgphoto = ImageTk.PhotoImage(self.img)
        self.imgtext = Text(castselTk, width=800, height=650)
        self.imgtext.image_create(END, image=self.imgphoto)
        self.imgtext.place(x=0, y=0)
        self.etgetsel()
        mainloop()

    def etgetsel(self):
        mycolor = '#215297'
        s = "安妮 海瑟薇"
        print('传递到的名字为' + s)
        conn_info = pyodbc.connect(
            'DRIVER={SQL Server};server=localhost;PORT=1433;database=DoubanJUN;user=sa;password=Junrupan9393')
        curs = conn_info.cursor()
        # 连接数据库
        print("database chongya!!!")

        self.filmnameCNLabel = Label(
            castselTk, text=s, font=('百度综艺简体', 20), anchor=NW,bg=mycolor,fg='white')
        self.filmnameCNLabel.place(x=370, y=70, width=350, height=41)
        # 从显示演员的中文名
        castname = '''SELECT  castName FROM casts   WHERE castNameCN ='%s' ''' % s

        curs.execute(castname)
        resultname = curs.fetchone()[0]
        print(resultname)
        self.filmnameLabel = Label(
            castselTk, text=resultname, font=('微软雅黑', 14), anchor=NW,bg=mycolor,fg='white')
        self.filmnameLabel.place(x=370, y=120, width=230, height=30)
        # 从SQL数据库中获取演员的英文名

        castcountry = '''SELECT  castCountry FROM casts   WHERE castNameCN ='%s' ''' % s
        curs.execute(castcountry)
        resultcountry = str(curs.fetchall()[
                            0][0])

        self.countryLabel = Label(
            castselTk, text=resultcountry, font=('微软雅黑', 14), anchor=NW,bg=mycolor,fg='white')
        self.countryLabel.place(x=370, y=160, width=370, height=40)
        # 从SQL数据库中获取演员的国家

        castbirth = '''SELECT  castBirthday FROM casts   WHERE castNameCN ='%s' ''' % s
        curs.execute(castbirth)
        resultbirth = str(curs.fetchall()[
                          0][0])
        self.birthLabel = Label(
            castselTk, text=resultbirth, font=('微软雅黑', 14), anchor=NW,bg=mycolor,fg='white')
        self.birthLabel.place(x=370, y=200, width=370, height=40)
        # 从SQL数据库中获取演员的生日

        img = '''SELECT castURL2 FROM casts  WHERE castNameCN ='%s' ''' % s
        curs.execute(img)
        resultimg = curs.fetchone()[0]
        print(resultimg)
        self.img_open = Image.open(resultimg)
        self.img_png = ImageTk.PhotoImage(self.img_open)
        self.castimage = Label(castselTk, bg='white',
                               height=200, width=200, image=self.img_png)
        self.castimage.place(x=110, y=70)
        # 从SQL数据库中获取演员的图片URL地址

        self.sclabel = Label(castselTk, text='评分',
                             font=('微软雅黑', 20), anchor=NW,bg=mycolor,fg='white')
        self.sclabel.place(x=480, y=340, width=71, height=41)
        # Label“评分”

        castscore = '''SELECT  castRate FROM  casts  WHERE castNameCN ='%s' ''' % s
        curs.execute(castscore)
        #resultscore = str(curs.fetchall()[0][0])
        resultscore = '7.5'
        print(resultscore)
        self.scoreLabel = Label(castselTk, text=resultscore, font=(
            'Times New Roman', 34), anchor=NW,bg=mycolor,fg='white')
        self.scoreLabel.place(x=490, y=390, width=80, height=80)
        # 从SQL数据库中获取演员的评分

        self.sclabel = Label(castselTk, text='我的评分',
                             font=('微软雅黑', 20), anchor=NW,bg=mycolor,fg='white')
        self.sclabel.place(x=620, y=340, width=131, height=41)
        # Label“我的评分”

        self.scoreentry = Entry(castselTk, textvariable=StringVar(), text='0.0',
                                font=('Times New Roman', 34),bg=mycolor,fg='white')  # entry 输入评分
        self.scoreentry.place(x=630, y=400, width=80, height=70)

        self.scoresubmit = Button(
            castselTk, text='提交', bg='red', fg='white')  # 查询Button
        self.scoresubmit.place(x=630, y=490, width=93, height=28)

        self.filmlabel = Label(castselTk, text='出演电影', font=('微软雅黑', 16),bg=mycolor,fg='white')
        self.filmlabel.place(x=110, y=300, width=121, height=41)
        # Label“出演电影”

        mvimg = '''SELECT imgURL2 FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
        and castNameCN ='%s' ''' % s
        curs.execute(mvimg)
        self.resultmvimg = str(curs.fetchall()[0][0])
        print(self.resultmvimg)
        self.mvimg_open = Image.open(self.resultmvimg)
        self.mvimg_png = ImageTk.PhotoImage(self.mvimg_open)
        self.movieimage = Label(castselTk, bg='white',
                                height=140, width=120, image=self.mvimg_png)
        self.movieimage.place(x=110, y=360)
        # 从SQL数据库中获取电影的图片URL地址

        filmnameCN = '''SELECT  movieNameCN FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
        and castNameCN ='%s' ''' % s
        curs.execute(filmnameCN)
        nameCN = str(curs.fetchall()[
                     0][0])
        self.filmnameCNLabel = Label(castselTk, text=nameCN, font=(
            '微软雅黑', 18), anchor=NW,bg=mycolor,fg='white')  # Label“标签”
        self.filmnameCNLabel.place(x=250, y=360, width=130, height=40)
        # 从SQL数据库中获取电影的中文名

        filmname = '''SELECT  movieName FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
        and castNameCN ='%s' ''' % s
        curs.execute(filmname)
        name = str(curs.fetchall()[0][0])
        self.filmnameLabel = Label(castselTk, text=name, font=(
            'Times New Roman', 12), anchor=NW,bg=mycolor,fg='white')  # Label“标签”
        self.filmnameLabel.place(x=250, y=400, width=160, height=20)
        # 从SQL数据库中获取电影的英文名

        filmdate = '''SELECT  movieDate FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
               and castNameCN ='%s' ''' % s
        curs.execute(filmdate)
        date = str(curs.fetchall()[0][0])
        self.filmdateLabel = Label(castselTk, text=date, font=(
            'Times New Roman', 12), anchor=NW,bg=mycolor,fg='white')  # Label“标签”
        self.filmdateLabel.place(x=250, y=430, width=130, height=40)
        # 从SQL数据库中获取电影的日期

        conn_info.close()


castselTk = Toplevel()
castselTk.title('演员详情')  # 设置窗口标题
castselTk.geometry('800x650')
castselapp = castsel(castselTk)
castselTk.mainloop()
