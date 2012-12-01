#!/usr/bin/env python

# focusevent.py

import wx
from wx import gizmos
import pygame
import os,sys

import wx, wx.html
import sys

import subprocess

from data import questions,catnames

class LED(wx.Panel):
    """
    create nice LED clock showing the current time
    """
    def __init__(self, parent, value):
        pos = wx.DefaultPosition
        wx.Panel.__init__(self, parent, -1)
        size = wx.DefaultSize
        style = gizmos.LED_ALIGN_CENTER
        self.led = gizmos.LEDNumberCtrl(self, -1, pos, size, style)
        self.led.SetValue(value)
        # default colours are green on black
        self.led.SetBackgroundColour("blue")
        self.led.SetForegroundColour("yellow")


aboutText = """<head bgcolor="blue></head><body><p>Sorry, there is no information about this program.<img
src="media/jeopardy_logo.jpg" It is
running on version %(wxpy)s of <b>wxPython</b> and %(python)s of <b>Python</b>.
See <a href="http://wiki.wxpython.org">wxPython Wiki</a></p></head>""" 

template= """<center>
<br>
<font color='white' size=4>
%s
</font>
</center>
"""
class HtmlWindow(wx.html.HtmlWindow):
    def __init__(self, parent, id, size=(600,400)):
        wx.html.HtmlWindow.__init__(self,parent, id, size=size)
        if "gtk2" in wx.PlatformInfo:
            self.SetStandardFonts()

    def OnLinkClicked(self, link):
        wx.LaunchDefaultBrowser(link.GetHref())

class Question(wx.Dialog):
    def __init__(self, pool='',idx=0, qa=0):
        wx.Dialog.__init__(self, None, -1, "About <<project>>",
            style=wx.DEFAULT_DIALOG_STYLE|wx.THICK_FRAME|wx.RESIZE_BORDER|
                wx.TAB_TRAVERSAL|wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL,
                size=wx.DisplaySize())
        hwin = HtmlWindow(self, -1, size=(400,200))
        hwin.SetFonts( '','',range(30,90,9))
        vers = {}
        vers["python"] = sys.version.split()[0]
        vers["wxpy"] = wx.VERSION_STRING
        #hwin.SetPage(aboutText % vers)
        hwin.pool = pool
        hwin.idx = idx
        self.qa = qa
        self.pool = pool
        self.idx = idx
        hwin.SetPage(template % questions[pool][idx][qa])
        btn = hwin.FindWindowById(wx.ID_OK)
        irep = hwin.GetInternalRepresentation()
        hwin.SetSize((irep.GetWidth()+25, irep.GetHeight()+10))
        hwin.SetForegroundColour('white')
        hwin.SetBackgroundColour('blue')
        x, y = self.GetSize()
        #box = wx.BoxSizer(wx.VERTICAL)
        #box.Add(hwin, 1, wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND |wx.ALL | wx.ALIGN_CENTER, 10)
        #self.SetSizer(box)

        #self.SetClientSize(hwin.GetSize())
        hwin.CentreOnParent(wx.BOTH)
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()
        self.Bind(wx.EVT_CHAR, self.OnKeyDown)
        self.hwin = hwin
        self.hwin.Bind(wx.EVT_CHAR, self.OnKeyDown)
        #self.Bind(wx.EVT_PAINT, self.OnPaint)

    def test(self):
        dlg = Question(self.pool, self.idx, 1)
        dlg.ShowModal()
        dlg.Destroy()  
        if len(questions[self.pool][self.idx]) > 2:
            dispatch = questions[self.pool][self.idx][2]
            if evt.GetKeyCode() in dispatch:
                dispatch[evt.GetKeyCode()]()

    def OnKeyDown(self, evt):
        if evt.GetKeyCode() == 121: #go to the answer ('y' pressed)
            subprocess.Popen(["mplayer","media/elevatording.wav"])
            dlg = Question(self.pool, self.idx, 1)
            dlg.ShowModal()
            dlg.Destroy()  
        elif evt.GetKeyCode() == 110: #go to the answer ('y' pressed) 
            subprocess.call(["mplayer","media/buzzerheavy.wav"])
        elif evt.GetKeyCode() == 108: #go to the answer ('y' pressed) 
            subprocess.call(["mplayer","media/cannedlaugh.mp3"])
        elif evt.GetKeyCode() == 106: #go to the answer ('y' pressed) 
            subprocess.call(["mplayer","media/jeopardymusic.flv"])
        if len(questions[self.pool][self.idx]) > 2:
            dispatch = questions[self.pool][self.idx][2]
            if evt.GetKeyCode() in dispatch:
                dispatch[evt.GetKeyCode()]()

        print evt.GetKeyCode() 
        #evt.Skip()
    #def OnPaint(self, event):
    #    x, y = self.GetSize()
    #    self.hwin.SetPosition((0,y/2))



