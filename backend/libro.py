from backend.hoja_libro import obtenerHojaDeLibros

def obtenerLibros():
    hoja = obtenerHojaDeLibros()
    libros = []
    # Iterar sobre las filas saltando la cabecera
    for fila in hoja.iter_rows(min_row=2, values_only=True):
        if fila[0] is not None:  # Verificar que el ID no esté vacío
            libros.append({
                "id": fila[0],
                "titulo": fila[1],
                "autor": fila[2],
                "descripcion": fila[3]
            })
    return libros
