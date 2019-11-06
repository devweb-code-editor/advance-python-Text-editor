import wx
import wx.lib.dialogs
import wx.stc as stc

fasec = {
    'times': 'Times new Roman',
    'mono': 'Couriei New',
    'helv': 'Arial',
    'other': 'Comic Sans MS',
    'size': 10,
    'size2': 8,
}

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.leftMarginWidth = 25

        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.control = stc.StyledTextCtrl(self, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)

        # control + = to zoom in
        self.control.CmdKeyAssign(ord('='), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)

        # control - = to zoom out
        self.control.CmdKeyAssign(ord('-'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)



        self.Show()
app = wx.App()
frame = MainWindow(None, "My text Editor")
app.MainLoop()

