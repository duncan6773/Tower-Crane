from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog, QVBoxLayout, QMessageBox, QDialog, QApplication, QProgressBar
from PyQt5.QtCore import Qt, QObject, QTimer

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle, Circle, Polygon

from customDialoug import craneCalDial, shaperDial, PasswordDialog, NotifyBox, faultBox, UsbSelectDialog, commandGenBox

import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import serial
import threading
import pickle
import os 


"""
Author: Will Duncan
Date:   8/14/2024  

This is a script to connect more of the backend applications of the crane GUI. This should be 
the script that handles data processing, transfer, and plotting. It will also connect each of the buttons to functions and might 
add photos and other elements that the basic GUI builder is unable to do 


"""


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class SerialThread(threading.Thread):
    """
    This class handles the serial communication to the Arduino system. It opens the serial port, reads messages,
    and sends messages to the Arduino. Anything sent to the Arduino must be done through this class.
    """

    def __init__(self, callback, port='COM3'):
        super().__init__()
        self.running = False
        self.callBack = callback
        self.ser = None
        self.start_serial(port)

    def start_serial(self, port):
        print(f"Starting Serial on port: {port}")
        try:
            self.ser = serial.Serial(port, 115200)
            self.running = True
            # Try to tell the crane where it was last at
            try:
                time.sleep(1)
                with open("resources/pos.pkl", 'rb') as f:
                    p0_a, p1_a, p2_a = pickle.load(f)
                    userInput = f'c,{p0_a},{p1_a},{p2_a},\n'
                    self.sendMessage(userInput)
            except:
                pass
        except Exception as e:
            self.running = False
            print("Serial Initialization error:", e)

    def run(self):
        if self.ser is None:
            print("Serial port not started")
            return

        try:
            while self.running:
                if self.ser.in_waiting > 0:
                    serial_data = self.ser.readline().decode('utf-8').strip()
                    try:
                        self.callBack(serial_data)
                    except Exception as e:
                        print(f"Callback processing error: {e}")
        except Exception as e:
            print("Serial Port Error. Please restart. TODO: Implement auto-reconnect")
            self.running = False
        finally:
            self.stop()

    def sendMessage(self, msg):
        if not self.ser:
            print("Serial port not started")
            return

        if type(msg) != str:
            msg = str(msg)

        try:
            self.ser.write(msg.encode())
        except Exception as e:
            print(f"Message sending failed: {e}")
        time.sleep(0.001)  # Delay for stability

    def stop(self):
        self.running = False
        if self.ser:
            self.ser.close()
            self.ser = None
        print("Serial connection closed")

    def update_port(self, new_port):
        if self.running:
            self.stop()
        self.start_serial(new_port)
        self.start()

class keyboardFilter(QObject):
    def __init__(self,backend):
        """This class handles all events dealing with the keyboard. Whenever someone presses a button on the keyboard while in the gui
        an event is triggered and this determines how to repsond. Because laptop keys have a really fast debounce time, timers 
        were implemented to to allow a cooldown window before the gui acknowleges a key release. When the timer runs out, the 
        cooresponding debounce function for the axis is called 
        
        Currently it is set up to acknowledge the WSAD keys where w and s are for slewing and A and D are for trolley movment 
        
        """
        super().__init__()
        # self.main_window = main_window
        self.backend = backend

        self.trolleyTimer = QTimer(self)
        self.hoistTimer = QTimer(self)
        self.slewTimer = QTimer(self)

        self.trolleyTimer.timeout.connect(self.trolleyDebounce)
        self.hoistTimer.timeout.connect(self.hoistDebounce)
        self.slewTimer.timeout.connect(self.slewDebounce)

        self.movingRight = False
        self.movingLeft = False
        self.movingC = False
        self.movingCC = False
        self.movingUp = False 
        self.movingDown = False

    def eventFilter(self, source, event):

        if event.type() == QtCore.QEvent.KeyPress:
            #TODO edit this to be clockwise and cc for the crane 
            if event.key() == Qt.Key_Q:
                # self.left.setDown(True
                if(not self.movingLeft and not self.movingRight):
                    self.backend.moveLeftTrolley(self.movingLeft, 0.75)
                    self.movingLeft = True
                #to deal with debouncing 
                if self.trolleyTimer.isActive():
                    self.trolleyTimer.stop()
                return True  # Event handled, do not propagate further
            
            elif event.key() == Qt.Key_E:
                # self.right.setDown(True)
                if(not self.movingRight and not self.movingLeft):
                    self.backend.moveRightTrolley(self.movingRight, 0.75)
                    self.movingRight = True
                if self.trolleyTimer.isActive():
                    self.trolleyTimer.stop()
                return True  # Event handled, do not propagate further
            
            elif event.key() == Qt.Key_A:
                # self.right.setDown(True)
                if(not self.movingC and not self.movingCC):
                    self.backend.moveLeftMotor(self.movingC,0, 0.75)
                    self.movingC = True
                if self.slewTimer.isActive():
                    self.slewTimer.stop()
                return True  # Event handled, do not propagate further
            elif event.key() == Qt.Key_D:
                # self.right.setDown(True)
                if(not self.movingCC and not self.movingC):
                    self.backend.moveRightMotor(self.movingCC,0, 0.75)
                    self.movingCC = True
                if self.slewTimer.isActive():
                    self.slewTimer.stop()
                return True  # Event handled, do not propagate further
            elif event.key() == Qt.Key_W:
                # self.right.setDown(True)
                if(not self.movingUp and not self.movingDown):
                    self.backend.moveRightMotor(self.movingUp,2,0.75)
                    self.movingUp = True
                if self.hoistTimer.isActive():
                    self.hoistTimer.stop()
                return True  # Event handled, do not propagate further
            elif event.key() == Qt.Key_S:
                # self.right.setDown(True)
                if(not self.movingDown and not self.movingUp):
                    self.backend.moveLeftMotor(self.movingDown,2, 0.75)
                    self.movingDown = True
                if self.hoistTimer.isActive():
                    self.hoistTimer.stop()
                return True  # Event handled, do not propagate further
            


        elif event.type() == QtCore.QEvent.KeyRelease:
            if event.key() == Qt.Key_Q:
                if not self.trolleyTimer.isActive():
                    self.trolleyTimer.start(30) 
                return True  # Event handled, do not propagate further
            elif event.key() == Qt.Key_E:
                #start a timer to check for debouncing
                if not self.trolleyTimer.isActive():
                    self.trolleyTimer.start(30) 
                return True  # Event handled, do not propagate further
            elif event.key() == Qt.Key_A:
                #start a timer to check for debouncing
                if not self.slewTimer.isActive():
                    self.slewTimer.start(30) 
                return True  # Event handled, do not propagate further
            elif event.key() == Qt.Key_D:
                #start a timer to check for debouncing
                if not self.slewTimer.isActive():
                    self.slewTimer.start(30) 
                return True  # Event handled, do not propagate further
            elif event.key() == Qt.Key_W:
                #start a timer to check for debouncing
                if not self.hoistTimer.isActive():
                    self.hoistTimer.start(30) 
                return True  # Event handled, do not propagate further
            elif event.key() == Qt.Key_S:
                #start a timer to check for debouncing
                if not self.hoistTimer.isActive():
                    self.hoistTimer.start(30) 
                return True  # Event handled, do not propagate further

        return super().eventFilter(source, event)
    
    def trolleyDebounce(self):
        #This function is called if there is a long enough pulse so that we know it is not just the button debouncing 
        #TODO come up with a better name 
        #stop the timer and free up resources
        self.trolleyTimer.stop()
        #stop moving whatever direction we are moving in
        if(self.movingRight):
            self.backend.moveRightTrolley(self.movingRight, 0.75)
            self.movingRight = False
        elif(self.movingLeft):
            self.backend.moveLeftTrolley(self.movingLeft, 0.75)
            self.movingLeft = False

    def hoistDebounce(self):
        #This function is called if there is a long enough pulse so that we know it is not just the button debouncing 
        #TODO come up with a better name 
        #stop the timer and free up resources
        self.hoistTimer.stop()
       
        #stop moving whatever direction we are moving in
        if(self.movingUp):
            self.backend.moveRightMotor(self.movingUp,2, 0.75)
            self.movingUp = False
        elif(self.movingDown):
            self.backend.moveLeftMotor(self.movingDown,2, 0.75)
            self.movingDown = False

    def slewDebounce(self):
        #This function is called if there is a long enough pulse so that we know it is not just the button debouncing 
        #TODO come up with a better name 
        #stop the timer and free up resources
        self.slewTimer.stop()
        #stop moving whatever direction we are moving in
        if(self.movingC):
            self.backend.moveLeftMotor(self.movingC,0, 0.75)
            self.movingC = False
        elif(self.movingCC):
            self.backend.moveRightMotor(self.movingCC,0, 0.75)
            self.movingCC = False

