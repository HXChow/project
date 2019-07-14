from PyQt5.QtMultimediaWidgets import QVideoWidget

class myVideoWidget(QVideoWidget):
    def __init__(self,parent=None):
        super(QVideoWidget,self).__init__(parent)