from PySide6.QtGui import QContextMenuEvent, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QPushButton, QMenu
from audioreader.audioreader import Audioreader
from PySide6.QtCore import QUrl, QFileInfo
import os

# importer dans mainwindow_ui : from cartouches.unecartouche import Une_cartouche
# changer dans mainwindow_ui les QPushButton en Une_Cartouche

class Une_cartouche(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)

        self.file   = None
        self.player = None
        
        self.clicked.connect(self.pb_clicked)
        
        # right click
        self.context_menu = QMenu(self)
        action_set_text = self.context_menu.addAction('set_text')
        action_set_text.triggered.connect(self.handle_action_set_text)
 
    
    def pb_clicked(self):
        print('clicked')
            
        if self.file != None:
            print('if : file is not null')
            self.player = Audioreader.player
            Audioreader.stop_audio()
            print(f'self.player : {self.player}')
            print(f'source : {self.player.source()}')
            
            self.player.setSource(self.file)
            
            print(f'source after set: {self.player.source()}')
            
            Audioreader.play_audio()
            
        
    def dragEnterEvent(self, event):
        event.accept()
    
    def dropEvent(self, event):
        print(f'dragged file : {event.mimeData().text()}')
        self.file = event.mimeData().text()
        self.setText(QFileInfo(self.file).fileName())
        
    def contextMenuEvent(self, event):
        self.context_menu.exec(event.globalPos())
    
    def handle_action_set_text(self):
        self.setText('action worked')