from base import Student

def print_atributtes(Students_List):
    for Student in Students_List:
        print(f"----------------------------------------------\nName: {Student.getName()}\nApellido:  {Student.getLastname()}\nEdad: {Student.getAge()}\n")
        

class Main():
    def main():
        Students_List=[]
        cant=int(input(f"----------------------------------------------\nIngrese la cantidad de estudiantes: "))
        for i in range(cant):
            name=input(f"----------------------------------------------\nIngrese el nombre del estudiante {i+1}: ")
            lastname=input(f"Ingrese el apellido del estudiante: ")
            age=int(input("Ingrese la edad: "))

            My_Student=Student(name,lastname,age)
            Students_List.append(My_Student)

        print_atributtes(Students_List)

    main()