#CAPTURA DE PANTALLA (windows API)

**Descripción**

Al pulsar la tecla "Imppnt" captura una imagen de pantalla y la almacena en el portapapeles en formato BITMAP. El script hará todo este proceso y dará como resultado una imagen de la captura de pantalla en formato PNG.

Para esto:

* Se enviara a windows el código de la tecla virtual de "Imppnt".
* Acceder al portapapeles y se obtendrá la dirección de memoria del struct DIB que seguido esta el mapa de bits.
* Bloquear esta dirección para que windows no la reutilice.
* Llenar la cabecera de BITMAP.
* Almacenar las cabeceras y el mapa de bits en un buffer.
* Convertir imagen BITMAP a PNG.
* Crear archivo PNG.
