# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scalingTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LeftSide = QtWidgets.QVBoxLayout()
        self.LeftSide.setSpacing(0)
        self.LeftSide.setObjectName("LeftSide")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.LeftSide.addWidget(self.quickWidget)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.LeftSide.addWidget(self.widget)
        self.CurrentTrackingInfo = QtWidgets.QHBoxLayout()
        self.CurrentTrackingInfo.setContentsMargins(-1, -1, 0, -1)
        self.CurrentTrackingInfo.setSpacing(0)
        self.CurrentTrackingInfo.setObjectName("CurrentTrackingInfo")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayout_5.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setMidLineWidth(8)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.CurrentTrackingInfo.addLayout(self.verticalLayout_5)
        self.TrackingInfo = QtWidgets.QVBoxLayout()
        self.TrackingInfo.setObjectName("TrackingInfo")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.TrackingInfo.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.TrackingInfo.addWidget(self.label_6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.TrackingInfo.addWidget(self.label)
        self.CurrentTrackingInfo.addLayout(self.TrackingInfo)
        self.CurrentTrackingInfo.setStretch(0, 2)
        self.CurrentTrackingInfo.setStretch(1, 1)
        self.LeftSide.addLayout(self.CurrentTrackingInfo)
        self.LeftSide.setStretch(2, 5)
        self.horizontalLayout_2.addLayout(self.LeftSide)
        self.RightSide = QtWidgets.QVBoxLayout()
        self.RightSide.setSpacing(2)
        self.RightSide.setObjectName("RightSide")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_10.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_10.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_10.addWidget(self.pushButton_8)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_10.addWidget(self.pushButton_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.in_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.in_label_3.setObjectName("in_label_3")
        self.horizontalLayout_3.addWidget(self.in_label_3)
        self.cc_cc_button = QtWidgets.QPushButton(self.centralwidget)
        self.cc_cc_button.setMinimumSize(QtCore.QSize(0, 50))
        self.cc_cc_button.setObjectName("cc_cc_button")
        self.horizontalLayout_3.addWidget(self.cc_cc_button)
        self.cc_button = QtWidgets.QPushButton(self.centralwidget)
        self.cc_button.setMinimumSize(QtCore.QSize(0, 50))
        self.cc_button.setObjectName("cc_button")
        self.horizontalLayout_3.addWidget(self.cc_button)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.trolley_back_back_button = QtWidgets.QPushButton(self.centralwidget)
        self.trolley_back_back_button.setMinimumSize(QtCore.QSize(0, 50))
        self.trolley_back_back_button.setObjectName("trolley_back_back_button")
        self.verticalLayout_9.addWidget(self.trolley_back_back_button)
        self.trolley_back_button = QtWidgets.QPushButton(self.centralwidget)
        self.trolley_back_button.setMinimumSize(QtCore.QSize(0, 50))
        self.trolley_back_button.setObjectName("trolley_back_button")
        self.verticalLayout_9.addWidget(self.trolley_back_button)
        self.trolley_forward_button = QtWidgets.QPushButton(self.centralwidget)
        self.trolley_forward_button.setMinimumSize(QtCore.QSize(0, 50))
        self.trolley_forward_button.setObjectName("trolley_forward_button")
        self.verticalLayout_9.addWidget(self.trolley_forward_button)
        self.trolley_forward_forward_button = QtWidgets.QPushButton(self.centralwidget)
        self.trolley_forward_forward_button.setMinimumSize(QtCore.QSize(0, 50))
        self.trolley_forward_forward_button.setObjectName("trolley_forward_forward_button")
        self.verticalLayout_9.addWidget(self.trolley_forward_forward_button)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.c_button = QtWidgets.QPushButton(self.centralwidget)
        self.c_button.setMinimumSize(QtCore.QSize(0, 50))
        self.c_button.setObjectName("c_button")
        self.horizontalLayout_3.addWidget(self.c_button)
        self.c_c_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.c_c_button.sizePolicy().hasHeightForWidth())
        self.c_c_button.setSizePolicy(sizePolicy)
        self.c_c_button.setMinimumSize(QtCore.QSize(0, 50))
        self.c_c_button.setObjectName("c_c_button")
        self.horizontalLayout_3.addWidget(self.c_c_button)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.RightSide.addLayout(self.horizontalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_7.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_8.addWidget(self.pushButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(300, 0))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_11.addWidget(self.pushButton_3)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(300, 0))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_11.addWidget(self.pushButton_9)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.RightSide.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2.addLayout(self.RightSide)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Slewing (Degrees)"))
        self.label_4.setText(_translate("MainWindow", "Trolley Position (mm)"))
        self.label_2.setText(_translate("MainWindow", "Hoist Height (mm)"))
        self.label_5.setText(_translate("MainWindow", "53.26"))
        self.label_6.setText(_translate("MainWindow", "48.57"))
        self.label.setText(_translate("MainWindow", "125"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.pushButton.setText(_translate("MainWindow", "Stop"))
        self.label_8.setText(_translate("MainWindow", "Up"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.label_7.setText(_translate("MainWindow", "Down"))
        self.in_label_3.setText(_translate("MainWindow", "CCW"))
        self.cc_cc_button.setText(_translate("MainWindow", "PushButton"))
        self.cc_button.setText(_translate("MainWindow", "PushButton"))
        self.label_9.setText(_translate("MainWindow", "Out"))
        self.trolley_back_back_button.setText(_translate("MainWindow", "PushButton"))
        self.trolley_back_button.setText(_translate("MainWindow", "PushButton"))
        self.trolley_forward_button.setText(_translate("MainWindow", "PushButton"))
        self.trolley_forward_forward_button.setText(_translate("MainWindow", "PushButton"))
        self.label_10.setText(_translate("MainWindow", "IN"))
        self.c_button.setText(_translate("MainWindow", "PushButton"))
        self.c_c_button.setText(_translate("MainWindow", "PushButton"))
        self.label_12.setText(_translate("MainWindow", "CW"))
        self.pushButton_4.setText(_translate("MainWindow", "Record"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
from PyQt5 import QtQuickWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
