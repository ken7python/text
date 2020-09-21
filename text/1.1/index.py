n = ""
import wx
import os
import time
import tkinter, tkinter.filedialog, tkinter.messagebox
import chardet
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
    data = open(hifa, "w")
    data.write(text.GetValue())
    data.close()
    get_file()
def faop(ofa):
    # ファイルをオープンする
    global hifa
    hifa = ofa
    data = open(hifa, "rb")
    # すべての内容を読み込む
    contents = data.read()

    # すべての内容を表示する
    text.SetValue(contents)

    #ファイルをクローズする
    data.close()
    fi.SetValue(hifa)
def fileopen(event):
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    faop(file)
    
    
text = wx.TextCtrl(panel,pos=(200,100),size=(800,690), style=wx.TE_MULTILINE)
save_button = wx.Button(panel, -1, pos=(10, 10), label='保存')
ofa_button = wx.Button(panel, -1, pos=(10, 50), label='ファイルを開く')
st = wx.StaticText(panel,-1,"ファイルの名前",pos=(100,15))
fn = wx.TextCtrl(panel,pos=(170,10))
kou = wx.Button(panel,pos=(100,50),label="最新表示")

font = wx.Font(25, wx.FONTFAMILY_DEFAULT, 
               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
text.SetFont(font)
text.SetForegroundColour("#ffffff")
text.SetBackgroundColour('#333333')



get_file()


save_button.Bind(wx.EVT_BUTTON, click_save_button)
kou.Bind(wx.EVT_BUTTON, get_kousin)
ofa_button.Bind(wx.EVT_BUTTON, fileopen)

frame.Show()
    
app.MainLoop()