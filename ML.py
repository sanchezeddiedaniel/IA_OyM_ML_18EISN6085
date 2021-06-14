# THIS IS THE REALIZATION OF A PROGRAM BASED ON MACHINE LEARNING, SUPERVISED LEARNING BY APPLYING THE SKLEARN LIBRARY.
# WHICH DETERMINES BY AN ENTRY OF THE CHARACTERISTICS PRINT THE ANIMAL THAT IT IS. 
# WHETHER IT IS A PIGEON, PENGUIN, COW OR MONKEY.

# REALIZAR UN PROGRAMA BASADO EN MACHINE LEARNING CON
# APRENDIZAJE SUPERVISADO CON LA LIBRERÍA SKLEARN,
# QUE PUEDA DETERMINAR MEDIANTE UNA ENTRADA CUAL DE
# LOS SIGUIENTES ANIMALES ES EL IDENTIFICADO:
# PALOMA, PINGÜINO, VACA, MONO.

#LIBRERIA SKLEARN CON ENTRENAMIENTO DE ARBOLES DE DECISION
from sklearn import tree
#Libreria OS para poder limpiar mi pantalla y usar comandos del sistema.
import os

#ML = MACHINE LEARNING - APRENDIZAJE AUTOMATICO
#INTRODUCIMOS LOS DATOS EXISTENTES DE NUESTRA ML
CAR = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20]]

#RESULTADOS DE LOS DATOS OBTENIDOS PARA CREAR ML
ANIMALES = [["VACA"],["MONO"],["PINGUINO"],["MONO"],["VACA"],["PALOMA"],["PINGUINO"],["PALOMA"],["MONO"],["PALOMA"],["MONO"],["PINGUINO"],["PALOMA"],["VACA"],["PINGUINO"],["PALOMA"],["VACA"],["MONO"],["PINGUINO"],["VACA"]]

#ARBOL DE DECISION
arbol = tree.DecisionTreeClassifier()
arbol = arbol.fit(CAR,ANIMALES)

#Metodo para la entrada de datos
def entrada():
    #Encabezado con las caracteristicas...
    print("="*140)
    print("\t","\t", "\t", "\t", "Eddie Sanchez", "\t", "\t", "18-EISN-6-085", "\t", "\t", "Ingrese Solo Numeros")
    print("="*140)
    print("1. Hocico", "\t", "\t", "2. Primates", "\t", "\t", "\t", "3. Nadadores", "\t", "\t", "4. SEMEJANTES A HUMANOS", "\t", "5. Pasto", "\t")
    print("6. Vuelan", "\t", "\t", "7. Nieve ", "\t", "\t", "\t", "8. Granivoras", "\t", "\t", "9. Pulgares", "\t", "\t",  "\t", "10. Nidos")
    print("11. Trepan", "\t", "\t", "12. Bucean", "\t", "\t", "\t", "13. Mensajeras", "\t", "14. Cuernos", "\t", "\t", "\t", "15. Hielo")
    print("16. Cuello Robusto", "\t", "17. Peso de hasta 1,000KG", "\t", "18. Dedos", "\t", "\t", "19. Comen del Océano", "\t", "\t", "20. Altura de hasta 1.30M")
    print("="*140)
#INPUT DE LOS DATOS A ANALIZAR
    try:
        SEL = int(input("Ingrese una caracteristica del animal: "))
        #QAE = QUE ANIMAL ES
        if SEL > 20:
            print("No selecciono ninguna caracteristica.")
            print("Vuelva Pronto...")
        elif SEL < 1:
            print("No selecciono ninguna caracteristica.")
            print("Vuelva Pronto...")
        else:    
            QAE = arbol.predict([[SEL]])
            #imprimimos el resultado
            print(QAE)
            
    except:
        os.system ("cls")
        #Si el OS es Unix/Linux/MacOS/BSD cambiar "cls" por "clear"
        print("Error de Entrada, Ingrese Solo Numeros")      
        return entrada()
entrada()
