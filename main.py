import tkinter as tk
import tkinter.messagebox as mbox
from sys import path
from time import time
from tkinter import filedialog

from pyexpat.errors import messages

import name
from name import get_name, path_excel,namedirect
from randoma import read_excel, make_random
from threading import Timer

root = tk.Tk()
root.title("简易点名小程序")
root.geometry("900x500")
mbox.showinfo("通知",message="本软件完全免费并开源，如果您花了钱，\n那么说明您上当了")

def hit_me():
    namedirect.clear()
    if t.get()=="":
        mbox.showinfo("别耍我",message="群聊名不能为空")
    else:
        get_name(t.get())
        mbox.showinfo("已完成",message="已完成")
def hit_me2():
    folder_path = filedialog.askdirectory(title="请选择文件夹")
    if folder_path:
        t1.delete(0, tk.END)
        t1.insert(0, folder_path)

def hit_me3():
    if t2.get() == "" or t1.get() == "":
        mbox.showinfo("别耍我", message="文件名不能为空")
    else:
        path_excel(csvname=t2.get(),path=t1.get())
        mbox.showinfo("已按当前路径生成",message="已完成")



def hit_me4():
    folder_path = filedialog.askopenfilename(title="请选择文件")
    if folder_path:
        t3.delete(0, tk.END)
        t3.insert(0, folder_path)
        read_excel(t3.get())


def hit_me5():
    l4.configure(text=make_random())





# 控件元素（两行同一套 column：标签 | 输入框 | 按钮）
l = tk.Label(root, text="请输入群聊名,以此获得群成员名：", font=("Arial", 10, "bold"), width=25, height=1)
l1 = tk.Label(root, text="点击边上按钮，请选择文件夹：", font=("Arial", 10, "bold"), width=25, height=1)
l2=tk.Label(root, text="输入文件名：", font=("Arial", 10, "bold"), width=25, height=1)
l3=tk.Label(root, text="选择需要点名的名单：", font=("Arial", 10, "bold"), width=25, height=1)
l4 = tk.Label(root, text="暂未开始点名", font=("Arial", 30, "bold"), width=25, height=3)

t = tk.Entry(root, show=None, font=("Arial", 15, "bold"), width=15)
t1 = tk.Entry(root, show=None, font=("Arial", 15, "bold"), width=15)
t2 = tk.Entry(root, show=None, font=("Arial", 15, "bold"), width=15)
t3 = tk.Entry(root, show=None, font=("Arial", 15, "bold"), width=20)


b1 = tk.Button(root, text="获取", width=10, height=2, command=hit_me)
b2 = tk.Button(root, text="浏览", width=10, height=2, command=hit_me2)
b3 = tk.Button(root,text="生成", width=10, height=2, command=hit_me3)#等会调用name文件
b4= tk.Button(root,text="选择文件", width=10, height=2, command=hit_me4)
b5=tk.Button(root,text="开点", width=50, height=2, command=hit_me5)#等会利用读取到的csv产生随机数

# 渲染：两行 column 对齐（0=标签 1=输入 2=按钮）
l.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
t.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
b1.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
l1.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
l2.grid(row=2, column=0, padx=5, pady=5, sticky=tk.EW)
l3.grid(row=3, column=0, padx=5, pady=5, sticky=tk.EW)
l4.grid(row=5, column=1, padx=5, pady=5, sticky=tk.EW)

t1.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
b2.grid(row=1, column=2, padx=5, pady=5, sticky=tk.EW)
t2.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
t3.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)
b3.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)
b4.grid(row=3, column=2, padx=5, pady=5, sticky=tk.EW)
b5.grid(row=4, column=1, padx=5, pady=5, sticky=tk.EW)
root.columnconfigure(1, weight=1)
root.mainloop()