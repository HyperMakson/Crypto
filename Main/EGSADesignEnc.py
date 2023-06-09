from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 265)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.labelEGSA = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelEGSA.setFont(font)
        self.labelEGSA.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelEGSA.setMinimumSize(QtCore.QSize(250, 100))
        self.labelEGSA.setObjectName("labelEGSA")
        self.gridLayout.addWidget(self.labelEGSA, 0, 2, 1, 5)
        self.labelP1 = QtWidgets.QLabel(parent=Form)
        self.labelP1.setMaximumSize(QtCore.QSize(150, 50))
        self.labelP1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelP1.setObjectName("labelP1")
        self.gridLayout.addWidget(self.labelP1, 1, 3, 1, 1)
        self.labelP2 = QtWidgets.QLabel(parent=Form)
        self.labelP2.setMaximumSize(QtCore.QSize(50, 50))
        self.labelP2.setObjectName("labelP2")
        self.gridLayout.addWidget(self.labelP2, 1, 4, 1, 1)
        self.labelG1 = QtWidgets.QLabel(parent=Form)
        self.labelG1.setMaximumSize(QtCore.QSize(150, 50))
        self.labelG1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelG1.setObjectName("labelG1")
        self.gridLayout.addWidget(self.labelG1, 1, 5, 1, 1)
        self.labelG2 = QtWidgets.QLabel(parent=Form)
        self.labelG2.setMaximumSize(QtCore.QSize(50, 50))
        self.labelG2.setObjectName("labelG2")
        self.gridLayout.addWidget(self.labelG2, 1, 6, 1, 1)
        self.labelX1 = QtWidgets.QLabel(parent=Form)
        self.labelX1.setMaximumSize(QtCore.QSize(150, 50))
        self.labelX1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelX1.setObjectName("labelX1")
        self.gridLayout.addWidget(self.labelX1, 2, 3, 1, 1)
        self.labelX2 = QtWidgets.QLabel(parent=Form)
        self.labelX2.setMaximumSize(QtCore.QSize(50, 50))
        self.labelX2.setObjectName("labelX2")
        self.gridLayout.addWidget(self.labelX2, 2, 4, 1, 1)
        self.labelY1 = QtWidgets.QLabel(parent=Form)
        self.labelY1.setMaximumSize(QtCore.QSize(150, 50))
        self.labelY1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelY1.setObjectName("labelY1")
        self.gridLayout.addWidget(self.labelY1, 2, 5, 1, 1)
        self.labelY2 = QtWidgets.QLabel(parent=Form)
        self.labelY2.setMaximumSize(QtCore.QSize(150, 50))
        self.labelY2.setObjectName("labelY2")
        self.gridLayout.addWidget(self.labelY2, 2, 6, 1, 1)
        self.labelAnotherY1 = QtWidgets.QLabel(parent=Form)
        self.labelAnotherY1.setMaximumSize(QtCore.QSize(150, 50))
        self.labelAnotherY1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelAnotherY1.setObjectName("labelAnotherY1")
        self.gridLayout.addWidget(self.labelAnotherY1, 3, 5, 1, 1)
        self.labelAnotherY2 = QtWidgets.QLabel(parent=Form)
        self.labelAnotherY2.setMaximumSize(QtCore.QSize(150, 50))
        self.labelAnotherY2.setObjectName("labelAnotherY2")
        self.gridLayout.addWidget(self.labelAnotherY2, 3, 6, 1, 1)
        self.btnStart = QtWidgets.QPushButton(parent=Form)
        self.btnStart.setMaximumSize(QtCore.QSize(150, 30))
        self.btnStart.setObjectName("btnStart")
        self.gridLayout.addWidget(self.btnStart, 1, 2, 1, 1)
        self.btnSave = QtWidgets.QPushButton(parent=Form)
        self.btnSave.setMaximumSize(QtCore.QSize(150, 30))
        self.btnSave.setObjectName("btnSave")
        self.gridLayout.addWidget(self.btnSave, 2, 2, 1, 1)
        self.btnSelY = QtWidgets.QPushButton(parent=Form)
        self.btnSelY.setMaximumSize(QtCore.QSize(150, 30))
        self.btnSelY.setObjectName("btnSelY")
        self.gridLayout.addWidget(self.btnSelY, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.btnSel = QtWidgets.QPushButton(parent=Form)
        self.btnSel.setMaximumSize(QtCore.QSize(150, 30))
        self.btnSel.setObjectName("btnSel")
        self.gridLayout.addWidget(self.btnSel, 5, 2, 1, 1)
        self.labelHash1 = QtWidgets.QLabel(parent=Form)
        self.labelHash1.setMaximumSize(QtCore.QSize(150, 50))
        self.labelHash1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelHash1.setObjectName("labelHash1")
        self.gridLayout.addWidget(self.labelHash1, 5, 3, 1, 1)
        self.labelHash2 = QtWidgets.QLabel(parent=Form)
        self.labelHash2.setMaximumSize(QtCore.QSize(150, 50))
        self.labelHash2.setObjectName("labelHash2")
        self.gridLayout.addWidget(self.labelHash2, 5, 4, 1, 1)
        self.labelK1 = QtWidgets.QLabel(parent=Form)
        self.labelK1.setMaximumSize(QtCore.QSize(150, 50))
        self.labelK1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelK1.setObjectName("labelK1")
        self.gridLayout.addWidget(self.labelK1, 5, 5, 1, 1)
        self.labelK2 = QtWidgets.QLabel(parent=Form)
        self.labelK2.setMaximumSize(QtCore.QSize(150, 50))
        self.labelK2.setObjectName("labelK2")
        self.gridLayout.addWidget(self.labelK2, 5, 6, 1, 1)
        self.labelR1 = QtWidgets.QLabel(parent=Form)
        self.labelR1.setMaximumSize(QtCore.QSize(150, 50))
        self.labelR1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelR1.setObjectName("labelR1")
        self.gridLayout.addWidget(self.labelR1, 6, 5, 1, 1)
        self.labelR2 = QtWidgets.QLabel(parent=Form)
        self.labelR2.setMaximumSize(QtCore.QSize(150, 50))
        self.labelR2.setObjectName("labelR2")
        self.gridLayout.addWidget(self.labelR2, 6, 6, 1, 1)
        self.btnEnc = QtWidgets.QPushButton(parent=Form)
        self.btnEnc.setMaximumSize(QtCore.QSize(150, 30))
        self.btnEnc.setObjectName("btnEnc")
        self.gridLayout.addWidget(self.btnEnc, 7, 3, 1, 1)
        self.btnSaveEDS = QtWidgets.QPushButton(parent=Form)
        self.btnSaveEDS.setMaximumSize(QtCore.QSize(150, 30))
        self.btnSaveEDS.setObjectName("btnSaveEDS")
        self.gridLayout.addWidget(self.btnSaveEDS, 8, 3, 1, 1)
        self.labelEDS1 = QtWidgets.QLabel(parent=Form)
        self.labelEDS1.setMaximumSize(QtCore.QSize(150, 50))
        self.labelEDS1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelEDS1.setObjectName("labelEDS1")
        self.gridLayout.addWidget(self.labelEDS1, 8, 4, 1, 1)
        self.labelEDS2 = QtWidgets.QLabel(parent=Form)
        self.labelEDS2.setMaximumSize(QtCore.QSize(150, 50))
        self.labelEDS2.setObjectName("labelEDS2")
        self.gridLayout.addWidget(self.labelEDS2, 8, 5, 1, 1)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 9, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 9, 1, 1)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Encryption"))
        self.labelEGSA.setText(_translate("Form", "Шифрование по алгоритму EGSA"))
        self.labelP1.setText(_translate("Form", "Число p:"))
        self.labelP2.setText(_translate("Form", "num"))
        self.labelG1.setText(_translate("Form", "Число g:"))
        self.labelG2.setText(_translate("Form", "num"))
        self.labelX1.setText(_translate("Form", "Число x:"))
        self.labelX2.setText(_translate("Form", "num"))
        self.labelY1.setText(_translate("Form", "Число y:"))
        self.labelY2.setText(_translate("Form", "num"))
        self.labelAnotherY1.setText(_translate("Form", "Другой y:"))
        self.labelAnotherY2.setText(_translate("Form", "num"))
        self.btnStart.setText(_translate("Form", "Получить числа"))
        self.btnSave.setText(_translate("Form", "Сохранить числа"))
        self.btnSelY.setText(_translate("Form", "Выбрать y"))
        self.btnSel.setText(_translate("Form", "Выбрать файл"))
        self.labelHash1.setText(_translate("Form", "Hash:"))
        self.labelHash2.setText(_translate("Form", "num"))
        self.labelK1.setText(_translate("Form", "Число k:"))
        self.labelK2.setText(_translate("Form", "num"))
        self.labelR1.setText(_translate("Form", "Число r:"))
        self.labelR2.setText(_translate("Form", "num"))
        self.btnEnc.setText(_translate("Form", "Зашифровать"))
        self.btnSaveEDS.setText(_translate("Form", "Сохранить ЭЦП"))
        self.labelEDS1.setText(_translate("Form", "ЭЦП:"))
        self.labelEDS2.setText(_translate("Form", "num"))
