import sys
from window.mainwindow_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSplitter
from audioreader.audioreader import Audioreader
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import Qt

# changer dans mainwindow_ui les QPushButton en Une_cartouche
# import ressources.ressources_rc
# from fileexplorer.fileexplorer import File_explorer
# from cartouches.unecartouche import Une_cartouche


class Run(QMainWindow ,Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.show()
        
        widget = QWidget()
        hlayout = QVBoxLayout()
        splitter = QSplitter()
        
        obj1 = self.frame_sub_main
        obj2 = self.frame_treeview
        
        splitter.addWidget(obj2)
        splitter.addWidget(obj1)
        splitter.setOrientation(Qt.Orientation.Horizontal)
        hlayout.addWidget(splitter)
        widget.setLayout(hlayout)
        self.setCentralWidget(widget)
        
   
if __name__ == "__main__":
    # classes's instances        
    app           = QApplication(sys.argv)
    audio_output  = QAudioOutput()
    player        = QMediaPlayer()
    window        = Run()
    audioreader   = Audioreader(window, audio_output, player)

    # path_style = QFile('../qtdesigner/ressources/style.qss')
    # path_style.open(QFile.OpenModeFlag.ReadOnly)
    # style_sheet = str(path_style.readAll())
    # app.setStyleSheet(style_sheet)
    app.exec()