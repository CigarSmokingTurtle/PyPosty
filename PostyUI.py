# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyPosty.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../PycharmProjects/PyPosty/src/hammer-and-sickle-md.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.postButton = QtWidgets.QPushButton(self.centralwidget)
        self.postButton.setGeometry(QtCore.QRect(10, 630, 75, 23))
        self.postButton.setObjectName("postButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 100, 1081, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 47, 21))
        self.label_3.setObjectName("label_3")
        self.installTabUsertimeCheck = QtWidgets.QCheckBox(self.tab)
        self.installTabUsertimeCheck.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.installTabUsertimeCheck.setObjectName("installTabUsertimeCheck")
        self.installTabUsertimeValue = QtWidgets.QLineEdit(self.tab)
        self.installTabUsertimeValue.setGeometry(QtCore.QRect(110, 30, 391, 20))
        self.installTabUsertimeValue.setObjectName("installTabUsertimeValue")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 81, 20))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.installTabUserAgentValue = QtWidgets.QLineEdit(self.tab)
        self.installTabUserAgentValue.setGeometry(QtCore.QRect(110, 60, 391, 20))
        self.installTabUserAgentValue.setObjectName("installTabUserAgentValue")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 81, 20))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.installTabIPValue = QtWidgets.QLineEdit(self.tab)
        self.installTabIPValue.setGeometry(QtCore.QRect(110, 90, 391, 20))
        self.installTabIPValue.setObjectName("installTabIPValue")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 81, 20))
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        self.installTabIDValue1 = QtWidgets.QLineEdit(self.tab)
        self.installTabIDValue1.setGeometry(QtCore.QRect(110, 140, 391, 21))
        self.installTabIDValue1.setObjectName("installTabIDValue1")
        self.installTabPayloadPreview = QtWidgets.QPlainTextEdit(self.tab)
        self.installTabPayloadPreview.setEnabled(False)
        self.installTabPayloadPreview.setGeometry(QtCore.QRect(620, 30, 451, 311))
        self.installTabPayloadPreview.setReadOnly(True)
        self.installTabPayloadPreview.setObjectName("installTabPayloadPreview")
        self.installTabEditCheck = QtWidgets.QCheckBox(self.tab)
        self.installTabEditCheck.setGeometry(QtCore.QRect(540, 30, 70, 21))
        self.installTabEditCheck.setObjectName("installTabEditCheck")
        self.installTabIDSelect1 = QtWidgets.QComboBox(self.tab)
        self.installTabIDSelect1.setGeometry(QtCore.QRect(30, 140, 69, 22))
        self.installTabIDSelect1.setObjectName("installTabIDSelect1")
        self.installTabIDSelect1.addItem("")
        self.installTabIDSelect1.addItem("")
        self.installTabIDSelect1.addItem("")
        self.installTabIDSelect1.addItem("")
        self.installTabIDSelect1.addItem("")
        self.installTabIDSelect1.addItem("")
        self.installTabIDSelect1.addItem("")
        self.installTabIDSelect2 = QtWidgets.QComboBox(self.tab)
        self.installTabIDSelect2.setEnabled(False)
        self.installTabIDSelect2.setGeometry(QtCore.QRect(30, 170, 69, 22))
        self.installTabIDSelect2.setObjectName("installTabIDSelect2")
        self.installTabIDSelect2.addItem("")
        self.installTabIDSelect2.addItem("")
        self.installTabIDSelect2.addItem("")
        self.installTabIDSelect2.addItem("")
        self.installTabIDSelect2.addItem("")
        self.installTabIDSelect2.addItem("")
        self.installTabIDSelect2.addItem("")
        self.installTabIDSelect3 = QtWidgets.QComboBox(self.tab)
        self.installTabIDSelect3.setEnabled(False)
        self.installTabIDSelect3.setGeometry(QtCore.QRect(30, 200, 69, 22))
        self.installTabIDSelect3.setObjectName("installTabIDSelect3")
        self.installTabIDSelect3.addItem("")
        self.installTabIDSelect3.addItem("")
        self.installTabIDSelect3.addItem("")
        self.installTabIDSelect3.addItem("")
        self.installTabIDSelect3.addItem("")
        self.installTabIDSelect3.addItem("")
        self.installTabIDSelect3.addItem("")
        self.installTabIDSelect4 = QtWidgets.QComboBox(self.tab)
        self.installTabIDSelect4.setEnabled(False)
        self.installTabIDSelect4.setGeometry(QtCore.QRect(30, 230, 69, 22))
        self.installTabIDSelect4.setObjectName("installTabIDSelect4")
        self.installTabIDSelect4.addItem("")
        self.installTabIDSelect4.addItem("")
        self.installTabIDSelect4.addItem("")
        self.installTabIDSelect4.addItem("")
        self.installTabIDSelect4.addItem("")
        self.installTabIDSelect4.addItem("")
        self.installTabIDSelect4.addItem("")
        self.installTabIDSelect5 = QtWidgets.QComboBox(self.tab)
        self.installTabIDSelect5.setEnabled(False)
        self.installTabIDSelect5.setGeometry(QtCore.QRect(30, 260, 69, 22))
        self.installTabIDSelect5.setObjectName("installTabIDSelect5")
        self.installTabIDSelect5.addItem("")
        self.installTabIDSelect5.addItem("")
        self.installTabIDSelect5.addItem("")
        self.installTabIDSelect5.addItem("")
        self.installTabIDSelect5.addItem("")
        self.installTabIDSelect5.addItem("")
        self.installTabIDSelect5.addItem("")
        self.installTabIDSelect6 = QtWidgets.QComboBox(self.tab)
        self.installTabIDSelect6.setEnabled(False)
        self.installTabIDSelect6.setGeometry(QtCore.QRect(30, 290, 69, 22))
        self.installTabIDSelect6.setObjectName("installTabIDSelect6")
        self.installTabIDSelect6.addItem("")
        self.installTabIDSelect6.addItem("")
        self.installTabIDSelect6.addItem("")
        self.installTabIDSelect6.addItem("")
        self.installTabIDSelect6.addItem("")
        self.installTabIDSelect6.addItem("")
        self.installTabIDSelect6.addItem("")
        self.installTabIDValue2 = QtWidgets.QLineEdit(self.tab)
        self.installTabIDValue2.setEnabled(False)
        self.installTabIDValue2.setGeometry(QtCore.QRect(110, 170, 391, 21))
        self.installTabIDValue2.setObjectName("installTabIDValue2")
        self.installTabIDValue3 = QtWidgets.QLineEdit(self.tab)
        self.installTabIDValue3.setEnabled(False)
        self.installTabIDValue3.setGeometry(QtCore.QRect(110, 200, 391, 21))
        self.installTabIDValue3.setObjectName("installTabIDValue3")
        self.installTabIDValue4 = QtWidgets.QLineEdit(self.tab)
        self.installTabIDValue4.setEnabled(False)
        self.installTabIDValue4.setGeometry(QtCore.QRect(110, 230, 391, 21))
        self.installTabIDValue4.setObjectName("installTabIDValue4")
        self.installTabIDValue5 = QtWidgets.QLineEdit(self.tab)
        self.installTabIDValue5.setEnabled(False)
        self.installTabIDValue5.setGeometry(QtCore.QRect(110, 260, 391, 21))
        self.installTabIDValue5.setObjectName("installTabIDValue5")
        self.installTabIDValue6 = QtWidgets.QLineEdit(self.tab)
        self.installTabIDValue6.setEnabled(False)
        self.installTabIDValue6.setGeometry(QtCore.QRect(110, 290, 391, 21))
        self.installTabIDValue6.setObjectName("installTabIDValue6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 47, 21))
        self.label_7.setObjectName("label_7")
        self.eventTabUsertimeCheck = QtWidgets.QCheckBox(self.tab_2)
        self.eventTabUsertimeCheck.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.eventTabUsertimeCheck.setObjectName("eventTabUsertimeCheck")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(110, 30, 391, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 81, 20))
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setObjectName("label_8")
        self.eventTabUserAgentValue = QtWidgets.QLineEdit(self.tab_2)
        self.eventTabUserAgentValue.setGeometry(QtCore.QRect(110, 60, 391, 20))
        self.eventTabUserAgentValue.setObjectName("eventTabUserAgentValue")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 90, 71, 20))
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.eventTabIPValue = QtWidgets.QLineEdit(self.tab_2)
        self.eventTabIPValue.setGeometry(QtCore.QRect(110, 90, 391, 20))
        self.eventTabIPValue.setObjectName("eventTabIPValue")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 81, 20))
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setObjectName("label_10")
        self.eventTabIDSelect1 = QtWidgets.QComboBox(self.tab_2)
        self.eventTabIDSelect1.setGeometry(QtCore.QRect(30, 140, 69, 22))
        self.eventTabIDSelect1.setObjectName("eventTabIDSelect1")
        self.eventTabIDSelect1.addItem("")
        self.eventTabIDSelect1.addItem("")
        self.eventTabIDSelect1.addItem("")
        self.eventTabIDSelect1.addItem("")
        self.eventTabIDSelect1.addItem("")
        self.eventTabIDSelect1.addItem("")
        self.eventTabIDSelect1.addItem("")
        self.eventTabIDValue1 = QtWidgets.QLineEdit(self.tab_2)
        self.eventTabIDValue1.setGeometry(QtCore.QRect(110, 140, 391, 21))
        self.eventTabIDValue1.setObjectName("eventTabIDValue1")
        self.eventTabIDSelect2 = QtWidgets.QComboBox(self.tab_2)
        self.eventTabIDSelect2.setEnabled(False)
        self.eventTabIDSelect2.setGeometry(QtCore.QRect(30, 170, 69, 22))
        self.eventTabIDSelect2.setObjectName("eventTabIDSelect2")
        self.eventTabIDSelect2.addItem("")
        self.eventTabIDSelect2.addItem("")
        self.eventTabIDSelect2.addItem("")
        self.eventTabIDSelect2.addItem("")
        self.eventTabIDSelect2.addItem("")
        self.eventTabIDSelect2.addItem("")
        self.eventTabIDSelect2.addItem("")
        self.eventTabIDValue2 = QtWidgets.QLineEdit(self.tab_2)
        self.eventTabIDValue2.setEnabled(False)
        self.eventTabIDValue2.setGeometry(QtCore.QRect(110, 170, 391, 21))
        self.eventTabIDValue2.setObjectName("eventTabIDValue2")
        self.eventTabPayloadPreview = QtWidgets.QPlainTextEdit(self.tab_2)
        self.eventTabPayloadPreview.setEnabled(False)
        self.eventTabPayloadPreview.setGeometry(QtCore.QRect(620, 30, 451, 311))
        self.eventTabPayloadPreview.setReadOnly(True)
        self.eventTabPayloadPreview.setObjectName("eventTabPayloadPreview")
        self.eventTabEditCheck = QtWidgets.QCheckBox(self.tab_2)
        self.eventTabEditCheck.setGeometry(QtCore.QRect(540, 30, 70, 21))
        self.eventTabEditCheck.setObjectName("eventTabEditCheck")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(20, 200, 81, 20))
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setObjectName("label_11")
        self.eventTabEventNameValue = QtWidgets.QLineEdit(self.tab_2)
        self.eventTabEventNameValue.setGeometry(QtCore.QRect(110, 200, 391, 20))
        self.eventTabEventNameValue.setObjectName("eventTabEventNameValue")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(20, 230, 81, 20))
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setObjectName("label_12")
        self.eventTabEventDataValue = QtWidgets.QTextEdit(self.tab_2)
        self.eventTabEventDataValue.setGeometry(QtCore.QRect(110, 230, 391, 111))
        self.eventTabEventDataValue.setObjectName("eventTabEventDataValue")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.customTabPayloadValue = QtWidgets.QTextEdit(self.tab_3)
        self.customTabPayloadValue.setGeometry(QtCore.QRect(3, 40, 1071, 311))
        self.customTabPayloadValue.setObjectName("customTabPayloadValue")
        self.customTabGETRadio = QtWidgets.QRadioButton(self.tab_3)
        self.customTabGETRadio.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.customTabGETRadio.setObjectName("customTabGETRadio")
        self.customTabPOSTRadio = QtWidgets.QRadioButton(self.tab_3)
        self.customTabPOSTRadio.setGeometry(QtCore.QRect(70, 10, 61, 21))
        self.customTabPOSTRadio.setChecked(True)
        self.customTabPOSTRadio.setObjectName("customTabPOSTRadio")
        self.customTabPayloadTypeValue = QtWidgets.QComboBox(self.tab_3)
        self.customTabPayloadTypeValue.setGeometry(QtCore.QRect(130, 10, 211, 21))
        self.customTabPayloadTypeValue.setObjectName("customTabPayloadTypeValue")
        self.customTabPayloadTypeValue.addItem("")
        self.customTabPayloadTypeValue.addItem("")
        self.customTabPayloadTypeValue.addItem("")
        self.tabWidget.addTab(self.tab_3, "")
        self.serverResponseCodeAll = QtWidgets.QTextEdit(self.centralwidget)
        self.serverResponseCodeAll.setGeometry(QtCore.QRect(13, 490, 1071, 131))
        self.serverResponseCodeAll.setReadOnly(True)
        self.serverResponseCodeAll.setObjectName("serverResponseCodeAll")
        self.postQtyValue = QtWidgets.QSpinBox(self.centralwidget)
        self.postQtyValue.setGeometry(QtCore.QRect(100, 632, 37, 20))
        self.postQtyValue.setMinimum(1)
        self.postQtyValue.setObjectName("postQtyValue")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(160, 630, 511, 21))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 50)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.serverResponseCodeLine = QtWidgets.QLineEdit(self.centralwidget)
        self.serverResponseCodeLine.setGeometry(QtCore.QRect(680, 630, 401, 20))
        self.serverResponseCodeLine.setReadOnly(True)
        self.serverResponseCodeLine.setObjectName("serverResponseCodeLine")
        self.endpointSelector = QtWidgets.QComboBox(self.centralwidget)
        self.endpointSelector.setGeometry(QtCore.QRect(80, 70, 91, 21))
        self.endpointSelector.setObjectName("endpointSelector")
        self.endpointSelector.addItem("")
        self.endpointSelector.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 72, 61, 16))
        self.label.setObjectName("label")
        self.endpointValue = QtWidgets.QLineEdit(self.centralwidget)
        self.endpointValue.setGeometry(QtCore.QRect(170, 70, 401, 21))
        self.endpointValue.setObjectName("endpointValue")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 70, 61, 21))
        self.label_2.setObjectName("label_2")
        self.appGUIDValue = QtWidgets.QLineEdit(self.centralwidget)
        self.appGUIDValue.setGeometry(QtCore.QRect(650, 70, 441, 20))
        self.appGUIDValue.setObjectName("appGUIDValue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuSave = QtWidgets.QMenu(self.menuMenu)
        self.menuSave.setObjectName("menuSave")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionGlobals = QtWidgets.QAction(MainWindow)
        self.actionGlobals.setObjectName("actionGlobals")
        self.actionDefaults = QtWidgets.QAction(MainWindow)
        self.actionDefaults.setObjectName("actionDefaults")
        self.actionSave_All = QtWidgets.QAction(MainWindow)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionSave_As_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_As_2.setObjectName("actionSave_As_2")
        self.actionTutorial = QtWidgets.QAction(MainWindow)
        self.actionTutorial.setObjectName("actionTutorial")
        self.actionDebug = QtWidgets.QAction(MainWindow)
        self.actionDebug.setCheckable(True)
        self.actionDebug.setObjectName("actionDebug")
        self.menuSave.addAction(self.actionSave_All)
        self.menuSave.addAction(self.actionSave_As_2)
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.menuSave.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionGlobals)
        self.menuSettings.addAction(self.actionDefaults)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionDebug)
        self.menuHelp.addAction(self.actionTutorial)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyPosty! v.01"))
        self.postButton.setText(_translate("MainWindow", "Post!"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Data:"))
        self.installTabUsertimeCheck.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">ONLY ENABLE </span>when you want an exact time. Default will use current time.</p></body></html>"))
        self.installTabUsertimeCheck.setText(_translate("MainWindow", "Usertime"))
        self.label_4.setText(_translate("MainWindow", "Device UA:"))
        self.label_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>Origination IP Address</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "IP Address:"))
        self.label_6.setText(_translate("MainWindow", "Device IDs:"))
        self.installTabPayloadPreview.setToolTip(_translate("MainWindow", "<html><head/><body><p>JSON Payload Preview <span style=\" font-weight:600;\">DO NOT EDIT </span>unless you know what you\'re doing</p></body></html>"))
        self.installTabEditCheck.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">DO NOT CHECK</span> unless you\'re familiar with JSON payloads</p></body></html>"))
        self.installTabEditCheck.setText(_translate("MainWindow", "Edit"))
        self.installTabIDSelect1.setItemText(0, _translate("MainWindow", "<none>"))
        self.installTabIDSelect1.setItemText(1, _translate("MainWindow", "IDFA"))
        self.installTabIDSelect1.setItemText(2, _translate("MainWindow", "ADID"))
        self.installTabIDSelect1.setItemText(3, _translate("MainWindow", "Android"))
        self.installTabIDSelect1.setItemText(4, _translate("MainWindow", "MAC"))
        self.installTabIDSelect1.setItemText(5, _translate("MainWindow", "IMEI"))
        self.installTabIDSelect1.setItemText(6, _translate("MainWindow", "ODIN"))
        self.installTabIDSelect2.setItemText(0, _translate("MainWindow", "<none>"))
        self.installTabIDSelect2.setItemText(1, _translate("MainWindow", "IDFA"))
        self.installTabIDSelect2.setItemText(2, _translate("MainWindow", "ADID"))
        self.installTabIDSelect2.setItemText(3, _translate("MainWindow", "Android"))
        self.installTabIDSelect2.setItemText(4, _translate("MainWindow", "MAC"))
        self.installTabIDSelect2.setItemText(5, _translate("MainWindow", "IMEI"))
        self.installTabIDSelect2.setItemText(6, _translate("MainWindow", "ODIN"))
        self.installTabIDSelect3.setItemText(0, _translate("MainWindow", "<none>"))
        self.installTabIDSelect3.setItemText(1, _translate("MainWindow", "IDFA"))
        self.installTabIDSelect3.setItemText(2, _translate("MainWindow", "ADID"))
        self.installTabIDSelect3.setItemText(3, _translate("MainWindow", "Android"))
        self.installTabIDSelect3.setItemText(4, _translate("MainWindow", "MAC"))
        self.installTabIDSelect3.setItemText(5, _translate("MainWindow", "IMEI"))
        self.installTabIDSelect3.setItemText(6, _translate("MainWindow", "ODIN"))
        self.installTabIDSelect4.setItemText(0, _translate("MainWindow", "<none>"))
        self.installTabIDSelect4.setItemText(1, _translate("MainWindow", "IDFA"))
        self.installTabIDSelect4.setItemText(2, _translate("MainWindow", "ADID"))
        self.installTabIDSelect4.setItemText(3, _translate("MainWindow", "Android"))
        self.installTabIDSelect4.setItemText(4, _translate("MainWindow", "MAC"))
        self.installTabIDSelect4.setItemText(5, _translate("MainWindow", "IMEI"))
        self.installTabIDSelect4.setItemText(6, _translate("MainWindow", "ODIN"))
        self.installTabIDSelect5.setItemText(0, _translate("MainWindow", "<none>"))
        self.installTabIDSelect5.setItemText(1, _translate("MainWindow", "IDFA"))
        self.installTabIDSelect5.setItemText(2, _translate("MainWindow", "ADID"))
        self.installTabIDSelect5.setItemText(3, _translate("MainWindow", "Android"))
        self.installTabIDSelect5.setItemText(4, _translate("MainWindow", "MAC"))
        self.installTabIDSelect5.setItemText(5, _translate("MainWindow", "IMEI"))
        self.installTabIDSelect5.setItemText(6, _translate("MainWindow", "ODIN"))
        self.installTabIDSelect6.setItemText(0, _translate("MainWindow", "<none>"))
        self.installTabIDSelect6.setItemText(1, _translate("MainWindow", "IDFA"))
        self.installTabIDSelect6.setItemText(2, _translate("MainWindow", "ADID"))
        self.installTabIDSelect6.setItemText(3, _translate("MainWindow", "Android"))
        self.installTabIDSelect6.setItemText(4, _translate("MainWindow", "MAC"))
        self.installTabIDSelect6.setItemText(5, _translate("MainWindow", "IMEI"))
        self.installTabIDSelect6.setItemText(6, _translate("MainWindow", "ODIN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Install"))
        self.label_7.setText(_translate("MainWindow", "Data:"))
        self.eventTabUsertimeCheck.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">ONLY ENABLE </span>when you want an exact time. Default will use current time.</p></body></html>"))
        self.eventTabUsertimeCheck.setText(_translate("MainWindow", "Usertime"))
        self.label_8.setText(_translate("MainWindow", "Device UA:"))
        self.label_9.setToolTip(_translate("MainWindow", "<html><head/><body><p>Origination IP Address</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "IP Address:"))
        self.label_10.setText(_translate("MainWindow", "Device IDs:"))
        self.eventTabIDSelect1.setItemText(0, _translate("MainWindow", "<none>"))
        self.eventTabIDSelect1.setItemText(1, _translate("MainWindow", "IDFA"))
        self.eventTabIDSelect1.setItemText(2, _translate("MainWindow", "ADID"))
        self.eventTabIDSelect1.setItemText(3, _translate("MainWindow", "Android"))
        self.eventTabIDSelect1.setItemText(4, _translate("MainWindow", "MAC"))
        self.eventTabIDSelect1.setItemText(5, _translate("MainWindow", "IMEI"))
        self.eventTabIDSelect1.setItemText(6, _translate("MainWindow", "ODIN"))
        self.eventTabIDSelect2.setItemText(0, _translate("MainWindow", "<none>"))
        self.eventTabIDSelect2.setItemText(1, _translate("MainWindow", "IDFA"))
        self.eventTabIDSelect2.setItemText(2, _translate("MainWindow", "ADID"))
        self.eventTabIDSelect2.setItemText(3, _translate("MainWindow", "Android"))
        self.eventTabIDSelect2.setItemText(4, _translate("MainWindow", "MAC"))
        self.eventTabIDSelect2.setItemText(5, _translate("MainWindow", "IMEI"))
        self.eventTabIDSelect2.setItemText(6, _translate("MainWindow", "ODIN"))
        self.eventTabPayloadPreview.setToolTip(_translate("MainWindow", "<html><head/><body><p>JSON Payload Preview <span style=\" font-weight:600;\">DO NOT EDIT </span>unless you know what you\'re doing</p></body></html>"))
        self.eventTabEditCheck.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">DO NOT CHECK</span> unless you\'re familiar with JSON payloads</p></body></html>"))
        self.eventTabEditCheck.setText(_translate("MainWindow", "Edit"))
        self.label_11.setText(_translate("MainWindow", "Event Name:"))
        self.label_12.setText(_translate("MainWindow", "Event Data:"))
        self.eventTabEventDataValue.setPlaceholderText(_translate("MainWindow", "{     \"id\" : \"123\"     \"name\" : \"test_item\"     \"currency\" : \"USD\"     \"sum\" : \"200\" }"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Event"))
        self.customTabGETRadio.setText(_translate("MainWindow", "GET"))
        self.customTabPOSTRadio.setText(_translate("MainWindow", "POST"))
        self.customTabPayloadTypeValue.setItemText(0, _translate("MainWindow", "JSON"))
        self.customTabPayloadTypeValue.setItemText(1, _translate("MainWindow", "HTML"))
        self.customTabPayloadTypeValue.setItemText(2, _translate("MainWindow", "XML"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Custom"))
        self.serverResponseCodeAll.setToolTip(_translate("MainWindow", "<html><head/><body><p>Server response code window</p></body></html>"))
        self.serverResponseCodeLine.setToolTip(_translate("MainWindow", "<html><head/><body><p>Individual payload server response window</p></body></html>"))
        self.endpointSelector.setItemText(0, _translate("MainWindow", "Kochava"))
        self.endpointSelector.setItemText(1, _translate("MainWindow", "Custom"))
        self.label.setText(_translate("MainWindow", "Endpoint:"))
        self.endpointValue.setPlaceholderText(_translate("MainWindow", "http://control.kochava.com/track/json"))
        self.label_2.setText(_translate("MainWindow", "App GUID:"))
        self.appGUIDValue.setPlaceholderText(_translate("MainWindow", "koconversionsdemo174ea19bc63928c"))
        self.menuMenu.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionGlobals.setText(_translate("MainWindow", "Globals"))
        self.actionDefaults.setText(_translate("MainWindow", "Defaults"))
        self.actionSave_All.setText(_translate("MainWindow", "Save All"))
        self.actionSave_As_2.setText(_translate("MainWindow", "Save As..."))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial"))
        self.actionDebug.setText(_translate("MainWindow", "Debug"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

