#CAPTURA DE PANTALLA (WINDOWS API)

**Descripcion**

Al pulsar la tecla "Imppnt" captura una imagen de pantalla y la almacena en el portapapeles en formato BITMAP. 
El script hara todo este proceso y dara como resultado la una imagen de la captura de pantalla en formato PNG.

Para esto:
* Se enviara a windows el codigo de la tecla virtual de "Imppnt". 
* Acceder al portapapeles y se obtendra la direccion de memoria del struct DIB que seguido esta el mapa de bits.
* Bloquear esta direccion para que windows no la reutilize.
* Llenar la cabecera de BITMAP
* Almacenar las cabeceras y el mapa de bits en un buffer
* Convertir imagen BITMAP a PNG
