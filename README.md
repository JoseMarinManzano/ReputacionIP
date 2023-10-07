# ReputacionIP
Aquí vamos a encontrar un pequeño script escrito en Python que mediante la API de virustotal, vamos a comprobar la reputación de una IP, si tiene votos negativos, el ASN y el proveedor de la IP.
Antes, debemos tener un fichero con todas las IP's que queremos comprobar. El resultado nos lo saca en un CSV para su porterior tratamiendo.

![image](https://github.com/JoseMarinManzano/JoseMarinManzano/assets/147179609/7a8455bf-1771-45a5-a8a2-ff0f6f438f59)

Requisitos previos:

  1. Debemos tener en el mismo directorio un fichero llamado listado_ip.csv con las IP's que queremos escanear.
  2. Debemos introducir la API KEY de VIRUSTOTAL en la variable api_key.
  3. Una vez acabado el proceso, nos devolverá un fichero CSV llamado output.csv con toda la información obtenida
  4. Además, lo pinta en pantalla.
     
