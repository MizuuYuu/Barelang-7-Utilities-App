import sys
from dynamixel_sdk import *
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QMenuBar

class MXSeries:
    ADDR_TORQUE_ENABLE = 64
    ADDR_GOAL_POSITION = 116
    ADDR_PRESENT_POSITION = 132
    POSITION_ZERO = 2048
    MAX_RESOLUTION = 4096
    MAX_ANGLE = 360

class XSeries:
    ADDR_TORQUE_ENABLE = 64
    ADDR_GOAL_POSITION = 116
    ADDR_PRESENT_POSITION = 132
    POSITION_ZERO = 2048
    MAX_RESOLUTION = 4096
    MAX_ANGLE = 360

class XL320:
    ADDR_TORQUE_ENABLE = 24
    ADDR_GOAL_POSITION = 30
    ADDR_PRESENT_POSITION = 37
    POSITION_ZERO = 512
    MAX_RESOLUTION = 1024
    MAX_ANGLE = 300

TORQUE_ENABLE = 1
TORQUE_DISABLE = 0

# DEVICENAME = "/dev/ttyUSB0"
# portHandler = PortHandler(DEVICENAME)

# PROTOCOL_VERSION = 2
# packetHandler = PacketHandler(PROTOCOL_VERSION)

# if portHandler.openPort():
#     print("Succeeded to open the port")
# else:
#     print("Failed to open the port")
#     print("Press any key to terminate...")
#     quit()


# # Set port baudrate
# BAUDRATE = 1000000
# if portHandler.setBaudRate(BAUDRATE):
#     print("Succeeded to change the baudrate")
# else:
#     print("Failed to change the baudrate")
#     print("Press any key to terminate...")
#     quit()

def writePosition(series, id, goal_deg_position):
    # if series == "MX_Series":
    #     dxl_goal_position = int(MXSeries.POSITION_ZERO + MXSeries.MAX_RESOLUTION * goal_deg_position / MXSeries.MAX_ANGLE)
    #     dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, id, MXSeries.ADDR_GOAL_POSITION, dxl_goal_position)
    # elif series == "X_Series":
    #     dxl_goal_position = int(XSeries.POSITION_ZERO + XSeries.MAX_RESOLUTION * goal_deg_position / XSeries.MAX_ANGLE)
    #     dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, id, XSeries.ADDR_GOAL_POSITION, dxl_goal_position)
    # elif series == "XL320":
    #     dxl_goal_position = int(XL320.POSITION_ZERO + XL320.MAX_RESOLUTION * goal_deg_position / XL320.MAX_ANGLE)
    #     dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, id, XL320.ADDR_GOAL_POSITION, dxl_goal_position)
    # if dxl_comm_result != COMM_SUCCESS:
    #     print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    # elif dxl_error != 0:
    #     print("%s" % packetHandler.getRxPacketError(dxl_error))
    pass

def writeHardness(series, id, data_torque):
    # if series == "MX_Series":
    #     dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, id, MXSeries.ADDR_TORQUE_ENABLE, data_torque)
    # elif series == "X_Series":
    #     dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, id, XSeries.ADDR_TORQUE_ENABLE, data_torque)
    # elif series == "XL320":
    #     dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, id, XL320.ADDR_TORQUE_ENABLE, data_torque)
    # if dxl_comm_result != COMM_SUCCESS:
    #     print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    # elif dxl_error != 0:
    #     print("%s" % packetHandler.getRxPacketError(dxl_error))
    pass

