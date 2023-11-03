# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Shapefile_Layer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QVariant
from qgis.core import QgsVectorLayer, QgsProject, QgsVectorFileWriter, QgsField
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QComboBox
from qgscheckablecombobox import QgsCheckableComboBox
from qgsexternalresourcewidget import QgsExternalResourceWidget
from qgsfilterlineedit import QgsFilterLineEdit
from qgsprojectionselectionwidget import QgsProjectionSelectionWidget
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(652, 523)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 30, 571, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.mQgsExternalResourceWidget = QgsExternalResourceWidget(self.formLayoutWidget)
        self.mQgsExternalResourceWidget.setObjectName("mQgsExternalResourceWidget")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mQgsExternalResourceWidget)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.mComboBox = QgsCheckableComboBox(self.formLayoutWidget)
        self.mComboBox.setObjectName("mComboBox")
        self.mComboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mComboBox)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.mComboBox_2 = QgsCheckableComboBox(self.formLayoutWidget)
        self.mComboBox_2.setObjectName("mComboBox_2")
        self.mComboBox_2.addItem("")
        self.mComboBox_2.addItem("")
        self.mComboBox_2.addItem("")
        self.mComboBox_2.addItem("")
        self.mComboBox_2.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mComboBox_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.mQgsProjectionSelectionWidget = QgsProjectionSelectionWidget(self.formLayoutWidget)
        self.mQgsProjectionSelectionWidget.setObjectName("mQgsProjectionSelectionWidget")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.mQgsProjectionSelectionWidget)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 200, 571, 141))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 571, 123))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.mLineEdit_10 = QgsFilterLineEdit(self.formLayoutWidget_2)
        self.mLineEdit_10.setProperty("qgisRelation", "")
        self.mLineEdit_10.setObjectName("mLineEdit_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mLineEdit_10)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.mComboBox_6 = QgsCheckableComboBox(self.formLayoutWidget_2)
        self.mComboBox_6.setObjectName("mComboBox_6")
        self.mComboBox_6.addItem("")
        self.mComboBox_6.addItem("")
        self.mComboBox_6.addItem("")
        self.mComboBox_6.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mComboBox_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_5.addWidget(self.label_19)
        self.mLineEdit_11 = QgsFilterLineEdit(self.formLayoutWidget_2)
        self.mLineEdit_11.setProperty("qgisRelation", "")
        self.mLineEdit_11.setObjectName("mLineEdit_11")
        self.horizontalLayout_5.addWidget(self.mLineEdit_11)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_5.addWidget(self.label_20)
        self.mLineEdit_12 = QgsFilterLineEdit(self.formLayoutWidget_2)
        self.mLineEdit_12.setProperty("qgisRelation", "")
        self.mLineEdit_12.setObjectName("mLineEdit_12")
        self.horizontalLayout_5.addWidget(self.mLineEdit_12)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 350, 581, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 20, 571, 89))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.formLayoutWidget_3)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.tableWidget_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(420, 480, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton.clicked.connect(self.add_to_fields_list)

        self.buttonBox.accepted.connect(self.create_new_layer)
        

        self.layout = QVBoxLayout(Form)
        self.layout.addWidget(self.formLayoutWidget)
        self.layout.addWidget(self.groupBox)
        self.layout.addWidget(self.groupBox_2)
        self.layout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "File Name"))
        self.label_2.setText(_translate("Form", "File Encoding"))
        self.mComboBox.setItemText(0, _translate("Form", "UTF-8"))
        self.label_3.setText(_translate("Form", "Geometry Type"))
        self.mComboBox_2.setItemText(0, _translate("Form", "No Geometry"))
        self.mComboBox_2.setItemText(1, _translate("Form", "Point"))
        self.mComboBox_2.setItemText(2, _translate("Form", "MultiPoint"))
        self.mComboBox_2.setItemText(3, _translate("Form", "LineString"))
        self.mComboBox_2.setItemText(4, _translate("Form", "Polygon"))
        self.label_4.setText(_translate("Form", "Additional dimension"))
        self.radioButton_3.setText(_translate("Form", "None"))
        self.radioButton.setText(_translate("Form", "Z( +M values)"))
        self.radioButton_2.setText(_translate("Form", "M values"))
        self.groupBox.setTitle(_translate("Form", "New Fields"))
        self.label_17.setText(_translate("Form", "Name"))
        self.label_18.setText(_translate("Form", "Type"))
        self.mComboBox_6.setItemText(0, _translate("Form", "Test (String)"))
        self.mComboBox_6.setItemText(1, _translate("Form", "Interger(32 bit)"))
        self.mComboBox_6.setItemText(2, _translate("Form", "Decimal( Double)"))
        self.mComboBox_6.setItemText(3, _translate("Form", "Date"))
        self.label_19.setText(_translate("Form", "Length"))
        self.label_20.setText(_translate("Form", "Precision"))
        self.pushButton.setText(_translate("Form", "Add to Fields List"))
        self.groupBox_2.setTitle(_translate("Form", "Fields List"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Type"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Length"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Precision"))

    def create_new_layer(self):
        import os  # Make sure to import the os module

        # Get the full file path from the QgsExternalResourceWidget
        fullFilePath = self.mQgsExternalResourceWidget.documentPath()

        # Use os.path to get the base name of the file (without the directory)
        fileName = os.path.basename(fullFilePath)

        fileEncoding = self.mComboBox.currentText()
        geometryType = self.mComboBox_2.currentText()
        isNone = self.radioButton_3.isChecked()
        fields = self.get_all_fields()

        # Create a new memory layer with the specified geometry type and fields
        layer = QgsVectorLayer(f"{geometryType}?crs=epsg:4326", fileName, "memory")
        provider = layer.dataProvider()
        provider.addAttributes(fields)
        layer.updateFields()

        # Save the layer to a Shapefile
        options = QgsVectorFileWriter.SaveVectorOptions()
        options.driverName = "ESRI Shapefile"
        options.fileEncoding = "utf-8"
        QgsVectorFileWriter.writeAsVectorFormat(layer, f"D:/qgis/{fileName}.shp", options)

        # Add the layer to the Layers panel
        QgsProject.instance().addMapLayer(layer)
        
    
    def get_qvariant_type(self, field_type):
        if field_type == "Test (String)":
            return QVariant.String
        elif field_type == "Interger(32 bit)":
            return QVariant.Int
        elif field_type == "Decimal( Double)":
            return QVariant.Double
        elif field_type == "Date":
            return QVariant.Date
        else:
            return QVariant.Invalid

    def get_all_fields(self):
        fields = []
        for row in range(self.tableWidget_4.rowCount()):
            fieldNameItem = self.tableWidget_4.item(row, 0)
            fieldTypeItem = self.tableWidget_4.item(row, 1)
            fieldLengthItem = self.tableWidget_4.item(row, 2)
            fieldPrecisionItem = self.tableWidget_4.item(row, 3)
            if fieldNameItem and fieldTypeItem and fieldLengthItem and fieldPrecisionItem:
                fieldName = fieldNameItem.text()
                fieldType = self.get_qvariant_type(fieldTypeItem.text())
                fieldLength = int(fieldLengthItem.text())
                fieldPrecision = int(fieldPrecisionItem.text())
                
                # Create a QgsField with the collected information
                field = QgsField(fieldName, fieldType, len=fieldLength, prec=fieldPrecision)
                fields.append(field)
        return fields



    def get_field_info(self):
        fieldName = self.mLineEdit_10.text()
        fieldType = self.mComboBox_6.currentText()
        fieldLength = int(self.mLineEdit_11.text()) if self.mLineEdit_11.text() else 0
        fieldPrecision = int(self.mLineEdit_12.text()) if self.mLineEdit_12.text() else 0
        return fieldName, fieldType, fieldLength, fieldPrecision


    def add_to_fields_list(self):
        fieldName, fieldType, fieldLength, fieldPrecision = self.get_field_info()
        rowPosition = self.tableWidget_4.rowCount()
        self.tableWidget_4.insertRow(rowPosition)
        self.tableWidget_4.setItem(rowPosition, 0, QTableWidgetItem(fieldName))
        self.tableWidget_4.setItem(rowPosition, 1, QTableWidgetItem(fieldType))
        self.tableWidget_4.setItem(rowPosition, 2, QTableWidgetItem(str(fieldLength)))
        self.tableWidget_4.setItem(rowPosition, 3, QTableWidgetItem(str(fieldPrecision)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())