# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LobsterGeneralLogViewerhgxGib.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QSizePolicy,
    QSplitter, QStatusBar, QTextEdit, QTreeView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1071, 777)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetTop = QWidget(self.centralwidget)
        self.widgetTop.setObjectName(u"widgetTop")
        self.verticalLayout_11 = QVBoxLayout(self.widgetTop)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.splitter = QSplitter(self.widgetTop)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLeftLogView = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLeftLogView.setObjectName(u"verticalLeftLogView")
        self.verticalLeftLogView.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLeftLogView.addWidget(self.textEdit)

        self.splitter.addWidget(self.verticalLayoutWidget_2)
        self.verticalLayoutWidget_4 = QWidget(self.splitter)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalRightTreeView = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalRightTreeView.setObjectName(u"verticalRightTreeView")
        self.verticalRightTreeView.setContentsMargins(0, 0, 0, 0)
        self.treeView = QTreeView(self.verticalLayoutWidget_4)
        self.treeView.setObjectName(u"treeView")

        self.verticalRightTreeView.addWidget(self.treeView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalRightTreeView.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.verticalLayoutWidget_4)

        self.verticalLayout_11.addWidget(self.splitter)


        self.verticalLayout.addWidget(self.widgetTop)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1071, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current file:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a log file to read it's content...", None))
    # retranslateUi

