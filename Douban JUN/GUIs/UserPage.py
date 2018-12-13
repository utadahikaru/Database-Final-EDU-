from tkinter import *
from PIL import ImageTk, Image
import pymysql
import pyodbc


class usersel():
    def __init__(self, master):
        userselTk = master
        self.img = Image.open('C:\Database-Final-EDU-\Douban JUN\GUIs\\background2.jpg')
        self.imgphoto = ImageTk.PhotoImage(self.img)
        self.imgtext = Text(userselTk, width=800, height=650)
        self.imgtext.image_create(END, image=self.imgphoto)
        self.imgtext.place(x=0, y=0)
        self.usergetsel()
        mainloop()

    def usergetsel(self):
        s = "Diana"
        print('传递到的名字为' + s)
        conn_info = pyodbc.connect(
            'DRIVER={SQL Server};server=localhost;PORT=1433;database=DoubanJUN;user=sa;password=Junrupan9393')
        curs = conn_info.cursor()
        # 连接数据库
        print("database chongya!!!")
        mycolor='#215297'

        self.defaultLabel = Label(
            userselTk, text="用户名", font=('黑体', 20), anchor=NW,bg=mycolor,fg='white'
        )

        self.defaultLabel.place(x=360, y=80, width=90, height=40)

        self.usernameLabel = Label(
            userselTk, text=s, font=('微软雅黑', 40), anchor=NW,bg=mycolor,fg='white')
        self.usernameLabel.place(x=360, y=130, width=200, height=70)
        # 显示用户名

        img = '''SELECT imgURL FROM users  WHERE userName ='%s' ''' % s
        curs.execute(img)
        #userimg = curs.fetchone()[0]
        userimg = "C:\Database-Final-EDU-\Douban JUN\GUIs\cxk.jpg"
        self.userimgopen = Image.open(userimg)
        self.img_pnguser = ImageTk.PhotoImage(self.userimgopen)
        self.castimage = Label(userselTk, bg='white',
                               height=200, width=200, image=self.img_pnguser)
        self.castimage.place(x=100, y=70)
        # 从SQL数据库中获取user的图片URL地址

        self.seenMovies = Label(
            userselTk, text="我看过的电影", font=('微软雅黑', 15), anchor=NW,bg=mycolor,fg='white')
        self.seenMovies.place(x=100, y=290, width=130, height=34)

        #img2 = '''select movies.imgURL from usersSee,users,movies
        #where movies.movieId=usersSee.movieId
        #and
        #usersSee.userId = users.userId
        #and
        #userName='%s' ''' % s
        #curs.execute(img2)
        #seenimg = curs.fetchone()[0]
        seenimg = "C:\Database-Final-EDU-\Douban JUN\GUIs\duanbeishan2.jpg"
        self.userimgsee = Image.open(seenimg)
        self.uSee = ImageTk.PhotoImage(self.userimgsee)
        self.uSeeimage = Label(userselTk, bg='white',
                               height=100, width=100, image=self.uSee)
        self.uSeeimage.place(x=100, y=340)
        # 从SQL数据库中获取userSee的图片URL地址

        #movieSQL = '''select movies.movieNameCN from usersSee,users,movies
        #where movies.movieId=usersSee.movieId
        #and
        #usersSee.userId = users.userId
        #and
        #userName='%s' ''' % s
        #curs.execute(movieSQL)
        #movieName = curs.fetchone()[0]
        movieName='Brokeback Mountain'
        self.movieNameLabel = Label(
            userselTk, text=movieName, font=('微软雅黑', 15), anchor=NW,bg=mycolor,fg='white')
        self.movieNameLabel.place(x=250, y=340, width=260, height=40)

        #rateSQL = '''select userRate from usersSee,users
        #where usersSee.userId = users.userId
        #and
        #userName='%s' ''' % s
        #curs.execute(rateSQL)
        #movieRate = curs.fetchone()[0]
        movieRate = "8.5"
        self.movieRateLabel = Label(
            userselTk, text=movieRate, font=('Times New Roman', 30), anchor=NW,bg=mycolor,fg='white')
        self.movieRateLabel.place(x=250, y=390, width=80, height=50)

        self.lovecasts = Label(
            userselTk, text="我喜欢的影星", font=('微软雅黑', 15), anchor=NW,bg=mycolor,fg='white')
        self.lovecasts.place(x=100, y=470, width=130, height=36)

        #img3 = '''select casts.castURL from usersLove,users,casts
        #where casts.castId=usersLove.castId
        #and
        #usersLove.userId = users.userId
        #and
        #userName='%s' ''' % s
        #curs.execute(img3)
        #castimg = curs.fetchone()[0]
        castimg = "C:\Database-Final-EDU-\Douban JUN\GUIs\\annehatheway.jpeg"
        self.usercast = Image.open(castimg)
        self.uLov = ImageTk.PhotoImage(self.usercast)
        self.uLovimage = Label(userselTk, bg='white',
                               height=100, width=100, image=self.uLov)
        self.uLovimage.place(x=100, y=520)

        #castSQL = '''select casts.castNameCN from usersLove,users,casts
        #where casts.castId=usersLove.castId
        #and
        #usersLove.userId = users.userId
        #and
        #userName='%s' ''' % s
        #curs.execute(castSQL)
        #castName = curs.fetchone()[0]
        castName = "安妮 海瑟薇"
        self.castNameLabel = Label(
            userselTk, text=castName, font=('微软雅黑', 15), anchor=NW,bg=mycolor,fg='white')
        self.castNameLabel.place(x=250, y=520, width=160, height=40)

        #rateSQL = '''select userLoveRate from usersLove,users
        #where usersLove.userId = users.userId
        #and 
        #userName='%s' ''' % s
        #curs.execute(rateSQL)
        #castRate = curs.fetchone()[0]
        castRate = "9.7"
        self.castRateLabel = Label(
            userselTk, text=castRate, font=('Times New Roman', 30), anchor=NW,bg=mycolor,fg='white')
        self.castRateLabel.place(x=250, y=570, width=80, height=50)

        conn_info.close()


userselTk = Toplevel()
userselTk.title('个人主页')
userselTk.geometry('800x650')
couselapp = usersel(userselTk)
userselTk.mainloop()
