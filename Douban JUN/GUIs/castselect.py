from tkinter import *
from PIL import ImageTk, Image
import pymysql


class castsel():
    def __init__(self, master):
        castselTk = master
        castselTk = master
        self.castentry = Entry(castselTk, textvariable=StringVar(
        ), text='请输入演员名称：', font=('Times New Roman', 12))  # Label“请输入电影名称”
        self.castentry.place(x=220, y=50, width=300, height=35)
        self.castselbt1 = Button(
            castselTk, text='查询', command=self.castgetsel, bg='green', fg='white')  # 查询Button
        self.castselbt1.place(x=560, y=50, width=100, height=35)

        mainloop()


castselTk = Toplevel()
castselTk.title('演员查询')  # 设置窗口标题
castselTk.geometry('800x650')
castselapp = castsel(castselTk)
castselTk.mainloop()
