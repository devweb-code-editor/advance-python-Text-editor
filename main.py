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
        self.dirname = ''    # hold the currnt directory
        self.filename = ''      #hold the file name
        self.leftMarginWidth = 25
        # toggle line numbers in preferences menu
        self.lineNumbersEnable = True

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

        editmenu = wx.Menu()
        menuUndo = editmenu.Append(wx.ID_UNDO, "&Undo", "Undo last action")
        menuRedo = editmenu.Append(wx.ID_REDO, "&Redo", "Redo last action")
        editmenu.AppendSeparator()
        menuSelectAll = editmenu.Append(wx.ID_SELECTALL, "&Select ALl", "Select the entire Document")
        menuCopy = editmenu.Append(wx.ID_COPY, "&Copy", "Copy Selected text")
        munuCut = editmenu.Append(wx.ID_CUT, "&Cut", "Cut the selected text")
        menuPast = editmenu.Append(wx.ID_PASTE, "&Paste", "Paste text from the clipboard")

        prefmenu = wx.Menu()
        menulineNumber = prefmenu.Append(wx.ID_ANY, "Toggle &Line Numbers", "Show/Hide line numbers colum")

        helumenu = wx.Menu()

        munuHowTo  = helumenu.Append(wx.ID_ANY, "&How to", "Get help using the editor")
        helumenu.AppendSeparator()
        menuAbout = helumenu.Append(wx.ID_ABOUT, "&about", "Read about the editor and its making")


        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        menuBar.Append(editmenu, "&Edit")
        menuBar.Append(prefmenu, "&Preferences")
        menuBar.Append(helumenu, "&help")
        self.SetMenuBar(menuBar)

        self.Show()

    def OnNew(self, e):
        self.filename = ''
        self.control.SetValue("")




app = wx.App()
frame = MainWindow(None, "My text Editor")
app.MainLoop()

