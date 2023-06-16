from cosas import *

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)

    print("-----------Herencia------------")

    al1 = Alumno("Jose", 19, "2355332", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("-----------Herencia Profe------------")
    profe1 = Profesor("Jesus", 30 + 16, 363728, "Ingenieria de Software")
    print(profe1)
    profe1.dormir()

    print("-------Herencia Ayudante Profe--------")
    ayudante = AyudanteProfesor("Adrian", 20, "43322", "ICO", 23223, "Ing. de Software", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("P.O.O")
    print(ayudante)


main()
