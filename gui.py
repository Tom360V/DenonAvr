import sys
import random
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QGroupBox, QHBoxLayout)
from PySide2.QtCore import Slot, Qt

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = ["Hello Bla", "123", "blabla",
            "Hola Mundo", "zzzzzz"]

        self.horizontalGroupBox = QGroupBox("Horizontal layout")

        self.button1 = QPushButton("Click me!")
        self.button2 = QPushButton("Click me!")
        self.text = QLabel("Hello World")
        self.text.setAlignment(Qt.AlignCenter)


        self.gblayout = QHBoxLayout();
        self.gblayout.addWidget(self.button1)
        self.gblayout.addWidget(self.button2)
        self.horizontalGroupBox.setLayout(self.gblayout)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.horizontalGroupBox)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button1.clicked.connect(self.magic1)
        self.button2.clicked.connect(self.magic2)

    @Slot()
    def magic1(self):
        self.text.setText(random.choice(self.hello))
    @Slot()
    def magic2(self):
        self.text.setText("DEFAULT")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