def readPosition(series, id):
    # if series == "MX_Series":
    #     dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, id, MXSeries.ADDR_PRESENT_POSITION)
    #     cur_deg_position = (dxl_present_position - MXSeries.POSITION_ZERO) * MXSeries.MAX_ANGLE / MXSeries.MAX_RESOLUTION
    # elif series == "X_Series":
    #     dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, id, XSeries.ADDR_PRESENT_POSITION)
    #     cur_deg_position = (dxl_present_position - XSeries.POSITION_ZERO) * XSeries.MAX_ANGLE / XSeries.MAX_RESOLUTION
    # elif series == "XL320":
    #     dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, id, XL320.ADDR_PRESENT_POSITION)
    #     cur_deg_position = (dxl_present_position - XL320.POSITION_ZERO) * XL320.MAX_ANGLE / XL320.MAX_RESOLUTION
    # if dxl_comm_result != COMM_SUCCESS:
    #     print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    # elif dxl_error != 0:
    #     print("%s" % packetHandler.getRxPacketError(dxl_error))
    # return cur_deg_position
    pass

class hipFunction:
    def __init__(self, window):
        self.window = window
        self.window.buttonServo13.clicked.connect(self.servo13hardness)
        self.window.spinBoxServo13.valueChanged.connect(self.servo13position)
        self.button13Pressed = 0
        self.DXL_SERIES = "X_Series"
        self.DXL_ID = 13
    def servo13hardness(self):
        if self.button13Pressed == 0:
            print("Servo 13 Locked")
            self.window.buttonServo13.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID, TORQUE_ENABLE)
            self.cur_deg_position_13 = readPosition(self.DXL_SERIES, self.DXL_ID)
            self.window.spinBoxServo13.setValue(self.cur_deg_position_13)
            self.button13Pressed = 1
        else:
            print("Servo 13 Unlocked")
            self.window.buttonServo13.setText("Lock")
            writeHardness(self.DXL_SERIES, self.DXL_ID, TORQUE_DISABLE)
            self.button13Pressed = 0
    def servo13position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID, self.window.spinBoxServo13.value())

class chestFunction:
    def __init__(self, window):
        self.window = window
        self.window.buttonServo14.clicked.connect(self.servo14hardness)
        self.window.spinBoxServo14.valueChanged.connect(self.servo14position)
        self.button14Pressed = 0
        self.DXL_SERIES = "MX_Series"
        self.DXL_ID = 14
    def servo14hardness(self):
        if self.button14Pressed == 0:
            print("Servo 14 Locked")
            self.window.buttonServo14.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID, TORQUE_ENABLE)
            self.cur_deg_position_14 = readPosition(self.DXL_SERIES, self.DXL_ID)
            self.window.spinBoxServo14.setValue(self.cur_deg_position_14)
            self.button14Pressed = 1
        else:
            print("Servo 14 Unlocked")
            self.window.buttonServo14.setText("Lock")
            writeHardness(self.DXL_SERIES, self.DXL_ID, TORQUE_DISABLE)
            self.button14Pressed = 0
    def servo14position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID, self.window.spinBoxServo14.value())

