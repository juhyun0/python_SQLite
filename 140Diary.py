# -*- coding: utf-8 -*-

from datetime import datetime
import sqlite3
import wx
import wx.html2 #Webview
import ntpath #파일 이름 추출
import base64 #이미지 URI 인코딩

RECORD_PER_PAGE = 5

class MainFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init(self, None, title = "140자 일기장", size = wx.Size(715,655), style = wx.DEFAULT_FRAME_STYLE)
		self.MaxImageSize=200
		self.mainPnel=wx.Panel(self)

		#일기 입력창
		self.leftPanel=wx.Panel(self.mainPanel)
		self.leftPanel.SetMaxSize(wx.Size(200,-1))
		self.input_image_path=""
		self.inputTextCtrl=wx.TextCtrl(self.leftPanel, size=wx.Size(200,100), style=wx.TE_MULTILINE)

		self.inputTextCtrl.SetMaxLength(140) #일기 텍스트를 입력받는 위젯의 최대 텍스트 길이는 140
		self.inputTextCtrl.Bind(wx.EVT_TEXT, self.OnTypeText)
		self.lengthStaticText=wx.StaticText(self.leftPanel, style=wx.ALIGN_RIGHT)
		self.selectImageButton=wx.Button(self.leftPanel, label="이미지 추가")
		self.selectImageButton.Bind(wx.EVT_BUTTON, self.OnFindImageFile)
		self.imageStaticBitmap=wx.StaticBitmap(self.leftPanel)
		self.inputButton=wx.Button(self.leftPanel, label="저장")
		self.inputButton.Bind(wx.EVT_BUTTON, self.OnInputButton)

		#일기 표시 창
		self.rightPanel = wx.Panel(self.mainPanel)
		self.outputHtmlWnd=wx.html2.WebView.New(self.rightPanel)
		self.outputHymlWnd.Bind(wx.html2.EVT_WEBVIEW_NAVIGATING, self.OnNavigating)

		#위젯 배치
		leftPanelSizer=wx.StaticBoxSizer(
			wx.VERTICAL, self.leftPanel, "글 남기기")
		leftPanelSizer.Add(self.inputTextCtrl, 0, wx.ALL, 5)
		leftPanelSizer.Add(self.lengthStaticText, 0, wx.ALIGN_RIGHT|wx.RIGHT,5)
		leftPanelSizer.Add(self.selectImageButton, 0, wx.ALIGN_RIGHT|wx.RIGHT,5)
		leftPanelSizer.Add(self.imageStaticBitmap, 0, wx.ALIGN_RIGHT|wx.RIGHT,5)
		leftPanelSizer.Add(self.inputButton, 0, wx.ALIGN_RIGHT|wx.RIGHT,5)
		self.leftPanel.SetSizer(leftPanelSizer)

		htmlWndSizer=wx.GridSizer(1,1,0,0)
		htmlWndSizer.Add(self.outputHtmlWnd, 0, wx.ALL|wx.EXPAND, 5)

		self.rightPanel.SetSizer(htmlWndSizer)
		self.rightPanel.Layout()
		htmlWndSizer.Fit(self.rightPanel)

		mainSizer=wx.BoxSizer(wx.HORIZONTAL)
		mainSizer.Add(self.leftPanel, 1, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND,5)
		mainSizer.Add(self.rightPanel, 1, wx.ALL|wx.EXPAND, 5)
		self.mainPanel.SetSizer(mainSizer)
		self.Layout()

		#Database 초기화
		self.conn=sqlite3.connect("minutediary.db")
		self.cursor=self.conn.cursor()
		self.CheckSchema()
		self.LoadDiary(0)
		
