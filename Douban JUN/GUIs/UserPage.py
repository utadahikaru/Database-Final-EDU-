from tkinter import *
from PIL import ImageTk,Image
import pyodbc

class usersel():
    def __init__(self,master):
        couselTk=master
        mainloop()


userselTk=Tk(className='个人主页') #设置窗口标题
userselTk.geometry('600x600')
couselapp=usersel(userselTk)
userselTk.mainloop()