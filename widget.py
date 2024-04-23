from PySide6.QtWidgets import QWidget, QPushButton, QMessageBox
from design import Ui_widget

class Widget(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 455, 300, 450)
        self.setMaximumHeight(450)
        self.setMaximumWidth(300)
        self.setMinimumHeight(450)
        self.setMinimumWidth(300)

        # 16 is zero

        self.pushButton_16.clicked.connect(self.on_button_click)
        #17 is decimal

        self.pushButton_17.clicked.connect(self.on_button_click)
        self.pushButton_01.clicked.connect(self.on_button_click)
        self.pushButton_02.clicked.connect(self.on_button_click)
        self.pushButton_03.clicked.connect(self.on_button_click)
        self.pushButton_04.clicked.connect(self.on_button_click)
        self.pushButton_05.clicked.connect(self.on_button_click)
        self.pushButton_06.clicked.connect(self.on_button_click)
        self.pushButton_07.clicked.connect(self.on_button_click)
        self.pushButton_08.clicked.connect(self.on_button_click)
        self.pushButton_09.clicked.connect(self.on_button_click)
        self.pushButton_addition.clicked.connect(self.on_button_click)
        self.pushButton_subtraction.clicked.connect(self.on_button_click)
        self.pushButton_multiplication.clicked.connect(self.on_button_click)
        self.pushButton_division.clicked.connect(self.on_button_click)
        self.pushButton_equals.clicked.connect(self.on_button_click)
        self.pushButton_cancel.clicked.connect(self.on_button_click)

    def on_button_click(self):
        button = self.sender()
        current_text = self.resultLabel.text()

        if current_text == "0":
           current_text = ""

        if button.text() == "=":
            dialog = QMessageBox()
            try:
                result = str(eval(current_text))
                self.resultLabel.setText(result)
                self.sumLabel.setText(current_text + button.text())

            except ZeroDivisionError:
                self.resultLabel.setText("Error")
                dialog.setText("Attempted division by zero")
                dialog.setWindowTitle("Error")
                dialog.setIcon(QMessageBox.Icon.Critical)
                dialog.exec()
            except Exception as e:
                self.resultLabel.setText("Error: Invalid expression")
                self.resultLabel.setText("Error")
                dialog.setText("Invalid expression")
                dialog.setWindowTitle("Error")
                dialog.setIcon(QMessageBox.Icon.Critical)
                dialog.exec()
        else:
            self.resultLabel.setText(current_text + button.text())        
            self.sumLabel.setText(current_text + button.text()) 

        if button.text() == "C":
            self.resultLabel.setText("0")
            self.sumLabel.setText("")           
