import sys
from PyQt5 import QtWidgets, QtGui


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.resize(300, 100)
        self.setWindowTitle("Hello")

    def closeEvent(self, event):
        print('Закрытие приложения!') # Вместо print сюда можно поместить, например, метод сохранения настроек, закрытие соединение с базой данных, и т.д.
        
    def resizeEvent(self, event):
        print(self.size()) # Выводим в консоль текущий размер окна

    def mouseDoubleClickEvent(self, event):
        print('Mouse double clicked!!!') # Догадайтесь :)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())