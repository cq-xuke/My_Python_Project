# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:52:40 2017

@author: cq_xuke
"""
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.font as tkFont
import os
import time
from tkinter.messagebox import *

root = Tk()
root.resizable(0, 0)
root.config(bg='#FFFAFA')
ssid = StringVar()
value = StringVar()
message = StringVar()
state = StringVar()
message.set('欢迎来到wifi热点小助手')
state.set('未建立虚拟wifi')


def createwin_disable():
    result = askyesno(title='禁用', message='禁用虚拟wifi后必须重新初试化才能开启wifi，是否继续？')
    if result == True:
        os.system('netsh wlan set hostednetwork mode=disallow')
        showwarning(title="禁用", message="禁用成功！")
        State()


# 初始化窗口
def createwin_init():
    win_init = Toplevel(root)
    win_init.title('初始化')
    win_init.resizable(0, 0)
    win_init.deiconify()
    frame1 = Frame(win_init)
    frame1.pack(padx=20, pady=4)

    label1 = Label(frame1, text='ssid: ', width=4, anchor=W)
    label1.grid(row=0, column=0)
    entry1 = Entry(frame1, textvariable=ssid, width=20)
    entry1.grid(row=0, column=1)
    entry1.focus()

    label2 = Label(frame1, text='key: ', width=4, anchor=W)
    label2.grid(row=1, column=0)
    entry2 = Entry(frame1, textvariable=value, width=20)
    entry2.grid(row=1, column=1)

    def reset():
        entry1.delete(0)
        ssid.set('')
        value.set('')
        label3.config(text='重置成功')

    def done():
        if not ssid.get() or not value.get():
            label3.config(text='请输入用户名或密码')
        else:
            op = init()
            if op == 0:
                label3.config(text='设置成功！')
            else:
                label3.config(text='设置失败！')

    fdown = Frame(win_init)
    fdown.pack()
    bt1 = Button(fdown, text='重置', command=reset)
    bt1.grid(row=1, column=1)

    bt2 = Button(fdown, text='确定', command=done)
    bt2.grid(row=1, column=2)
    label3 = Label(win_init)
    label3.pack()


def createwin_about():
    showinfo(title="关于 WIFI热点小助手",
             message="WIFI热点小助手 1.0.0\n作者：Cq_xuke\n发布时间：2017.10")


def createwin_intro():
    showinfo(title="说明",
             message="初试化后请打开网络和共享中心将虚拟wifi与已链接的网络建立共享；\n否则虚拟wifi无法链接网络；\n部分无线网卡不支持开启虚拟wifi")


# 主窗口
root.title("WIFI热点小助手")
open_wifi_cmd = "netsh wlan start hostednetwork"
close_wifi_cmd = "netsh wlan stop hostednetwork"
state_cmd = "netsh wlan show hostednetwork"


def show_result(how, cmd):
    result = os.system(cmd)
    if result != 0:
        if how == 1:
            message.set("请检查无线网卡是否打开，设置是否正确")
        else:
            message.set("关闭WIFI失败！")
    else:
        if how == 1:
            message.set("WIFI已打开")
            State()

        else:
            message.set("WIFI已关闭")
    State()


def open_wifi():
    cmd = open_wifi_cmd
    show_result(1, cmd)


def close_wifi():
    cmd = close_wifi_cmd
    show_result(0, cmd)


def State():
    s = os.popen(state_cmd)
    state.set(s.read().strip())


def init():
    os.system("netsh wlan set hostednetwork mode=allow")
    SSID = ssid.get()
    KEY = value.get()
    op = os.system('netsh wlan set hostednetwork ssid="%s" key="%s"' % (SSID, KEY))
    State()
    return op


labelframe = LabelFrame(root, bg='#778899', text='当前状态', font=('宋体', 11, 'bold'), relief=GROOVE, width=100, height=300)
labelframe.pack(padx=5, pady=2)
labe1 = Label(labelframe, fg='blue', bg='#F0F8FF', textvariable=message, width=40)
labe2 = Label(labelframe, justify='left', bg='#DCDCDC', textvariable=state, width=40, height=20)
labe1.pack()
labe2.pack()

frame = Frame(root)
frame.pack(pady=6)
Button1 = Button(frame, text='开启', command=open_wifi)
Button1.grid(row=1, column=1)
Button2 = Button(frame, text='关闭', command=close_wifi)
Button2.grid(row=1, column=2)
Button3 = Button(frame, text='刷新', command=State)
Button3.grid(row=1, column=3)

menubar = Menu(root)
root.config(menu=menubar)

option = Menu(menubar)
option.add_command(label='初始化', command=createwin_init)
option.add_command(label='禁用', command=createwin_disable)
option.add_command(label='退出', command=root.destroy)
menubar.add_cascade(label='选项', menu=option)

help_ = Menu(menubar)
help_.add_command(label='说明', command=createwin_intro)
help_.add_command(label='关于...', command=createwin_about)
menubar.add_cascade(label='帮助', menu=help_)
root.mainloop()
