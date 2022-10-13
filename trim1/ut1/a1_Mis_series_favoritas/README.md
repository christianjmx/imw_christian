# Mis series favoritas - Christian Moreno #
## Instalación de nginx ##

- Instalamos el nginx y verificamos que esté activo.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/1.png)

## Configuración del nginx ##

- Creamos el nuevo archivo de configuración del sitio web con el nombre adecuado.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/2.png)

- El archivo de configuración debe quedar así.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/3.png)

- Creamos el enlace simbólico.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/4.png)

- Creamos el fichero que va ha contener la página web en el sitio especificado.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/5.png)

- Escribimos algo en el archivo que contiene la página web para comprobar su correcto funcionamiento.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/6.png)

- Añadimos el host en la máquina con la que os estamos conectando por ssh para que funcione la web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/7.png)

- Comprobamos que la página web funciona en el espácio que hemos creado.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/8.png)

## Creación de la página web ##

- Descargamos las imágenes de las portadas en la máquina con la que estamos conectados por ssh y las descargamos al servidor a un directorio
  que tengamos permisos mediante el comando "scp" (Hacemos eso con todas las portadas).
  
![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/9.png)

- Movemos las imagenes al directorio donde está la página web.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/10.png)

- Creamos el link con la portada en la página web, tiene que quedar así:

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/11.png)

- Repetimos el proceso con todas las demás portadas.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/12.png)

- Comprobamos que haciendo 'click' en la portada nos lleva a la respectiva página en IMDB.

![image](https://github.com/christianjmx/imw_christian/blob/main/trim1/ut1/a1_Mis_series_favoritas/img/13.png)



























