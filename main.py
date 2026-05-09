from utils.terminal import limpiar
from frontend.libro import listarLibros

def menu():
    while True:
        limpiar()
        print("==========================================")
        print("       SISTEMA DE GESTIÓN DE LIBROS       ")
        print("==========================================")
        print("1. Listar Libros")
        print("2. Agregar Libro (Próximamente)")
        print("3. Salir")
        print("==========================================")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            listarLibros()
        elif opcion == "2":
            input("\nFunción no implementada aún. Presione Enter...")
        elif opcion == "3":
            print("\n¡Hasta luego!")
            break
        else:
            input("\nOpción no válida. Presione Enter...")

if __name__ == "__main__":
    menu()
