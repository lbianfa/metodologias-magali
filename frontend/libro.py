from backend.libro import obtenerLibros
from utils.terminal import limpiar
from tabulate import tabulate

def listarLibros():
    limpiar()
    print("==================================================")
    print("               LISTA DE LIBROS                    ")
    print("==================================================")
    
    libros = obtenerLibros()
    
    if not libros:
        print("\nNo hay libros registrados.")
    else:
        # Usando tabulate para presentar los datos
        tabla = [[l['id'], l['titulo'], l['autor']] for l in libros]
        print(tabulate(tabla, headers=["ID", "Título", "Autor"], tablefmt="grid"))
    
    print("\n==================================================")
    input("Presione Enter para volver al menú...")
