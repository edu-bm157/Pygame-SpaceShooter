from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout

app = QApplication([])
ANCHO_VENTANA = 300
ALTO_VENTANA = 200
class VentanaPrincipal(QWidget):
    """
    Clase que se encarga de crear la ventana principal de la aplicación. Esta clae cuenta con 3 métodos propios:
    setDistribution
    setFunctionality
    setStyles"""
    def __init__(self):
        """
        El constructor de esta clase se encarga de definir el nombre de la ventana, que color de fondo tendrá,
        qué posición y tamaño tendrá apoyandose de las constantes ANCHO_VENTANA y ALTO_VENTANA.
        También hace el llamado a los métodos setDistribution, setFunctionality y setStyles.
        """
        super().__init__()
        self.setWindowTitle("Calculadora Python")
        self.setGeometry(100,100, ANCHO_VENTANA, ALTO_VENTANA)
        
        self.setDistribution()
        self.setStyles()
        self.setFunctionality()
    
    def setDistribution(self):
        """
        Este método se encarga de definir la distribución de los widgets dentro de la ventana.
        Crea un QLabel para mostrar el resultado y varios QPushButton para los números y operadores."""
        self.resultado = QLabel("0")
        self.boton1 = QPushButton("1")
        self.boton2 = QPushButton("2")
        self.boton3 = QPushButton("3")
        self.boton4 = QPushButton("4")
        self.boton5 = QPushButton("5")
        self.boton6 = QPushButton("6")
        self.boton7 = QPushButton("7")
        self.boton8 = QPushButton("8")
        self.boton9 = QPushButton("9")
        self.boton0 = QPushButton("0")
        self.boton_mas = QPushButton("+")
        self.boton_menos = QPushButton("-")
        self.boton_multiplicar = QPushButton("×")
        self.boton_dividir = QPushButton("÷")
        self.boton_limpiar_operacion = QPushButton("C")
        self.boton_igual = QPushButton("=")
        layout_grid = QGridLayout()
        layout_grid.addWidget(self.boton1, 0,0)
        layout_grid.addWidget(self.boton2, 0,1)
        layout_grid.addWidget(self.boton3, 0,2)
        layout_grid.addWidget(self.boton4, 1,0)
        layout_grid.addWidget(self.boton5, 1,1)
        layout_grid.addWidget(self.boton6, 1,2)
        layout_grid.addWidget(self.boton7, 2,0)
        layout_grid.addWidget(self.boton8, 2,1)
        layout_grid.addWidget(self.boton9, 2,2)
        layout_grid.addWidget(self.boton0, 3,0)
        layout_grid.addWidget(self.boton_limpiar_operacion, 3,1)
        layout_grid.addWidget(self.boton_mas, 0,3)
        layout_grid.addWidget(self.boton_menos, 1,3)
        layout_grid.addWidget(self.boton_multiplicar, 2,3)
        layout_grid.addWidget(self.boton_dividir, 3,3)
        layout_grid.addWidget(self.boton_igual, 3,2)
        layout_grid.addWidget(self.resultado,4 ,0, 4, 4)

        self.setLayout(layout_grid)

    def setFunctionality(self):
        """
        Este método se encarga de conectar los botones con sus respectivas funciones.
        Cada botón numérico se conecta a la función agregar_numero, los operadores a agregar_operador,
        """
        # Conecta todos los botones numéricos
        self.boton0.pressed.connect(lambda: self.agregar_numero("0"))
        self.boton1.pressed.connect(lambda: self.agregar_numero("1"))
        self.boton2.pressed.connect(lambda: self.agregar_numero("2"))
        self.boton3.pressed.connect(lambda: self.agregar_numero("3"))
        self.boton4.pressed.connect(lambda: self.agregar_numero("4"))
        self.boton5.pressed.connect(lambda: self.agregar_numero("5"))
        self.boton6.pressed.connect(lambda: self.agregar_numero("6"))
        self.boton7.pressed.connect(lambda: self.agregar_numero("7"))
        self.boton8.pressed.connect(lambda: self.agregar_numero("8"))
        self.boton9.pressed.connect(lambda: self.agregar_numero("9"))
        # Conecta operadores
        self.boton_mas.pressed.connect(lambda: self.agregar_operador("+"))
        self.boton_menos.pressed.connect(lambda: self.agregar_operador("-"))
        self.boton_multiplicar.pressed.connect(lambda: self.agregar_operador("*"))
        self.boton_dividir.pressed.connect(lambda: self.agregar_operador("/"))
        # Conecta igual y limpiar
        self.boton_igual.pressed.connect(self.calcular_resultado)
        self.boton_limpiar_operacion.pressed.connect(self.limpiar)

        self.operacion = ""

    def setStyles(self):
        """
        Este método se encarga de darle la estética a nuestra aplicación con ayuda de atributos usados
        en CSS (Cascading Style Sheets).
        """
        botones_numericos = [self.boton1,
                             self.boton2,
                             self.boton3,
                             self.boton4,
                             self.boton5,
                             self.boton6,
                             self.boton7,
                             self.boton8,
                             self.boton9,
                             self.boton0]
        for boton in botones_numericos:
            boton.setStyleSheet("font-size: 20px;" \
                                "color:white;" \
                                "background-color: #303c4f;" \
                                "border-radius:5px")
        botones_operadores = [self.boton_mas, self.boton_menos, self.boton_multiplicar,
                              self.boton_dividir, self.boton_igual, self.boton_limpiar_operacion]
        for boton in botones_operadores:
            boton.setStyleSheet("font-size: 20px;" \
                                "color:white;" \
                                "background-color: #3c5078;" \
                                "border-radius:5px;")
        self.resultado.setStyleSheet("font-size: 30px;" \
                                     "color:White;" \
                                     "background-color: #1d2530;" \
                                     "font-family: Calibri;")

    def agregar_numero(self, numero):
        if self.resultado.text() == "0":
            self.resultado.setText(numero)
            self.operacion = numero
        else:
            self.resultado.setText(self.resultado.text() + numero)
            self.operacion += numero

    def agregar_operador(self, operador):
        if self.operacion and self.operacion[-1] not in "+-*/":
            self.resultado.setText(self.resultado.text() + operador)
            self.operacion += operador

    def calcular_resultado(self):
        try:
            resultado = str(eval(self.operacion))
            self.resultado.setText(resultado)
            self.operacion = resultado
        except Exception:
            self.resultado.setText("Error")
            self.operacion = ""

    def limpiar(self):
        self.resultado.setText("0")
        self.operacion = ""

mi_ventana = VentanaPrincipal()
mi_ventana.show()
app.exec_()