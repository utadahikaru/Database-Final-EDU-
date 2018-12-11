from tkinter import *
from PIL import ImageTk, Image
import pymysql


class usersel():
    def __init__(self, master):
        userselTk = master
        self.usergetsel()

        mainloop()

    def usergetsel(self):
        s = "JUN"
        print('传递到的名字为' + s)
        conn_info = pymysql.connect(
            "localhost", "test", "testnimabi", "DOUBAN_JUN")
        curs = conn_info.cursor()
        # 连接数据库
        print("database chongya!!!")

        self.defaultLabel = Label(
            userselTk, text="用户名", font=('黑体', 20), anchor=NW
        )

        self.defaultLabel.place(x=350, y=80, width=100, height=50)

        self.usernameLabel = Label(
            userselTk, text=s, font=('微软雅黑', 80), anchor=NW)
        self.usernameLabel.place(x=360, y=130, width=500, height=100)
        # 显示用户名

        img = '''SELECT imgURL FROM users  WHERE userName ='%s' ''' % s
        curs.execute(img)
        userimg = curs.fetchone()[0]
        #userimg = "Douban JUN/GUIs/cxk.jpg"
        self.userimgopen = Image.open(userimg)
        self.img_pnguser = ImageTk.PhotoImage(self.userimgopen)
        self.castimage = Label(userselTk, bg='white',
                               height=200, width=200, image=self.img_pnguser)
        self.castimage.place(x=100, y=70)
        # 从SQL数据库中获取user的图片URL地址

        self.seenMovies = Label(
            userselTk, text="我看过的电影", font=('微软雅黑', 15), anchor=NW)
        self.seenMovies.place(x=100, y=250, width=500, height=100)

        img2 = '''select movies.imgURL from usersSee,users,movies
        where movies.movieId=usersSee.movieId
        and
        usersSee.userId = users.userId
        and
        userName='%s' ''' % s
        curs.execute(img2)
        seenimg = curs.fetchone()[0]
        #seenimg = "Douban JUN/GUIs/duanbeishan.jpeg"
        self.userimgsee = Image.open(seenimg)
        self.uSee = ImageTk.PhotoImage(self.userimgsee)
        self.uSeeimage = Label(userselTk, bg='white',
                               height=100, width=100, image=self.uSee)
        self.uSeeimage.place(x=100, y=280)
        # 从SQL数据库中获取userSee的图片URL地址

        movieSQL = '''select movies.movieNameCN from usersSee,users,movies
        where movies.movieId=usersSee.movieId
        and
        usersSee.userId = users.userId
        and
        userName='%s' ''' % s
        curs.execute(movieSQL)
        movieName = curs.fetchone()[0]
        self.movieNameLabel = Label(
            userselTk, text=movieName, font=('微软雅黑', 15), anchor=NW)
        self.movieNameLabel.place(x=210, y=285, width=500, height=100)

        rateSQL = '''select userRate from usersSee,users
        where usersSee.userId = users.userId
        and 
        userName='%s' ''' % s
        curs.execute(rateSQL)
        movieRate = curs.fetchone()[0]
        #movieRate = "8.5"
        self.movieRateLabel = Label(
            userselTk, text=movieRate, font=('微软雅黑', 20), anchor=NW)
        self.movieRateLabel.place(x=210, y=340, width=500, height=100)

        self.lovecasts = Label(
            userselTk, text="我喜欢的影星", font=('微软雅黑', 15), anchor=NW)
        self.lovecasts.place(x=100, y=370, width=370, height=100)

        img3 = '''select casts.castURL from usersLove,users,casts
        where casts.castId=usersLove.castId
        and
        usersLove.userId = users.userId
        and
        userName='%s' ''' % s
        curs.execute(img3)
        castimg = curs.fetchone()[0]
        #castimg = "Douban JUN/GUIs/annehatheway.jpeg"
        self.usercast = Image.open(castimg)
        self.uLov = ImageTk.PhotoImage(self.usercast)
        self.uLovimage = Label(userselTk, bg='white',
                               height=100, width=100, image=self.uLov)
        self.uLovimage.place(x=100, y=400)

        castSQL = '''select casts.castNameCN from usersLove,users,casts
        where casts.castId=usersLove.castId
        and
        usersLove.userId = users.userId
        and
        userName='%s' ''' % s
        curs.execute(castSQL)
        castName = curs.fetchone()[0]
        #castName = "安妮 海瑟薇"
        self.castNameLabel = Label(
            userselTk, text=castName, font=('微软雅黑', 15), anchor=NW)
        self.castNameLabel.place(x=210, y=405, width=500, height=100)

        rateSQL = '''select userLoveRate from usersLove,users
        where usersLove.userId = users.userId
        and 
        userName='%s' ''' % s
        curs.execute(rateSQL)
        castRate = curs.fetchone()[0]
        #castRate = "9.7"
        self.castRateLabel = Label(
            userselTk, text=castRate, font=('微软雅黑', 20), anchor=NW)
        self.castRateLabel.place(x=210, y=460, width=500, height=100)

        conn_info.close()


userselTk = Toplevel()

userselTk.geometry('600x600')
couselapp = usersel(userselTk)
userselTk.mainloop()
