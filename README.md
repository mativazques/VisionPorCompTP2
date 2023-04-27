# Trabajo Práctico Nro. 2

## Consigna: 
Teniendo en cuenta que:
- Una transformación afín se representa con una matriz de 2 × 3.
- Tiene 6 grados de libertad y puede ser recuperada con 3 puntos.

Usando como base el programa escrito en la práctica 1, se pide: 

- Crear un programa que permita seleccionar con el ratón 3 puntos de una primera imagen.
- Luego crear un método que compute una transformación afín entre las esquinas de
una segunda imagen y los 3 puntos seleccionados.
- Por último aplicar esta transformación sobre la segunda imagen, e incrustarla en la
primera imagen.

Ayuda: 

```sh
  cv2.getAffineTransform
  ```
```sh
  cv2.warpAffine
  ```

Para correr el programa colocar en la consola:
```sh
  python3 tp2.py
  ```

Para salir del programa presione "Q".

## Desarrollo

Se utilizará como imagen base:

![Imagen destino](FuenteSRC.jpg)

La imagen que se transformará es: 

![Imagen fuente](FuenteSRC.png)

Se crea un fondo con el fondo negro que se combinará con la imagen transformada, de otra forma se superpondrían: 

![Imagen fuente](back.jpg)

La imagen fuente transformada es: 

![Imagen fuente](front.jpg)

Finalmente, a continuación se observa el resultado de la aplicación de la transformada: 

![Resultado](resultado_tp2.jpg)

