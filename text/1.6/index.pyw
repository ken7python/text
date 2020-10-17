n = ""
import subprocess
import wx
import os
from tkinter import filedialog
import tkinter as tk
import codecs
import chardet
import sys

# -*- coding: utf-8 -*-
root=tk.Tk()
root.withdraw()
global hifa
global kekka
global er
global hifo
hifo = ""
er = 0
hifa = ""
app = wx.App(False)
frame = wx.Frame(None,-1,"テキストエディタ",size=(1000,900))
panel = wx.Panel(frame,wx.ID_ANY)

fi = wx.TextCtrl(panel,-1,pos=(200,50),size=(800,50))
fi.Disable()
fontfi = wx.Font(15, wx.FONTFAMILY_MODERN,
               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL ,False,u'Consolas')
fi.SetFont(fontfi)

os.chdir(os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop")
 
text = wx.TextCtrl(panel,pos=(200,100),size=(800,690), style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB)


global koma
koma = wx.TextCtrl(panel,pos=(0,150),size=(200,400), style=wx.TE_MULTILINE)
font = wx.Font(10, wx.FONTFAMILY_MODERN,
               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL ,False,u'Consolas')
koma.SetFont(font)
#koma.Disable()
save_button = wx.Button(panel, -1, pos=(10, 10), label='保存')
ofa_button = wx.Button(panel, -1, pos=(10, 50), label='ファイルを開く')
ofo_button = wx.Button(panel, -1, pos=(10, 80), label='フォルダを開く')
zikkou_button = wx.Button(panel, -1, pos=(10, 110), label='実行')
kou = wx.Button(panel,pos=(100,50),label="最新表示")

font = wx.Font(20, wx.FONTFAMILY_MODERN,
               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL ,False,u'Consolas')
text.SetFont(font)
text.SetForegroundColour("#ffffff")
text.SetBackgroundColour('#333333')

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
        wx.MessageBox(u'ファイルを開いていません', u'テキストエディタ', wx.OK)
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
    if hifo == "":
        iDir = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop"
    else:
        iDir = hifo
    fl = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    faop(fl)
def komando(k):
    er = 0
    result = subprocess.run([k,str(os.path.split(hifa)[1])],stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='shift_jis')
    if result.stderr == "":
        er = 0
        kekka = result.stdout
        if str(os.path.splitext(hifa)[1]) == ".java":
            name = os.path.splitext(os.path.basename(os.path.split(hifa)[1]))[0]
            result = subprocess.run(['java',name], stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='shift_jis')
            if not result.stderr == "":
                er = 1
                kekka = result.stderr
            koma.SetValue(kekka)
        else:
            name = str(os.path.split(hifa)[1])
        if er == 0:
            kekka = result.stdout
            koma.SetValue(kekka)
    else:
        kekka = result.stderr
        koma.SetValue(kekka)

def folder_open(event):
    iDir = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop"
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    os.chdir(iDirPath)
    global hifo
    hifo = iDirPath
    text.Value = ""
    get_file()

def zi(event):
    if not hifa == "":
        if str(os.path.splitext(hifa)[1]) == ".java":
            os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
            komando("javac")
        if str(os.path.splitext(hifa)[1]) == ".py":
            os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
            komando("python")
        if str(os.path.splitext(hifa)[1]) == ".htm":
            os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
            subprocess.Popen(['start',str(hifa)], shell=True)
        if str(os.path.splitext(hifa)[1]) == ".html":
            os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
            subprocess.Popen(['start',str(hifa)], shell=True)
        if str(os.path.splitext(hifa)[1]) == ".r":
            os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
            komando('Rscript')
        if str(os.path.splitext(hifa)[1]) == ".rb":
            os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
            komando('Ruby')
        if str(os.path.splitext(hifa)[1]) == ".go":
            os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
            result = subprocess.run(['go','run',str(hifa)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='shift_jis', shell=True)
            if not result.stderr == "":
                kekka = result.stderr
                koma.SetValue(kekka)
            else:
                kekka = result.stdout
                koma.SetValue(kekka)
        if str(os.path.splitext(hifa)[1]) == ".c":
            os.chdir(str(os.path.dirname(os.path.abspath(hifa))))
            komando('gcc')
            result = subprocess.run(['a.exe'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='shift_jis')
            if not result.stderr == "":
                kekka = result.stderr
                koma.SetValue(kekka)
            else:
                kekka = result.stdout
                koma.SetValue(kekka)
            
            
    else:
        wx.MessageBox(u'ファイルを開いていません', u'テキストエディタ', wx.OK)


get_file()

save_button.Bind(wx.EVT_BUTTON, click_save_button)
kou.Bind(wx.EVT_BUTTON, get_kousin)
zikkou_button.Bind(wx.EVT_BUTTON, zi)
ofa_button.Bind(wx.EVT_BUTTON, fileopen)
ofo_button.Bind(wx.EVT_BUTTON, folder_open)

hn = len(sys.argv)
if (hn > 1):
    faop(sys.argv[1])

frame.Show()
    
app.MainLoop()