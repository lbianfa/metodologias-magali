from backend.excel import obtenerLibro

libro = obtenerLibro()
titulo_hoja = "libros"

def inicializarHoja():
    hoja = libro.create_sheet(title=titulo_hoja)
    
    hoja.column_dimensions['A'].width = 10
    hoja.column_dimensions['B'].width = 30
    hoja.column_dimensions['C'].width = 25
    hoja.column_dimensions['D'].width = 50
    
    cabeceras = ("ID", "Título", "Autor", "Descripción")
    
    hoja.append(cabeceras)
    
    return hoja

def obtenerHojaDeLibros():
    if titulo_hoja in libro.sheetnames:
        return libro[titulo_hoja]
    else:
        return inicializarHoja()
