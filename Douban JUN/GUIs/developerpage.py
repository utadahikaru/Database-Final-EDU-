from tkinter import *
from PIL import ImageTk,Image
import pyodbc

class developsel():
    def __init__(self,master):
        insinfTk=master
        mainloop()

developTk=Tk(className='开发者信息') #设置窗口标题
developTk.geometry('800x600')
developapp=developsel(developTk)
developTk.mainloop()