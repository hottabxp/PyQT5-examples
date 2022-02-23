import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.init_ui() # Вызываем метод создания и настройки виджета

    def init_ui(self): # В данном методе создаем и настраиваем виджеты

        # Установка значений окна:
        self.resize(300, 100) # Изменить размер окна
        self.setWindowTitle("Hello") # Установить заголовок окна
        # self.setStyleSheet("background-color: red") # Сделать фон окна красным
        self.setStyleSheet("background-color: rgb(85, 87, 217);") # Также можно использовать rgb

        # Получение значений окна:
        win_title = self.windowTitle()
        win_height = self.height()
        win_width = self.width()
        win_size = self.size()

        # Печать в консоль параметров окна:
        print(f"Заголовок окна: {win_title}")
        print(f"Высота окна: {win_height}")
        print(f"Ширина окна: {win_width}")
        print(f"Размер окна: {win_size}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())