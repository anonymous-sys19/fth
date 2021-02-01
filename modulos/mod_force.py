import time
import os
import random

def colores ():
    listas = ['\033[1;36m','\033[1;31m','\033[1;34m','\033[1;30m','\033[1;37m','\033[1;35m','\033[1;32m','\033[1;33m']
    indice=random.randrange(len(listas))
    lista=listas[indice]
    print(lista)

# ----=cls,clear=---
def clear_cleanner():
    os.system('clear')
#-----KeyboardInterrupt----
#     -----not_start-----

#hola

def menu():
    colores()
    print('\n                   Brute_Forze__ftp_Forze\n\n')
    colores()
    time.sleep(0.50)
    salir = (os.system('exit'))
    colores()
    opciones = (''' 
    [ -01- ] Scann_Puertos
    [ -02- ] Brute_ftp
    [ -03- ] Brute_ssh
    [ -04- ] mysql_force
    [ -00- ] volver al menu
    [ -99- ] salir \n\n\n''')
    print(opciones)
#>----ffor opcion---<

def link():
    colores()
    menu()
    opcion = int(input('ingresa '))
    colores()
    if opcion == 1 :
        scan_nmap = input('Ingresa ip a scanear $ ')
        os.system('nmap ' + scan_nmap)
        menu()
        link()
    elif opcion == 2 :
        print(' Espere ingresando al systema ftp modulo\n')
        scaneo_nmap = input('Ingresa la ip para scannear ')
        if scaneo_nmap == scaneo_nmap :
            print('\n\n Espere Ejecutando la herramienta \n\n')
            print('\n                  Brute_Forze__ftp_Forze\n\n')
            time.sleep(0.50)
            os.system('nmap ' + scaneo_nmap )
            print('\n\n             Scaneo teminado\n')

            print('\n Quiere hacer el Brute_Forze__ftp_Forze [y/n]\n\n')
            nameif = input('$ ')
            if nameif == 'y' :
                print('\n En breve se ejecutara Brute_Forze__ftp_Forze \n')
                time.sleep(2)
                os.system('bash modsh/ftp_brute.sh')
            elif nameif == n :
                print (' Perfecto vuelve pronto ... ')
                link()
    elif opcion == 3 :
	    print ('Creando orden ... \n' )
	    time.sleep(2)
	    os.system('bash modsh/ssh_brute.sh')
    elif opcion == 4 :
        os.system('clear')
        os.system('bash modsh/mysql_force.sh')
        os.system('clear')
        os.system('bash modulos/modsh/mysql_force.sh')
    elif opcion == 99 :
        os.system ('exit')
    elif opcion == 00 :
        os.system('clear')
        os.system('python3 fth.py')
    elif opcion != opcion :
        print('error')
        link()
    else :
        print('error')
        os.system('clear')
        link()
link()