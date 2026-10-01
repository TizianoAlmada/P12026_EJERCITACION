Personas=[]
while True :
    print("1. Ingresar una persona nueva")
    print("2. Buscar persona por DNI")
    print("3. Buscar persona por nombre")
    print("4. Listar personas y su DNI")
    opcion=int(input("Ingrese la opcion: "))
if opcion==1:
    nombre=input("Ingrese el nombre de la persona")
    dni=int(input("Ingrese el DNI de la persona"))
    Personas[dni]=nombre
elif opcion==2:
    dni_a_buscar=int(input("Ingrese el Dni de la persona"))
    dni_encontrado=0
    for key in Personas.keys():
        if key == dni_a_buscar:
            dni_encontrado=key
    if dni_encontrado==0:
        print("No se encontro la persoona")
    else:
        print(f"Persona con DNI {dni_encontrado}: {Personas[dni_encontrado]}")        
elif opcion==4:
    for key in Personas.keys():
        print(f"{key}: {Personas[key]}")
