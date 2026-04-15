import os

#os.path.expanduser detecta automaticamente el usuario sin importar el pc donde esté "~"
ruta = os.path.expanduser("~/Downloads")

def obtener_tipo(extension) :
    tipos = {
        '.pdf' : 'PDFs',
        '.jpg' : 'Imagenes',
        '.jpeg' : 'Imagenes',
        '.xlsx' : 'Excel',
        '.txt' : 'Textos',
        '.docx' : 'Word',
    }
    return tipos.get(extension.lower(), 'Otros')