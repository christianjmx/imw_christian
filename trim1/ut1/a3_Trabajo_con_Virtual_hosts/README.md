# Trabajo con Virtual Hosts - Christian Moreno #

## Sitio Web 1 ##

- Creamos el nuevo sitio web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/1.png)

- Configuramos el sitio web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/2.png)

- Creamos el enlace simbólico.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/3.png)

- Creamos la ruta y el archivo index donde estará la página del sitio web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/4.png)

- Añadimos el host en la máquina remota.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/5.png)

- Reiniciamos el nginx.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/6.png)

- Comprobamos que la página básica funciona.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/7.png)

- Descargamos la imagen en la máquina remota.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/8.png)

- La descargamos al servidor mediante el comando SCP.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/9.png)

- Comprobamos que la imagen se descargó en el servidor y la movemos a la carpeta donde está el index de la página.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/10.png)

- Modificamos el index de la página web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/11.png)

- Comprobamos que la página funciona y muestra la imagen.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/12.png)

- En la misma root donde se guarda la página web del servidor, creamos una carpeta que se llame 'mec' y dentro otro index.html .

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/prueba%202/1.png)

- Escribimos algo en el index y comprobamos que la ruta está funcionando.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/prueba%202/2.png)

- Modificamos el fichero index para crear el link que nos lleva a la página deseada.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/prueba%202/3.png)

- Comprobamos que se muestra el link y que funciona.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/prueba%202/4.png)

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%201/prueba%202/5.png)

## Sitio Web 2 ##

- Creamos un nuevo sitio web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%202/1.png)

- Modificamos el archivo del servidor web para que escuche por el puerto 9000 y los demás parámetros.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%202/2.png)

- Creamos el enlace simbólico del sitio web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%202/3.png)

- Añadimos el host en la máquina remota.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%202/4.png)

- Comprobamos que funciona la página web con el contenido que nos pedía.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%202/5.png)

## Sitio Web 3 ##

- Creamos un nuevo sitio web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%203/1.png)

- Creamos el fichero de configuración básico para la primera comprobación de que todo funciona.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%203/2.png)

- Creamos el enlace simbólico.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%203/3.png)

- Creamos el directorio de la página web y el index.html

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%203/4.png)

- Añadimos el nuevo host a la máquina remota.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%203/5.png)

- Comprobamos que la conficguración básica funciona.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%203/6.png)

- Encriptamos una contraseña con 'perl' y creamo el archivo .htpasswd, que guardará el usuario y la contraseña para acceder a la web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%203/7.png)

- Modificamos el fichero de configuración del sitio web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%203/8.png)

- Recargamos el nginx y comprobamos que nos pide usuario/contraseña para cceder a la web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%203/9.png)ç

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a3_Trabajo_con_Virtual_hosts/web%203/10.png)
