class rightArmFunction:
    def __init__(self,window):
        self.window = window
        self.window.buttonServo15.clicked.connect(self.servo15hardness)
        self.window.spinBoxServo15.valueChanged.connect(self.servo15position)
        self.window.buttonServo17.clicked.connect(self.servo17hardness)
        self.window.spinBoxServo17.valueChanged.connect(self.servo17position)
        self.window.buttonServo18.clicked.connect(self.servo18hardness)
        self.window.spinBoxServo18.valueChanged.connect(self.servo18position)
        self.window.buttonServo19.clicked.connect(self.servo19hardness)
        self.window.spinBoxServo19.valueChanged.connect(self.servo19position)
        self.window.buttonServo20.clicked.connect(self.servo20hardness)
        self.window.spinBoxServo20.valueChanged.connect(self.servo20position)
        self.window.buttonServo21.clicked.connect(self.servo21hardness)
        self.window.spinBoxServo21.valueChanged.connect(self.servo21position)
        self.window.buttonRArm.clicked.connect(self.rightArmHardness)
        self.buttonRArmPressed = 0
        self.button15Pressed = 0
        self.button17Pressed = 0
        self.button18Pressed = 0
        self.button19Pressed = 0
        self.button20Pressed = 0
        self.button21Pressed = 0
        self.DXL_SERIES_SHOULDER = "X_Series"
        self.DXL_SERIES = "XL320"
        self.DXL_ID_SHOULDER = 15
        self.DXL_ID = [17, 18, 19, 20, 21]
    def rightArmHardness(self):
        if self.buttonRArmPressed == 0:
            print("Right Arm Locked")
            self.window.buttonRArm.setText("Unlock All")
            self.buttonRArmPressed = 1
            self.button15Pressed = 0
            self.button17Pressed = 0
            self.button18Pressed = 0
            self.button19Pressed = 0
            self.button20Pressed = 0
            self.button21Pressed = 0
        else:
            print("Right Arm Unlocked")
            self.window.buttonRArm.setText("Lock All")
            self.buttonRArmPressed = 0
            self.button15Pressed = 1
            self.button17Pressed = 1
            self.button18Pressed = 1
            self.button19Pressed = 1
            self.button20Pressed = 1
            self.button21Pressed = 1
        self.servo15hardness()
        self.servo17hardness()
        self.servo18hardness()
        self.servo19hardness()
        self.servo20hardness()
        self.servo21hardness()
    def servo15hardness(self):
        if self.button15Pressed == 0:
            print("Servo 15 Locked")
            self.window.buttonServo15.setText("Unlock")
            writeHardness(self.DXL_SERIES_SHOULDER, self.DXL_ID_SHOULDER, TORQUE_ENABLE)
            self.cur_deg_position_15 = readPosition(self.DXL_SERIES_SHOULDER, self.DXL_ID_SHOULDER)
            self.window.spinBoxServo15.setValue(self.cur_deg_position_15)
            self.button15Pressed = 1
        else:
            print("Servo 15 Unlocked")
            self.window.buttonServo15.setText("Lock")
            self.window.buttonRArm.setText("Lock All")
            writeHardness(self.DXL_SERIES_SHOULDER, self.DXL_ID_SHOULDER, TORQUE_DISABLE)
            self.buttonRArmPressed = 0
            self.button15Pressed = 0
    def servo15position(self):
        writePosition(self.DXL_SERIES_SHOULDER, self.DXL_ID_SHOULDER,self.window.spinBoxServo15.value())
    def servo17hardness(self):
        if self.button17Pressed == 0:
            print("Servo 17 Locked")
            self.window.buttonServo17.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[0], TORQUE_ENABLE)
            self.cur_deg_position_17 = readPosition(self.DXL_SERIES, self.DXL_ID[0])
            self.window.spinBoxServo17.setValue(self.cur_deg_position_17)
            self.button17Pressed = 1
        else:
            print("Servo 17 Unlocked")
            self.window.buttonServo17.setText("Lock")
            self.window.buttonRArm.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[0], TORQUE_DISABLE)
            self.buttonRArmPressed = 0
            self.button17Pressed = 0
    def servo17position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[0], self.window.spinBoxServo17.value())
    def servo18hardness(self):
        if self.button18Pressed == 0:
            print("Servo 18 Locked")
            self.window.buttonServo18.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[1], TORQUE_ENABLE)
            self.cur_deg_position_18 = readPosition(self.DXL_SERIES, self.DXL_ID[1])
            self.window.spinBoxServo18.setValue(self.cur_deg_position_18)
            self.button18Pressed = 1
        else:
            print("Servo 18 Unlocked")
            self.window.buttonServo18.setText("Lock")
            self.window.buttonRArm.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[1], TORQUE_DISABLE)
            self.buttonRArmPressed = 0
            self.button18Pressed = 0
    def servo18position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[1], self.window.spinBoxServo18.value())
    def servo19hardness(self):
        if self.button19Pressed == 0:
            print("Servo 19 Locked")
            self.window.buttonServo19.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[2], TORQUE_ENABLE)
            self.cur_deg_position_19 = readPosition(self.DXL_SERIES, self.DXL_ID[2])
            self.window.spinBoxServo19.setValue(self.cur_deg_position_19)
            self.button19Pressed = 1
        else:
            print("Servo 19 Unlocked")
            self.window.buttonServo19.setText("Lock")
            self.window.buttonRArm.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[2], TORQUE_DISABLE)
            self.buttonRArmPressed = 0
            self.button19Pressed = 0
    def servo19position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[2], self.window.spinBoxServo19.value())
    def servo20hardness(self):
        if self.button20Pressed == 0:
            print("Servo 20 Locked")
            self.window.buttonServo20.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[3], TORQUE_ENABLE)
            self.cur_deg_position_20 = readPosition(self.DXL_SERIES, self.DXL_ID[3])
            self.window.spinBoxServo20.setValue(self.cur_deg_position_20)
            self.button20Pressed = 1
        else:
            print("Servo 20 Unlocked")
            self.window.buttonServo20.setText("Lock")
            self.window.buttonRArm.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[3], TORQUE_DISABLE)
            self.buttonRArmPressed = 0
            self.button20Pressed = 0
    def servo20position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[3], self.window.spinBoxServo20.value())
    def servo21hardness(self):
        if self.button21Pressed == 0:
            print("Servo 21 Locked")
            self.window.buttonServo21.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[4], TORQUE_ENABLE)
            self.cur_deg_position_21 = readPosition(self.DXL_SERIES, self.DXL_ID[4])
            self.window.spinBoxServo21.setValue(self.cur_deg_position_21)
            self.button21Pressed = 1
        else:
            print("Servo 21 Unlocked")
            self.window.buttonServo21.setText("Lock")
            self.window.buttonRArm.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[4], TORQUE_DISABLE)
            self.buttonRArmPressed = 0
            self.button21Pressed = 0
    def servo21position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[4], self.window.spinBoxServo21.value())

