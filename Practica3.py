print("---------------------------------------------")
print("-------------PRACTICA SEMANA 3---------------")
# Declaración de variables
nombre = input("Ingrese su nombre completo: ")
grupo = input("Ingrese su grupo de clases: ")
carnet = int(input("Ingrese su numero de carnet: "))
exa1 = float(input("Ingrese su nota de primer examen: "))
exa2 = float(input("Ingrese su nota de segundo examen: "))
exa3 = float(input("Ingrese su nota de tercer examen: "))
ejercicios = float(input("Ingrese su nota total de ejercicios: "))
proyecto = float(input("Ingrese su nota del proyecto final: "))
# procesos
prome1 = (exa1 * 0.15) + (exa2 * 0.15) + (exa3 * 0.15)
prome2 = ejercicios * 0.25
prome3 = proyecto * 0.30
promedio = prome1 + prome2 + prome3
# salida 
print("-------------DATOS FINALES----------------")
print("Nombre completo del estudiante: "+nombre)
print("Grupo al que pertenece el estudiante: "+grupo)
print("Numero de carnet del estudiante: "+str(carnet))
print("Promedio final del estudiante es: "+str(promedio))

