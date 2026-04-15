import os
import shutil
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
    return tipos.get(extension.lower(), 'Otros') #.get(key, default)

def organizar_carpeta(ruta) :
    archivos = os.listdir(ruta) #os.listdir() lista el directorio y hace lista de lo que se encuentra dentro de la ruta
    
    for archivo in archivos : # Recorremos los archivos ya obtenidos con el método os.listdir()
        
        ruta_completa = os.path.join(ruta, archivo) #os.path.join(), concatena y da la ruta unida por los 2 parámetros, el segundo son ilimitados
        
        if not os.path.isfile(ruta_completa) : #os.path.isfile() Analiza si es un archivo lo que está dentro de la ruta
            continue  #Si dentro de la ruta recorre algo que no sea un archivo, solo continua
            
        
        extension = os.path.splitext(archivo)[1] #Separa la extension en 2, en este caso el nombre del archivo ("archivo") y la extension (".xxx")
        tipo = obtener_tipo(extension)
        
        carpeta_destino = os.path.join(ruta, tipo) #Concatenamos la ruta con el tipo para asi generar la carpeta que se creará
        os.makedirs(carpeta_destino, exist_ok=True) #Crea la carpeta ¡IMPORTANTE! Es .makedirs(), con mkdir() saltaria error ya que solo crea una carpeta
        
        destino_final = os.path.join(carpeta_destino, archivo)
        shutil.move(ruta_completa, destino_final)
        print(f"✅ {archivo} → {tipo}/")

# Ruta de prueba
ruta_test = os.path.join(os.path.dirname(__file__), 'test')
organizar_carpeta(ruta_test)