class leftArmFunction:
    def __init__(self,window):
        self.window = window
        self.window.buttonServo16.clicked.connect(self.servo16hardness)
        self.window.spinBoxServo16.valueChanged.connect(self.servo16position)
        self.window.buttonServo22.clicked.connect(self.servo22hardness)
        self.window.spinBoxServo22.valueChanged.connect(self.servo22position)
        self.window.buttonServo23.clicked.connect(self.servo23hardness)
        self.window.spinBoxServo23.valueChanged.connect(self.servo23position)
        self.window.buttonServo24.clicked.connect(self.servo24hardness)
        self.window.spinBoxServo24.valueChanged.connect(self.servo24position)
        self.window.buttonServo25.clicked.connect(self.servo25hardness)
        self.window.spinBoxServo25.valueChanged.connect(self.servo25position)
        self.window.buttonServo26.clicked.connect(self.servo26hardness)
        self.window.spinBoxServo26.valueChanged.connect(self.servo26position)
        self.window.buttonLArm.clicked.connect(self.leftArmHardness)
        self.buttonLArmPressed = 0
        self.button16Pressed = 0
        self.button22Pressed = 0
        self.button23Pressed = 0
        self.button24Pressed = 0
        self.button25Pressed = 0
        self.button26Pressed = 0
        self.DXL_SERIES_SHOULDER = "X_Series"
        self.DXL_ID_SHOULDER = 16
        self.DXL_SERIES = "XL320"
        self.DXL_ID = [22, 23, 24, 25, 26]
    def leftArmHardness(self):
        if self.buttonLArmPressed == 0:
            print("Left Arm Locked")
            self.window.buttonLArm.setText("Unlock All")
            self.buttonLArmPressed = 1
            self.button16Pressed = 0
            self.button22Pressed = 0
            self.button23Pressed = 0
            self.button24Pressed = 0
            self.button25Pressed = 0
            self.button26Pressed = 0
        else:
            print("Left Arm Unlocked")
            self.window.buttonLArm.setText("Lock All")
            self.buttonLArmPressed = 0
            self.button16Pressed = 1
            self.button22Pressed = 1
            self.button23Pressed = 1
            self.button24Pressed = 1
            self.button25Pressed = 1
            self.button26Pressed = 1
        self.servo16hardness()
        self.servo22hardness()
        self.servo23hardness()
        self.servo24hardness()
        self.servo25hardness()
        self.servo26hardness()
    def servo16hardness(self):
        if self.button16Pressed == 0:
            print("Servo 16 Locked")
            self.window.buttonServo16.setText("Unlock")
            writeHardness(self.DXL_SERIES_SHOULDER, self.DXL_ID_SHOULDER, TORQUE_ENABLE)
            self.cur_deg_position_16 = readPosition(self.DXL_SERIES_SHOULDER, self.DXL_ID_SHOULDER)
            self.window.spinBoxServo16.setValue(self.cur_deg_position_16)
            self.button16Pressed = 1
        else:
            print("Servo 16 Unlocked")
            self.window.buttonServo16.setText("Lock")
            self.window.buttonLArm.setText("Lock All")
            writeHardness(self.DXL_SERIES_SHOULDER, self.DXL_ID_SHOULDER, TORQUE_DISABLE)
            self.buttonLArmPressed = 0
            self.button16Pressed = 0
    def servo16position(self):
        writePosition(self.DXL_SERIES_SHOULDER, self.DXL_ID_SHOULDER,self.window.spinBoxServo16.value())
    def servo22hardness(self):
        if self.button22Pressed == 0:
            print("Servo 22 Locked")
            self.window.buttonServo22.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[0], TORQUE_ENABLE)
            self.cur_deg_position_22 = readPosition(self.DXL_SERIES, self.DXL_ID[0])
            self.window.spinBoxServo22.setValue(self.cur_deg_position_22)
            self.button22Pressed = 1
        else:
            print("Servo 22 Unlocked")
            self.window.buttonServo22.setText("Lock")
            self.window.buttonLArm.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[0], TORQUE_DISABLE)
            self.buttonLArmPressed = 0
            self.button22Pressed = 0
    def servo22position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[0], self.window.spinBoxServo22.value())
    def servo23hardness(self):
        if self.button23Pressed == 0:
            print("Servo 23 Locked")
            self.window.buttonServo23.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[1], TORQUE_ENABLE)
            self.cur_deg_position_23 = readPosition(self.DXL_SERIES, self.DXL_ID[1])
            self.window.spinBoxServo23.setValue(self.cur_deg_position_23)
            self.button23Pressed = 1
        else:
            print("Servo 23 Unlocked")
            self.window.buttonServo23.setText("Lock")
            self.window.buttonLArm.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[1], TORQUE_DISABLE)
            self.buttonLArmPressed = 0
            self.button23Pressed = 0
    def servo23position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[1], self.window.spinBoxServo23.value())
    def servo24hardness(self):
        if self.button24Pressed == 0:
            print("Servo 24 Locked")
            self.window.buttonServo24.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[2], TORQUE_ENABLE)
            self.cur_deg_position_24 = readPosition(self.DXL_SERIES, self.DXL_ID[2])
            self.window.spinBoxServo24.setValue(self.cur_deg_position_24)
            self.button24Pressed = 1
        else:
            print("Servo 24 Unlocked")
            self.window.buttonServo24.setText("Lock")
            self.window.buttonLArm.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[2], TORQUE_DISABLE)
            self.buttonLArmPressed = 0
            self.button24Pressed = 0
    def servo24position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[2], self.window.spinBoxServo24.value())
    def servo25hardness(self):
        if self.button25Pressed == 0:
            print("Servo 25 Locked")
            self.window.buttonServo25.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[3], TORQUE_ENABLE)
            self.cur_deg_position_25 = readPosition(self.DXL_SERIES, self.DXL_ID[3])
            self.window.spinBoxServo25.setValue(self.cur_deg_position_25)
            self.button25Pressed = 1
        else:
            print("Servo 25 Unlocked")
            self.window.buttonServo25.setText("Lock")
            self.window.buttonLArm.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[3], TORQUE_DISABLE)
            self.buttonLArmPressed = 0
            self.button25Pressed = 0
    def servo25position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[3], self.window.spinBoxServo25.value())
    def servo26hardness(self):
        if self.button26Pressed == 0:
            print("Servo 26 Locked")
            self.window.buttonServo26.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[4], TORQUE_ENABLE)
            self.cur_deg_position_26 = readPosition(self.DXL_SERIES, self.DXL_ID[4])
            self.window.spinBoxServo26.setValue(self.cur_deg_position_26)
            self.button26Pressed = 1
        else:
            print("Servo 26 Unlocked")
            self.window.buttonServo26.setText("Lock")
            self.window.buttonLArm.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[4], TORQUE_DISABLE)
            self.buttonLArmPressed = 0
            self.button26Pressed = 0
    def servo26position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[4], self.window.spinBoxServo26.value())

