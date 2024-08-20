from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QComboBox, QMessageBox
from PyQt5 import QtGui
class craneCalDial(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Crane Calibration. Put -1 if you dont want to change the value")
        
        self.layout = QVBoxLayout()

        self.info_label = QLabel("Please Input Crane Calibration Values. Use -1 if you do not want the value to change ")
        self.layout.addWidget(self.info_label)

        self.value1_layout = QHBoxLayout()
        self.value1_label = QLabel("Slew Angle deg:")
        self.value1_input = QLineEdit()
        self.value1_layout.addWidget(self.value1_label)
        self.value1_layout.addWidget(self.value1_input)

        self.value2_layout = QHBoxLayout()
        self.value2_label = QLabel("Trolley Dist mm:")
        self.value2_input = QLineEdit()
        self.value2_layout.addWidget(self.value2_label)
        self.value2_layout.addWidget(self.value2_input)

        self.value3_layout = QHBoxLayout()
        self.value3_label = QLabel("Hoist Height mm:")
        self.value3_input = QLineEdit()
        self.value3_layout.addWidget(self.value3_label)
        self.value3_layout.addWidget(self.value3_input)

        self.layout.addLayout(self.value1_layout)
        self.layout.addLayout(self.value2_layout)
        self.layout.addLayout(self.value3_layout)

        self.buttons_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.buttons_layout.addWidget(self.ok_button)
        self.buttons_layout.addWidget(self.cancel_button)

        self.layout.addLayout(self.buttons_layout)

        self.setLayout(self.layout)

    def getValues(self):
        return self.value1_input.text(), self.value2_input.text(), self.value3_input.text()
    
class shaperDial(QDialog):
    def __init__(self, parent=None, amps = None, times = None):
        """
            This function makes the pop up box for the custom input shapers. 
        """
        super().__init__(parent)

        self.setWindowTitle("User Input Shaper")
        self.resize(600,600)
        self.setStyleSheet("background-color: lightblue;")
        
        self.layout = QVBoxLayout()
        self.shaperLayout = QHBoxLayout()
        self.info_label = QLabel("Please Input Shaper Amplitudes and times. Note all amplitudes are rounded to one decimal place and the times are to the nearest whole number.")
        self.info_label.setStyleSheet("font-size: 20px;")  # Set font size to 20px
        self.layout.addWidget(self.info_label)
        self.mainLeftLayout = QHBoxLayout()
        self.mainRightLayout =  QHBoxLayout()

        self.leftLabels = QVBoxLayout()
        self.leftAmps = QVBoxLayout()
        self.leftTimes = QVBoxLayout()

        self.rightLabels = QVBoxLayout()
        self.rightAmps = QVBoxLayout()
        self.rightTimes = QVBoxLayout()

        self.imLabel = QLabel("Impulse:")
        self.amLabel = QLabel("Amp %:")
        self.timeLabel = QLabel("Time ms:")
        self.imLabel.setStyleSheet("font-size: 20px;")  # Set font size to 20px
        self.amLabel.setStyleSheet("font-size: 20px;")  # Set font size to 20px
        self.timeLabel.setStyleSheet("font-size: 20px;")  # Set font size to 20px
        self.imLabel2 = QLabel("Impulse:")
        self.amLabel2 = QLabel("Amp %:")
        self.timeLabel2 = QLabel("Time ms:")
        self.imLabel2.setStyleSheet("font-size: 20px;")  # Set font size to 20px
        self.amLabel2.setStyleSheet("font-size: 20px;")  # Set font size to 20px
        self.timeLabel2.setStyleSheet("font-size: 20px;")  # Set font size to 20px
        self.leftLabels.addWidget(self.imLabel)
        self.leftAmps.addWidget(self.amLabel)
        self.leftTimes.addWidget(self.timeLabel)
        self.rightLabels.addWidget(self.imLabel2)
        self.rightAmps.addWidget(self.amLabel2)
        self.rightTimes.addWidget(self.timeLabel2)

        inputColor = "background-color: white;"

        self.a1_label = QLabel("Impulse 1:")
        self.a1_input = QLineEdit()
        self.t1_input = QLineEdit()
        self.a1_input.setText(str(amps[0]))
        self.t1_input.setText(str(times[0]))
        self.a1_input.setStyleSheet(inputColor)
        self.t1_input.setStyleSheet(inputColor)
        self.leftLabels.addWidget(self.a1_label)
        self.leftAmps.addWidget(self.a1_input)
        self.leftTimes.addWidget(self.t1_input)

        self.a2_label = QLabel("Impulse 2:")
        self.a2_input = QLineEdit()
        self.t2_input = QLineEdit()
        self.a2_input.setText(str(amps[1]))
        self.t2_input.setText(str(times[1]))
        self.a2_input.setStyleSheet(inputColor)
        self.t2_input.setStyleSheet(inputColor)
        self.leftLabels.addWidget(self.a2_label)
        self.leftAmps.addWidget(self.a2_input)
        self.leftTimes.addWidget(self.t2_input)

        self.a3_label = QLabel("Impulse 3:")
        self.a3_input = QLineEdit()
        self.t3_input = QLineEdit()
        self.a3_input.setText(str(amps[2]))
        self.t3_input.setText(str(times[2]))
        self.a3_input.setStyleSheet(inputColor)
        self.t3_input.setStyleSheet(inputColor)
        self.leftLabels.addWidget(self.a3_label)
        self.leftAmps.addWidget(self.a3_input)
        self.leftTimes.addWidget(self.t3_input)
        
        self.a4_label = QLabel("Impulse 4:")
        self.a4_input = QLineEdit()
        self.t4_input = QLineEdit()
        self.a4_input.setText(str(amps[3]))
        self.t4_input.setText(str(times[3]))
        self.a4_input.setStyleSheet(inputColor)
        self.t4_input.setStyleSheet(inputColor)
        self.leftLabels.addWidget(self.a4_label)
        self.leftAmps.addWidget(self.a4_input)
        self.leftTimes.addWidget(self.t4_input)

        self.a5_label = QLabel("Impulse 5:")
        self.a5_input = QLineEdit()
        self.t5_input = QLineEdit()
        self.a5_input.setText(str(amps[4]))
        self.t5_input.setText(str(times[4]))
        self.a5_input.setStyleSheet(inputColor)
        self.t5_input.setStyleSheet(inputColor)
        self.leftLabels.addWidget(self.a5_label)
        self.leftAmps.addWidget(self.a5_input)
        self.leftTimes.addWidget(self.t5_input)

        self.a6_label = QLabel("Impulse 6:")
        self.a6_input = QLineEdit()
        self.t6_input = QLineEdit()
        self.a6_input.setText(str(amps[5]))
        self.t6_input.setText(str(times[5]))
        self.a6_input.setStyleSheet(inputColor)
        self.t6_input.setStyleSheet(inputColor)
        self.leftLabels.addWidget(self.a6_label)
        self.leftAmps.addWidget(self.a6_input)
        self.leftTimes.addWidget(self.t6_input)

        self.a7_label = QLabel("Impulse 7:")
        self.a7_input = QLineEdit()
        self.t7_input = QLineEdit()
        self.a7_input.setText(str(amps[6]))
        self.t7_input.setText(str(times[6]))
        self.a7_input.setStyleSheet(inputColor)
        self.t7_input.setStyleSheet(inputColor)
        self.leftLabels.addWidget(self.a7_label)
        self.leftAmps.addWidget(self.a7_input)
        self.leftTimes.addWidget(self.t7_input)

        self.a8_label = QLabel("Impulse 8:")
        self.a8_input = QLineEdit()
        self.t8_input = QLineEdit()
        self.a8_input.setText(str(amps[7]))
        self.t8_input.setText(str(times[7]))
        self.a8_input.setStyleSheet(inputColor)
        self.t8_input.setStyleSheet(inputColor)
        self.leftLabels.addWidget(self.a8_label)
        self.leftAmps.addWidget(self.a8_input)
        self.leftTimes.addWidget(self.t8_input)

        self.a9_label = QLabel("Impulse 9:")
        self.a9_input = QLineEdit()
        self.t9_input = QLineEdit()
        self.a9_input.setText(str(amps[8]))
        self.t9_input.setText(str(times[8]))
        self.a9_input.setStyleSheet(inputColor)
        self.t9_input.setStyleSheet(inputColor)
        self.leftLabels.addWidget(self.a9_label)
        self.leftAmps.addWidget(self.a9_input)
        self.leftTimes.addWidget(self.t9_input)

        self.a10_label = QLabel("Impulse 10:")
        self.a10_input = QLineEdit()
        self.t10_input = QLineEdit()
        self.a10_input.setText(str(amps[9]))
        self.t10_input.setText(str(times[9]))
        self.a10_input.setStyleSheet(inputColor)
        self.t10_input.setStyleSheet(inputColor)
        self.leftLabels.addWidget(self.a10_label)
        self.leftAmps.addWidget(self.a10_input)
        self.leftTimes.addWidget(self.t10_input)

        self.a11_label = QLabel("Impulse 11:")
        self.a11_input = QLineEdit()
        self.t11_input = QLineEdit()
        self.a11_input.setText(str(amps[10]))
        self.t11_input.setText(str(times[10]))
        self.a11_input.setStyleSheet(inputColor)
        self.t11_input.setStyleSheet(inputColor)
        self.rightLabels.addWidget(self.a11_label)
        self.rightAmps.addWidget(self.a11_input)
        self.rightTimes.addWidget(self.t11_input)

        self.a12_label = QLabel("Impulse 12:")
        self.a12_input = QLineEdit()
        self.t12_input = QLineEdit()
        self.a12_input.setText(str(amps[11]))
        self.t12_input.setText(str(times[11]))
        self.a12_input.setStyleSheet(inputColor)
        self.t12_input.setStyleSheet(inputColor)
        self.rightLabels.addWidget(self.a12_label)
        self.rightAmps.addWidget(self.a12_input)
        self.rightTimes.addWidget(self.t12_input)

        self.a13_label = QLabel("Impulse 13:")
        self.a13_input = QLineEdit()
        self.t13_input = QLineEdit()
        self.a13_input.setText(str(amps[12]))
        self.t13_input.setText(str(times[12]))
        self.a13_input.setStyleSheet(inputColor)
        self.t13_input.setStyleSheet(inputColor)
        self.rightLabels.addWidget(self.a13_label)
        self.rightAmps.addWidget(self.a13_input)
        self.rightTimes.addWidget(self.t13_input)

        self.a14_label = QLabel("Impulse 14:")
        self.a14_input = QLineEdit()
        self.t14_input = QLineEdit()
        self.a14_input.setText(str(amps[13]))
        self.t14_input.setText(str(times[13]))
        self.a14_input.setStyleSheet(inputColor)
        self.t14_input.setStyleSheet(inputColor)
        self.rightLabels.addWidget(self.a14_label)
        self.rightAmps.addWidget(self.a14_input)
        self.rightTimes.addWidget(self.t14_input)

        self.a15_label = QLabel("Impulse 15:")
        self.a15_input = QLineEdit()
        self.t15_input = QLineEdit()
        self.a15_input.setText(str(amps[14]))
        self.t15_input.setText(str(times[14]))
        self.a15_input.setStyleSheet(inputColor)
        self.t15_input.setStyleSheet(inputColor)
        self.rightLabels.addWidget(self.a15_label)
        self.rightAmps.addWidget(self.a15_input)
        self.rightTimes.addWidget(self.t15_input)

        self.a16_label = QLabel("Impulse 16:")
        self.a16_input = QLineEdit()
        self.t16_input = QLineEdit()
        self.a16_input.setText(str(amps[15]))
        self.t16_input.setText(str(times[15]))
        self.a16_input.setStyleSheet(inputColor)
        self.t16_input.setStyleSheet(inputColor)
        self.rightLabels.addWidget(self.a16_label)
        self.rightAmps.addWidget(self.a16_input)
        self.rightTimes.addWidget(self.t16_input)

        self.a17_label = QLabel("Impulse 17:")
        self.a17_input = QLineEdit()
        self.t17_input = QLineEdit()
        self.a17_input.setText(str(amps[16]))
        self.t17_input.setText(str(times[16]))
        self.a17_input.setStyleSheet(inputColor)
        self.t17_input.setStyleSheet(inputColor)
        self.rightLabels.addWidget(self.a17_label)
        self.rightAmps.addWidget(self.a17_input)
        self.rightTimes.addWidget(self.t17_input)

        self.a18_label = QLabel("Impulse 18:")
        self.a18_input = QLineEdit()
        self.t18_input = QLineEdit()
        self.a18_input.setText(str(amps[17]))
        self.t18_input.setText(str(times[17]))
        self.a18_input.setStyleSheet(inputColor)
        self.t18_input.setStyleSheet(inputColor)
        self.rightLabels.addWidget(self.a18_label)
        self.rightAmps.addWidget(self.a18_input)
        self.rightTimes.addWidget(self.t18_input)

        self.a19_label = QLabel("Impulse 19:")
        self.a19_input = QLineEdit()
        self.t19_input = QLineEdit()
        self.a19_input.setText(str(amps[18]))
        self.t19_input.setText(str(times[18]))
        self.a19_input.setStyleSheet(inputColor)
        self.t19_input.setStyleSheet(inputColor)
        self.rightLabels.addWidget(self.a19_label)
        self.rightAmps.addWidget(self.a19_input)
        self.rightTimes.addWidget(self.t19_input)

        self.a20_label = QLabel("Impulse 20:")
        self.a20_input = QLineEdit()
        self.t20_input = QLineEdit()
        self.a20_input.setText(str(amps[19]))
        self.t20_input.setText(str(times[19]))
        self.a20_input.setStyleSheet(inputColor)
        self.t20_input.setStyleSheet(inputColor)
        self.rightLabels.addWidget(self.a20_label)
        self.rightAmps.addWidget(self.a20_input)
        self.rightTimes.addWidget(self.t20_input)



        self.mainLeftLayout.addLayout(self.leftLabels)
        self.mainLeftLayout.addLayout(self.leftAmps)
        self.mainLeftLayout.addLayout(self.leftTimes)
        self.mainRightLayout.addLayout(self.rightLabels)
        self.mainRightLayout.addLayout(self.rightAmps)
        self.mainRightLayout.addLayout(self.rightTimes)

        self.shaperLayout.addLayout(self.mainLeftLayout)
        self.shaperLayout.addLayout(self.mainRightLayout)

        self.layout.addLayout(self.shaperLayout)


        self.buttons_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.ok_button.setStyleSheet(inputColor)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet(inputColor)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.buttons_layout.addWidget(self.ok_button)
        self.buttons_layout.addWidget(self.cancel_button)

        self.layout.addLayout(self.buttons_layout)

        self.setLayout(self.layout)

    def getValues(self):
        times = [self.t1_input.text(),self.t2_input.text(),self.t3_input.text(),self.t4_input.text(),self.t5_input.text(),
                 self.t6_input.text(),self.t7_input.text(),self.t8_input.text(),self.t9_input.text(),self.t10_input.text(),
                 self.t11_input.text(),self.t12_input.text(),self.t13_input.text(),self.t14_input.text(),self.t15_input.text(),
                 self.t16_input.text(),self.t17_input.text(),self.t18_input.text(),self.t19_input.text(),self.t20_input.text()]
        amps = [self.a1_input.text(),self.a2_input.text(),self.a3_input.text(),self.a4_input.text(),self.a5_input.text(),
                self.a6_input.text(),self.a7_input.text(),self.a8_input.text(),self.a9_input.text(),self.a10_input.text(),
                self.a11_input.text(),self.a12_input.text(),self.a13_input.text(),self.a14_input.text(),self.a15_input.text(),
                self.a16_input.text(),self.a17_input.text(),self.a18_input.text(),self.a19_input.text(),self.a20_input.text()]
       
        times_float = [0]*20
        amps_float = [0] *20
    
        #for each value in the array 
        for i in range(20):
            #try to convert it to a float but if you cant, put zero
            try:
                times_float[i] = round(float(times[i]),0)
            except:
                pass
            try:
                amps_float[i] = round(float(amps[i]),1)
            except:
                pass

        # times_float = [float(x) for x in times]
        # amps_float = [float(x) for x in amps]

        return times_float,amps_float

class PasswordDialog(QDialog):
    def __init__(self, correct_password, parent=None):
        super().__init__(parent)
        self.correct_password = correct_password
        self.setWindowTitle('Password Entry')
        self.resize(300, 150)

        # Create layout
        layout = QVBoxLayout(self)

        # Information label
        self.info_label = QLabel("Please enter the password:", self)
        layout.addWidget(self.info_label)

        # Password input field
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Buttons
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK", self)
        self.cancel_button = QPushButton("Cancel", self)
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        # Connect buttons
        self.ok_button.clicked.connect(self.check_password)
        self.cancel_button.clicked.connect(self.reject)

    def check_password(self):
        if self.password_input.text() == self.correct_password:
            self.accept()
        else:
            self.info_label.setText("Incorrect password, please try again:")
            self.password_input.clear()

class NotifyBox(QDialog):
    def __init__(self, msg = " ", parent=None):
        super().__init__(parent)
        self.setWindowTitle('Notification ')
        self.resize(300, 150)

        # Create layout
        layout = QVBoxLayout(self)

        # Warning label
        self.warning_label = QLabel(msg, self)
        self.warning_label.setStyleSheet("color: black; font-weight: bold;")  # Style the warning message
        layout.addWidget(self.warning_label)

        # OK button
        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Add stretch to push the button to the right
        button_layout.addWidget(self.ok_button)
        layout.addLayout(button_layout)

class faultBox(QDialog):
    def __init__(self, motor0Faults, motor1Faults, motor2Faults, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Current Motor Faults')
        self.resize(300, 150)

        # Create main layout
        main_layout = QVBoxLayout(self)
        
        # Create motor layout
        motorLayout = QHBoxLayout()
        
        # Create sub-layouts
        slewLayout = QVBoxLayout()
        trolleyLayout = QVBoxLayout()
        hoistLayout = QVBoxLayout()

        # Warning labels
        self.trolleyLabel = QLabel("Trolley", self)
        self.slewLabel = QLabel("Slew", self)
        self.hositLabel = QLabel("Hoist", self)

        # Add labels to sub-layouts
        slewLayout.addWidget(self.slewLabel)
        for fault in motor0Faults:
            faultLabel = QLabel(fault)
            slewLayout.addWidget(faultLabel)

        trolleyLayout.addWidget(self.trolleyLabel)

        for fault in motor1Faults:
            faultLabel = QLabel(fault)
            trolleyLayout.addWidget(faultLabel)

        hoistLayout.addWidget(self.hositLabel)
        for fault in motor2Faults:
            faultLabel = QLabel(fault)
            hoistLayout.addWidget(faultLabel)

        # Add sub-layouts to motor layout
        motorLayout.addLayout(slewLayout)
        motorLayout.addLayout(trolleyLayout)
        motorLayout.addLayout(hoistLayout)

        # OK button
        self.clear_button = QPushButton("Clear Faults", self)
        self.clear_button.clicked.connect(self.accept)
        self.cancel_button = QPushButton("Close", self)
        self.cancel_button.clicked.connect(self.reject)

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Add stretch to push the button to the right
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.cancel_button)

        # Add motor layout and button layout to main layout
        main_layout.addLayout(motorLayout)
        main_layout.addLayout(button_layout)

class UsbSelectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Select USB Device')
        self.resize(300, 150)

        # Create layout
        layout = QVBoxLayout(self)

        # Info label
        self.info_label = QLabel("Select a USB device:", self)
        layout.addWidget(self.info_label)

        # Combo box
        self.usb_combo = QComboBox(self)
        layout.addWidget(self.usb_combo)

        # Fill combo box with USB devices
        self.populate_usb_devices()

        # OK button
        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

    def populate_usb_devices(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            device_name = f"{port.device} - {port.description}"
            self.usb_combo.addItem(device_name, port.device)

    def get_selected_device(self):
        return self.usb_combo.currentData()
    
class commandGenBox(QDialog):
    def __init__(self, parent=None, motor = 0, duration = None, amplitude = None):
        super().__init__(parent)

        self.setWindowTitle("Command Generation")
        
        self.layout = QVBoxLayout()
        font = QtGui.QFont()
        font.setPointSize(15)

        self.motorLabel = QLabel("Motor:")
        self.motorLabel.setFont(font)
        self.motorComboBox = QComboBox()
        self.motorComboBox.addItem("Trolley")
        self.motorComboBox.addItem("Slewing")
        self.motorComboBox.addItem("Hoisting")
        self.motorComboBox.setFont(font)

        self.motorComboBox.setCurrentIndex(motor)
        
        self.motorLayout = QHBoxLayout()
        self.motorLayout.addWidget(self.motorLabel)
        self.motorLayout.addWidget(self.motorComboBox)
        self.layout.addLayout(self.motorLayout)

        self.durLabel  = QLabel("Command Duration ms:")
        self.durLabel.setFont(font)
        self.dur_input = QLineEdit()
        self.dur_input.setFont(font)
        self.durLabel.setFont(font)
        self.durLayout = QHBoxLayout()
        self.dur_input.setText(duration)
        self.durLayout.addWidget(self.durLabel)
        self.durLayout.addWidget(self.dur_input)
        self.layout.addLayout(self.durLayout)

        self.ampLabel  = QLabel("Command Amplitude %:")
        self.ampLabel.setFont(font)
        self.amp_input = QLineEdit()
        self.amp_input.setText(amplitude)
        self.amp_input.setFont(font)
        self.ampLayout = QHBoxLayout()
        self.ampLayout.addWidget(self.ampLabel)
        self.ampLayout.addWidget(self.amp_input)
        self.layout.addLayout(self.ampLayout)


        self.buttons_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.buttons_layout.addWidget(self.ok_button)
        self.buttons_layout.addWidget(self.cancel_button)

        font2 = QtGui.QFont()
        font2.setPointSize(15)
        self.ok_button.setFont(font2)
        self.cancel_button.setFont(font2)
        self.layout.addLayout(self.buttons_layout)

        self.setLayout(self.layout)

    def getValues(self):
        dur = self.dur_input.text()
        return self.motorComboBox.currentIndex(), (self.dur_input.text()), (self.amp_input.text())
    