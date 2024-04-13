import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QButtonGroup, QHBoxLayout, QDialog, QDialogButtonBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
# Base de conocimiento 
reglas = [

    #pizzas
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Pepperoni Mia"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Chicago Hawaina"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Meat Lovers Hut Cheese"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Hut Cheese Suprema"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Cheesy Pop Hawaiana"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Pizza Salchicha Italiana"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Pizza de Pepperoni y Queso Azul"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Pizza de Sartén Honolulu"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Pizza de Pepperoni"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Pizza de Jamón"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Pizza Double Cheese"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Pizza de Queso"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Pizza Honolulu"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "Sí", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Pizza con Espinaca y Queso de Cabra"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "Sí", "diabetico": "No", "categoria_comida": "Pizza"}, "entonces": "Pizza de Base de Coliflor"},

    #Bebidas
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Refresco de cola"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Limonada"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "Sí", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Agua mineral"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Coca-Cola"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Coca-Cola Light"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Coca-Cola Zero"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Nestea"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Sprite"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Fanta Naranja"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Don Simon Tropical"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "Sí", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Coca-Cola Light"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "Sí", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Coca-Cola Zero"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "Sí", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Nestea"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "Sí", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Sprite"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "Sí", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Fanta Naranja"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "Sí", "diabetico": "No", "categoria_comida": "Bebidas"}, "entonces": "Don Simon Tropical"},

    #Hamburguesas
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Whopper"},
    {"si": {"tiempo": "Medio", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Doble Whopper"},
    {"si": {"tiempo": "Largo", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Triple Whopper"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Long Chicken"},
    {"si": {"tiempo": "Medio", "preferencia": "Saludable", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Steakhouse"},
    {"si": {"tiempo": "Largo", "preferencia": "Saludable", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Chicken Tendercrisp"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Whopper®"},
    {"si": {"tiempo": "Medio", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Doble Whopper®"},
    {"si": {"tiempo": "Largo", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Triple Whopper®"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Long Chicken®"},
    {"si": {"tiempo": "Medio", "preferencia": "Saludable", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Steakhouse"},
    {"si": {"tiempo": "Largo", "preferencia": "Saludable", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Chicken Tendercrisp®"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Big King®"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Big King® XXL"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Doble Cheeseburger"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Doble Cheeseburger BBQ"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Doble Cheese Bacon XXL"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Whopper Jr.®"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Doble Texas"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Hamburger"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Burger sin gluten"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Chicken Burger"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Cheeseburger"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Cheeseburger sin gluten"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Bacon Cheeseburger"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Bacon Chicken Cheeseburger"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Crispy Chicken®"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Chicken Wrap"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Cheeseburger Kids"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "The King Huevo"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "The King Huevo (Solo 1 Carne)"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "The King Bacon (1 Carne)"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "The King Bacon (2 Carnes)"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Bacon Tendercrisp®"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Doble cheese salad"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Fondue Burger Extra (1 carne)"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Fondue Burger Extra (2 carnes)"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Fondue Burger Extra Tendercrisp®"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Big FishTM"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Hamburguesa"}, "entonces": "Rebel Whopper®"},

    #Postres
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "King FusionTM OREO®"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "King FusionTM KIT KAT®"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "King FusionTM BROWNIE"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Brownie"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Brownie con helado"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Gofre"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Pancakes x2"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Danonino® Bebedino"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Danonino® Petitdino Chocolate"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Danonino® Petitdino Fresa"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "BURGER KING SANDYTM"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "BURGER KING SANDYTM con sirope de caramelo"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "BURGER KING SANDYTM con sirope de chocolate"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "BURGER KING SANDYTM con sirope de fresa"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Tarta con OREO®"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "OREO® Shake"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Choco OREO® Shake"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Chocolate Blanco Golden OREO® Shake"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Chocolate Shake"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Fresa Shake"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Vainilla Shake"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Tarta de cumpleaños (500 y 1000 g.)"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Postres"}, "entonces": "Muffin de chocolate"},

    #Ensaladas
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "Sí", "diabetico": "No", "categoria_comida": "Ensaladas"}, "entonces": "Ensalada Individual"},
    {"si": {"tiempo": "Medio", "preferencia": "Saludable", "vegetariano": "Sí", "diabetico": "No", "categoria_comida": "Ensaladas"}, "entonces": "Ensalada Delight"},
    {"si": {"tiempo": "Largo", "preferencia": "Saludable", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Ensaladas"}, "entonces": "Ensalada Delight con pollo crujiente"},
    {"si": {"tiempo": "Corto", "preferencia": "Saludable", "vegetariano": "No", "diabetico": "Sí", "categoria_comida": "Ensaladas"}, "entonces": "Ensalada con salsa césar"},

    #pollo
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pollo"}, "entonces": "McPollo"},
    {"si": {"tiempo": "Medio", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pollo"}, "entonces": "Chicken Mayo"},
    {"si": {"tiempo": "Largo", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "No", "categoria_comida": "Pollo"}, "entonces": "Chicken Burger BBQ"},
    {"si": {"tiempo": "Corto", "preferencia": "Sabrosa", "vegetariano": "No", "diabetico": "Sí", "categoria_comida": "Pollo"}, "entonces": "Alitas de Pollo"}
]


# Función para evaluar las reglas
def evaluar_reglas(preferencias):
    recomendaciones = []
    for regla in reglas:
        condicion_cumplida = True
        for clave, valor in regla["si"].items():
            if preferencias.get(clave, None) != valor:
                condicion_cumplida = False
                break
        if condicion_cumplida:
            recomendaciones.append(regla["entonces"])
    if recomendaciones:
        return recomendaciones
    else:
        return ["Opción no disponible"]



class VentanaRecomendacion(QDialog):
    def __init__(self, mensaje, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Recomendación')
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        # Crea un QLabel para la imagen
        label_imagen = QLabel()
        pixmap = QPixmap('ventana.png')  
        pixmap = pixmap.scaled(500, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label_imagen.setPixmap(pixmap)
        label_imagen.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_imagen)

        # Crea un QLabel para el mensaje
        label_mensaje = QLabel(mensaje)
        label_mensaje.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_mensaje)

        

        self.setLayout(layout)


# Aplicación principal
app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle('Sistema Experto de Comida Rápida')

# Layout principal
layout = QVBoxLayout()

# Crea un QLabel para el logo principal
label_logo = QLabel()
pixmap_logo = QPixmap('logo.png')  # Asegúrate de que 'logo_principal.png' sea la ruta a tu imagen de logo
pixmap_logo = pixmap_logo.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Ajusta el tamaño según necesites
label_logo.setPixmap(pixmap_logo)
label_logo.setAlignment(Qt.AlignCenter)  # Centra el logo en el layout si lo deseas

# Añade el QLabel del logo al layout principal
layout.addWidget(label_logo)

# Etiqueta para mostrar el resultado
resultado_label = QLabel('Selecciona tus opciones')
layout.addWidget(resultado_label)

# Función para obtener la recomendación y mostrarla en la ventana
def obtener_recomendacion():
    tiempo = grupo_tiempo.checkedButton().text() if grupo_tiempo.checkedButton() else "No seleccionado"
    preferencia = grupo_preferencia.checkedButton().text() if grupo_preferencia.checkedButton() else "No seleccionado"
    vegetariano = grupo_vegetariano.checkedButton().text() if grupo_vegetariano.checkedButton() else "No seleccionado"
    diabetico = grupo_diabetico.checkedButton().text() if grupo_diabetico.checkedButton() else "No seleccionado"
    categoria_comida = grupo_categoria_comida.checkedButton().text() if grupo_categoria_comida.checkedButton() else "No seleccionado"
    preferencias = {"tiempo": tiempo, "preferencia": preferencia, "vegetariano": vegetariano, "diabetico": diabetico, "categoria_comida": categoria_comida}
    recomendacion = evaluar_reglas(preferencias)
    if recomendacion == "Opción no disponible":
        mensaje = "Lo siento, no hay recomendaciones disponibles para la selección actual."
    else:
        mensaje = "Recomendación:\n" + "\n".join(recomendacion)
    ventana_recomendacion = VentanaRecomendacion(mensaje)
    ventana_recomendacion.exec_()



# Grupos de botones de radio
grupo_tiempo = QButtonGroup(ventana)
grupo_preferencia = QButtonGroup(ventana)
grupo_vegetariano = QButtonGroup(ventana)
grupo_diabetico = QButtonGroup(ventana)
grupo_categoria_comida = QButtonGroup(ventana)

# Layouts horizontales para cada grupo de botones de radio
layout_tiempo = QHBoxLayout()
layout_preferencia = QHBoxLayout()
layout_vegetariano = QHBoxLayout()
layout_diabetico = QHBoxLayout()
layout_categoria_comida = QHBoxLayout()

# Botones de radio para el tiempo
label_tiempo = QLabel('¿Cuánto tiempo tienes?')
layout.addWidget(label_tiempo)
tiempo_opciones = ['Corto', 'Medio', 'Largo']
for i, opcion in enumerate(tiempo_opciones):
    boton = QRadioButton(opcion)
    grupo_tiempo.addButton(boton)
    layout_tiempo.addWidget(boton)
    if i == 0:  # Selecciona el primer botón por defecto
        boton.setChecked(True)
layout.addLayout(layout_tiempo)

# Botones de radio para la preferencia
label_preferencia = QLabel('¿Qué prefieres?')
layout.addWidget(label_preferencia)
preferencia_opciones = ['Saludable', 'Sabrosa']
for i, opcion in enumerate(preferencia_opciones):
    boton = QRadioButton(opcion)
    grupo_preferencia.addButton(boton)
    layout_preferencia.addWidget(boton)
    if i == 0:  # Selecciona el primer botón por defecto
        boton.setChecked(True)
layout.addLayout(layout_preferencia)

# Botones de radio para vegetariano
label_vegetariano = QLabel('¿Eres vegetariano?')
layout.addWidget(label_vegetariano)
vegetariano_opciones = ['Sí', 'No']
for i, opcion in enumerate(vegetariano_opciones):
    boton = QRadioButton(opcion)
    grupo_vegetariano.addButton(boton)
    layout_vegetariano.addWidget(boton)
    if i == 0:  # Selecciona el primer botón por defecto
        boton.setChecked(True)
layout.addLayout(layout_vegetariano)

# Botones de radio para diabético
label_diabetico = QLabel('¿Eres diabético?')
layout.addWidget(label_diabetico)
diabetico_opciones = ['Sí', 'No']
for i, opcion in enumerate(diabetico_opciones):
    boton = QRadioButton(opcion)
    grupo_diabetico.addButton(boton)
    layout_diabetico.addWidget(boton)
    if i == 0:  # Selecciona el primer botón por defecto
        boton.setChecked(True)
layout.addLayout(layout_diabetico)

# Función para crear un botón de radio con imagen
def crear_boton_con_imagen(opcion, grupo, layout, imagen_path, size=(30, 30)):
    boton = QRadioButton(opcion)
    grupo.addButton(boton)
    layout.addWidget(boton)
    
    # Crea un QLabel para mostrar la imagen
    label_imagen = QLabel()
    pixmap = QPixmap(imagen_path)
    # Redimensiona el QPixmap al tamaño deseado
    pixmap = pixmap.scaled(size[0], size[1], Qt.KeepAspectRatio, Qt.SmoothTransformation)
    label_imagen.setPixmap(pixmap)
    layout.addWidget(label_imagen)
    
    return boton

# Botones de radio para categorías de comida con imágenes
label_categoria_comida = QLabel('¿Qué deseas comer?')
layout.addWidget(label_categoria_comida)
categoria_comida_opciones = ['Pizza', 'Bebidas', 'Hamburguesa', 'Postres', 'Ensaladas', 'Sopas', 'Pollo']
imagenes_categorias = ['pizza.png', 'bebida.png', 'hamburguesa.png', 'postres.png', 'ensaladas.png', 'sopas.png', 'pollo.png']

for i, opcion in enumerate(categoria_comida_opciones):
    imagen_path = imagenes_categorias[i]  
    boton = crear_boton_con_imagen(opcion, grupo_categoria_comida, layout_categoria_comida, imagen_path)
    if i == 0:  # Selecciona el primer botón por defecto
        boton.setChecked(True)

layout.addLayout(layout_categoria_comida)


# Botón para obtener la recomendación
boton_obtener = QPushButton("Obtener Recomendación")
boton_obtener.clicked.connect(obtener_recomendacion)
layout.addWidget(boton_obtener)

ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())
