#import library wxpython
import wx
import operator

#Buat Objek Applikasi
myapp = wx.App()

#inisialisasi frame
init_frame = wx.Frame(parent=None, title='Halo coy, semangat ya')

#munculkan framenya
init_frame.Show()

#looping objek nya
myapp.MainLoop()

class semangat(wx.Frame):
    def __init__(self, parent, title):
        super(semangat, self).__init__(parent, title=title)
        self.Show()
def main()


