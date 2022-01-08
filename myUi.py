# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import os
import time
import json
import raw_data_handle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 30, 141, 471))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(30, 60, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 90, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 120, 91, 19))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 150, 91, 19))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 180, 91, 19))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 210, 91, 19))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 240, 91, 19))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_8.setGeometry(QtCore.QRect(30, 270, 91, 19))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_9.setGeometry(QtCore.QRect(30, 300, 91, 19))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_10.setGeometry(QtCore.QRect(30, 330, 91, 19))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_11.setGeometry(QtCore.QRect(30, 360, 91, 19))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_12.setGeometry(QtCore.QRect(30, 390, 91, 19))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_13.setGeometry(QtCore.QRect(30, 420, 91, 19))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_14.setGeometry(QtCore.QRect(10, 30, 91, 19))
        self.checkBox_14.setTristate(False)
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_14.stateChanged.connect(self.all_select)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 40, 241, 211))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_15 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_15.setGeometry(QtCore.QRect(30, 30, 91, 19))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_16.setGeometry(QtCore.QRect(30, 70, 91, 19))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_15.setChecked(True)
        self.checkBox_16.setChecked(True)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(500, 40, 251, 211))
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_17 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_17.setGeometry(QtCore.QRect(30, 40, 91, 19))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_18.setGeometry(QtCore.QRect(30, 80, 91, 19))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_17.setChecked(True)
        self.checkBox_18.setChecked(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 460, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(220, 280, 531, 161))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.groupBox.setTitle(_translate("MainWindow", "测量根"))
        self.checkBox.setText(_translate("MainWindow", "A"))
        self.checkBox_2.setText(_translate("MainWindow", "B"))
        self.checkBox_3.setText(_translate("MainWindow", "C"))
        self.checkBox_4.setText(_translate("MainWindow", "D"))
        self.checkBox_5.setText(_translate("MainWindow", "E"))
        self.checkBox_6.setText(_translate("MainWindow", "F"))
        self.checkBox_7.setText(_translate("MainWindow", "G"))
        self.checkBox_8.setText(_translate("MainWindow", "H"))
        self.checkBox_9.setText(_translate("MainWindow", "I"))
        self.checkBox_10.setText(_translate("MainWindow", "J"))
        self.checkBox_11.setText(_translate("MainWindow", "K"))
        self.checkBox_12.setText(_translate("MainWindow", "L"))
        self.checkBox_13.setText(_translate("MainWindow", "M"))
        self.checkBox_14.setText(_translate("MainWindow", "全选"))
        self.groupBox_2.setTitle(_translate("MainWindow", "IPv4"))
        self.checkBox_15.setText(_translate("MainWindow", "路由路径"))
        self.checkBox_16.setText(_translate("MainWindow", "参考时延"))
        self.groupBox_3.setTitle(_translate("MainWindow", "IPv6"))
        self.checkBox_17.setText(_translate("MainWindow", "路由路径"))
        self.checkBox_18.setText(_translate("MainWindow", "参考时延"))
        self.pushButton.setText(_translate("MainWindow", "开始监测"))

    def all_select(self):
        if self.checkBox_14.checkState() == Qt.Checked:
            self.checkBox.setChecked(True)
            self.checkBox_2.setChecked(True)
            self.checkBox_3.setChecked(True)
            self.checkBox_4.setChecked(True)
            self.checkBox_5.setChecked(True)
            self.checkBox_6.setChecked(True)
            self.checkBox_7.setChecked(True)
            self.checkBox_8.setChecked(True)
            self.checkBox_9.setChecked(True)
            self.checkBox_10.setChecked(True)
            self.checkBox_11.setChecked(True)
            self.checkBox_12.setChecked(True)
            self.checkBox_13.setChecked(True)


    def click(self):
        env = ""
        str = ""
        if self.checkBox.checkState() == Qt.Checked:
            env += " a.root-servers.net"
            str += "a"
        if self.checkBox_2.checkState() == Qt.Checked:
            env += " b.root-servers.net"
            str += "b"
        if self.checkBox_3.checkState() == Qt.Checked:
            env += " c.root-servers.net"
            str += "c"
        if self.checkBox_4.checkState() == Qt.Checked:
            env += " d.root-servers.net"
            str += "d"
        if self.checkBox_5.checkState() == Qt.Checked:
            env += " e.root-servers.net"
            str += "e"
        if self.checkBox_6.checkState() == Qt.Checked:
            env += " f.root-servers.net"
            str += "f"
        if self.checkBox_7.checkState() == Qt.Checked:
            env += " g.root-servers.net"
            str += "g"
        if self.checkBox_8.checkState() == Qt.Checked:
            env += " h.root-servers.net"
            str += "h"
        if self.checkBox_9.checkState() == Qt.Checked:
            env += " i.root-servers.net"
            str += "i"
        if self.checkBox_10.checkState() == Qt.Checked:
            env += " j.root-servers.net"
            str += "j"
        if self.checkBox_11.checkState() == Qt.Checked:
            env += " k.root-servers.net"
            str += "k"
        if self.checkBox_12.checkState() == Qt.Checked:
            env += " l.root-servers.net"
            str += "l"
        if self.checkBox_13.checkState() == Qt.Checked:
            env += " m.root-servers.net"
            str += "m"
        if str == "":
            return
        ipv4_command = "./detect_ipv4.sh"
        ipv6_command = "./detect_ipv6.sh"
        if self.groupBox_2.isChecked():
            if self.checkBox_15.checkState() == Qt.Checked:
                ipv4_command += " -t"
            else:
                ipv4_command += " -not"
            if self.checkBox_16.checkState() == Qt.Checked:
                ipv4_command += " -r"
            else:
                ipv4_command += " -nor"
        if self.groupBox_3.isChecked():
            if self.checkBox_17.checkState() == Qt.Checked:
                ipv6_command += " -t"
            else:
                ipv6_command += " -not"
            if self.checkBox_18.checkState() == Qt.Checked:
                ipv6_command += " -r"
            else:
                ipv6_command += " -nor"
        while True:
            print("start")
            self.plainTextEdit.setPlainText("detecting...")
            os.system("./detect.sh"+env)
            #print("./detect.sh"+env)
            if self.groupBox_2.isChecked():
                self.plainTextEdit.setPlainText("...")
                os.system(ipv4_command+env)
                #print(ipv4_command+env)
            if self.groupBox_3.isChecked():
                self.plainTextEdit.setPlainText("...")
                os.system(ipv6_command+env)
                #print(ipv6_command+env)

            self.plainTextEdit.setPlainText("decodeing...")
            raw_data_handle.data_init()
            ipv4 = self.groupBox_2.isChecked()
            ipv4_ist = (self.checkBox_15.checkState() == Qt.Checked)
            ipv4_isr = (self.checkBox_16.checkState() == Qt.Checked)
            ipv6 = self.groupBox_3.isChecked()
            ipv6_ist = (self.checkBox_17.checkState() == Qt.Checked)
            ipv6_isr = (self.checkBox_18.checkState() == Qt.Checked)
            _thread = []
            for root in str:
                self.plainTextEdit.setPlainText("handle "+root.upper()+"-root data")
                thread = raw_data_handle.myThread(root.upper(), "raw_data_"+root+".txt", ipv4, ipv4_ist, ipv4_isr , ipv6, ipv6_ist, ipv6_isr)
                _thread.append(thread)
            for t in _thread:
                t.start()
            for t in _thread:
                t.join()
            for t in _thread:
                if t._error:
                    raw_data_handle.error_record(t.ID)
                    exit(0)
            with open("log.json", "w") as write_f:
                write_f.write(json.dumps(raw_data_handle.data, ensure_ascii=False))
            raw_data_handle.save()
            self.plainTextEdit.setPlainText("sleep 30s")
            print("end")
            time.sleep(30)