class neckFunction:
    def __init__(self,window):
        self.window = window
        self.window.buttonServo27.clicked.connect(self.servo27hardness)
        self.window.spinBoxServo27.valueChanged.connect(self.servo27position)
        self.window.buttonServo28.clicked.connect(self.servo28hardness)
        self.window.spinBoxServo28.valueChanged.connect(self.servo28position)
        self.window.buttonServo29.clicked.connect(self.servo29hardness)
        self.window.spinBoxServo29.valueChanged.connect(self.servo29position)
        self.window.buttonNeck.clicked.connect(self.neckHardness)
        self.buttonNeckPressed = 0
        self.button27Pressed = 0
        self.button28Pressed = 0
        self.button29Pressed = 0
        self.DXL_SERIES = "XL320"
        self.DXL_ID = [27, 28, 29]
    def neckHardness(self):
        if self.buttonNeckPressed == 0:
            print("Neck Locked")
            self.window.buttonNeck.setText("Unlock All")
            self.buttonNeckPressed = 1
            self.button27Pressed = 0
            self.button28Pressed = 0
            self.button29Pressed = 0
        else:
            print("Neck Unlocked")
            self.window.buttonNeck.setText("Lock All")
            self.buttonNeckPressed = 0
            self.button27Pressed = 1
            self.button28Pressed = 1
            self.button29Pressed = 1
        self.servo27hardness()
        self.servo28hardness()
        self.servo29hardness()
    def servo27hardness(self):
        if self.button27Pressed == 0:
            print("Servo 27 Locked")
            self.window.buttonServo27.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[0], TORQUE_ENABLE)
            self.cur_deg_position_27 = readPosition(self.DXL_SERIES, self.DXL_ID[0])
            self.window.spinBoxServo27.setValue(self.cur_deg_position_27)
            self.button27Pressed = 1
        else:
            print("Servo 27 Unlocked")
            self.window.buttonServo27.setText("Lock")
            self.window.buttonNeck.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[0], TORQUE_DISABLE)
            self.button27Pressed = 0
            self.buttonNeckPressed = 0
    def servo27position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[0], self.window.spinBoxServo27.value())
    def servo28hardness(self):
        if self.button28Pressed == 0:
            print("Servo 28 Locked")
            self.window.buttonServo28.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[1], TORQUE_ENABLE)
            self.cur_deg_position_28 = readPosition(self.DXL_SERIES, self.DXL_ID[1])
            self.window.spinBoxServo28.setValue(self.cur_deg_position_28)
            self.button28Pressed = 1
        else:
            print("Servo 28 Unlocked")
            self.window.buttonServo28.setText("Lock")
            self.window.buttonNeck.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[1], TORQUE_DISABLE)
            self.button28Pressed = 0
            self.buttonNeckPressed = 0
    def servo28position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[1], self.window.spinBoxServo28.value())
    def servo29hardness(self):
        if self.button29Pressed == 0:
            print("Servo 29 Locked")
            self.window.buttonServo29.setText("Unlock")
            writeHardness(self.DXL_SERIES, self.DXL_ID[2], TORQUE_ENABLE)
            self.cur_deg_position_29 = readPosition(self.DXL_SERIES, self.DXL_ID[2])
            self.window.spinBoxServo29.setValue(self.cur_deg_position_29)
            self.button29Pressed = 1
        else:
            print("Servo 29 Unlocked")
            self.window.buttonServo29.setText("Lock")
            self.window.buttonNeck.setText("Lock All")
            writeHardness(self.DXL_SERIES, self.DXL_ID[2], TORQUE_DISABLE)
            self.button29Pressed = 0
            self.buttonNeckPressed = 0
    def servo29position(self):
        writePosition(self.DXL_SERIES, self.DXL_ID[2], self.window.spinBoxServo29.value())


