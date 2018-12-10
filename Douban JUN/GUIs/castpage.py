from tkinter import *
from PIL import ImageTk, Image
import pymysql


class castsel():
    def __init__(self, master):
        castselTk = master
        self.etgetsel()
        mainloop()

    def etgetsel(self):
        s = "盖尔 加朵"
        print('传递到的名字为' + s)
        conn_info = pymysql.connect(
            "localhost", "test", "testnimabi", "DOUBAN_JUN")
        curs = conn_info.cursor()
        # 连接数据库
        print("database chongya!!!")

        self.filmnameCNLabel = Label(
            castselTk, text=s, font=('微软雅黑', 20), anchor=NW)
        self.filmnameCNLabel.place(x=370, y=70, width=350, height=41)
        # 从显示演员的中文名
        castname = '''SELECT  castName FROM casts   WHERE castNameCN ='%s' ''' % s
        curs.execute(castname)
        #resultname = str(curs.fetchall()[0][0])
        resultname = 'Gal Gadot'
        print(resultname)
        self.filmnameLabel = Label(
            castselTk, text=resultname, font=('微软雅黑', 12), anchor=NW)
        self.filmnameLabel.place(x=370, y=120, width=230, height=30)
        # 从SQL数据库中获取演员的英文名

        castcountry = '''SELECT  castCountry FROM casts   WHERE castNameCN ='%s' ''' % s
        curs.execute(castcountry)
        resultcountry = str(curs.fetchall()[
                            0][0])

        self.countryLabel = Label(
            castselTk, text=resultcountry, font=('微软雅黑', 12), anchor=NW)
        self.countryLabel.place(x=370, y=170, width=370, height=40)
        # 从SQL数据库中获取演员的国家

        castbirth = '''SELECT  castBirthday FROM casts   WHERE castNameCN ='%s' ''' % s
        curs.execute(castbirth)
        resultbirth = str(curs.fetchall()[
                          0][0])
        self.birthLabel = Label(
            castselTk, text=resultbirth, font=('微软雅黑', 12), anchor=NW)
        self.birthLabel.place(x=370, y=210, width=370, height=40)
        # 从SQL数据库中获取演员的生日

        img = '''SELECT castURL FROM casts  WHERE castNameCN ='%s' ''' % s
        curs.execute(img)
        #resultimg = str(curs.fetchall()[0][0])
        # print(resultimg)
        #self.img_open = Image.open(resultimg)
        #self.img_png = ImageTk.PhotoImage(img_open)
        #self.castimage = Label(castselTk, bg='white',
                               #height=200, width=200, image=img_png)
        #self.castimage.place(x=110, y=70)
        # 从SQL数据库中获取演员的图片URL地址

        self.sclabel = Label(castselTk, text='评分',
                             font=('微软雅黑', 20), anchor=NW)
        self.sclabel.place(x=480, y=340, width=71, height=41)
        # Label“评分”

        castscore = '''SELECT  castRate FROM  casts  WHERE castNameCN ='%s' ''' % s
        curs.execute(castscore)
        #resultscore = str(curs.fetchall()[0][0])
        resultscore = '7.5'
        print(resultscore)
        self.scoreLabel = Label(castselTk, text=resultscore, font=(
            'Times New Roman', 34), anchor=NW)
        self.scoreLabel.place(x=490, y=390, width=80, height=80)
        # 从SQL数据库中获取演员的评分

        self.sclabel = Label(castselTk, text='我的评分',
                             font=('微软雅黑', 20), anchor=NW)
        self.sclabel.place(x=620, y=340, width=131, height=41)
        # Label“我的评分”

        self.scoreentry = Entry(castselTk, textvariable=StringVar(), text='0.0',
                                font=('Times New Roman', 34))  # entry 输入评分
        self.scoreentry.place(x=630, y=400, width=80, height=70)

        self.scoresubmit = Button(
            castselTk, text='提交', bg='red', fg='white')  # 查询Button
        self.scoresubmit.place(x=630, y=490, width=93, height=28)

        self.filmlabel = Label(castselTk, text='出演电影', font=('微软雅黑', 16))
        self.filmlabel.place(x=110, y=300, width=121, height=41)
        # Label“出演电影”

        #mvimg = '''SELECT imgURL FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
        #and castNameCN ='%s' ''' % s
        #curs.execute(mvimg)
        #resultmvimg = str(curs.fetchall()[0][0])
        #print(resultmvimg)
        #mvimg_open = Image.open(resultmvimg)
        #mvimg_png = ImageTk.PhotoImage(mvimg_open)
        #self.movieimage = Label(castselTk, bg='white',
                                #height=140, width=120, image=mvimg_png)
        #self.movieimage.place(x=110, y=360)
        # 从SQL数据库中获取电影的图片URL地址

        filmnameCN = '''SELECT  movieNameCN FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
        and castNameCN ='%s' ''' % s
        curs.execute(filmnameCN)
        nameCN = str(curs.fetchall()[
                     0][0])
        self.filmnameCNLabel = Label(castselTk, text=nameCN, font=(
            '微软雅黑', 18), anchor=NW)  # Label“标签”
        self.filmnameCNLabel.place(x=250, y=360, width=130, height=40)
        # 从SQL数据库中获取电影的中文名

        filmname = '''SELECT  movieName FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
        and castNameCN ='%s' ''' % s
        curs.execute(filmname)
        name = str(curs.fetchall()[0][0])
        self.filmnameLabel = Label(castselTk, text=name, font=(
            'Times New Roman', 12), anchor=NW)  # Label“标签”
        self.filmnameLabel.place(x=250, y=400, width=160, height=20)
        # 从SQL数据库中获取电影的英文名

        filmdate = '''SELECT  movieDate FROM casts,movies,castShow  WHERE casts.castId = castShow.castId and movies.movieId = castShow.movieId
               and castNameCN ='%s' ''' % s
        curs.execute(filmdate)
        date = str(curs.fetchall()[0][0])
        self.filmdateLabel = Label(castselTk, text=date, font=(
            'Times New Roman', 12), anchor=NW)  # Label“标签”
        self.filmdateLabel.place(x=250, y=430, width=130, height=40)
        # 从SQL数据库中获取电影的日期

        conn_info.close()


castselTk = Toplevel()
castselTk.title('演员详情')  # 设置窗口标题
castselTk.geometry('800x650')
castselapp = castsel(castselTk)
castselTk.mainloop()
