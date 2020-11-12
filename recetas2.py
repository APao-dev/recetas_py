


class MisRecetas ():
     def __init__(self, nombreR, ingredientesR, coccionR, dificultadR):
        self.nombre = nombreR       
        self.ingredientes = ingredientesR
        self.duracion = coccionR
        self.dificultad = dificultadR

     def mostrarReceta(self):
         print(self.nombre + self.ingredientes + self.duracion + self.dificultad)
           

receta1 = MisRecetas(nombreR="PIZZA", ingredientesR="Harina Agua Levadura Sal Aceite Salsa Mozzarella", coccionR="1 hora", dificultadR="Muy baja" ) 
receta2 = MisRecetas(nombreR="FLAN CASERO", ingredientesR="Un litro de leche, una docena de huevos, una taza y media de azucar, esencia de vainilla", coccionR="2 horas", dificultadR="Media" ) 
receta3 = MisRecetas(nombreR="EMPANADAS DE JAMÓN QUESO", ingredientesR="12 Tapas de empanadas, 200 gr de jamón, 250 gr. de queso, huevos duros", coccionR="45 minutos", dificultadR="Muy baja" )

miRecetario = []
miRecetario.append(receta1)
miRecetario.append(receta2)
miRecetario.append(receta3)

numeroReceta = int(input("Si quieres consultar alguna receta, ingresa su Número \n"))
miRecetario[numeroReceta].mostrarReceta()

    
