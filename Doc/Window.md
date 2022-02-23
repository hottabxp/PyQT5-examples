# Работа с главным окном
### [Код](../Examples/window/window.py)

В первом примере мы настраивали главное окно в конструкторе MyWindow. Но создание и настройка виджетов лучше вынести в отдельный метод, и этом метод уже вызывать в конструкторе.
Пример:
```python
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.init_ui() # Вызываем метод создания и настройки виджета

    def init_ui(self): # В данном методе создаем и настраиваем виджеты
        self.resize(300, 100) # Изменить размер окна
        self.setWindowTitle("Hello") # Установить заголовок окна

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```
 При таком подходе нам будет проще ориентироваться в коде.
 Теперь рассмотрим самые основные методы для работы с виджетами (в данном случае с "главным окном"):
 
 1) windowTitle() - метод возвращает строку, которая находится в заголовке нашего окна;
 2) height(), width() - получить высоту и ширину окна (виджета).
 3) size() - получить объект QSize(высота, ширина).
 4) resize(w: int, h: int) - установить размер окна (ширина, высота).
 5) setGeometry(ax: int, ay: int, aw: int, ah: int) - установить положение и размер окна.
 6) setWindowTitle:(str) - установить заголовок окна.
 7) setStyleSheet(str) - установить стиль виджета. StyleSheet - это таблица стилей, очень похожа на CSS. Дополнительно можно узнать в офф. документации - [Qt Style Sheets Examples](https://doc.qt.io/qtforpython/overviews/stylesheet-examples.html).

 Простой пример:
 ```python
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
 ```
Результат:

![](/Doc/images/window.png)