class recordFunction:
    def __init__(self, window):
        self.window = window
        self.window.buttonCapture.clicked.connect(self.capturePosition)
        self.window.spinBoxMotNum.valueChanged.connect(self.currentMotionNumber)
        self.dataMotion = []
        with open("motion_GUI.lua",'r') as file:
            self.dataMotion = file.read().split('--#')
        self.dataMotion.remove('')
        print(self.dataMotion)
    def capturePosition(self):
        self.motionNumber = "--#--motion %d--#\n"%self.window.spinBoxMotNum.value()
        self.outputRecord = " {\nangles=vector.new({\n %.1f,\n %.1f,\n %.1f,\n %.1f,\n %.1f, %.1f, %.1f, %.1f, %.1f,\n %.1f, %.1f, %.1f, %.1f, %.1f,\n %.1f, %.1f, %.1f,\n})*math.pi/180,duration = 5\n },\n\n" % (self.window.spinBoxServo13.value()*-1, self.window.spinBoxServo14.value()*-1, self.window.spinBoxServo15.value()*-1, self.window.spinBoxServo16.value()*-1, self.window.spinBoxServo17.value(), self.window.spinBoxServo18.value(), self.window.spinBoxServo19.value()*-1, self.window.spinBoxServo20.value()*-1, self.window.spinBoxServo21.value(), self.window.spinBoxServo22.value(), self.window.spinBoxServo23.value()*-1, self.window.spinBoxServo24.value(), self.window.spinBoxServo25.value()*-1, self.window.spinBoxServo26.value()*-1, self.window.spinBoxServo27.value()*-1, self.window.spinBoxServo28.value()*-1, self.window.spinBoxServo29.value())
        if "--motion %d"%self.window.spinBoxMotNum.value() in self.dataMotion or self.motionNumber in self.dataMotion:
            self.dataMotion.pop(self.window.spinBoxMotNum.value()*2)
            self.dataMotion.pop(self.window.spinBoxMotNum.value()*2)
        self.dataMotion.insert(self.window.spinBoxMotNum.value()*2,self.motionNumber)
        self.dataMotion.insert(self.window.spinBoxMotNum.value()*2+1,self.outputRecord)
        with open('motion_GUI.lua','w') as file:
            file.writelines(self.dataMotion)
    def currentMotionNumber(self):
        pass
    
class WindowRecMot(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.window = loader.load("RecordMotion.ui", None)
        self.groupbox_record=recordFunction(self.window)
        self.groupbox_neck=neckFunction(self.window)
        self.groupbox_chest=chestFunction(self.window)
        self.groupbox_hip=hipFunction(self.window)
        self.groupbox_rightArm=rightArmFunction(self.window)
        self.groupbox_leftArm=leftArmFunction(self.window)
        self.window.show()

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    main_window = WindowRecMot()
try:
    sys.exit(app.exec())
except SystemExit:
    id=14 #for id in range(1, 30):
    data_torque = 0
    # if id == 13:
    #     dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, id, MXSeries.ADDR_TORQUE_ENABLE, data_torque)
    # elif id <= 16:
    #     dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, id, XSeries.ADDR_TORQUE_ENABLE, data_torque)
    # else:
    #     dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, id, XL320.ADDR_TORQUE_ENABLE, data_torque)
    # if dxl_comm_result != COMM_SUCCESS:
    #     print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    # elif dxl_error != 0:
    #     print("%s" % packetHandler.getRxPacketError(dxl_error))
    # portHandler.closePort()
