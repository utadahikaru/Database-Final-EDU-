from tkinter import *
from PIL import ImageTk, Image
import pymysql


class castselect():
    def __init__(self, master):
        castselectTk = master
        filmselTk = master
        self.img = Image.open('C:\Database-Final-EDU-\Douban JUN\GUIs\\background2.jpg')
        self.imgphoto = ImageTk.PhotoImage(self.img)
        self.imgtext = Text(filmselTk, width=800, height=650)
        self.imgtext.image_create(END, image=self.imgphoto)
        self.imgtext.place(x=0, y=0)
        self.castentry = Entry(castselectTk, textvariable=StringVar(
        ), text='请输入演员名称：', font=('Times New Roman', 12),bg='white')  # Label“请输入电影名称”
        self.castentry.place(x=220, y=50, width=300, height=35)
        self.castselectbt1 = Button(
            castselectTk, text='查询', command=self.directtocast, bg='green', fg='white')  # 查询Button
        self.castselectbt1.place(x=560, y=50, width=100, height=35)

        mainloop()

    def directtocast(self):
        #actornameCN = self.actorLabelCN.cget("text")
        actornameCN = self.castentry.get()
        print(actornameCN)
        import castpage
        castpage.castsel(actornameCN)

    def castgetsel(self):
        s = self.castentry.get()
        try:
            print("database chongya!!!")
            conn_info = pymysql.connect(
                "localhost", "test", "testnimabi", "DOUBAN_JUN")
            curs = conn_info.cursor()
            # 连接数据库
            print("database chongya!!!")

            conn_info.close()

        except:
            print("lljbd")

        return 0


castselectTk = Toplevel()
castselectTk.title('演员查询')  # 设置窗口标题
castselectTk.geometry('800x650')
castselectapp = castselect(castselectTk)
castselectTk.mainloop()
