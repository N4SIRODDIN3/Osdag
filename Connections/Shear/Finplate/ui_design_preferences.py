# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_preferences.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(760, 523)
        self.gridLayout_5 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_2.addWidget(self.btn_save, 0, 2, 1, 1)
        self.btn_close = QtWidgets.QPushButton(Dialog)
        self.btn_close.setObjectName("btn_close")
        self.gridLayout_2.addWidget(self.btn_close, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.btn_defaults = QtWidgets.QPushButton(Dialog)
        self.btn_defaults.setObjectName("btn_defaults")
        self.gridLayout_2.addWidget(self.btn_defaults, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Bolt = QtWidgets.QWidget()
        self.tab_Bolt.setObjectName("tab_Bolt")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tab_Bolt)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_5 = QtWidgets.QLabel(self.tab_Bolt)
        self.label_5.setObjectName("label_5")
        self.gridLayout_19.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_3 = QtWidgets.QLabel(self.tab_Bolt)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.tab_Bolt)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_8.addWidget(self.line_4, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_Bolt)
        self.textBrowser.setMinimumSize(QtCore.QSize(210, 320))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_8.addWidget(self.textBrowser, 2, 0, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_8, 0, 2, 4, 1)
        self.line = QtWidgets.QFrame(self.tab_Bolt)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_19.addWidget(self.line, 1, 0, 1, 2)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab_Bolt)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_Bolt)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_Bolt)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab_Bolt)
        self.label_26.setObjectName("label_26")
        self.gridLayout_17.addWidget(self.label_26, 1, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_15 = QtWidgets.QLabel(self.tab_Bolt)
        self.label_15.setObjectName("label_15")
        self.gridLayout_11.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_Bolt)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_11.addWidget(self.label_7, 0, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.tab_Bolt)
        self.label_13.setObjectName("label_13")
        self.gridLayout_11.addWidget(self.label_13, 2, 0, 1, 2)
        self.gridLayout_17.addLayout(self.gridLayout_11, 2, 0, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_17, 0, 0, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.txt_boltHoleClearance = QtWidgets.QLineEdit(self.tab_Bolt)
        self.txt_boltHoleClearance.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_boltHoleClearance.setObjectName("txt_boltHoleClearance")
        self.gridLayout_9.addWidget(self.txt_boltHoleClearance, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_Bolt)
        self.label_9.setObjectName("label_9")
        self.gridLayout_9.addWidget(self.label_9, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_Bolt)
        self.label_8.setObjectName("label_8")
        self.gridLayout_9.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_Bolt)
        self.label_11.setObjectName("label_11")
        self.gridLayout_9.addWidget(self.label_11, 2, 2, 1, 1)
        self.txt_boltFu = QtWidgets.QLineEdit(self.tab_Bolt)
        self.txt_boltFu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_boltFu.setObjectName("txt_boltFu")
        self.gridLayout_9.addWidget(self.txt_boltFu, 2, 1, 1, 1)
        self.combo_boltHoleType = QtWidgets.QComboBox(self.tab_Bolt)
        self.combo_boltHoleType.setFocusPolicy(QtCore.Qt.TabFocus)
        self.combo_boltHoleType.setObjectName("combo_boltHoleType")
        self.combo_boltHoleType.addItem("")
        self.combo_boltHoleType.addItem("")
        self.gridLayout_9.addWidget(self.combo_boltHoleType, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.txt_frictional_resistance = QtWidgets.QLineEdit(self.tab_Bolt)
        self.txt_frictional_resistance.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_frictional_resistance.setObjectName("txt_frictional_resistance")
        self.gridLayout_12.addWidget(self.txt_frictional_resistance, 1, 0, 1, 1)
        self.txt_slip_factor = QtWidgets.QLineEdit(self.tab_Bolt)
        self.txt_slip_factor.setText("")
        self.txt_slip_factor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_slip_factor.setObjectName("txt_slip_factor")
        self.gridLayout_12.addWidget(self.txt_slip_factor, 0, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_12, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(209, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_15, 0, 1, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_18, 2, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 201, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem3, 3, 1, 1, 1)
        self.label_note = QtWidgets.QLabel(self.tab_Bolt)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_note.setFont(font)
        self.label_note.setObjectName("label_note")
        self.gridLayout_19.addWidget(self.label_note, 4, 0, 1, 2)
        self.tabWidget.addTab(self.tab_Bolt, "")
        self.tab_Weld = QtWidgets.QWidget()
        self.tab_Weld.setObjectName("tab_Weld")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_Weld)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_16 = QtWidgets.QLabel(self.tab_Weld)
        self.label_16.setObjectName("label_16")
        self.gridLayout_13.addWidget(self.label_16, 0, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_17 = QtWidgets.QLabel(self.tab_Weld)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 0, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.tab_Weld)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_7.addWidget(self.line_5, 1, 0, 1, 1)
        self.textBrowser_weldDescription = QtWidgets.QTextBrowser(self.tab_Weld)
        self.textBrowser_weldDescription.setMinimumSize(QtCore.QSize(210, 320))
        self.textBrowser_weldDescription.setObjectName("textBrowser_weldDescription")
        self.gridLayout_7.addWidget(self.textBrowser_weldDescription, 2, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_7, 0, 2, 4, 1)
        self.line_8 = QtWidgets.QFrame(self.tab_Weld)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_13.addWidget(self.line_8, 1, 0, 1, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_22 = QtWidgets.QLabel(self.tab_Weld)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)
        self.combo_weldType = QtWidgets.QComboBox(self.tab_Weld)
        self.combo_weldType.setObjectName("combo_weldType")
        self.combo_weldType.addItem("")
        self.combo_weldType.addItem("")
        self.gridLayout_3.addWidget(self.combo_weldType, 0, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.tab_Weld)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_Weld)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_Weld)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 1, 1, 1)
        self.txt_weldFu = QtWidgets.QLineEdit(self.tab_Weld)
        self.txt_weldFu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_weldFu.setObjectName("txt_weldFu")
        self.gridLayout_3.addWidget(self.txt_weldFu, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_Weld)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 3, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_3, 2, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 288, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem4, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_Weld, "")
        self.tab_Detailing = QtWidgets.QWidget()
        self.tab_Detailing.setObjectName("tab_Detailing")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_Detailing)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_38 = QtWidgets.QLabel(self.tab_Detailing)
        self.label_38.setObjectName("label_38")
        self.gridLayout_6.addWidget(self.label_38, 0, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.line_6 = QtWidgets.QFrame(self.tab_Detailing)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_10.addWidget(self.line_6, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab_Detailing)
        self.label_18.setObjectName("label_18")
        self.gridLayout_10.addWidget(self.label_18, 0, 0, 1, 1)
        self.textBrowser_detailingDescription = QtWidgets.QTextBrowser(self.tab_Detailing)
        self.textBrowser_detailingDescription.setMinimumSize(QtCore.QSize(210, 0))
        self.textBrowser_detailingDescription.setObjectName("textBrowser_detailingDescription")
        self.gridLayout_10.addWidget(self.textBrowser_detailingDescription, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_10, 0, 2, 5, 1)
        self.line_11 = QtWidgets.QFrame(self.tab_Detailing)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_6.addWidget(self.line_11, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_39 = QtWidgets.QLabel(self.tab_Detailing)
        self.label_39.setObjectName("label_39")
        self.gridLayout_4.addWidget(self.label_39, 0, 0, 1, 1)
        self.combo_detailingEdgeType = QtWidgets.QComboBox(self.tab_Detailing)
        self.combo_detailingEdgeType.setObjectName("combo_detailingEdgeType")
        self.combo_detailingEdgeType.addItem("")
        self.combo_detailingEdgeType.addItem("")
        self.gridLayout_4.addWidget(self.combo_detailingEdgeType, 0, 1, 1, 2)
        self.label_29 = QtWidgets.QLabel(self.tab_Detailing)
        self.label_29.setObjectName("label_29")
        self.gridLayout_4.addWidget(self.label_29, 1, 0, 1, 1)
        self.txt_detailingGap = QtWidgets.QLineEdit(self.tab_Detailing)
        self.txt_detailingGap.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_detailingGap.setObjectName("txt_detailingGap")
        self.gridLayout_4.addWidget(self.txt_detailingGap, 1, 1, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.tab_Detailing)
        self.label_36.setObjectName("label_36")
        self.gridLayout_4.addWidget(self.label_36, 1, 2, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.tab_Detailing)
        self.label_40.setObjectName("label_40")
        self.gridLayout_4.addWidget(self.label_40, 2, 0, 1, 1)
        self.combo_detailing_memebers = QtWidgets.QComboBox(self.tab_Detailing)
        self.combo_detailing_memebers.setObjectName("combo_detailing_memebers")
        self.combo_detailing_memebers.addItem("")
        self.combo_detailing_memebers.addItem("")
        self.gridLayout_4.addWidget(self.combo_detailing_memebers, 2, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 2, 0, 2, 1)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 255, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem6, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab_Detailing, "")
        self.tab_Design = QtWidgets.QWidget()
        self.tab_Design.setObjectName("tab_Design")
        self.label_19 = QtWidgets.QLabel(self.tab_Design)
        self.label_19.setGeometry(QtCore.QRect(21, 31, 84, 16))
        self.label_19.setObjectName("label_19")
        self.combo_design_method = QtWidgets.QComboBox(self.tab_Design)
        self.combo_design_method.setGeometry(QtCore.QRect(160, 31, 227, 22))
        self.combo_design_method.setObjectName("combo_design_method")
        self.combo_design_method.addItem("")
        self.tabWidget.addTab(self.tab_Design, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Design preferences"))
        self.btn_save.setText(_translate("Dialog", "Save"))
        self.btn_close.setText(_translate("Dialog", "Close"))
        self.btn_defaults.setText(_translate("Dialog", "Defaults"))
        self.label_5.setText(_translate("Dialog", "Inputs"))
        self.label_3.setText(_translate("Dialog", "Description"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td colspan=\"3\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">IS 800 Table 20 Typical Average Values for Coefficient of Friction (</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">µ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">f</span><span style=\" font-size:8pt;\">)</span></p></td></tr></table>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td width=\"26\"></td>\n"
"<td width=\"383\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Treatment of Surfaces</span></p></td>\n"
"<td width=\"78\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  µ_f</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">i)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Surfaces not treated</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.2</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">ii)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Surfaces blasted with short or grit with any loose rust removed, no pitting</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.5</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">iii)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Surfaces blasted with short or grit and hot-dip galvanized</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.1</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">iv)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Surfaces blasted with short or grit and spray - metallized with zinc (thickness 50-70 µm)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.25</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">v)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Surfaces blasted with shot or grit and painted with ethylzinc silicate coat (thickness 30-60 µm)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.3</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">vi)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Sand blasted surface, after light rusting</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.52</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">vii)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Surfaces blasted with shot or grit and painted with ethylzinc silicate coat (thickness 60-80 µm)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.3</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">viii)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Surfaces blasted with shot or grit and painted with alcalizinc silicate coat (thickness 60-80 µm)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.3</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">ix)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Surfaces blasted with shot or grit and spray metallized with aluminium (thickness &gt;50 µm)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.5</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">x)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Clean mill scale</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.33</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">xi)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Sand blasted surface</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.48</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">xii)</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Red lead painted surface</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  0.1</span></p></td></tr></table></body></html>"))
        self.label.setText(_translate("Dialog", "Bolt hole type"))
        self.label_2.setText(_translate("Dialog", "Bolt hole clearance (custom)"))
        self.label_4.setText(_translate("Dialog", "Material grade overwrite"))
        self.label_26.setText(_translate("Dialog", "                                               "))
        self.label_15.setText(_translate("Dialog", "Slip factor (µ_f)"))
        self.label_7.setText(_translate("Dialog", "HSFG bolt design parameters:"))
        self.label_13.setText(_translate("Dialog", "Number of effective interfaces offering\n"
"frictional resistance to slip (n_e)"))
        self.txt_boltHoleClearance.setText(_translate("Dialog", "2"))
        self.label_9.setText(_translate("Dialog", "mm"))
        self.label_8.setText(_translate("Dialog", "Fu"))
        self.label_11.setText(_translate("Dialog", "MPa"))
        self.txt_boltFu.setText(_translate("Dialog", "800"))
        self.combo_boltHoleType.setItemText(0, _translate("Dialog", "Standard"))
        self.combo_boltHoleType.setItemText(1, _translate("Dialog", "Over-sized"))
        self.txt_frictional_resistance.setText(_translate("Dialog", "1"))
        self.label_note.setText(_translate("Dialog", "NOTE : If slip is permitted under the design load, design the bolt as a\n"
"bearing bolt and select corresponding (higher) blot grade."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Bolt), _translate("Dialog", "Bolt"))
        self.label_16.setText(_translate("Dialog", "Inputs"))
        self.label_17.setText(_translate("Dialog", "Description"))
        self.textBrowser_weldDescription.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Shop weld takes a material safety factor of 1.25</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Field weld takes a material safety factor of 1.5</span></p></body></html>"))
        self.label_22.setText(_translate("Dialog", "Type of weld"))
        self.combo_weldType.setItemText(0, _translate("Dialog", "Shop weld"))
        self.combo_weldType.setItemText(1, _translate("Dialog", "Field weld"))
        self.label_27.setText(_translate("Dialog", "                                 "))
        self.label_6.setText(_translate("Dialog", "Material grade overwrite"))
        self.label_10.setText(_translate("Dialog", "Fu"))
        self.txt_weldFu.setText(_translate("Dialog", "410"))
        self.label_12.setText(_translate("Dialog", "MPa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Weld), _translate("Dialog", "Weld"))
        self.label_38.setText(_translate("Dialog", "Inputs"))
        self.label_18.setText(_translate("Dialog", "Description"))
        self.textBrowser_detailingDescription.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The minimum edge and distances from the centre of any hole to the nearest edge of a plate shall not be less than </span><span style=\" font-size:8pt; font-weight:600;\">1.7</span><span style=\" font-size:8pt;\"> times the hole diameter in case of </span><span style=\" font-size:8pt; font-weight:600;\">[a- sheared or hand flame cut edges] </span><span style=\" font-size:8pt;\">and </span><span style=\" font-size:8pt; font-weight:600;\">1.5 </span><span style=\" font-size:8pt;\">times the hole diameter in case of </span><span style=\" font-size:8pt; font-weight:600;\">[b - Rolled, machine-flame cut, sawn and palned edges]</span><span style=\" font-size:8pt;\"> (IS 800 - cl. 10. 2. 4. 2)</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri\'; font-size:8pt; vertical-align:middle;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This gap should include the tolerace value of 5mm. So if the assumed clearance is 5mm, then the gap should be = 10mm (= 5mm {clearance} + 5 mm{tolerance})</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri\'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Specifying whether the members are exposed to corrosive influences, here, only affects the calculation of the maximum edge distance as per cl. 10.2.4.3</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label_39.setText(_translate("Dialog", "Type of edges"))
        self.combo_detailingEdgeType.setItemText(0, _translate("Dialog", "a - Sheared or hand flame cut"))
        self.combo_detailingEdgeType.setItemText(1, _translate("Dialog", "b - Rolled, machine-flame cut, sawn and planed"))
        self.label_29.setText(_translate("Dialog", "Gap between beam & support"))
        self.txt_detailingGap.setText(_translate("Dialog", "10"))
        self.label_36.setText(_translate("Dialog", "mm"))
        self.label_40.setText(_translate("Dialog", "Are the members exposed to\n"
"corrosive influences?"))
        self.combo_detailing_memebers.setItemText(0, _translate("Dialog", "No"))
        self.combo_detailing_memebers.setItemText(1, _translate("Dialog", "Yes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Detailing), _translate("Dialog", "Detailing"))
        self.label_19.setText(_translate("Dialog", "Design Method"))
        self.combo_design_method.setItemText(0, _translate("Dialog", "Limit State Design"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Design), _translate("Dialog", "Design"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

