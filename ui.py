# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ui(object):
    def setupUi(self, ui):
        ui.setObjectName("ui")
        ui.setWindowModality(QtCore.Qt.ApplicationModal)
        ui.resize(430, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.sizePolicy().hasHeightForWidth())
        ui.setSizePolicy(sizePolicy)
        ui.setMinimumSize(QtCore.QSize(430, 250))
        ui.setMaximumSize(QtCore.QSize(430, 250))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        ui.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(ui)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 200))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.color_invert_f = QtWidgets.QCheckBox(self.layoutWidget)
        self.color_invert_f.setText("")
        self.color_invert_f.setObjectName("color_invert_f")
        self.horizontalLayout_3.addWidget(self.color_invert_f)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.x_invert_f = QtWidgets.QCheckBox(self.layoutWidget)
        self.x_invert_f.setText("")
        self.x_invert_f.setObjectName("x_invert_f")
        self.horizontalLayout_7.addWidget(self.x_invert_f)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.y_invert_f = QtWidgets.QCheckBox(self.layoutWidget)
        self.y_invert_f.setText("")
        self.y_invert_f.setObjectName("y_invert_f")
        self.horizontalLayout_8.addWidget(self.y_invert_f)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.copper_f = QtWidgets.QCheckBox(self.layoutWidget)
        self.copper_f.setText("")
        self.copper_f.setObjectName("copper_f")
        self.horizontalLayout_4.addWidget(self.copper_f)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.l_layer = QtWidgets.QLabel(self.layoutWidget)
        self.l_layer.setObjectName("l_layer")
        self.verticalLayout.addWidget(self.l_layer)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sourcefullpath = QtWidgets.QLineEdit(self.layoutWidget)
        self.sourcefullpath.setObjectName("sourcefullpath")
        self.horizontalLayout.addWidget(self.sourcefullpath)
        self.btn_getfile = QtWidgets.QToolButton(self.layoutWidget)
        self.btn_getfile.setObjectName("btn_getfile")
        self.horizontalLayout.addWidget(self.btn_getfile)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.x_size = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.x_size.setMinimum(1.0)
        self.x_size.setMaximum(999.99)
        self.x_size.setProperty("value", 50.0)
        self.x_size.setObjectName("x_size")
        self.verticalLayout_2.addWidget(self.x_size)
        self.y_size = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.y_size.setMinimum(1.0)
        self.y_size.setMaximum(999.99)
        self.y_size.setProperty("value", 50.0)
        self.y_size.setObjectName("y_size")
        self.verticalLayout_2.addWidget(self.y_size)
        self.width = QtWidgets.QSpinBox(self.layoutWidget)
        self.width.setMinimum(1)
        self.width.setProperty("value", 5)
        self.width.setObjectName("width")
        self.verticalLayout_2.addWidget(self.width)
        self.layer = QtWidgets.QComboBox(self.layoutWidget)
        self.layer.setMaxVisibleItems(11)
        self.layer.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.layer.setObjectName("layer")
        self.layer.addItem("")
        self.layer.addItem("")
        self.layer.addItem("")
        self.layer.addItem("")
        self.layer.addItem("")
        self.layer.addItem("")
        self.layer.addItem("")
        self.layer.addItem("")
        self.layer.addItem("")
        self.layer.addItem("")
        self.verticalLayout_2.addWidget(self.layer)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.thresholdSlider = QtWidgets.QSlider(self.layoutWidget)
        self.thresholdSlider.setMaximum(255)
        self.thresholdSlider.setProperty("value", 127)
        self.thresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.thresholdSlider.setObjectName("thresholdSlider")
        self.horizontalLayout_2.addWidget(self.thresholdSlider)
        self.threshold_label = QtWidgets.QLabel(self.layoutWidget)
        self.threshold_label.setObjectName("threshold_label")
        self.horizontalLayout_2.addWidget(self.threshold_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.btn_convert = QtWidgets.QPushButton(ui)
        self.btn_convert.setGeometry(QtCore.QRect(10, 213, 411, 31))
        self.btn_convert.setObjectName("btn_convert")

        self.retranslateUi(ui)
        self.layer.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(ui)

    def retranslateUi(self, ui):
        _translate = QtCore.QCoreApplication.translate
        ui.setWindowTitle(_translate("ui", "LCEDA图片转换器"))
        self.label_7.setText(_translate("ui", "图像反相"))
        self.label_9.setText(_translate("ui", "水平翻转"))
        self.label_10.setText(_translate("ui", "垂直翻转"))
        self.label_8.setText(_translate("ui", "创建铜皮"))
        self.label.setText(_translate("ui", "图片路径"))
        self.label_2.setText(_translate("ui", "X最大尺寸/mm"))
        self.label_3.setText(_translate("ui", "Y最大尺寸/mm"))
        self.label_4.setText(_translate("ui", "线宽/mil"))
        self.l_layer.setText(_translate("ui", "层级"))
        self.label_6.setText(_translate("ui", "图像阈值"))
        self.sourcefullpath.setText(_translate("ui", ".\\img\\ico.png"))
        self.btn_getfile.setText(_translate("ui", "选取文件"))
        self.layer.setCurrentText(_translate("ui", "顶层阻焊层"))
        self.layer.setItemText(0, _translate("ui", "顶层"))
        self.layer.setItemText(1, _translate("ui", "底层"))
        self.layer.setItemText(2, _translate("ui", "顶层丝印层"))
        self.layer.setItemText(3, _translate("ui", "底层丝印层"))
        self.layer.setItemText(4, _translate("ui", "顶层焊盘层"))
        self.layer.setItemText(5, _translate("ui", "底层焊盘层"))
        self.layer.setItemText(6, _translate("ui", "顶层阻焊层"))
        self.layer.setItemText(7, _translate("ui", "底层阻焊层"))
        self.layer.setItemText(8, _translate("ui", "边框层"))
        self.layer.setItemText(9, _translate("ui", "文档层"))
        self.threshold_label.setText(_translate("ui", "127"))
        self.btn_convert.setText(_translate("ui", "生成文件"))