class MyWindow(wx.Panel):
    def __init__(self, parent, name="", idx=-1):
        wx.Panel.__init__(self, parent, -1)
        self.idx = idx
        self.name = name
        
        box = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(box)
        self.box = box

        self.color = '#0000b3'
        self.SetBackgroundColour(self.color)
        if idx == -1:
            #self.text = wx.TextCtrl(self, -1, value=name)
            text = wx.StaticText(self, -1, name,  
                    style=wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL)
            text.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD))
            text.SetSize(text.GetBestSize())
            text.SetForegroundColour("white")
            self.text = text
        else:
            text = wx.StaticText(self, -1, str((self.idx+1)*100), 
                    #(50,50), 
                    #size=(100,100),
                    style=wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL)
            text.SetFont(wx.Font(40, wx.SWISS, wx.NORMAL, wx.BOLD))
            text.SetSize(text.GetBestSize())
            text.SetForegroundColour("yellow")
            text.SetBackgroundColour(self.color)
            self.text = text

            pass
            #size =  self.GetSize()
            #style = gizmos.LED_ALIGN_CENTER
            #pos = wx.DefaultPosition
            #self.led = LED(self, "100")

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.Bind(wx.EVT_SET_CURSOR, self.OnSetCursor)
        if self.idx != -1:
            self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
            self.text.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
            self.Bind(wx.EVT_RIGHT_DOWN, self.showPoints)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnKillFocus)
        box.Add(self.text, 1, wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND |wx.ALL | wx.ALIGN_CENTER, 10)
        #print self.text.GetSize(), '---', self.GetSize(), box.GetMinSizeTuple()

        self.Bind(wx.EVT_CHAR, self.OnKeyDown)
    def OnKeyDown(self, evt):
        if evt.GetKeyCode() == 121: #go to the answer ('y' pressed) 
            subprocess.Popen(["mplayer","media/elevatording.wav"])
        elif evt.GetKeyCode() == 110: #wrong answer ('n' pressed) 
            subprocess.call(["mplayer","media/buzzerheavy.wav"])
        elif evt.GetKeyCode() == 108: # make a canned laugh ('l' pressed) 
            subprocess.call(["mplayer","media/cannedlaugh.mp3"])
        elif evt.GetKeyCode() == 106: # play jeopardy music ('j' pressed) 
            subprocess.call(["mplayer","media/jeopardymusic.flv",])
        elif evt.GetKeyCode() == 'r' : # reload everything
            FocusEvent(None, -1, 'focus event')
    def showPoints(self,evt):
        self.text.SetLabel(str((self.idx+1)*100))

        print self.text.GetLabel()

    def OnPaint(self, event):
        pass
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen(self.color, 4))
        dc.SetBrush(wx.Brush('blue', 9))
        dc.SetBackground(wx.Brush(self.color))
        #dc.ClearBackground()
        dc.SetBackgroundMode(wx.TRANSPARENT)
        x, y = self.GetSize()
        dc.DrawRoundedRectangle(0, 0, x, y,11)
        tx, ty = self.text.GetSize()
        self.text.SetPosition((x/2-tx/2,y/2-ty/2.))
        #dc.FloodFill(0, 0,'blue', 0)

    def OnSize(self, event):
        x, y = self.GetSize()
        print self.name, ':\t', self.text.GetLabel()
        self.text.Wrap(x)
        self.Refresh()

    def OnSetFocus(self, event):
        self.color = '#0099f7'
        #sizeT = (640,480)
        #self.w = CircleWindow(self, -1, size = sizeT)
        #self.w.Show(1)
        self.Refresh()
    
    def OnSetCursor(self, event):
        self.color = '#FF0000'
        #sizeT = (640,480)
        #self.w = CircleWindow(self, -1, size = sizeT)
        #self.w.Show(1)
        self.Refresh()
    
    def OnMouseDown(self, event):
        self.color = '#FF0000'
        self.text.SetLabel("")
        dlg = Question(self.name, self.idx)
        # XXX: take the next line out after done testing questions
        dlg.test()
        dlg.ShowModal()
        dlg.Destroy()  
        #sizeT = (640,480)
        #self.w = CircleWindow(self, -1, size = sizeT)
        #self.w.Show(1)
        self.Refresh()

    def OnKillFocus(self, event):
        self.color = '#0000b3'
        self.Refresh()

class FocusEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(750, 850))
        self.SetBackgroundColour('black')
        #panel = wx.Panel(self, -1)

        catheads = [(MyWindow(self,x.upper()), 1, wx.EXPAND,9) for x in catnames]
        catheading = wx.GridSizer(1,len(catnames)  , 10, 10)
        #wx.BoxSizer(wx.HORIZONTAL)
        catheading.AddMany(catheads)

        #Cat1=  [(MyWindow(self,idx=x), 1, wx.EXPAND,9) for x in range(6)]
        #Cat2=  [(MyWindow(self,idx=x), 1, wx.EXPAND,9) for x in range(5)]
        #Cat3=  [(MyWindow(self,idx=x), 1, wx.EXPAND,9) for x in range(5)]
        #cats = [ Cat1, Cat2, Cat3]
        cats=[]
        for c in catnames:
            pbox = lambda x: (MyWindow(self,c,idx=x), 1, wx.EXPAND,9) 
            cats.append([pbox(x) for x in range(len(questions[c]))])

        maxcat = max([len(x) for x in cats])
        print maxcat

        #top = MyWindow(self)
        grid = wx.GridSizer(maxcat,len(cats)  , 10, 10)
        #grid = wx.GridSizer(len(cats), maxcat  , 10, 10)
        for cat in cats:
            #anel = wx.Panel(self, -1)
            box = wx.BoxSizer(wx.VERTICAL)
            box.AddMany(cat)
            #panel.SetSizer(box)
            grid.Add(box,1,wx.EXPAND,9) 
        
        biggrid = wx.BoxSizer(wx.VERTICAL)
        biggrid.Add(catheading, 2,wx.EXPAND , 20)
        biggrid.AddSpacer((10,10))
        biggrid.Add(grid, 15, wx.EXPAND, 9)
        
        #split1 = wx.SplitterWindow(self, -1,
        #    style=wx.SP_LIVE_UPDATE)
        ## set splitter window's direction and content
        ## top or left content first, then give initial sash position
        #split1.SplitVertically(top,top, 150)

        #panel = wx.Panel(self, -1)
        #panel.SetSizer(biggrid)
        #panel.Show(True)
        self.SetSizer(biggrid)
        self.Centre()
        self.Show(True)

app = wx.App()
FocusEvent(None, -1, 'focus event')
app.MainLoop()
