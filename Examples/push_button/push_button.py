import sys
from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.resize(300, 100)
        self.setWindowTitle("Hello")
        
        self.box_layout = QtWidgets.QHBoxLayout() # Создаем BoxLayout layout

        self.button = QtWidgets.QPushButton()
        self.button.setText('Button')
        self.button.clicked.connect(self.click) 

        self.box_layout.addWidget(self.button) # Добавляем на layout кнопку
        self.setLayout(self.box_layout) # Устанавливаем окну layout

    def click(self): # Метод обработки нажатия на кнопку
        self.button.setText('Кнопка нажата!')
        self.setWindowTitle('Кнопка нажата!')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())