class cranePosCanvas(FigureCanvas):

    
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.craneRadius = 1080 #mm
        self.innerRadius = 250
        self.armWidth = 45
        self.trolleyLen = 80
        self.trolleyWidth = 110

        

        self.axes = fig.add_subplot(111,)
        self.axes.get_xaxis().set_visible(False)
        self.axes.get_yaxis().set_visible(False)
        super().__init__(fig)
        self.setParent(parent)
        # self.plot()
        self.drawnShapes = {}

    def draw_rectangle(self, center, width, height, angle, edgecolor='blue', facecolor='none'):
        # Calculate bottom-left corner (for compatibility with rotation)
        bottom_left = (center[0] - width / 2, center[1] - height / 2)
        # rectangle = Rectangle(bottom_left, width, height, angle=angle, edgecolor=edgecolor, facecolor=facecolor, transform=self.axes.transData)
        rectangle = Rectangle(bottom_left, width, height, angle=angle, edgecolor=edgecolor, facecolor=facecolor,rotation_point='center')
        self.axes.add_patch(rectangle)
        self.draw()

    def draw_circle(self, center, radius, edgecolor='green', facecolor='none', iden = 1):
        circle = Circle(center, radius, edgecolor=edgecolor, facecolor=facecolor, transform=self.axes.transData)
        self.axes.add_patch(circle)
        self.draw()
        self.drawnShapes[iden] = circle

    def set_axis_limits(self):
        # self.axes.set_xlim(x_limits)
        # self.axes.set_ylim(y_limits)
        self.axes.set_xlim((-self.craneRadius,self.craneRadius))
        self.axes.set_ylim((-self.craneRadius,self.craneRadius))
        self.draw()
    
    def draw_triangle(self, vertices, edgecolor='black', facecolor='black', iden=2):
        triangle = Polygon(vertices, closed=True, edgecolor=edgecolor, facecolor=facecolor, transform=self.axes.transData)
        self.axes.add_patch(triangle)
        self.draw()
        self.drawnShapes[iden] = triangle

    def drawCrane(self, trolleyPos, curAngle):
        #trolley
        # self.axes.clear()
        try:
            self.drawnShapes[0].remove()
        except:
            self.set_axis_limits()
            self.draw_circle((0,0),self.innerRadius, facecolor='black',edgecolor='black')
            self.draw_circle((0,0),self.craneRadius, facecolor='none',edgecolor='black')
            vertices = [(0,0),(1000,585),(1000,-585)]
            self.draw_triangle(vertices
                               )
        # trolleyPos = trolleyPos+self.innerRadius

        #slewing Arm
        # self.draw_rectangle(center=(np.cos(np.deg2rad(curAngle))*self.craneRadius/2,np.sin(np.deg2rad(curAngle))*self.craneRadius/2), width=self.armWidth, height=self.craneRadius, angle=curAngle-90, edgecolor='black')
        # self.draw_rectangle(center=(np.cos(np.deg2rad(curAngle))*trolleyPos,np.sin(np.deg2rad(curAngle))*trolleyPos), width=self.trolleyLen, height=self.trolleyLen, angle=curAngle-90, edgecolor='blue')
        #CenterPiece
        # self.draw_rectangle(center=(0,0), width=self.trolleyWidth, height=self.trolleyLen, angle =curAngle-90)
        
        self.draw_circle((trolleyPos*np.cos(np.deg2rad(curAngle)),trolleyPos*np.sin(np.deg2rad(curAngle))),40,edgecolor='green', iden=0, facecolor='green')
        
        
