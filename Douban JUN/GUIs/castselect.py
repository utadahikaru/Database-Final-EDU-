from tkinter import *
from PIL import ImageTk,Image
import pyodbc
import pymysql

class castsel():
    def __init__(self,master):
        castselTk=master
        mainloop()



castselTk = Toplevel()
castselTk.title('演员查询') #设置窗口标题
castselTk.geometry('800x650')
castselapp=castsel(castselTk)
castselTk.mainloop()