import time

from PyQt5 import QtCore, QtGui, QtWidgets


class FactorialThread(QtCore.QThread):
    result = QtCore.pyqtSignal(int, int)
    processing = QtCore.pyqtSignal(str, str)
    infoType = QtCore.pyqtSignal(str)

    def __init__(self, numbers):
        super().__init__()
        self.numbers = numbers

    def run(self):
        for number in self.numbers:
            self.processing.emit("Procesando Hilo: Factorial", str(number))
            if number % 2 != 0:
                self.infoType.emit("Tipo: Impar")
                factorial = 1
                for i in range(1, number + 1):
                    factorial *= i
                self.result.emit(number, factorial)
            else:
                pass
            self.msleep(5000)

class SquareThread(QtCore.QThread):
    result = QtCore.pyqtSignal(int, int)
    processing = QtCore.pyqtSignal(str, str)
    infoType = QtCore.pyqtSignal(str)

    def __init__(self, numbers):
        super().__init__()
        self.numbers = numbers

    def run(self):
        for number in self.numbers:
            self.processing.emit("Procesando Hilo: Cuadrado", str(number))
            if number % 2 == 0:
                self.infoType.emit("Tipo: par")
                square = number ** 2
                self.result.emit(number, square)
            self.msleep(5000)

class MultiplicationTableThread(QtCore.QThread):
    update = QtCore.pyqtSignal(str)
    processing = QtCore.pyqtSignal(str, str)

    def __init__(self, numbers):
        super().__init__()
        self.numbers = numbers

    def run(self):
        for number in self.numbers:
            self.processing.emit("Procesando Hilo: Multiplicacion", str(number))
            table = "\n".join([f"{number} * {i} = {number * i}" for i in range(1, 11)])
            self.update.emit(table)
            self.msleep(5000)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.processingNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.processingNumLabel.setGeometry(QtCore.QRect(40, 40, 301, 16))
        self.processingNumLabel.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.processingNumLabel.setObjectName("processingNumLabel")
        self.wholeNumList = QtWidgets.QListWidget(self.centralwidget)
        self.wholeNumList.setGeometry(QtCore.QRect(30, 220, 171, 341))
        self.wholeNumList.setObjectName("wholeNumList")
        self.oddNumList = QtWidgets.QListWidget(self.centralwidget)
        self.oddNumList.setGeometry(QtCore.QRect(230, 220, 171, 341))
        self.oddNumList.setObjectName("oddNumList")
        self.pairNumList = QtWidgets.QListWidget(self.centralwidget)
        self.pairNumList.setGeometry(QtCore.QRect(430, 220, 171, 341))
        self.pairNumList.setObjectName("pairNumList")
        self.numList = QtWidgets.QListWidget(self.centralwidget)
        self.numList.setGeometry(QtCore.QRect(630, 220, 171, 341))
        self.numList.setObjectName("numList")
        self.processingThreadLabel = QtWidgets.QLabel(self.centralwidget)
        self.processingThreadLabel.setGeometry(QtCore.QRect(40, 90, 301, 16))
        self.processingThreadLabel.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.processingThreadLabel.setObjectName("processingThreadLabel")
        self.typeLabel = QtWidgets.QLabel(self.centralwidget)
        self.typeLabel.setGeometry(QtCore.QRect(440, 70, 201, 21))
        self.typeLabel.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.typeLabel.setObjectName("typeLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 71, 81))
        self.label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 140, 91, 81))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 140, 111, 81))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(670, 170, 91, 41))
        self.label_7.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.executeButton = QtWidgets.QPushButton(self.centralwidget)
        self.executeButton.setGeometry(QtCore.QRect(590, 590, 93, 28))
        self.executeButton.setObjectName("executeButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(710, 590, 93, 28))
        self.exitButton.setObjectName("exitButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.processingNumLabel.setText(_translate("MainWindow", "Procesando Número: "))
        self.processingThreadLabel.setText(_translate("MainWindow", "Procesando Hilo:"))
        self.typeLabel.setText(_translate("MainWindow", "Tipo:"))
        self.label_2.setText(_translate("MainWindow", "Lista de \n"
"Números \n"
"Enteros"))
        self.label_3.setText(_translate("MainWindow", "Factorial de\n"
" Números\n"
" Impares"))
        self.label_6.setText(_translate("MainWindow", "Potencias de\n"
" Números\n"
" Pares"))
        self.label_7.setText(_translate("MainWindow", "Tablas de\n"
" Números"))
        self.executeButton.setText(_translate("MainWindow", "Ejecutar"))
        self.exitButton.setText(_translate("MainWindow", "Salir"))

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.multiplicationTableThread = None
        self.squareThread = None
        self.factorialThread = None
        self.setupUi(self)
        self.executeButton.clicked.connect(self.startThreads)
        self.exitButton.clicked.connect(self.close)

    def startThreads(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.num_enteros()

        self.factorialThread = FactorialThread(numbers)
        self.factorialThread.result.connect(self.displayFactorial)
        self.factorialThread.processing.connect(self.updateProcessingLabel)
        self.factorialThread.infoType.connect(self.Typelabel)
        self.factorialThread.start()
        time.sleep(1)

        self.squareThread = SquareThread(numbers)
        self.squareThread.result.connect(self.displaySquare)
        self.squareThread.processing.connect(self.updateProcessingLabel)
        self.squareThread.infoType.connect(self.Typelabel)
        self.squareThread.start()

        self.multiplicationTableThread = MultiplicationTableThread(numbers)
        self.multiplicationTableThread.update.connect(self.displayTable)
        self.multiplicationTableThread.processing.connect(self.updateProcessingLabel)
        self.multiplicationTableThread.start()

    def displayFactorial(self, number, factorial):
        self.oddNumList.addItem(f"{number} != {factorial}")

    def displaySquare(self, number, square):
        self.pairNumList.addItem(f"{number} ^ 2 = {square}")

    def displayTable(self, text):
        self.numList.clear()
        self.numList.addItem(text)

    def updateProcessingLabel(self, message, number):
        self.processingThreadLabel.setText(message)
        self.processingNumLabel.setText('Procesando Número: ' + number)

    def Typelabel(self, message):
        self.typeLabel.setText(message)

    def num_enteros(self):
        self.wholeNumList.clear()
        for numero in range(1, 21):
            self.wholeNumList.addItem(str(numero))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec_())
