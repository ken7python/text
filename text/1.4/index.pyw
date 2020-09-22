n = ""
import subprocess
import wx
import os
import time
import tkinter,tkinter.filedialog,tkinter.messagebox
import codecs
import chardet
import sys

# -*- coding: utf-8 -*-
global hifa
hifa = ""
app = wx.App(False)
frame = wx.Frame(None,-1,"テキストエディタ",size=(1000,900))
panel = wx.Panel(frame,wx.ID_ANY)

fi = wx.TextCtrl(panel,-1,pos=(200,50),size=(800,50))
fi.Disable()
fontfi = wx.Font(15, wx.FONTFAMILY_DEFAULT, 
               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
fi.SetFont(fontfi)

def get_kousin(event):
    ls_file_name = os.listdir() 
    fi.Clear()
    for i in range(len(ls_file_name)):
        fi.AppendText(ls_file_name[i]+"  ")

def get_file():
    ls_file_name = os.listdir() 
    fi.Clear()
    for i in range(len(ls_file_name)):
        fi.AppendText(ls_file_name[i]+"  ")
def click_save_button(event):  # 保存ボタンをクリック時の動作
    if not hifa == "":
        data = codecs.open(hifa, "w" , hc)
        data.write(text.GetValue())
        data.close()
        get_file()
    else:
        tkinter.messagebox.showinfo("テキストエディタ","ファイルを開いていません")
def faop(ofa):
    # ファイルをオープンする
    global hifa
    hifa = ofa
    os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
    datak = codecs.open(hifa, "rb")
    data = codecs.open(hifa,"rb",chardet.detect(datak.read())['encoding'])
    global hc
    hc = chardet.detect(datak.read())['encoding']
    # すべての内容を読み込む
    contents = data.read()

    # すべての内容を表示する
    text.SetValue(contents)

    #ファイルをクローズする
    datak.close()
    data.close()
    fi.SetValue(hifa)
def fileopen(event):
    fTyp = [("","*")]
    iDir = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop"
    fl = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    faop(fl)
def komando(k):
    result = subprocess.run([k,str(os.path.split(hifa)[1])], stdout=subprocess.PIPE,encoding=hc)
    global kekka
    kekka = result.stdout
    koma.SetValue(kekka)
def zi(event):
    if str(os.path.splitext(hifa)[1]) == ".java":
        os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
        komando("java")
    if str(os.path.splitext(hifa)[1]) == ".py":
        os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
        komando("python")
    if str(os.path.splitext(hifa)[1]) == ".htm":
        os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
        subprocess.Popen(['start',str(hifa)], shell=True)
    if str(os.path.splitext(hifa)[1]) == ".html":
        os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
        subprocess.Popen(['start',str(hifa)], shell=True)
 
text = wx.TextCtrl(panel,pos=(200,100),size=(800,690), style=wx.TE_MULTILINE)
koma = wx.TextCtrl(panel,pos=(0,150),size=(200,400), style=wx.TE_MULTILINE)
koma.Disable()
save_button = wx.Button(panel, -1, pos=(10, 10), label='保存')
ofa_button = wx.Button(panel, -1, pos=(10, 50), label='ファイルを開く')
zikkou_button = wx.Button(panel, -1, pos=(10, 80), label='実行')
kou = wx.Button(panel,pos=(100,50),label="最新表示")

font = wx.Font(25, wx.FONTFAMILY_DEFAULT, 
               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
text.SetFont(font)
text.SetForegroundColour("#ffffff")
text.SetBackgroundColour('#333333')



get_file()

save_button.Bind(wx.EVT_BUTTON, click_save_button)
kou.Bind(wx.EVT_BUTTON, get_kousin)
zikkou_button.Bind(wx.EVT_BUTTON, zi)
ofa_button.Bind(wx.EVT_BUTTON, fileopen)


hn = len(sys.argv)
if (hn > 1):
    faop(sys.argv[1])



frame.Show()
    
app.MainLoop()