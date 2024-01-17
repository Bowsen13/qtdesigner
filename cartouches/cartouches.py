
# import helpers as h
from PySide6.QtGui import QDragLeaveEvent
import PySide6.QtMultimedia
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QMainWindow ,QFileDialog, QPushButton
from PySide6.QtCore import QUrl
from window.mainwindow_ui import Ui_MainWindow
from audioreader.audioreader import Audioreader
import os
from PySide6.QtGui import QDragEnterEvent, QDropEvent

class One_Cartouche(QMainWindow):
    def __init__(self, pb, instance_audioreader, instance_mainwindow, inst_fileexplorer):
        super().__init__()
        # creation attibuts
        # instances
        self.pb = pb
        self.audio = instance_audioreader
        self.main = instance_mainwindow
        self.file_explorer = inst_fileexplorer
        
        # attributs
        self.file = ''
        # self.mark_pos = []
        # self.fader = 'fader pour ce fichier'
        # self.duration = 10
        # self.label = 'label'
        # logique
        
        
    def dragEnterEvent(self, event):
        event.accept()
        print('drag enter event')
    
    def dropEvent(self, event):
        print('drop event')
        self.pb.setText(event.mimeData().text())
        
    # functions
    
    def pb_clicked(self, inst_cart, val):
        # print(f'clicked val : {val}')
        # print(f'clicked pb : {inst_cart}')
        self.pb.setText(f'{val}')
            
    def rename(self):
        pass
    
    def to_audio_reader(self):
        return self.file, self, self.mark_pos, self.fader, self.pb, self.duration, self.label
    
    def get_file_path(self):
        index = self.main.treeView.currentIndex()
        file_path = self.file_explorer.model.filePath(index)
        os.startfile(file_path)
        self.on_drop()
    
    
class Cartouches:      
    def __init__(self, inst_mainwindow):
        
        # instancition des classes
        # creations des atributs
        self.main = inst_mainwindow
        self.array_pbs = [
            self.main.pb_cart_01, self.main.pb_cart_02, self.main.pb_cart_03,
            self.main.pb_cart_04, self.main.pb_cart_05, self.main.pb_cart_06,
            self.main.pb_cart_07, self.main.pb_cart_08, self.main.pb_cart_09,
            self.main.pb_cart_10, self.main.pb_cart_11, self.main.pb_cart_12,
            self.main.pb_cart_13, self.main.pb_cart_14, self.main.pb_cart_15,
            self.main.pb_cart_16
            ]
        
        #logic
        # ajoute le nom d'item egal au nb de btn
        self.arr_file_cart = []
        for i in range(len(self.array_pbs)):
            self.arr_file_cart.append(i)
        
    # functions 
    
    def inst_onecartouche(self, inst_audioreader, inst_mainwindow, inst_fileexplorer):
        # objectif : creer une instance de cartouche, pour chaque cartouche existante,
        #            en leur attribuant leur fonctionnalitees
        self.arr_inst_cart = []
        for i in range(len(self.array_pbs)):
            self.arr_inst_cart.append(One_Cartouche(self.array_pbs[i], inst_audioreader, inst_mainwindow, inst_fileexplorer))
            self.arr_inst_cart[i].pb.clicked.connect(lambda inst_cart=self.arr_inst_cart[i], val2=i: inst_cart.pb_clicked(inst_cart, val2))
            #self.arr_inst_cart[i].pb.dropEvent(lambda inst_cart=self.arr_inst_cart[i] : inst_cart.drop_event())
            
            
            
            
    
    
    
    
    
    
        