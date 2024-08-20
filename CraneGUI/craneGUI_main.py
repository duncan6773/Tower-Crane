# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'craneGUI_commandGeneration.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from craneGUIActions import craneGUIBackend

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1295, 904)
        MainWindow.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.crane_loc_img = QtWidgets.QWidget(self.centralwidget)
        self.crane_loc_img.setGeometry(QtCore.QRect(40, 80, 471, 471))
        self.crane_loc_img.setObjectName("crane_loc_img")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(500, 0, 91, 480))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.up_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up_label.sizePolicy().hasHeightForWidth())
        self.up_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.up_label.setFont(font)
        self.up_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.up_label.setAlignment(QtCore.Qt.AlignCenter)
        self.up_label.setObjectName("up_label")
        self.verticalLayout.addWidget(self.up_label)
        self.hoist_up_up_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hoist_up_up_button.sizePolicy().hasHeightForWidth())
        self.hoist_up_up_button.setSizePolicy(sizePolicy)
        self.hoist_up_up_button.setMinimumSize(QtCore.QSize(0, 100))
        self.hoist_up_up_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hoist_up_up_button.setText("")
        self.hoist_up_up_button.setIconSize(QtCore.QSize(30, 30))
        self.hoist_up_up_button.setObjectName("hoist_up_up_button")
        self.verticalLayout.addWidget(self.hoist_up_up_button)
        self.hoist_up_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.hoist_up_button.setMinimumSize(QtCore.QSize(0, 100))
        self.hoist_up_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hoist_up_button.setText("")
        self.hoist_up_button.setObjectName("hoist_up_button")
        self.verticalLayout.addWidget(self.hoist_up_button)
        self.hoist_down_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.hoist_down_button.setMinimumSize(QtCore.QSize(0, 100))
        self.hoist_down_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hoist_down_button.setText("")
        self.hoist_down_button.setObjectName("hoist_down_button")
        self.verticalLayout.addWidget(self.hoist_down_button)
        self.hoist_down_down_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.hoist_down_down_button.setMinimumSize(QtCore.QSize(0, 100))
        self.hoist_down_down_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hoist_down_down_button.setText("")
        self.hoist_down_down_button.setObjectName("hoist_down_down_button")
        self.verticalLayout.addWidget(self.hoist_down_down_button)
        self.down_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.down_label.sizePolicy().hasHeightForWidth())
        self.down_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.down_label.setFont(font)
        self.down_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.down_label.setAlignment(QtCore.Qt.AlignCenter)
        self.down_label.setObjectName("down_label")
        self.verticalLayout.addWidget(self.down_label)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(910, 0, 102, 502))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.out_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_label.sizePolicy().hasHeightForWidth())
        self.out_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.out_label.setFont(font)
        self.out_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out_label.setAlignment(QtCore.Qt.AlignCenter)
        self.out_label.setObjectName("out_label")
        self.verticalLayout_2.addWidget(self.out_label)
        self.trolley_back_back_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trolley_back_back_button.sizePolicy().hasHeightForWidth())
        self.trolley_back_back_button.setSizePolicy(sizePolicy)
        self.trolley_back_back_button.setMinimumSize(QtCore.QSize(100, 100))
        self.trolley_back_back_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.trolley_back_back_button.setText("")
        self.trolley_back_back_button.setObjectName("trolley_back_back_button")
        self.verticalLayout_2.addWidget(self.trolley_back_back_button)
        self.trolley_back_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.trolley_back_button.setMinimumSize(QtCore.QSize(0, 100))
        self.trolley_back_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.trolley_back_button.setText("")
        self.trolley_back_button.setObjectName("trolley_back_button")
        self.verticalLayout_2.addWidget(self.trolley_back_button)
        self.trolley_spacer = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.trolley_spacer.setMinimumSize(QtCore.QSize(0, 44))
        self.trolley_spacer.setMaximumSize(QtCore.QSize(50, 44))
        self.trolley_spacer.setText("")
        self.trolley_spacer.setObjectName("trolley_spacer")
        self.verticalLayout_2.addWidget(self.trolley_spacer)
        self.trolley_forward_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.trolley_forward_button.setMinimumSize(QtCore.QSize(0, 100))
        self.trolley_forward_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.trolley_forward_button.setText("")
        self.trolley_forward_button.setObjectName("trolley_forward_button")
        self.verticalLayout_2.addWidget(self.trolley_forward_button)
        self.trolley_forward_forward_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.trolley_forward_forward_button.setMinimumSize(QtCore.QSize(0, 100))
        self.trolley_forward_forward_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.trolley_forward_forward_button.setText("")
        self.trolley_forward_forward_button.setObjectName("trolley_forward_forward_button")
        self.verticalLayout_2.addWidget(self.trolley_forward_forward_button)
        self.in_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_label.sizePolicy().hasHeightForWidth())
        self.in_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.in_label.setFont(font)
        self.in_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.in_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_label.setObjectName("in_label")
        self.verticalLayout_2.addWidget(self.in_label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(640, 210, 632, 102))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_label_3.sizePolicy().hasHeightForWidth())
        self.in_label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.in_label_3.setFont(font)
        self.in_label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.in_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.in_label_3.setObjectName("in_label_3")
        self.horizontalLayout.addWidget(self.in_label_3)
        self.cc_cc_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cc_cc_button.setMinimumSize(QtCore.QSize(100, 100))
        self.cc_cc_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cc_cc_button.setText("")
        self.cc_cc_button.setObjectName("cc_cc_button")
        self.horizontalLayout.addWidget(self.cc_cc_button)
        self.cc_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cc_button.setMinimumSize(QtCore.QSize(100, 100))
        self.cc_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cc_button.setText("")
        self.cc_button.setObjectName("cc_button")
        self.horizontalLayout.addWidget(self.cc_button)
        self.slew_spacer = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.slew_spacer.setMinimumSize(QtCore.QSize(0, 100))
        self.slew_spacer.setMaximumSize(QtCore.QSize(110, 16777215))
        self.slew_spacer.setText("")
        self.slew_spacer.setObjectName("slew_spacer")
        self.horizontalLayout.addWidget(self.slew_spacer)
        self.c_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.c_button.setMinimumSize(QtCore.QSize(100, 100))
        self.c_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.c_button.setText("")
        self.c_button.setObjectName("c_button")
        self.horizontalLayout.addWidget(self.c_button)
        self.c_c_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.c_c_button.setMinimumSize(QtCore.QSize(100, 100))
        self.c_c_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.c_c_button.setText("")
        self.c_c_button.setObjectName("c_c_button")
        self.horizontalLayout.addWidget(self.c_c_button)
        self.in_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_label_2.sizePolicy().hasHeightForWidth())
        self.in_label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.in_label_2.setFont(font)
        self.in_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.in_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.in_label_2.setObjectName("in_label_2")
        self.horizontalLayout.addWidget(self.in_label_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 550, 561, 211))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(19, 20, 521, 171))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.pos_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.pos_layout.setContentsMargins(0, 0, 0, 0)
        self.pos_layout.setObjectName("pos_layout")
        self.pos_infoLayout = QtWidgets.QVBoxLayout()
        self.pos_infoLayout.setObjectName("pos_infoLayout")
        self.crane_status_info_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.crane_status_info_label.setFont(font)
        self.crane_status_info_label.setObjectName("crane_status_info_label")
        self.pos_infoLayout.addWidget(self.crane_status_info_label)
        self.slew_info_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slew_info_label.sizePolicy().hasHeightForWidth())
        self.slew_info_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.slew_info_label.setFont(font)
        self.slew_info_label.setObjectName("slew_info_label")
        self.pos_infoLayout.addWidget(self.slew_info_label)
        self.trolley_info_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.trolley_info_label.setFont(font)
        self.trolley_info_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.trolley_info_label.setObjectName("trolley_info_label")
        self.pos_infoLayout.addWidget(self.trolley_info_label)
        self.hoist_info_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.hoist_info_label.setFont(font)
        self.hoist_info_label.setObjectName("hoist_info_label")
        self.pos_infoLayout.addWidget(self.hoist_info_label)
        self.pos_layout.addLayout(self.pos_infoLayout)
        self.pos_detailLayout = QtWidgets.QVBoxLayout()
        self.pos_detailLayout.setSpacing(11)
        self.pos_detailLayout.setObjectName("pos_detailLayout")
        self.crane_status_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crane_status_label.sizePolicy().hasHeightForWidth())
        self.crane_status_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.crane_status_label.setFont(font)
        self.crane_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.crane_status_label.setObjectName("crane_status_label")
        self.pos_detailLayout.addWidget(self.crane_status_label)
        self.slew_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slew_label.sizePolicy().hasHeightForWidth())
        self.slew_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.slew_label.setFont(font)
        self.slew_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slew_label.setObjectName("slew_label")
        self.pos_detailLayout.addWidget(self.slew_label)
        self.trolley_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trolley_label.sizePolicy().hasHeightForWidth())
        self.trolley_label.setSizePolicy(sizePolicy)
        self.trolley_label.setMinimumSize(QtCore.QSize(70, 0))
        self.trolley_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.trolley_label.setFont(font)
        self.trolley_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.trolley_label.setAlignment(QtCore.Qt.AlignCenter)
        self.trolley_label.setObjectName("trolley_label")
        self.pos_detailLayout.addWidget(self.trolley_label)
        self.hoist_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hoist_label.sizePolicy().hasHeightForWidth())
        self.hoist_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.hoist_label.setFont(font)
        self.hoist_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hoist_label.setObjectName("hoist_label")
        self.pos_detailLayout.addWidget(self.hoist_label)
        self.pos_layout.addLayout(self.pos_detailLayout)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(580, 630, 631, 131))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.traj_run_button = QtWidgets.QPushButton(self.frame_2)
        self.traj_run_button.setGeometry(QtCore.QRect(350, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.traj_run_button.setFont(font)
        self.traj_run_button.setObjectName("traj_run_button")
        self.traj_stop_button = QtWidgets.QPushButton(self.frame_2)
        self.traj_stop_button.setGeometry(QtCore.QRect(500, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.traj_stop_button.setFont(font)
        self.traj_stop_button.setObjectName("traj_stop_button")
        self.loadTraj_button = QtWidgets.QPushButton(self.frame_2)
        self.loadTraj_button.setGeometry(QtCore.QRect(350, 10, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loadTraj_button.setFont(font)
        self.loadTraj_button.setObjectName("loadTraj_button")
        self.traj_label = QtWidgets.QLabel(self.frame_2)
        self.traj_label.setGeometry(QtCore.QRect(10, 10, 331, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.traj_label.sizePolicy().hasHeightForWidth())
        self.traj_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.traj_label.setFont(font)
        self.traj_label.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.traj_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.traj_label.setAlignment(QtCore.Qt.AlignCenter)
        self.traj_label.setObjectName("traj_label")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(580, 550, 631, 81))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setMidLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.shaper_ComboBox = QtWidgets.QComboBox(self.frame_3)
        self.shaper_ComboBox.setGeometry(QtCore.QRect(10, 10, 601, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shaper_ComboBox.sizePolicy().hasHeightForWidth())
        self.shaper_ComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.shaper_ComboBox.setFont(font)
        self.shaper_ComboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.shaper_ComboBox.setMaxCount(2147483644)
        self.shaper_ComboBox.setObjectName("shaper_ComboBox")
        self.shaper_ComboBox.addItem("")
        self.shaper_ComboBox.addItem("")
        self.shaper_ComboBox.addItem("")
        self.shaper_ComboBox.addItem("")
        self.shaper_ComboBox.addItem("")
        self.shaper_ComboBox.addItem("")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(20, 760, 561, 91))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(2)
        self.frame_4.setMidLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, -1, 531, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rec_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rec_button.sizePolicy().hasHeightForWidth())
        self.rec_button.setSizePolicy(sizePolicy)
        self.rec_button.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.rec_button.setFont(font)
        self.rec_button.setObjectName("rec_button")
        self.horizontalLayout_2.addWidget(self.rec_button)
        self.recTime_info_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recTime_info_label.sizePolicy().hasHeightForWidth())
        self.recTime_info_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.recTime_info_label.setFont(font)
        self.recTime_info_label.setObjectName("recTime_info_label")
        self.horizontalLayout_2.addWidget(self.recTime_info_label)
        self.recTime_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recTime_label.sizePolicy().hasHeightForWidth())
        self.recTime_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.recTime_label.setFont(font)
        self.recTime_label.setObjectName("recTime_label")
        self.horizontalLayout_2.addWidget(self.recTime_label)
        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 3)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(580, 760, 631, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setMidLineWidth(1)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame_5)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 601, 71))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.warningLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.warningLayout.setContentsMargins(0, 0, 0, 0)
        self.warningLayout.setObjectName("warningLayout")
        self.fault_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.fault_button.sizePolicy().hasHeightForWidth())
        self.fault_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fault_button.setFont(font)
        self.fault_button.setObjectName("fault_button")
        self.warningLayout.addWidget(self.fault_button)
        self.eStop_button = QtWidgets.QPushButton(self.centralwidget)
        self.eStop_button.setGeometry(QtCore.QRect(610, 40, 261, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.eStop_button.sizePolicy().hasHeightForWidth())
        self.eStop_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.eStop_button.setFont(font)
        self.eStop_button.setObjectName("eStop_button")
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.crane_loc_img.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.eStop_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1295, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTroubleShooting = QtWidgets.QMenu(self.menubar)
        self.menuTroubleShooting.setObjectName("menuTroubleShooting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_Shaper_1 = QtWidgets.QAction(MainWindow)
        self.actionExport_Shaper_1.setObjectName("actionExport_Shaper_1")
        self.actionExport_Shaper_2 = QtWidgets.QAction(MainWindow)
        self.actionExport_Shaper_2.setObjectName("actionExport_Shaper_2")
        self.actionExport_Recording_Data = QtWidgets.QAction(MainWindow)
        self.actionExport_Recording_Data.setObjectName("actionExport_Recording_Data")
        self.actionChange_User_Shaper_1 = QtWidgets.QAction(MainWindow)
        self.actionChange_User_Shaper_1.setObjectName("actionChange_User_Shaper_1")
        self.actionChange_User_Shaper_2 = QtWidgets.QAction(MainWindow)
        self.actionChange_User_Shaper_2.setObjectName("actionChange_User_Shaper_2")
        self.actionCalibrate_Auto = QtWidgets.QAction(MainWindow)
        self.actionCalibrate_Auto.setObjectName("actionCalibrate_Auto")
        self.actionEdit_Slew_Angle = QtWidgets.QAction(MainWindow)
        self.actionEdit_Slew_Angle.setObjectName("actionEdit_Slew_Angle")
        self.actionEdit_Trolley_Height = QtWidgets.QAction(MainWindow)
        self.actionEdit_Trolley_Height.setObjectName("actionEdit_Trolley_Height")
        self.actionEdit_manual_calibration = QtWidgets.QAction(MainWindow)
        self.actionEdit_manual_calibration.setObjectName("actionEdit_manual_calibration")
        self.actionReconnect_to_Crane = QtWidgets.QAction(MainWindow)
        self.actionReconnect_to_Crane.setObjectName("actionReconnect_to_Crane")
        self.menuFile.addAction(self.actionExport_Shaper_1)
        self.menuFile.addAction(self.actionExport_Shaper_2)
        self.menuFile.addAction(self.actionExport_Recording_Data)
        self.menuEdit.addAction(self.actionChange_User_Shaper_1)
        self.menuEdit.addAction(self.actionChange_User_Shaper_2)
        self.menuTroubleShooting.addAction(self.actionCalibrate_Auto)
        self.menuTroubleShooting.addAction(self.actionEdit_manual_calibration)
        self.menuTroubleShooting.addAction(self.actionReconnect_to_Crane)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTroubleShooting.menuAction())

        self.retranslateUi(MainWindow)

        self.backend = craneGUIBackend(MainWindow)
        self.backend.setTrolleyButtons(self.trolley_back_button,self.trolley_back_back_button, self.trolley_forward_button, self.trolley_forward_forward_button)
        self.backend.setSlewingButtons(self.cc_button,self.cc_cc_button,self.c_button,self.c_c_button)
        self.backend.setHoistButtons(self.hoist_down_button,self.hoist_down_down_button,self.hoist_up_button,self.hoist_up_up_button)
        self.backend.setShaperMenue(self.shaper_ComboBox)
        self.backend.setupTraj(self.loadTraj_button,self.traj_run_button,self.traj_stop_button,self.traj_label)
        
        self.backend.setUpRecording(self.rec_button, self.recTime_label)
        self.backend.updateInfoLabels(self.slew_label, self.trolley_label, self.hoist_label, craneInfo= self.crane_status_label, layout = self.pos_detailLayout)
        self.backend.setCraneLocPlot(self.crane_loc_img)
        self.backend.setupTroubleShootMenu(self.actionCalibrate_Auto,self.actionEdit_manual_calibration,self.actionReconnect_to_Crane)
        self.backend.setupCustomeShaperMenu(self.actionChange_User_Shaper_1,self.actionChange_User_Shaper_2)
        self.backend.setupFaultsButton(self.fault_button)
        self.backend.setupFileActions(self.actionExport_Recording_Data,self.actionExport_Shaper_1,self.actionExport_Shaper_2)
        self.backend.setupEstop(self.eStop_button)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.up_label.setText(_translate("MainWindow", "UP"))
        self.down_label.setText(_translate("MainWindow", "DOWN"))
        self.out_label.setText(_translate("MainWindow", "OUT"))
        self.in_label.setText(_translate("MainWindow", "IN"))
        self.in_label_3.setText(_translate("MainWindow", "CCW"))
        self.in_label_2.setText(_translate("MainWindow", "CW"))
        self.crane_status_info_label.setText(_translate("MainWindow", "Crane Status: "))
        self.slew_info_label.setText(_translate("MainWindow", "Slew Angle deg"))
        self.trolley_info_label.setText(_translate("MainWindow", "Trolley Position mm"))
        self.hoist_info_label.setText(_translate("MainWindow", "Hoist Length mm"))
        self.crane_status_label.setText(_translate("MainWindow", "NOT CONNECTED"))
        self.slew_label.setText(_translate("MainWindow", "38.06"))
        self.trolley_label.setText(_translate("MainWindow", "850.50"))
        self.hoist_label.setText(_translate("MainWindow", "110.25"))
        self.traj_run_button.setText(_translate("MainWindow", "Run"))
        self.traj_stop_button.setText(_translate("MainWindow", "Stop"))
        self.loadTraj_button.setText(_translate("MainWindow", "Make Command"))
        self.traj_label.setText(_translate("MainWindow", "Command Gen:"))
        self.shaper_ComboBox.setItemText(0, _translate("MainWindow", "No Shaping/ Impulse"))
        self.shaper_ComboBox.setItemText(1, _translate("MainWindow", "Zero Vibration ZV shaper"))
        self.shaper_ComboBox.setItemText(2, _translate("MainWindow", "Error Intolerant EI Shaper"))
        self.shaper_ComboBox.setItemText(3, _translate("MainWindow", "Custom Shaper 1"))
        self.shaper_ComboBox.setItemText(4, _translate("MainWindow", "Custom Shaper 2"))
        self.shaper_ComboBox.setItemText(5, _translate("MainWindow", "Trajectory Mode"))
        self.rec_button.setText(_translate("MainWindow", "Record "))
        self.recTime_info_label.setText(_translate("MainWindow", "Time:"))
        self.recTime_label.setText(_translate("MainWindow", "0:00"))
        self.fault_button.setText(_translate("MainWindow", "Faults"))
        self.eStop_button.setText(_translate("MainWindow", "Estop"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTroubleShooting.setTitle(_translate("MainWindow", "TroubleShooting"))
        self.actionExport_Shaper_1.setText(_translate("MainWindow", "Export Shaper 1"))
        self.actionExport_Shaper_2.setText(_translate("MainWindow", "Export Shaper 2"))
        self.actionExport_Recording_Data.setText(_translate("MainWindow", "Export Recording Data"))
        self.actionChange_User_Shaper_1.setText(_translate("MainWindow", "Change User Shaper 1"))
        self.actionChange_User_Shaper_2.setText(_translate("MainWindow", "Change User Shaper 2"))
        self.actionCalibrate_Auto.setText(_translate("MainWindow", "Calibrate Auto"))
        self.actionEdit_Slew_Angle.setText(_translate("MainWindow", "Edit Slew Angle"))
        self.actionEdit_Trolley_Height.setText(_translate("MainWindow", "Edit Trolley Position"))
        self.actionEdit_manual_calibration.setText(_translate("MainWindow", "Manual Calibration"))
        self.actionReconnect_to_Crane.setText(_translate("MainWindow", "Reconnect to Crane"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
