import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


df=pd.read_excel("data.xlsx", engine='openpyxl')

df=df.drop("model",axis=1)
df=df.drop("Unnamed: 0",axis=1)
df=df.drop("Column1",axis=1)
df=df[df.year!=1970]

y=df["price"].values
x=df.drop("price",axis=1).values

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.33,random_state=10)
scaler = MinMaxScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

model = load_model("car_price_analyzer_model.h5")

brand=-1; #0=Mercedes,1=Audi,2=BMW,3=Ford,4=Toyota
fuelType=-1 #1=Petrol,2=Diesel,3=Hybrid,4=Electric,5=Other
transmission=-1 #2=Manual,3=Semi-Auto,4=Automatic,5=Other

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        Form.setMinimumSize(QtCore.QSize(500, 500))
        Form.setMaximumSize(QtCore.QSize(500, 500))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.audi = QtWidgets.QRadioButton(Form)
        self.audi.setGeometry(QtCore.QRect(20, 100, 51, 20))
        self.audi.setObjectName("audi")
        self.br = QtWidgets.QButtonGroup(Form)
        self.br.setObjectName("br")
        self.br.addButton(self.audi)
        self.bmw = QtWidgets.QRadioButton(Form)
        self.bmw.setGeometry(QtCore.QRect(80, 100, 51, 20))
        self.bmw.setObjectName("bmw")
        self.br.addButton(self.bmw)
        self.ford = QtWidgets.QRadioButton(Form)
        self.ford.setGeometry(QtCore.QRect(140, 100, 51, 20))
        self.ford.setObjectName("ford")
        self.br.addButton(self.ford)
        self.mercedes = QtWidgets.QRadioButton(Form)
        self.mercedes.setGeometry(QtCore.QRect(200, 100, 81, 20))
        self.mercedes.setObjectName("mercedes")
        self.br.addButton(self.mercedes)
        self.toyota = QtWidgets.QRadioButton(Form)
        self.toyota.setGeometry(QtCore.QRect(290, 100, 81, 20))
        self.toyota.setObjectName("toyota")
        self.br.addButton(self.toyota)
        self.diesel = QtWidgets.QRadioButton(Form)
        self.diesel.setGeometry(QtCore.QRect(90, 260, 61, 20))
        self.diesel.setObjectName("diesel")
        self.ft = QtWidgets.QButtonGroup(Form)
        self.ft.setObjectName("ft")
        self.ft.addButton(self.diesel)
        self.other_fuel = QtWidgets.QRadioButton(Form)
        self.other_fuel.setGeometry(QtCore.QRect(310, 260, 81, 20))
        self.other_fuel.setObjectName("other_fuel")
        self.ft.addButton(self.other_fuel)
        self.petrol = QtWidgets.QRadioButton(Form)
        self.petrol.setGeometry(QtCore.QRect(20, 260, 61, 20))
        self.petrol.setObjectName("petrol")
        self.ft.addButton(self.petrol)
        self.electric = QtWidgets.QRadioButton(Form)
        self.electric.setGeometry(QtCore.QRect(230, 260, 71, 20))
        self.electric.setObjectName("electric")
        self.ft.addButton(self.electric)
        self.hybrid = QtWidgets.QRadioButton(Form)
        self.hybrid.setGeometry(QtCore.QRect(160, 260, 61, 20))
        self.hybrid.setObjectName("hybrid")
        self.ft.addButton(self.hybrid)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.year = QtWidgets.QLineEdit(Form)
        self.year.setGeometry(QtCore.QRect(70, 140, 120, 24))
        self.year.setObjectName("year")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(260, 130, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.mileage = QtWidgets.QLineEdit(Form)
        self.mileage.setGeometry(QtCore.QRect(340, 140, 120, 24))
        self.mileage.setText("")
        self.mileage.setObjectName("mileage")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tax = QtWidgets.QLineEdit(Form)
        self.tax.setGeometry(QtCore.QRect(50, 190, 81, 24))
        self.tax.setObjectName("tax")
        self.mpg = QtWidgets.QLineEdit(Form)
        self.mpg.setGeometry(QtCore.QRect(200, 190, 81, 24))
        self.mpg.setObjectName("mpg")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(160, 180, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(310, 180, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.engine_size = QtWidgets.QLineEdit(Form)
        self.engine_size.setGeometry(QtCore.QRect(380, 190, 81, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.engine_size.setFont(font)
        self.engine_size.setObjectName("engine_size")
        self.manual = QtWidgets.QRadioButton(Form)
        self.manual.setGeometry(QtCore.QRect(20, 330, 71, 20))
        self.manual.setObjectName("manual")
        self.tr = QtWidgets.QButtonGroup(Form)
        self.tr.setObjectName("tr")
        self.tr.addButton(self.manual)
        self.semiauto = QtWidgets.QRadioButton(Form)
        self.semiauto.setGeometry(QtCore.QRect(100, 330, 91, 20))
        self.semiauto.setObjectName("semiauto")
        self.tr.addButton(self.semiauto)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 290, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.other_transmission = QtWidgets.QRadioButton(Form)
        self.other_transmission.setGeometry(QtCore.QRect(280, 330, 71, 21))
        self.other_transmission.setObjectName("other_transmission")
        self.tr.addButton(self.other_transmission)
        self.automatic = QtWidgets.QRadioButton(Form)
        self.automatic.setGeometry(QtCore.QRect(190, 330, 81, 20))
        self.automatic.setObjectName("automatic")
        self.tr.addButton(self.automatic)
        self.calculate = QtWidgets.QPushButton(Form)
        self.calculate.setGeometry(QtCore.QRect(20, 390, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculate.setFont(font)
        self.calculate.setObjectName("calculate")
        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(190, 400, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")

        self.audi.toggled.connect(self.audiSelected)
        self.bmw.toggled.connect(self.bmwSelected)
        self.ford.toggled.connect(self.fordSelected)
        self.mercedes.toggled.connect(self.mercSelected)
        self.toyota.toggled.connect(self.toyotaSelected)

        self.petrol.toggled.connect(self.petrolSelected)
        self.diesel.toggled.connect(self.dieselSelected)
        self.hybrid.toggled.connect(self.hybridSelected)
        self.electric.toggled.connect(self.electricSelected)
        self.other_fuel.toggled.connect(self.otherFSelected)

        self.manual.toggled.connect(self.manualSelected)
        self.semiauto.toggled.connect(self.semiASelected)
        self.automatic.toggled.connect(self.automaticSelected)
        self.other_transmission.toggled.connect(self.otherTSelected)

        self.calculate.clicked.connect(self.calculateFunc)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def mercSelected(self):
        global brand
        brand=0;

    def audiSelected(self):
        global brand
        brand=1;

    def bmwSelected(self):
        global brand
        brand=2;

    def fordSelected(self):
        global brand
        brand=3;

    def toyotaSelected(self):
        global brand
        brand=4;

    def petrolSelected(self):
        global fuelType
        fuelType = 1;

    def dieselSelected(self):
        global fuelType
        fuelType = 2;

    def hybridSelected(self):
        global fuelType
        fuelType = 3;

    def electricSelected(self):
        global fuelType
        fuelType = 4;

    def otherFSelected(self):
        global fuelType
        fuelType = 5;

    def manualSelected(self):
        global transmission
        transmission = 2;

    def semiASelected(self):
        global transmission
        transmission = 3;

    def automaticSelected(self):
        global transmission
        transmission = 4;

    def otherTSelected(self):
        global transmission
        transmission = 5;

    def calculateFunc(self):
        try:
            brandInt=brand
            fuelTypeInt=fuelType
            transmissionInt=transmission
            yearInt=int(self.year.text())
            mileageInt = int(self.mileage.text())
            taxInt = int(self.tax.text())
            mpgInt = int(self.mpg.text())
            engineSizeInt = int(self.engine_size.text())
            if(yearInt>1940 and yearInt<2022 and mileageInt>0 and taxInt>0 and mpgInt>0 and engineSizeInt>0 and
                    brandInt!=-1 and fuelTypeInt!=-1 and transmissionInt!=-1):
                car = pd.Series(
                    {"year": yearInt, "transmission": transmissionInt, "mileage": mileageInt, "fuelType": fuelTypeInt,
                     "tax": taxInt, "mpg": mpgInt, "engineSize": engineSizeInt, "brand": brandInt})
                car = scaler.transform(car.values.reshape(-1, 8))
                self.result.setText(str(model.predict(car)[0][0])+" £")
            else:
                self.result.setText("Error! Check Values.")
        except:
            self.result.setText("Error! Check Values.")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Car Price Analyzer"))
        self.label.setText(_translate("Form", "Car Price Analyzer"))
        self.label_2.setText(_translate("Form", "Brand"))
        self.audi.setText(_translate("Form", "Audi"))
        self.bmw.setText(_translate("Form", "BMW"))
        self.ford.setText(_translate("Form", "Ford"))
        self.mercedes.setText(_translate("Form", "Mercedes"))
        self.toyota.setText(_translate("Form", "Toyota"))
        self.diesel.setText(_translate("Form", "Diesel"))
        self.other_fuel.setText(_translate("Form", "Other"))
        self.petrol.setText(_translate("Form", "Petrol"))
        self.electric.setText(_translate("Form", "Electric"))
        self.hybrid.setText(_translate("Form", "Hybrid"))
        self.label_3.setText(_translate("Form", "Fuel Type"))
        self.label_4.setText(_translate("Form", "Year"))
        self.label_5.setText(_translate("Form", "Mileage"))
        self.label_6.setText(_translate("Form", "Tax"))
        self.label_7.setText(_translate("Form", "mpg"))
        self.label_8.setText(_translate("Form", "Engine Size"))
        self.manual.setText(_translate("Form", "Manual"))
        self.semiauto.setText(_translate("Form", "Semi-Auto"))
        self.label_9.setText(_translate("Form", "Transmission"))
        self.other_transmission.setText(_translate("Form", "Other"))
        self.automatic.setText(_translate("Form", "Automatic"))
        self.calculate.setText(_translate("Form", "Calculate"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())