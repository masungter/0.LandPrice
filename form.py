# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1045, 390)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(732, 60, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 1011, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_cal = QtWidgets.QPushButton(Dialog)
        self.pushButton_cal.setGeometry(QtCore.QRect(930, 301, 93, 28))
        self.pushButton_cal.setObjectName("pushButton_cal")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(510, 340, 201, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_land = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_land.setObjectName("lineEdit_land")
        self.horizontalLayout.addWidget(self.lineEdit_land)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(720, 340, 201, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_building = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_building.setObjectName("lineEdit_building")
        self.horizontalLayout_2.addWidget(self.lineEdit_building)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(832, 60, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(720, 300, 201, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_year = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.horizontalLayout_4.addWidget(self.lineEdit_year)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(930, 60, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_cal_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_cal_2.setGeometry(QtCore.QRect(930, 341, 93, 28))
        self.pushButton_cal_2.setObjectName("pushButton_cal_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(24, 26, 571, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(24, 56, 571, 21))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "불러오기"))
        self.pushButton_cal.setText(_translate("Dialog", "공공API"))
        self.label.setText(_translate("Dialog", "대지 비율:"))
        self.label_2.setText(_translate("Dialog", "건물 비율:"))
        self.pushButton_3.setText(_translate("Dialog", "초기화"))
        self.label_3.setText(_translate("Dialog", "검색 연도:"))
        self.pushButton_4.setText(_translate("Dialog", "내보내기"))
        self.pushButton_cal_2.setText(_translate("Dialog", "비율 계산"))
        self.label_4.setText(_translate("Dialog", "1. 주소(pnu)에 해당하는 토지/개발주택/공공주택 가격을 불러오는 프로그램"))
        self.label_5.setText(_translate("Dialog", "2. input 파일은 price.xlsx 로 \"4113310500130100001\" 와 같은 데이터를 입력한다"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
