# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class GoBangFrame
###########################################################################

class GoBangFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"五子棋", pos = wx.DefaultPosition, size = wx.Size( 500,421 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer3 = wx.GridSizer( 10, 10, 0, 0 )
		
		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		self.m_radioBtn2.Set(wx.RED_BRUSH)
		gSizer3.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
		
		self.m_radioBtn21 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		
		self.m_radioBtn21.SetBackgroundColour("#Fa74f7")
		#self.m_radioBtn21.SetForegroundColour("#0a74f7")
		#self.m_radioBtn21.SetOwnForegroundColour("#0a74f7")
		gSizer3.Add( self.m_radioBtn21, 0, wx.ALL, 5 )
		
		self.m_radioBtn22 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn22, 0, wx.ALL, 5 )
		self.m_radioBtn22.Set
		self.m_radioBtn23 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn23, 0, wx.ALL, 5 )
		
		self.m_radioBtn24 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn24, 0, wx.ALL, 5 )
		
		self.m_radioBtn25 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn25, 0, wx.ALL, 5 )
		
		self.m_radioBtn26 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn26, 0, wx.ALL, 5 )
		
		self.m_radioBtn27 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn27, 0, wx.ALL, 5 )
		
		self.m_radioBtn28 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn28, 0, wx.ALL, 5 )
		
		self.m_radioBtn29 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn29, 0, wx.ALL, 5 )
		
		self.m_radioBtn210 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn210, 0, wx.ALL, 5 )
		
		self.m_radioBtn211 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn211, 0, wx.ALL, 5 )
		
		self.m_radioBtn212 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn212, 0, wx.ALL, 5 )
		
		self.m_radioBtn213 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn213, 0, wx.ALL, 5 )
		
		self.m_radioBtn214 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn214, 0, wx.ALL, 5 )
		
		self.m_radioBtn216 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		self.m_radioBtn216.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, True, wx.EmptyString ) )
		
		gSizer3.Add( self.m_radioBtn216, 0, wx.ALL, 5 )
		
		self.m_radioBtn217 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		self.m_radioBtn217.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 72, 94, 90, False, wx.EmptyString ) )
		
		gSizer3.Add( self.m_radioBtn217, 0, wx.ALL, 5 )
		
		self.m_radioBtn218 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn218, 0, wx.ALL, 5 )
		
		self.m_radioBtn219 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn219, 0, wx.ALL, 5 )
		
		self.m_radioBtn220 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn220, 0, wx.ALL, 5 )
		
		self.m_radioBtn221 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn221, 0, wx.ALL, 5 )
		
		self.m_radioBtn222 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn222, 0, wx.ALL, 5 )
		
		self.m_radioBtn223 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn223, 0, wx.ALL, 5 )
		
		self.m_radioBtn224 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn224, 0, wx.ALL, 5 )
		
		self.m_radioBtn225 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn225, 0, wx.ALL, 5 )
		
		self.m_radioBtn3 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn3, 0, wx.ALL, 5 )
		
		self.m_radioBtn31 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		gSizer3.Add( self.m_radioBtn31, 0, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

