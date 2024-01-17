# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QTreeView, QVBoxLayout, QWidget)
import ressources.ressources_rc
from cartouches.unecartouche import Une_cartouche
from fileexplorer.fileexplorer import File_explorer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(666, 527)
        MainWindow.setAcceptDrops(True)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAcceptDrops(True)
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setAcceptDrops(True)
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 1, 3, 1)

        self.frame = QFrame(self.frame_main)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 25))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(115, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.label_tps_left = QLabel(self.frame)
        self.label_tps_left.setObjectName(u"label_tps_left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_tps_left.sizePolicy().hasHeightForWidth())
        self.label_tps_left.setSizePolicy(sizePolicy1)
        self.label_tps_left.setMinimumSize(QSize(0, 20))
        self.label_tps_left.setTextFormat(Qt.AutoText)

        self.gridLayout_5.addWidget(self.label_tps_left, 1, 3, 1, 1)

        self.horslider_audio_duration = QSlider(self.frame)
        self.horslider_audio_duration.setObjectName(u"horslider_audio_duration")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.horslider_audio_duration.sizePolicy().hasHeightForWidth())
        self.horslider_audio_duration.setSizePolicy(sizePolicy2)
        self.horslider_audio_duration.setMinimumSize(QSize(0, 20))
        self.horslider_audio_duration.setPageStep(0)
        self.horslider_audio_duration.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.horslider_audio_duration, 1, 1, 1, 1)

        self.label_tps_actu = QLabel(self.frame)
        self.label_tps_actu.setObjectName(u"label_tps_actu")
        sizePolicy1.setHeightForWidth(self.label_tps_actu.sizePolicy().hasHeightForWidth())
        self.label_tps_actu.setSizePolicy(sizePolicy1)
        self.label_tps_actu.setMinimumSize(QSize(0, 20))

        self.gridLayout_5.addWidget(self.label_tps_actu, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 2, 1, 2)

        self.frame_3 = QFrame(self.frame_main)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setAcceptDrops(True)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeView = File_explorer(self.frame_3)
        self.treeView.setObjectName(u"treeView")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy4)
        self.treeView.setMinimumSize(QSize(100, 0))
        self.treeView.setMaximumSize(QSize(300, 16777215))
        self.treeView.setAcceptDrops(True)
        self.treeView.setDragEnabled(True)
        self.treeView.setDragDropMode(QAbstractItemView.DragDrop)
        self.treeView.setDefaultDropAction(Qt.CopyAction)
        self.treeView.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.treeView)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 3, 1)

        self.frame_cartouches = QFrame(self.frame_main)
        self.frame_cartouches.setObjectName(u"frame_cartouches")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_cartouches.sizePolicy().hasHeightForWidth())
        self.frame_cartouches.setSizePolicy(sizePolicy5)
        self.frame_cartouches.setMinimumSize(QSize(400, 200))
        self.frame_cartouches.setAcceptDrops(True)
        self.frame_cartouches.setFrameShape(QFrame.StyledPanel)
        self.frame_cartouches.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_cartouches)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 6, 4, 1)

        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 4, 4, 1)

        self.progressBar_2 = QProgressBar(self.frame_cartouches)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)
        self.progressBar_2.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.progressBar_2, 1, 8, 4, 1)

        self.pb_cart_01 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_01.setObjectName(u"pb_cart_01")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pb_cart_01.sizePolicy().hasHeightForWidth())
        self.pb_cart_01.setSizePolicy(sizePolicy6)
        self.pb_cart_01.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_01, 1, 0, 1, 1)

        self.pb_cart_03 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_03.setObjectName(u"pb_cart_03")
        sizePolicy6.setHeightForWidth(self.pb_cart_03.sizePolicy().hasHeightForWidth())
        self.pb_cart_03.setSizePolicy(sizePolicy6)
        self.pb_cart_03.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_03, 1, 2, 1, 1)

        self.pb_cart_04 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_04.setObjectName(u"pb_cart_04")
        sizePolicy6.setHeightForWidth(self.pb_cart_04.sizePolicy().hasHeightForWidth())
        self.pb_cart_04.setSizePolicy(sizePolicy6)
        self.pb_cart_04.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_04, 1, 3, 1, 1)

        self.line = QFrame(self.frame_cartouches)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 5, 4, 1)

        self.pb_cart_02 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_02.setObjectName(u"pb_cart_02")
        sizePolicy6.setHeightForWidth(self.pb_cart_02.sizePolicy().hasHeightForWidth())
        self.pb_cart_02.setSizePolicy(sizePolicy6)
        self.pb_cart_02.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_02, 1, 1, 1, 1)

        self.pb_cart_07 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_07.setObjectName(u"pb_cart_07")
        sizePolicy6.setHeightForWidth(self.pb_cart_07.sizePolicy().hasHeightForWidth())
        self.pb_cart_07.setSizePolicy(sizePolicy6)
        self.pb_cart_07.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_07, 2, 2, 1, 1)

        self.pb_cart_09 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_09.setObjectName(u"pb_cart_09")
        sizePolicy6.setHeightForWidth(self.pb_cart_09.sizePolicy().hasHeightForWidth())
        self.pb_cart_09.setSizePolicy(sizePolicy6)
        self.pb_cart_09.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_09, 3, 0, 1, 1)

        self.pb_cart_05 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_05.setObjectName(u"pb_cart_05")
        sizePolicy6.setHeightForWidth(self.pb_cart_05.sizePolicy().hasHeightForWidth())
        self.pb_cart_05.setSizePolicy(sizePolicy6)
        self.pb_cart_05.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_05, 2, 0, 1, 1)

        self.pb_cart_08 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_08.setObjectName(u"pb_cart_08")
        sizePolicy6.setHeightForWidth(self.pb_cart_08.sizePolicy().hasHeightForWidth())
        self.pb_cart_08.setSizePolicy(sizePolicy6)
        self.pb_cart_08.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_08, 2, 3, 1, 1)

        self.pb_cart_06 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_06.setObjectName(u"pb_cart_06")
        sizePolicy6.setHeightForWidth(self.pb_cart_06.sizePolicy().hasHeightForWidth())
        self.pb_cart_06.setSizePolicy(sizePolicy6)
        self.pb_cart_06.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_06, 2, 1, 1, 1)

        self.pb_cart_11 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_11.setObjectName(u"pb_cart_11")
        sizePolicy6.setHeightForWidth(self.pb_cart_11.sizePolicy().hasHeightForWidth())
        self.pb_cart_11.setSizePolicy(sizePolicy6)
        self.pb_cart_11.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_11, 3, 2, 1, 1)

        self.pb_cart_10 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_10.setObjectName(u"pb_cart_10")
        sizePolicy6.setHeightForWidth(self.pb_cart_10.sizePolicy().hasHeightForWidth())
        self.pb_cart_10.setSizePolicy(sizePolicy6)
        self.pb_cart_10.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_10, 3, 1, 1, 1)

        self.pb_cart_13 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_13.setObjectName(u"pb_cart_13")
        sizePolicy6.setHeightForWidth(self.pb_cart_13.sizePolicy().hasHeightForWidth())
        self.pb_cart_13.setSizePolicy(sizePolicy6)
        self.pb_cart_13.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_13, 4, 0, 1, 1)

        self.pb_cart_14 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_14.setObjectName(u"pb_cart_14")
        sizePolicy6.setHeightForWidth(self.pb_cart_14.sizePolicy().hasHeightForWidth())
        self.pb_cart_14.setSizePolicy(sizePolicy6)
        self.pb_cart_14.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_14, 4, 1, 1, 1)

        self.pb_cart_15 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_15.setObjectName(u"pb_cart_15")
        sizePolicy6.setHeightForWidth(self.pb_cart_15.sizePolicy().hasHeightForWidth())
        self.pb_cart_15.setSizePolicy(sizePolicy6)
        self.pb_cart_15.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_15, 4, 2, 1, 1)

        self.pb_cart_12 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_12.setObjectName(u"pb_cart_12")
        sizePolicy6.setHeightForWidth(self.pb_cart_12.sizePolicy().hasHeightForWidth())
        self.pb_cart_12.setSizePolicy(sizePolicy6)
        self.pb_cart_12.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_12, 3, 3, 1, 1)

        self.pb_cart_16 = Une_cartouche(self.frame_cartouches)
        self.pb_cart_16.setObjectName(u"pb_cart_16")
        sizePolicy6.setHeightForWidth(self.pb_cart_16.sizePolicy().hasHeightForWidth())
        self.pb_cart_16.setSizePolicy(sizePolicy6)
        self.pb_cart_16.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.pb_cart_16, 4, 3, 1, 1)

        self.verslider_audio_volume = QSlider(self.frame_cartouches)
        self.verslider_audio_volume.setObjectName(u"verslider_audio_volume")
        self.verslider_audio_volume.setMinimumSize(QSize(30, 0))
        self.verslider_audio_volume.setAutoFillBackground(False)
        self.verslider_audio_volume.setMaximum(99)
        self.verslider_audio_volume.setPageStep(0)
        self.verslider_audio_volume.setValue(0)
        self.verslider_audio_volume.setSliderPosition(0)
        self.verslider_audio_volume.setTracking(True)
        self.verslider_audio_volume.setOrientation(Qt.Vertical)
        self.verslider_audio_volume.setInvertedAppearance(False)
        self.verslider_audio_volume.setInvertedControls(False)
        self.verslider_audio_volume.setTickPosition(QSlider.NoTicks)
        self.verslider_audio_volume.setTickInterval(0)

        self.gridLayout_2.addWidget(self.verslider_audio_volume, 1, 7, 4, 1)


        self.gridLayout.addWidget(self.frame_cartouches, 0, 2, 1, 2)

        self.frame_2 = QFrame(self.frame_main)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy7)
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setSizeIncrement(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.pb_pause = QPushButton(self.frame_2)
        self.pb_pause.setObjectName(u"pb_pause")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pb_pause.sizePolicy().hasHeightForWidth())
        self.pb_pause.setSizePolicy(sizePolicy8)
        self.pb_pause.setMinimumSize(QSize(0, 20))
        self.pb_pause.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icon/images/icons8-pause-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_pause.setIcon(icon)

        self.gridLayout_4.addWidget(self.pb_pause, 1, 1, 1, 1)

        self.pb_stop = QPushButton(self.frame_2)
        self.pb_stop.setObjectName(u"pb_stop")
        sizePolicy8.setHeightForWidth(self.pb_stop.sizePolicy().hasHeightForWidth())
        self.pb_stop.setSizePolicy(sizePolicy8)
        self.pb_stop.setMinimumSize(QSize(0, 20))
        self.pb_stop.setMaximumSize(QSize(16777215, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icon/images/icons8-arr\u00eater-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_stop.setIcon(icon1)

        self.gridLayout_4.addWidget(self.pb_stop, 1, 2, 1, 1)

        self.pushButton_22 = QPushButton(self.frame_2)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 20))

        self.gridLayout_4.addWidget(self.pushButton_22, 2, 1, 1, 1)

        self.pb_play = QPushButton(self.frame_2)
        self.pb_play.setObjectName(u"pb_play")
        self.pb_play.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.pb_play.sizePolicy().hasHeightForWidth())
        self.pb_play.setSizePolicy(sizePolicy8)
        self.pb_play.setMinimumSize(QSize(0, 20))
        self.pb_play.setMaximumSize(QSize(16777215, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/icon/images/icons8-jouer-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_play.setIcon(icon2)
        self.pb_play.setCheckable(False)

        self.gridLayout_4.addWidget(self.pb_play, 1, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.frame_2)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(0, 20))

        self.gridLayout_4.addWidget(self.pushButton_21, 2, 2, 1, 1)

        self.pb_mute = QPushButton(self.frame_2)
        self.pb_mute.setObjectName(u"pb_mute")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pb_mute.sizePolicy().hasHeightForWidth())
        self.pb_mute.setSizePolicy(sizePolicy9)
        self.pb_mute.setMinimumSize(QSize(0, 20))
        icon3 = QIcon()
        icon3.addFile(u":/icon/images/icons8-muet-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_mute.setIcon(icon3)

        self.gridLayout_4.addWidget(self.pb_mute, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 2, 2, 1, 2)


        self.gridLayout_3.addWidget(self.frame_main, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 666, 18))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pb_play, self.pb_pause)
        QWidget.setTabOrder(self.pb_pause, self.pb_stop)
        QWidget.setTabOrder(self.pb_stop, self.pb_mute)
        QWidget.setTabOrder(self.pb_mute, self.pushButton_22)
        QWidget.setTabOrder(self.pushButton_22, self.pushButton_21)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_tps_left.setText(QCoreApplication.translate("MainWindow", u"- 00:00:00", None))
        self.label_tps_actu.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.pb_cart_01.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_03.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_04.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_02.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_07.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_09.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_05.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_08.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_06.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_cart_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_pause.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.pb_stop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_play.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_mute.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

