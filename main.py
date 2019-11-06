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
        # not show white space
        self.control.SetViewWhiteSpace(False)
        # line numbers
        self.control.SetMargins(5, 0)
        self.control.SetMarginType(1, stc.STC_MARGIN_NUMBER)
        self.control.SetMarginWidth(1, self.leftMarginWidth)

        # status  bar
        self.CreateStatusBar()
        self.StatusBar.SetBackgroundColour((220, 220, 220))

        # Menubar
        filemenu = wx.Menu()
        menunew = filemenu.Append(wx.ID_NEW, "&New", "Create a new Document")
        menuOpen = filemenu.Append(wx.ID_OPEN, "&open", "Open a existing document")
        menuSave = filemenu.Append(wx.ID_SAVE, "&save", "save the current Document")
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "Save &As", "Save a new Document")
        filemenu.AppendSeparator()
        menuClose = filemenu.Append(wx.ID_EXIT, "&close", "Close the Application")


        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)


        self.Show()

app = wx.App()
frame = MainWindow(None, "My text Editor")
app.MainLoop()

