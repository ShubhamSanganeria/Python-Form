# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FORM.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Form(object):
    flag=0
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 768)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/PC/Desktop/images.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Name = QtWidgets.QLineEdit(Form)
        self.Name.setObjectName("Name")
        # self.Name.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Name)
        self.Contact = QtWidgets.QLineEdit(Form)
        self.Contact.setInputMask("+91 999 999 9999")
        self.Contact.setObjectName("Contact")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Contact)
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setInputMask("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.confirm = QtWidgets.QLineEdit(Form)
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm.setObjectName("confirm")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.confirm)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.male = QtWidgets.QRadioButton(Form)
        self.male.setObjectName("male")
        self.horizontalLayout_3.addWidget(self.male)
        self.female = QtWidgets.QRadioButton(Form)
        self.female.setObjectName("female")
        self.horizontalLayout_3.addWidget(self.female)
        self.others = QtWidgets.QRadioButton(Form)
        self.others.setObjectName("others")
        self.horizontalLayout_3.addWidget(self.others)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.toogle = QtWidgets.QPushButton(Form)
        self.toogle.setCheckable(True)
        self.toogle.setObjectName("toogle")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.toogle)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, 10, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setObjectName("ok")
        self.horizontalLayout_4.addWidget(self.ok)
        self.refresh = QtWidgets.QPushButton(Form)
        self.refresh.setObjectName("refresh")
        self.horizontalLayout_4.addWidget(self.refresh)
        self.formLayout.setLayout(9, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 1)

        self.Name.textChanged.connect(self.check)

        self.retranslateUi(Form)
        self.refresh.clicked.connect(self.Name.clear)
        self.refresh.clicked.connect(self.Contact.clear)
        self.refresh.clicked.connect(self.password.clear)
        self.refresh.clicked.connect(self.confirm.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.ok.clicked.connect(self.pwd)
        self.toogle.setCheckable(True)
        self.toogle.toggle()
        self.toogle.clicked.connect(self.manage)
    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "PERSONAL INFORMATION"))
        self.label_2.setText(_translate("Form", "NAME"))
        self.label_3.setText(_translate("Form", "CONTACT"))
        self.label_4.setText(_translate("Form", "PASSWORD"))
        self.Contact.setText(_translate("Form", "+11   "))
        self.label_5.setText(_translate("Form", "Confirm Password"))
        self.label_7.setText(_translate("Form", "GENDER"))
        self.male.setText(_translate("Form", "MALE"))
        self.female.setText(_translate("Form", "FEMALE"))
        self.others.setText(_translate("Form", "OTHERS"))
        self.label_8.setText(_translate("Form", "Are you interested in studying extra subjects? "))
        self.toogle.setText(_translate("Form", "Yes"))
        self.comboBox.setItemText(0, _translate("Form", "Machine Learning"))
        self.comboBox.setItemText(1, _translate("Form", "Web Designing"))
        self.comboBox.setItemText(2, _translate("Form", "Android  App developement"))
        self.comboBox.setItemText(3, _translate("Form", "Embedded Systems"))
        self.comboBox.setItemText(4, _translate("Form", "Data Management"))
        self.comboBox.setItemText(5, _translate("Form", "Python"))
        self.comboBox.setItemText(6, _translate("Form", "IoT"))
        self.label_9.setText(_translate("Form", "Subjects you are interested in?"))
        self.ok.setText(_translate("Form", "OK"))
        self.refresh.setText(_translate("Form", "Refresh"))
    
    def pwd(self):

        txt=self.password.text()
        if self.confirm.text()==txt:
            nm=self.Name.text()
            phn=self.Contact.text()
            if(self.male.isChecked()):
                gn=self.male.text()
            elif(self.female.isChecked()):
                gn=self.female.text()
            else:
                gn=self.others.text()
            if(self.flag==0):
                ext=self.comboBox.currentText()
            else:
                ext="NA"
            print("ACCOUNT CREATED SUCCESSFULLY")
            mdata=sqlite3.connect('Database.db')
            rmt=mdata.cursor()
            rmt.execute('''INSERT INTO data3(NAME,PHONE_NO,SEX,EXTRA SUBJECT) VALUES(?,?,?,?);''',(nm,phn,gn,ext))
            mdata.commit()
            mdata.close()

            # print('''THE DETAILS ARE:
            #     NAME:{},
            #     Contact:{},
            #     Gender:{},
            #     Extra Subj:{}'''.format(nm,phn,gn,ext))
            self.clear()
        else:
            print("PASSWORDS DONT MATCH")
            self.confirm.clear()

    def check(self,text):
        
        if text.isalpha()==False:
            print("Only alphabets allowed")
            self.Name.setText("")
        # else:
        #     self.Name.setText(text)
    def manage(self):
        if self.toogle.isChecked():
            self.toogle.setText("Yes I want to")
            self.comboBox.setEnabled(True)
            self.flag=0
            
        else:
            self.toogle.setText("No I dont")
            self.comboBox.setDisabled(True)
            self.flag=1




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

