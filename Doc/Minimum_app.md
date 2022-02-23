# Минимальное приложение на PyQT5

Минимальное приложение выглядит следующим образом:
```python
import sys
from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.resize(300, 100) # Изменить размер окна
        self.setWindowTitle("Hello") # Установить заголовок окна


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```
![](/Doc/images/minimum.png)

В данном примере создается простое окно. В конструкторе класса MyWindow задается его размер (300x100 px) и задается текст заголовка. К методам главного окна доступ получаем через self. В следующем примере рассмотрим основные методы для работы с главным окном.