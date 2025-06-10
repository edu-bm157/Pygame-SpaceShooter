from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QButtonGroup


app = QApplication([])

ventana = QWidget()
ventana.setWindowTitle("Mi primer aplicación en PyQt5")
ventana.resize(200, 200)
ventana.move(700, 300)
ventana.show()

#----------Creación de un texto(label)----------------
texto = QLabel("¡Es un milagro!")
guia_vertical = QVBoxLayout()
texto2 = QLabel("")

#--------------------------Creción de un botón--------------------------
def mostrar_label():
    guia_vertical.addWidget(texto, alignment=Qt.AlignCenter)

boton = QPushButton('Confirmar')
boton.clicked.connect(mostrar_label)

boton_radio = QRadioButton('Botón de radio')
boton_radio2 = QRadioButton('Botón de radio 2')
boton_radio3 = QRadioButton('Botón de radio 3')
boton_radio.setChecked(True)
boton_radio2.setChecked(False)
boton_radio3.setChecked(False)




grupo_de_botones = QButtonGroup()
grupo_de_botones.addButton(boton_radio, 1)
grupo_de_botones.addButton(boton_radio2, 2)
grupo_de_botones.addButton(boton_radio3, 3)

def actualizarTexto2():
    texto2.setText("El botón seleccionado fue el número" + str(grupo_de_botones.checkedId()))

grupo_de_botones.buttonClicked.connect(actualizarTexto2)


# guia_vertical.addWidget(texto, alignment=Qt.AlignCenter)
guia_vertical.addWidget(texto2, alignment=Qt.AlignCenter)
guia_vertical.addWidget(boton, alignment=Qt.AlignCenter)
guia_vertical.addWidget(boton_radio, alignment=Qt.AlignCenter)
guia_vertical.addWidget(boton_radio2, alignment=Qt.AlignCenter)
guia_vertical.addWidget(boton_radio3, alignment=Qt.AlignCenter)

ventana.setLayout(guia_vertical)
app.exec_()