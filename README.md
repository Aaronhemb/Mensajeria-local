# Mensajeria-local


Antes de iniciar deben de cambiar la IP al cliente Host='La ip del segmento de su equipo' el puerto no es necesario que lo cambien a menos que quieran asignar uno fijo.

El Servidor en automatico toma la Ip del equipo por lo que no es necesario cambiarla.

![image](https://user-images.githubusercontent.com/93096758/222274050-2450da2f-b736-4b2d-b822-ebe9346bf9aa.png)


Cuando se realizan las puebas de servidor y del cliente debemos de ejecutar desde la consola donde se encuentra el cliente y servidor.

![image](https://user-images.githubusercontent.com/93096758/222273358-d56a2682-ee8a-4b23-baed-d640b5b7c47d.png)

Cuando iniciamos el cliente se abre la consola de CMD ya que es la forma como se comunica de forma local.

![image](https://user-images.githubusercontent.com/93096758/222274216-28131c31-18ee-4ba0-81b6-44591a3024f8.png)

Pero esta no realizara ninguna funcion solo quedara activa en lo que espera mensajes de servidor.

Al iniciar el servidor de la misma forma como lo hicimos con el cliente nos mostrara la ventana de CMD pero con diferencia

Nos trae la informacion de los clietes que estan activos , y nos mostrara el input donde escribir el mensaje que queremos enviar


![image](https://user-images.githubusercontent.com/93096758/222274487-19f53857-fa09-4255-a9f2-98eb4e26380d.png)

Escribimos nuestro mensaje y damos un enter .Nos solicitara el numero de la Ip que tienen el cliente que va a recibir el mensaje (la ip de la otra PC)

![image](https://user-images.githubusercontent.com/93096758/222274745-fac1223d-ec97-4677-8827-c22e0c6cc1eb.png)


Una vez coloquemos la Ip del equipo , daremos enter y en automatico enviara el mensaje al cliente

![image](https://user-images.githubusercontent.com/93096758/222274981-4dc374a6-66f5-46b5-94a2-f498c7c2e509.png)


El cliente recibira este mensaje en forma de alerta.



![image](https://user-images.githubusercontent.com/93096758/222275086-fbedf895-df05-4da9-a8d0-8cd41bd576d3.png)


El cliente no puede responder , bueno es lo que me solitiron . pero si se puede (si requieren modificar el codigo para que permita responder de la misma forma)

Y por ultimo para resolver el tema de que se quedaba abierta la pantalla del cliente, se soluciono de la sig manera.  un archivo VbS que se ejecute al arranque del 
Equipo , para que inicie el cliente pero lo oculte al mismo tiempo .


![image](https://user-images.githubusercontent.com/93096758/222275818-ccd071a6-3f57-406d-877a-83a14d21d449.png)


Para convertir python a .exe promero instalar pip install pip install pyinstaller una vez instalado usen el sig codigo en la ruta de la carpeta donde se encuentra el 
archivo python y desde consola inicien installer.

![image](https://user-images.githubusercontent.com/93096758/222276444-a6992369-3b1f-4214-9a01-95ba9ee5f907.png)


![image](https://user-images.githubusercontent.com/93096758/222276536-c91b5374-a157-4788-953f-41053eb8d51e.png)


una vez lo convierta en .exe lo pueden ejecutar desde cualquier pc el cliente  y usen el VBS para ocultar del cliente.

![image](https://user-images.githubusercontent.com/93096758/222276811-8d694bfa-2037-453e-b2ab-96f2d4525eba.png)


el archivo VBS deben de comificar la ruta donde se enceuntra el archivo Cliente para que no lo muestre en pantalla y listo . espero les sirva













