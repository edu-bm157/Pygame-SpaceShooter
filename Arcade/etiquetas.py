from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QButtonGroup

app = QApplication([])
ventana = QWidget()

etiqueta1 = QLabel("PHP")
etiqueta2 = QLabel("Python")
etiqueta3 = QLabel("SQL")
etiqueta4 = QLabel("JavaScript")
etiqueta5 = QLabel("Pascal")
etiqueta6 = QLabel("C++")

guia_horizontal1 = QVBoxLayout()
guia_horizontal2 = QVBoxLayout()
guia_horizontal3 = QVBoxLayout()

guia_vertical = QVBoxLayout()
guia_horizontal1.addWidget(etiqueta1, alignment=Qt.AlignLeft | Qt.AlignTop)
guia_horizontal1.addWidget(etiqueta2, alignment=Qt.AlignRight | Qt.AlignTop)
guia_horizontal1.addWidget(etiqueta3, alignment=Qt.AlignLeft | Qt.AlignCenter)
guia_horizontal1.addWidget(etiqueta4, alignment=Qt.AlignRight | Qt.AlignCenter)
guia_horizontal1.addWidget(etiqueta5, alignment=Qt.AlignLeft | Qt.AlignBottom)
guia_horizontal1.addWidget(etiqueta6, alignment=Qt.AlignRight | Qt.AlignBottom)

ventana.setLayout(guia_horizontal1)
ventana.show()
app.exec_()