class craneGUIBackend:

    def __init__(self,MainWindow):
        """This is a class that handles most of the functionailty or backend that is happening with the GUI. This API 
            has a variety of functions like setting up the buttons, adding images, plotting the data and more. 

            This code is designed to be utilized with a GUI made in the QT designer tool. Once the gui has been generated from the 
            designer, import this function and add the needed function calls at the end of the setup UI function 

        """

        #creates the graph 1 and 2 widgets for the x and y displacement data but they still need to be assigned to a vbox
        self.MainWindow = MainWindow
        self.isLeft = False
        self.isRight = False
        self.shaper = ""

        #### ####
        # Data for the excel sheet 
        self.isRecording = False

        self.v0_actual = []
        self.v1_actual = []
        self.v2_actual = []
        self.p0_actual = []
        self.p1_actual = []
        self.p2_actual = []

        self.curTrolleyPos = 0
        self.curSlewPos = 0
        self.curHoistHeight = 0

        self.v0_command = []
        self.v1_command = []
        self.v2_command = []
        self.v0_unshaped = []
        self.v1_unshaped = []
        self.v2_unshaped = []

        self.time = []
        ####
        # Trajectory loading 
        self.trajFile = ""

        ####
        # for command generation 

        self.commandGenMotor = 0
        self.commandGenDur = ''
        self.commandGenAmp = ''
        self.commandGenTimer = QTimer(self.MainWindow)
        self.commandGenTimer.timeout.connect(self.commandGenTimeout)

        ####
        #for faults menu
        self.motor0Faults = []
        self.motor1Faults = []
        self.motor2Faults = []
        self.hasFaults = False
        self.faultColor = False 
        self.faultTimer = QTimer(self.MainWindow)
        self.faultTimer.start(500)
        self.faultTimer.timeout.connect(self.toggleFaultColor)

        ####
        #plotting
        self.plotTol = 0.5
        ####
        self.recMaxLen = 1* 60/0.01
        ####
        #Custom Shaper Storage 
        self.c1Amps =[0]*20 #fancy way to make a 20*1 array of zeros 
        self.c1Times =[0]*20 #fancy way to make a 20*1 array of zeros 
        self.c2Amps =[0]*20 #fancy way to make a 20*1 array of zeros 
        self.c2Times =[0]*20 #fancy way to make a 20*1 array of zeros 
        ####

        

        # self.timer.timeout.connect(self.update_plot)
        self.serial_thread = None
        self.startSerial()
        
        self.keyboardHandler = keyboardFilter(self)
        MainWindow.installEventFilter(self.keyboardHandler)
        
    def startSerial(self):
        if self.serial_thread is not None:
            self.serial_thread.stop()
        
        port = 'COM3'  # Default port or get from some other source
        self.serial_thread = SerialThread(self.messageCallback, port)
        self.serial_thread.start()

    def recconectToCrane(self):
            #if the serial is already running, starting it again will cause a crash 
        dialog = UsbSelectDialog()
        if dialog.exec_() == QDialog.Accepted:
            new_port = dialog.get_selected_device()
            if self.serial_thread is not None:
                self.serial_thread.stop()
                self.serial_thread = None

            self.serial_thread = SerialThread(self.messageCallback, new_port)
            self.serial_thread.start()
            
    def setTrolleyButtons(self,leftTrolleyButton, doubleLeft, rightTrolleyButton, doubleRight):
        """Configures and sets up the trolley movement buttons"""
        #Load in the arrow images 
        # leftArrow = QIcon("resources/leftArrow.png")
        # rightArrow = QIcon("resources/rightArrow.png")
        # doubleLeftArrow = QIcon("resources/leftDoubleArrow.png")
        # doubleRightArrow = QIcon("resources/rightDoubleArrow.png")

        downArrow = QIcon("resources/downArrow.png")
        upArrow = QIcon("resources/upArrow.png")
        doubleDownArrow = QIcon("resources/downDoubleArrow.png")
        doubleUpArrow = QIcon("resources/upDoubleArrow.png")

        # doubleLeft = QtWidgets.QPushButton()
        
        #Set the button images 
        leftTrolleyButton.setIcon(upArrow)
        rightTrolleyButton.setIcon(downArrow)
        doubleLeft.setIcon(doubleUpArrow)
        doubleRight.setIcon(doubleDownArrow)
        #remove any text added to the buttons 
        leftTrolleyButton.setText("")
        rightTrolleyButton.setText("")
        doubleLeft.setText("")
        doubleRight.setText("")

        #Setting the arrow size within the button. Note if the icon is the same size as the button 
        #you wont get the hovering over animations or the pressed in animation so we subtract 5 
        doubleLeft.setIconSize(QtCore.QSize(doubleLeft.width(),doubleLeft.height()-5))
        doubleRight.setIconSize(QtCore.QSize(doubleRight.width(),doubleRight.height()-5))
        leftTrolleyButton.setIconSize(QtCore.QSize(leftTrolleyButton.width(),leftTrolleyButton.height()-5))
        rightTrolleyButton.setIconSize(QtCore.QSize(rightTrolleyButton.width(),rightTrolleyButton.height()-5))
        #Need to connect the functions to the button
        leftTrolleyButton.pressed.connect(lambda: self.moveLeftTrolley(False, 0.5))
        leftTrolleyButton.released.connect(lambda: self.moveLeftTrolley(True, 0.5))
        rightTrolleyButton.pressed.connect(lambda: self.moveRightTrolley(False, 0.5))
        rightTrolleyButton.released.connect(lambda: self.moveRightTrolley(True, 0.5))

        doubleLeft.pressed.connect(lambda: self.moveLeftTrolley(False, 1.0))
        doubleLeft.released.connect(lambda: self.moveLeftTrolley(True, 1.0))
        doubleRight.pressed.connect(lambda: self.moveRightTrolley(False, 1.0))
        doubleRight.released.connect(lambda: self.moveRightTrolley(True, 1.0))

        #Setting it up so that the buttons dont interfere with the keyboard 
        # a = QtWidgets.QPushButton(self.centralwidget)
        leftTrolleyButton.installEventFilter(self.keyboardHandler)
        rightTrolleyButton.installEventFilter(self.keyboardHandler)
        doubleLeft.installEventFilter(self.keyboardHandler)
        doubleRight.installEventFilter(self.keyboardHandler)

    def setSlewingButtons(self, left, doubleLeft, right, doubleRight):
        leftArrow = QIcon("resources/cc_arrow.png")
        rightArrow = QIcon("resources/c_arrow.png")
        doubleLeftArrow = QIcon("resources/cc_cc_arrow.png")
        doubleRightArrow = QIcon("resources/c_c_arrow.png")
        #Set the button images 
        left.setIcon(leftArrow)
        right.setIcon(rightArrow)
        doubleLeft.setIcon(doubleLeftArrow)
        doubleRight.setIcon(doubleRightArrow)

        doubleLeft.setIconSize(QtCore.QSize(doubleLeft.width(),doubleLeft.height()-5))
        doubleRight.setIconSize(QtCore.QSize(doubleRight.width(),doubleRight.height()-5))
        left.setIconSize(QtCore.QSize(left.width(),left.height()-5))
        right.setIconSize(QtCore.QSize(right.width(),right.height()-5))

        #remove any text added to the buttons 
        left.setText("")
        right.setText("")
        doubleLeft.setText("")
        doubleRight.setText("")
        left.pressed.connect(lambda: self.moveLeftMotor(False, 0,0.5))
        left.released.connect(lambda: self.moveLeftMotor(True, 0 , 0.5))
        right.pressed.connect(lambda: self.moveRightMotor(False, 0 , 0.5))
        right.released.connect(lambda: self.moveRightMotor(True, 0 , 0.5))

        doubleLeft.pressed.connect(lambda: self.moveLeftMotor(False, 0 , 1.0))
        doubleLeft.released.connect(lambda: self.moveLeftMotor(True, 0 , 1.0))
        doubleRight.pressed.connect(lambda: self.moveRightMotor(False, 0 , 1.0))
        doubleRight.released.connect(lambda: self.moveRightMotor(True, 0 , 1.0))

        #Setting it up so that the buttons dont interfere with the keyboard 
        # a = QtWidgets.QPushButton(self.centralwidget)
        left.installEventFilter(self.keyboardHandler)
        right.installEventFilter(self.keyboardHandler)
        doubleLeft.installEventFilter(self.keyboardHandler)
        doubleRight.installEventFilter(self.keyboardHandler)
        
    def setHoistButtons(self, down, doubleDown, up, doubleUp):
        downArrow = QIcon("resources/downArrow.png")
        upArrow = QIcon("resources/upArrow.png")
        doubleDownArrow = QIcon("resources/downDoubleArrow.png")
        doubleUpArrow = QIcon("resources/upDoubleArrow.png")
        #Set the button images 
        down.setIcon(downArrow)
        up.setIcon(upArrow)
        doubleDown.setIcon(doubleDownArrow)
        doubleUp.setIcon(doubleUpArrow)
        #remove any text added to the buttons 
        down.setText("")
        up.setText("")
        doubleDown.setText("")
        doubleUp.setText("")
        down.pressed.connect(lambda: self.moveLeftMotor(False, 2,0.5))
        down.released.connect(lambda: self.moveLeftMotor(True, 2 , 0.5))
        up.pressed.connect(lambda: self.moveRightMotor(False, 2 , 0.5))
        up.released.connect(lambda: self.moveRightMotor(True, 2 , 0.5))

        doubleDown.pressed.connect(lambda: self.moveLeftMotor(False, 2 , 1.0))
        doubleDown.released.connect(lambda: self.moveLeftMotor(True, 2 , 1.0))
        doubleUp.pressed.connect(lambda: self.moveRightMotor(False, 2 , 1.0))
        doubleUp.released.connect(lambda: self.moveRightMotor(True, 2 , 1.0))

        down.setIconSize(QtCore.QSize(down.width(),down.height()-5))
        up.setIconSize(QtCore.QSize(down.width(),down.height()-5))
        doubleUp.setIconSize(QtCore.QSize(doubleUp.width(),doubleUp.height()-5))
        doubleDown.setIconSize(QtCore.QSize(doubleDown.width(),doubleDown.height()-5))

        #Setting it up so that the buttons dont interfere with the keyboard 
        # a = QtWidgets.QPushButton(self.centralwidget)
        down.installEventFilter(self.keyboardHandler)
        up.installEventFilter(self.keyboardHandler)
        doubleDown.installEventFilter(self.keyboardHandler)
        doubleUp.installEventFilter(self.keyboardHandler)

    def setShaperMenue(self, dropDown):
        dropDown.currentIndexChanged.connect(self.on_combobox_changed)
        dropDown.installEventFilter(self.keyboardHandler) 

    #TODO move the commands to use move motor instead of trolley specific
    def moveLeftTrolley(self, isMoving, multiplier):
        if not isMoving:
            
            v1 = 0.0*multiplier
            v2 = 1.0*multiplier
            v3 = 0.0*multiplier
    
            user_input = 'v,' + str(v1) + ',' + str(v2) + ',' + str(v3)+ ',\n'
            try:
                self.serial_thread.sendMessage(user_input)
            except:
                pass
            
        else:
            # self.isLeft = False
            # user_input = '1\n'
            # user_input = 't,0.0,-1.0,0.0\n'
            v1 = 0.0*multiplier
            v2 = -1.0*multiplier
            v3 = 0.0*multiplier
            user_input = 'v,' + str(v1) + ',' + str(v2) + ',' + str(v3)+ ',\n'
            try:
                self.serial_thread.sendMessage(user_input)
            except:
                pass

    def moveRightTrolley(self, isMoving, multiplier):
        if not isMoving:
            
            v1 = 0.0*multiplier
            v2 = -1.0*multiplier
            v3 = 0.0*multiplier

            user_input = 'v,' + str(v1) + ',' + str(v2) + ',' + str(v3)+ ',\n'
            self.serial_thread.sendMessage(user_input)
        else:
            
            v1 = 0.0*multiplier
            v2 = 1.0*multiplier
            v3 = 0.0*multiplier

            user_input = 'v,' + str(v1) + ',' + str(v2) + ',' + str(v3)+ ',\n'
            self.serial_thread.sendMessage(user_input)

    def moveLeftMotor(self, isMoving, motorNumber, multiplier):
        #Motor 0 is slewing 
        #motor 1 is trolley 
        #motor 2 is hoisting 
        if not isMoving:
            #initialize all velos as zero
            motorVelos = [0,0,0]
            #only edit the velo of the motor we want to send
            motorVelos[motorNumber] = 1*multiplier
            #make the command
            user_input = 'v,' + str(motorVelos[0]) + ',' + str(motorVelos[1]) + ',' + str(motorVelos[2])+ ',\n'
            #send the command 
            self.serial_thread.sendMessage(user_input)

            time.sleep(0.1)  # Delay for stability
        else:
            #initialize all velos as zero
            motorVelos = [0,0,0]
            #only edit the velo of the motor we want to send
            motorVelos[motorNumber] = -1*multiplier
            #make the command
            user_input = 'v,' + str(motorVelos[0]) + ',' + str(motorVelos[1]) + ',' + str(motorVelos[2])+ ',\n'
            self.serial_thread.sendMessage(user_input)
            time.sleep(0.1)  # Delay for stability

    def moveRightMotor(self, isMoving, motorNumber, multiplier):
        #Motor 0 is slewing 
        #motor 1 is trolley 
        #motor 2 is hoisting 
        if not isMoving:
            #initialize all velos as zero
            motorVelos = [0,0,0]
            #only edit the velo of the motor we want to send
            motorVelos[motorNumber] = -1*multiplier
            #make the command
            user_input = 'v,' + str(motorVelos[0]) + ',' + str(motorVelos[1]) + ',' + str(motorVelos[2])+ ',\n'
            #send the command 
            self.serial_thread.sendMessage(user_input)

            time.sleep(0.1)  # Delay for stability
        else:
            #initialize all velos as zero
            motorVelos = [0,0,0]
            #only edit the velo of the motor we want to send
            motorVelos[motorNumber] = 1*multiplier
            #make the command
            user_input = 'v,' + str(motorVelos[0]) + ',' + str(motorVelos[1]) + ',' + str(motorVelos[2])+ ',\n'
            self.serial_thread.sendMessage(user_input)
            time.sleep(0.1)  # Delay for stability

    def on_combobox_changed(self, index):
        #figure out what flag characters to send to the arduino 
        shaperSig = { 0 :'iden',1 : 'zv', 2:'ei', 3 : 'u1', 4 : 'u2', 5: 'traj'}
        self.shaper = shaperSig[index]
        try:
            self.serial_thread.sendMessage('s,' + shaperSig[index] + ',\n')
        except:
            pass

        try:
            if(index == 5):
                self.findPath.setText("Choose File")
                self.pathLabel.setText("Trajectory")
                self.pathLabel.setStyleSheet("background-color : green")
            else:
                self.pathLabel.setStyleSheet("background-color : cyan")
                self.findPath.setText("Make Command")
                self.pathLabel.setText("Command Gen")
        except:
            pass

    def setupCraneImage(self, myLabel):
        # myLabel = QtWidgets.QLabel(self.centralwidget)
        craneImage = QPixmap("resources/quickCrane.png")
        myLabel.setPixmap(craneImage)
        myLabel.setScaledContents(True)

    def setUpRecording(self, rButton, rLabel):
        self.recLabel = rLabel
        
        self.rec_button = rButton
        self.rec_button.clicked.connect(self.recording_state)

    def recording_state(self):
        if(not self.isRecording):
            self.isRecording = True

            self.time= []
            self.v0_actual = []
            self.v1_actual = []
            self.v2_actual = []
            self.p1_actual = []
            self.p0_actual = []
            self.p2_actual= []

            self.v0_command= []
            self.v1_command= []
            self.v2_command= []

            self.v0_unshaped= []
            self.v1_unshaped= []
            self.v2_unshaped= []
    
            self.rec_button.setText("Recording")
        else:
            self.isRecording = False
            self.rec_button.setText("Record")
            self.recLabel.setText('0:00')

    def exportExcel(self):
        try:
            times = np.array(self.time)
            commandV0 = np.array(self.v0_command)
            actualV0 = np.array(self.v0_actual)
            actualP0 = np.array(self.p0_actual)
            unshapedV0 = np.array(self.v0_unshaped)

            commandV1 = np.array(self.v1_command)
            actualV1 = np.array(self.v1_actual)
            actualP1 = np.array(self.p1_actual)
            unshapedV1 = np.array(self.v1_unshaped)

            commandV2 = np.array(self.v2_command)
            actualV2 = np.array(self.v2_actual)
            actualP2 = np.array(self.p2_actual)
            unshapedV2 = np.array(self.v2_unshaped)
        # userInput = np.array(self.user)
            combined_array = np.column_stack((times, commandV1, actualV1, commandV0, actualV0, commandV2, actualV2,actualP1, actualP0, actualP2, unshapedV1,unshapedV0,unshapedV2))

            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            # print(desktop_path)
            file_name = os.path.join(desktop_path, 'recData', 'data.csv')
            try:
                # Ensure the recData directory exists
                rec_data_path = os.path.dirname(file_name)
                os.makedirs(rec_data_path, exist_ok=True)

                # Save the numpy array to the CSV file
                np.savetxt(file_name, combined_array, delimiter=",", header="Times ms, Command Velo Slew, Actual Velo Slew,Command Velo Trolley,Actual Velo Trolley,Command Velo Hoist,Actual Velo Hoist, Position Slew, Position Trolley, Position Hoist,Unshaped Slew, Unshaped Trolley, Unshaped Hoist", comments="")
                
                # Notify the user that saving is done
                dialog = NotifyBox(msg="Done Saving")
                if dialog.exec_() == QDialog.Accepted:
                    pass
            except Exception as e:
                # Notify the user of an error
                dialog = NotifyBox(msg="Error: Please close the data Excel sheet and export again.\nDetails: " + str(e))
                if dialog.exec_() == QDialog.Accepted:
                    pass
        except Exception as e:
            self.createWarning(e)
 
    def messageCallback(self,msg):
        #This is what processes the message from the arduino to the GUI

        try:
            if(msg[0] == 'd'):
                #that means data was recieved 
                msg = msg[2:]

                #t, v1_a,v1_c,p1_a, v0_a,v0_c, p0_a, v2_a, v2_c,p2_a,u1_c,u0_c,u2_c  = map(float, msg.split(','))
                t, v0_a,v0_c,p0_a, v1_a,v1_c, p1_a, v2_a, v2_c,p2_a,u1_c,u0_c,u2_c  = map(float, msg.split(','))
                self.slewLabel.setText(str(p1_a))
                # self.slewLabel.setStyleSheet("font-size: 20px;")
                self.trolleyLabel.setText(str(p0_a))
                # self.trolleyLabel.setStyleSheet("font-size: 20px;")
                self.hoistLabel.setText(str(p2_a))
                # self.hoistLabel.setStyleSheet("font-size: 20px;")

                if((np.abs(self.curSlewPos - p1_a) > self.plotTol) | (np.abs(self.curTrolleyPos - p0_a) >self.plotTol)| (np.abs(self.curHoistHeight - p2_a) >self.plotTol)):
                    self.craneLocPlot.drawCrane(p0_a + 250 ,p1_a)
                    self.curSlewPos = p1_a
                    self.curTrolleyPos = p0_a
                    self.curHoistHeight = p2_a

                    try:
                        if((p1_a > 0) & (p0_a > 0) & (p2_a > 0)):
                            with open("resources\pos.pkl", 'wb') as f:
                                pickle.dump([p1_a,p0_a,p2_a],f)
                                # print("Position saved: " + str(p0_a) + "    "+ str(p1_a)+ "     " + str(p2_a))
                    except:
                        pass
                if(self.isRecording):
                        #if we are recirding add the stuff to the data sheet
                        if(len(self.time)==0):
                            self.startTime = t
                            t = 0
                        else:
                            t = t - self.startTime

                        self.time.append(t)
                        self.v0_actual.append(v0_a)
                        self.v1_actual.append(v1_a)
                        self.v2_actual.append(v2_a)

                        self.p1_actual.append(p1_a)
                        self.p0_actual.append(p0_a)
                        self.p2_actual.append(p2_a)

                        self.v0_command.append(v0_c)
                        self.v1_command.append(v1_c)
                        self.v2_command.append(v2_c)

                        self.v0_unshaped.append(u0_c)
                        self.v1_unshaped.append(u1_c)
                        self.v2_unshaped.append(u2_c)
                        

                        try:
                            myTime = t-self.time[0]
                            myTime = myTime /1000
                            myTimeMin = np.floor(myTime/60)
                            myTimeSec = round(((myTime/60)%1)*60,0)
                            if (myTimeSec < 10):
                                self.recLabel.setText(str(int(myTimeMin)) + ":0" + str(int(myTimeSec)))
                            else:
                                self.recLabel.setText(str(int(myTimeMin)) + ":" + str(int(myTimeSec)))
                        except:
                            pass

            elif(msg[0] == 'f'):
                errorCodes = {0: '', 1: 'System Initializing', 16: 'Bad Config', 256: 'Bus Over voltage',
                              512: 'Bus Under Voltage', 1024: 'Bus Over Current', 2048: 'bus over regen current', 
                              4098: 'Bus Current over Soft Limit',  33554432: 'ESTOP',8192: 'Motor Over temp', 67108864: 'Spinout Detected',
                               134217728: 'Brake Resistor Disarmed', 268435456: 'Thermistor Disconected'}
                msg = msg[2:]
                f0,f1,f2 = msg.split(',')
                
                #See if the error is a known error else say its unkown
                try:
                    msg0 = errorCodes[int(f0)]
                except:
                    msg0 = 'Error Unkown: ' + f0
                try:
                    msg1 = errorCodes[int(f1)]
                except:
                    msg1 = 'Error Unkown: ' + f1
                try:
                    msg2 = errorCodes[int(f2)]
                except:
                    msg2 = 'Error Unkown: ' + f2


                self.checkUniqueString(msg0,self.motor0Faults)    
                self.checkUniqueString(msg1,self.motor1Faults)
                self.checkUniqueString(msg2,self.motor2Faults)
                if(not self.hasFaults):
                    # self.faultTimer.start(500)
                    self.hasFaults = True
                self.commandGenTimer.stop()
                print(msg)
            elif(msg[0] == 'i'):
                self.craneInfoLabel.setText(str(msg[2:]))
            else:
                print("Message Processing Error" + msg)

        except:
            print("Unkown Message" + msg)    

    def checkUniqueString(self, myString,myList):
        if myString not in myList:
            myList.append(myString)
        else:
            pass
        
    def setupTraj(self, chooseFile,startTraj,endTraj, pathLabel):
        # chooseFile =  QtWidgets.QPushButton()
        chooseFile.clicked.connect(self.findPath)
        #setting up the buttons so we can keep track and change their text
        self.findPath = chooseFile
        self.pathLabel = pathLabel
        # self.trajLabel.setStyleSheet("background-color : red")
        startTraj.clicked.connect(self.startPath)
        endTraj.clicked.connect(self.stopPath) 

    def findPath(self):
        #find the path to the trajectory file or sets up the command generated path 
        if(self.shaper == 'traj'):
            #if we are in the trajecotry mode open the file explorer
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            # QFileDialog.getOpenFileName
            self.trajFile, _ = QFileDialog.getOpenFileName(self.MainWindow, "QFileDialog.getOpenFileName()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
            if self.trajFile != "":
                try:
                        df = pd.read_excel(self.trajFile, engine='openpyxl')
                        #Serperate out trolley, slew, and hoist columns 
                        trolley = df.loc[:,"Trjectory Tangential"].to_numpy()
                        slew = df.loc[:,"Trajectory Radial"].to_numpy()
                        hoist = df.loc[:,"Trajectory Height"].to_numpy()
                        #Need to make sure the values dont break the crane
                        trolley[trolley>100] = 100
                        trolley[trolley<-100] = -100
                        slew[slew>100] = 100
                        slew[slew<-100] = -100
                        hoist[hoist>100] = 100
                        hoist[hoist<-100] = -100
                        for i in range(1600):
                            self.serial_thread.sendMessage('t,' + str(slew[i]) + ',' + str(trolley[i]) + ',' + str(hoist[i]) + ',\n')
                        # print("Trajectory Upload complete")
                        self.createWarning("Trajectory Upload Complete")
                        # print("Error: Not in trajectory Mode")
                except Exception as e:
                    self.createWarning("Error: FILE READ ERROR")
                    # print("FILE READ ERROR TODO MAKE THIS SOMETHING THAT APPEARS IN THE GUI")
        else:
            dialog = commandGenBox(motor=self.commandGenMotor,duration=self.commandGenDur,amplitude=self.commandGenAmp)
            if dialog.exec_() == QDialog.Accepted:
                if self.commandGenTimer.isActive():
                    self.createWarning("previous command is currently running please wait and retry")
                else:
                    self.commandGenMotor,self.commandGenDur,self.commandGenAmp = dialog.getValues()
                    
                    if(self.commandGenDur == "" or self.commandGenAmp == ''):
                        self.createWarning("Amplitude or Time was left blank")
                    else:
                        dur = float(self.commandGenDur)
                        self.commandGenDur = str(np.round(dur,0))
                        amp = float(self.commandGenAmp)
                        if amp > 100:
                            amp = 100
                        elif(amp<-100):
                            amp = -100
                        self.commandGenAmp = str(np.round(amp,1))
                
                #Need to check if either are blank, if so warn user crane wont run 
                          
    def startPath(self):
        #try to start the current command generated or trajectory path 
        if(self.shaper == 'traj'):
            try:
                self.serial_thread.sendMessage('t,'+'s,\n')
            except:
                pass
        else:
            if(self.commandGenDur == "" or self.commandGenAmp == ''):
                self.createWarning("Amplitude or Time was left blank")
            elif (self.commandGenTimer.isActive()):
                self.createWarning("previous command is currently running please wait and retry")
            else:
                try:
                    print("The user wants motor " + str(self.commandGenMotor) + " to run at " + str(self.commandGenAmp) + "percent  speed for " + str(self.commandGenDur) + "ms")
                    
                    self.commandGenTimer.start(int(float(self.commandGenDur)))
                    #TODO  actually move the motor 
                    if(self.commandGenMotor == 0):
                        #means this is the trolley 
                        print("Starting Trolley")
                        self.moveLeftTrolley(False, float(self.commandGenAmp)/100)
                    elif(self.commandGenMotor == 1):
                        #slewing
                        print("Starting Slew")
                        self.moveLeftMotor(False, 0 , float(self.commandGenAmp)/100)
                    elif(self.commandGenMotor == 2):
                        #slewing
                        print("Starting Hoisting")
                        self.moveLeftMotor(False, 2 , float(self.commandGenAmp)/100)
                        
                except Exception as e:
                    print(e)

    def commandGenTimeout(self):
        self.commandGenTimer.stop()
        if(self.commandGenMotor == 0):
            #means this is the trolley 
            print("Stopping Trolley")
            self.moveLeftTrolley(True, float(self.commandGenAmp)/100)
        elif(self.commandGenMotor == 1):
            #slewing
            print("Stopping Slewing")
            self.moveLeftMotor(True, 0 , float(self.commandGenAmp)/100)
        elif(self.commandGenMotor == 2):
            #Hoisting
            print("Stopping Hoisting")
            self.moveLeftMotor(True, 2 , float(self.commandGenAmp)/100)
        # time.sleep(0.1)
        # #Make sure the motors stop moving. This prevents issues with hitting the limit switches 
        # self.serial_thread.sendMessage('m,0,0,0,\n')

    def stopPath(self):
        #try to stop the current command generated or trajectory path 
        if(self.shaper == 'traj'):
            try:
                self.serial_thread.sendMessage('t,'+'e,\n')
            except:
                #stop the timer from triggering anything else
                self.commandGenTimer.stop()
                #tell the motors to stop moving 
                user_input =  'm,0,0,0,\n'
                self.serial_thread.sendMessage(user_input)

    def updateInfoLabels(self, slew, trolley, hoist, craneInfo = None, layout = None):
        """ Setups the labels on the gui that display the current location of the crane """
        #allows the backend to change the text of the labels 
        self.slewLabel = slew
        self.trolleyLabel = trolley
        self.hoistLabel = hoist
        self.craneInfoLabel = craneInfo
        layout = QVBoxLayout()
        # layout.setAlignment()
        # print('oop')
    
    def setCraneLocPlot(self, loc_widget):

        layout = QVBoxLayout(loc_widget)
        self.craneLocPlot = cranePosCanvas(loc_widget)
        self.craneLocPlot.drawCrane(500,00)
        layout.addWidget(self.craneLocPlot) 

    def setupTroubleShootMenu(self, autoCalibrate, editManual, reconect):
        """
        This function is to set up the troubleshooting drop down in the upper left part of the gui. Insert the
        names of the options into the function and this will connect the correct function to run when the button is 
        clicked. Currently, it sets up the autocalibrate button to run the autoCalibrate function and the other three to run 
        calibrate axis function 
        """
        autoCalibrate.triggered.connect(self.autoCalibrate)
        editManual.triggered.connect(self.calibrateAxis)
        
        reconect.triggered.connect(self.recconectToCrane)

    def calibrateAxis(self):
        """
        This function opens up a pop up window defined by the craneCalDial class from the custom Dialoug script
        It then reads in the values from that dialoug, filters them, and finally sends them to the arduino 
        """
        # if(self.checkPassword()):
        dialog = craneCalDial()
        if dialog.exec_() == QDialog.Accepted:
            value1, value2, value3 = dialog.getValues()
            # QMessageBox.information(self, "Input Values", f"Value 1: {value1}\nValue 2: {value2}\nValue 3: {value3}")
        else:
            value1, value2, value3 = "", "", ""
            # QMessageBox.information(self, "Input Cancelled", "No values were entered.")

        #now we need to get the information from the dialoug box and do something with it 
        #lets make sure the info is actually filled in 
        if (len(value1) != 0):
            value1 = int(float(value1))
        else:
            value1 = -1

        if (len(value2) != 0):
            value2 = int(float(value2))
        else:
            value2 = -1

        if (len(value3) != 0):
            value3 = int(float(value3))
        else:
            value3 = -1
        userInput = 'c,' + str(value1) +',' + str(value2) +','+str(value3)+',' +'\n'
        self.serial_thread.sendMessage(userInput)

    def autoCalibrate(self):
        """Sends the message to the arduino to perform the auto calirbation. The rest is 
           handled by the arduino itself """
        # print('c,a,\n')
        self.serial_thread.sendMessage('c,a\n')

    def setupCustomeShaperMenu(self, c1, c2):
        c1.triggered.connect(lambda: self.showCustomShaperMenu('c1'))
        c2.triggered.connect(lambda: self.showCustomShaperMenu('c2'))

    def showCustomShaperMenu(self, shaperNumber):
        """
        This function opens up a pop up window defined by the craneCalDial class from the custom Dialoug script
        It then reads in the values from that dialoug, filters them, and finally sends them to the arduino 
        """

        if(shaperNumber == 'c1'):
            dialog = shaperDial(times=self.c1Times,amps=self.c1Amps)
            if dialog.exec_() == QDialog.Accepted:
                self.c1Times,self.c1Amps = dialog.getValues()
                self.sendCustShaper(shaperNumber=1)

            else:
                pass
        else:
            dialog = shaperDial(times=self.c2Times,amps=self.c2Amps)
            if dialog.exec_() == QDialog.Accepted:
                self.c2Times,self.c2Amps = dialog.getValues()
                self.sendCustShaper(shaperNumber=2)
            # QMessageBox.information(self, "Input Values", f"Value 1: {value1}\nValue 2: {value2}\nValue 3: {value3}")
            else:
                pass

    def sendCustShaper(self, shaperNumber = 1):
        if(shaperNumber ==1):
            times = self.c1Times
            amps = [x * 10 for x in self.c1Amps] #cant have decimal places in the amplitude
        else:
            times = self.c2Times
            amps = [x * 10 for x in self.c2Amps] 
        #We need to make them into messages now 
        ampString = ','.join(map(str, amps))
        timesString = ','.join(map(str, times))
        self.serial_thread.sendMessage('a,'+ str(shaperNumber)+ ',' + ampString+ ',\n')
        time.sleep(0.1)
        self.serial_thread.sendMessage('b,'+ str(shaperNumber)+ ',' + timesString+ ',\n')
        time.sleep(0.2)
        if (self.shaper == 'u1' or self.shaper == 'u2'):
            self.serial_thread.sendMessage('s,u' + str(shaperNumber) + ',\n')

    def checkPassword(self, password = "is" ):
        """
        Makes a popup window from the custom dialoug script requesting the given password. It will allow
        users to make attemps until they get it right or press cancel. If the user presses cancel, this function 
        will return false. If the correct password is entered, it will return true
        """
        dialog = PasswordDialog(password)
        if dialog.exec_() == QDialog.Accepted:
            return True
        else:
            return False

    def setupFaultsButton(self,faultButton):
        #Setups the clear faults button to send the command to the arduino to clear faults 
        # faultButton.pressed.connect(lambda: self.serial_thread.sendMessage('f,cl,\n'))
        self.faultsButton = faultButton
        faultButton.pressed.connect(self.faultsMenu)

    def faultsMenu(self):
        dialog = faultBox(self.motor0Faults,self.motor1Faults,self.motor2Faults)
        if dialog.exec_() == QDialog.Accepted:
            self.serial_thread.sendMessage('f,cl,\n')
            self.hasFaults = False
            self.faultsButton.setStyleSheet("")
            self.motor0Faults = []
            self.motor1Faults = []
            self.motor2Faults = []
            # self.faultTimer.stop()

            # self.c1Times,self.c1Amps = dialog.getValues()
            # self.sendCustShaper(shaperNumber=1)

        else:
            pass

    def toggleFaultColor(self):
        # print("Trying to toggle")
        if(self.faultColor and self.hasFaults):
            self.faultsButton.setStyleSheet("") 
            self.faultColor = False
        elif(self.hasFaults): 
            self.faultsButton.setStyleSheet("background-color: red;")
            self.faultColor = True
        else:
            self.faultsButton.setStyleSheet("") 
            self.faultColor = False

    def setupEstop(self, estop):
        #Setting up the function that is run when the estop button is pressed
        # estop = QtWidgets.QPushButton
        estop.setStyleSheet("background-color : red; border-radius : 50")
        estop.pressed.connect(lambda: self.serial_thread.sendMessage('f,e,/n'))

    def setupFileActions(self, exportData,exportShaper1,exportShaper2):
        #setups the button actions under the file tab 
        exportData.triggered.connect(self.exportExcel)
        exportShaper1.triggered.connect(lambda: self.exportShaper(self.c1Times,self.c1Amps))
        exportShaper2.triggered.connect(lambda: self.exportShaper(self.c2Times,self.c2Amps))

    def exportShaper(self, t1, a1):
        # t1_np = np.array(t1)
        # a1_np = np.array(a1)
        myArr = np.column_stack((np.array(t1),np.array(a1)))
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        
        file_name = os.path.join(desktop_path, 'recData', 'exportedShaper.csv')

        try:
            # Ensure the recData directory exists
            rec_data_path = os.path.dirname(file_name)
            os.makedirs(rec_data_path, exist_ok=True)

            # Save the numpy array to the CSV file
            np.savetxt(file_name, myArr, delimiter=",", header="Times,Amp", comments="")
            # Notify the user that saving is done
            dialog = NotifyBox(msg="Shaper Exported Successfully")
            if dialog.exec_() == QDialog.Accepted:
                pass
        except Exception as e:
            # Notify the user of an error
            dialog = NotifyBox(msg="Error: Please close the data Excel sheet and export again.\nDetails: " + str(e))
            if dialog.exec_() == QDialog.Accepted:
                pass
       
    def createWarning(self, warningMsg = ''):
        dial = NotifyBox(msg=warningMsg)
        if dial.exec_() == QDialog.Accepted:
                print("Warning dialog was acknowledged.")





"""
Add these lines to bottom of ititialize gui right before the line self.retranslateUi(MainWindow)
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
"""