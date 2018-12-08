from tkinter import *
from PIL import ImageTk,Image
import pyodbc
import pymysql

class filmsel():
    def __init__(self,master):
        filmselTk=master



        #
        self.filmentry = Entry(filmselTk,textvariable=StringVar(),text='请输入电影名称：',font=('Times New Roman', 12)) #Label“请输入电影名称”
        self.filmentry.place(x=220, y=50, width=300, height=35)
        self.filmselbt1 = Button(filmselTk, text='查询', command=self.etgetsel,bg='green', fg='white') #查询Button
        self.filmselbt1.place(x=560, y=50, width=100, height=35)
        # self.filmnameCN = Label(filmselTk, text='', font=('Times New Roman', 16)) #Label电影中文名称
        # self.filmnameCN.place(x=340, y=120, width=370, height=40)
        # self.filmname = Label(filmselTk,text='', font=('Times New Roman', 12))  #Label电影英文名称
        # self.filmname.place(x=340, y=160, width=370, height=40)
        #
        # self.filmactrole = Label(filmselTk, text='', font=('Times New Roman', 11)) #Label演员饰演角色



        mainloop()

    def directtocast(self):
        actornameCN = self.actorLabelCN.cget("text")
        print(actornameCN)
        import castpage
        castpage.castsel(actornameCN)



    def etgetsel(self):
        s = self.filmentry.get()
        try:
            conn_info = pyodbc.connect(
                        'DRIVER={SQL Server};server=localhost;PORT=1433;database=DoubanJUN;user=sa;password=Junrupan9393')
            curs = conn_info.cursor()
            #连接数据库
            print("database chongya!!!")
            filmnameCN = '''SELECT  movieNameCN FROM movies   WHERE movieNameCN ='%s' ''' % s
            if curs.execute(filmnameCN).fetchall() != []:
                nameCN = str(curs.execute(filmnameCN).fetchall()[0]).replace("('", "").replace("', )", "")
                self.filmnameCNLabel = Label(filmselTk, text=nameCN, font=('微软雅黑', 20), anchor=NW)  # Label“标签”
                self.filmnameCNLabel.place(x=320, y=100, width=150, height=40)
            #从SQL数据库中获取电影的中文名

            filmname = '''SELECT  movieName FROM movies   WHERE movieNameCN ='%s' ''' % s

            name = str(curs.execute(filmname).fetchall()[0]).replace("('", "").replace("', )", "")
            self.filmnameLabel = Label(filmselTk, text=name, font=('Times New Roman', 16), anchor=NW)  # Label“标签”
            self.filmnameLabel.place(x=320, y=150, width=150, height=30)
            # 从SQL数据库中获取电影的英文名

            filmclass = '''SELECT  movieclass FROM movies   WHERE movieNameCN ='%s' ''' % s
            fmclass = str(curs.execute(filmclass).fetchall()[0]).replace("('", "").replace("', )", "")
            self.filmclassLabel = Label(filmselTk, text=fmclass, font=('Times New Roman', 16), anchor=NW)  # Label“标签”
            self.filmclassLabel.place(x=320, y=190, width=150, height=30)
            # 从SQL数据库中获取电影的类别

            filmdate = '''SELECT  movieDate FROM movies   WHERE movieNameCN ='%s' ''' % s
            date = str(curs.execute( filmdate).fetchall()[0]).replace("('", "").replace("', )", "")
            self.filmdateLabel = Label(filmselTk, text=date, font=('Times New Roman', 16), anchor=NW)  # Label“标签”
            self.filmdateLabel.place(x=550, y=190, width=150, height=30)
            # 从SQL数据库中获取电影的时间

            actorCN = '''SELECT  casts.castNameCN FROM  castShow,casts,movies   
                           WHERE castShow.castId = casts.castId and castShow.movieId = movies.movieId 
                           and movieNameCN ='%s' ''' % s
            resultactorCN = str(curs.execute(actorCN).fetchall()[0]).replace("('", "").replace("', )", "")
            self.actorLabelCN = Label(filmselTk, text=resultactorCN, font=('Times New Roman', 14),anchor=NW)  # Label“标签”
            self.actorLabelCN.place(x=500, y=260, width=230, height=40)
            # 从SQL数据库中获取演员中文名

            actor = '''SELECT  casts.castName FROM  castShow,casts,movies   
                        WHERE castShow.castId = casts.castId and castShow.movieId = movies.movieId 
                        and movieNameCN ='%s' ''' % s
            resultactor = str(curs.execute(actor).fetchall()[0]).replace("('", "").replace("', )", "")
            self.actorLabel = Label(filmselTk, text=resultactor, font=('Times New Roman', 12),anchor=NW)  # Label“标签”
            self.actorLabel.place(x=500, y=290, width=230, height=40)
            # 从SQL数据库中获取演员英文名


            score = '''SELECT  movies.movieRate FROM  movies   
                                        WHERE movieNameCN ='%s' ''' % s
            resultscore = curs.execute(score).fetchall()
            # 从SQL数据库中获取电影的评分

            self.scoreCN = Label(filmselTk, text='评分', font=('微软雅黑', 20))  # Label“标签”
            self.scoreCN.place(x=140, y=430, width=71, height=41)
            self.score = Label(filmselTk, text='0.0', font=('微软雅黑', 34))  # Label 电影评分
            self.score.place(x=130, y=480, width=81, height=81)
            self.scoreCN = Label(filmselTk, text='我的评分', font=('微软雅黑', 20))  # Label“标签”
            self.scoreCN.place(x=610, y=420, width=120, height=41)
            self.scoreentry = Entry(filmselTk, textvariable=StringVar(), text='0.0',
                                   font=('Times New Roman', 34))  # entry 输入评分
            self.scoreentry.place(x=630, y=480, width=80, height=70)
            self.scoresubmit = Button(filmselTk, text='提交', bg='red', fg='white')  # 查询Button
            self.scoresubmit.place(x=630, y=570, width=93, height=28)
            self.filmact = Label(filmselTk, text='主演', font=('微软雅黑', 14), anchor=NW)  # Label“主演”
            self.filmact.place(x=340, y=230, width=70, height=40)

            self.castpagebt = Button(filmselTk, text='演员表跳转', command=self.directtocast, bg='green', fg='white')  # 查询Button
            self.castpagebt.place(x=260, y=250, width=100, height=35)

            img = '''SELECT imgURL FROM movies  WHERE movieNameCN ='%s' '''%s
            resultimg = str(curs.execute(img).fetchall()[0]).replace("('", "").replace("', )", "")
            print(resultimg)
            img_open = Image.open(resultimg)
            img_png = ImageTk.PhotoImage(img_open)
            self.filmimage = Label(filmselTk, bg='white', height=280, width=210, image=img_png)
            self.filmimage.place(x=70, y=120)
            # self.filmimage.pack()
            # 从SQL数据库中获取电影的图片URL地址

            actimg1 = '''SELECT castURL FROM casts,castShow,movies  WHERE casts.castId = castShow.castId and castShow.movieId = movies.movieId and movieNameCN ='%s' ''' % s
            actimg1 = str(curs.execute(actimg1).fetchall()[0]).replace("('", "").replace("', )", "")
            print(actimg1)
            actimg1_open = Image.open(actimg1)
            actimg1_png = ImageTk.PhotoImage(actimg1_open)
            print(actimg1_png)
            self.actimage = Label(filmselTk, bg='white', height=130, width=130,image=actimg1_png)
            self.actimage.place(x=340, y=260)
            # self.actimage.pack()
            # 从SQL数据库中获取演员的图片URL地址

            self.actimage.delete(0.0, END)
            self.actimage.insert(1.0, '没有该电影信息')
            # if nameCN==[]:
            #     self.filmseltx1.delete(0.0, END)
            #     self.filmseltx1.insert(1.0, '没有该电影信息')
            #     conn_info.close()
            # else:
            #     print(1)
            #     self.filmnameCN.delete(0.0, END)
            #     self.filmnameCN.insert(1.0, filmnameCN)   # 插入该电影的中文名字
            #     # self.filmname.delete(0.0, END)
            #     # self.filmname.insert(1.0, filmname)         # 插入该电影的名字
            #     # self.actname.delete(0.0, END)
            #     # self.actname.insert(1.0, resultactor)       #插入演员的名字
            #     # self.score.delete(0.0, END)
            #     # self.score.insert(1.0, resultscore)       #插入该电影的评分


            conn_info.close()
        except:
                print("lljbd")
                self.filmnameCNLabel.delete(0.0,END)
                self.filmnameCNLabel.insert(1.0,'连接数据库失败')

        return resultactorCN


filmselTk = Toplevel()
filmselTk.title('电影查询') #设置窗口标题
filmselTk.geometry('800x650')
filmselapp=filmsel(filmselTk)
filmselTk.mainloop()