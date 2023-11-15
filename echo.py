#Incluimos las librerías
import socket
import sys
#Creamos el socket de comunicación
try:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
 print ('Fallo al crear socket')
 sys.exit()
print ('Socket Creado')
#Creamos las variables para comunicarnos
IP = '192.168.2.117'
puerto = 80
#Intentamos iniciar la comunicación
try:
 s.connect((IP,puerto))
except socket.error as e:
 print ('Fallo al conectar')
 s.close()
 sys.exit()
print ('Conectado')
#Variable para mantener el bucle while
Salida = True
#Bucle while sale cuando se introduce por teclado Adios
while Salida:
 #Solicita ingresar un mensaje para enviar
 print ('Introduzca mensaje')
 msg = input()
 #Comprueba si el mensaje es Adios
 if msg=='Adios':
 #Si lo es configura la salida del bucle
  Salida = False
 #Envía el mensaje
 try:
 #Codifica antes de enviar
  s.sendall(msg.encode())
 except socket.error as e:
  print ('error al enviar el mensaje')
  s.close()
  sys.exit()
 print('Mensaje enviado exitosamente')
 #Recibe la respuesta
 respuesta = s.recv(1024)
 print (respuesta.decode())
#Finaliza el bucle, cierra los sockets y cierra el programa
s.close()
print ('Socket cerrado. Saliendo...')
sys.exit()
