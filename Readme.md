Instalar homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Instalar python3
brew install python3

Instalar pyenv para gestionar las versiones de python
brew install pyenv

# Crear un entorno virtual de Python en MacOS

Para crear un entorno virtual de Python en MacOS, puedes seguir los siguientes pasos:

1. Abre la Terminal en tu Mac.
2. Navega hasta el directorio donde deseas crear el entorno virtual.
3. Ejecuta el siguiente comando para crear el entorno virtual:

```bash
python3 -m venv {{nombre_del_entorno_virtual}}
```

Reemplaza `{{nombre_del_entorno_virtual}}` con el nombre que desees darle a tu entorno virtual.

4. Una vez que se haya creado el entorno virtual, actívalo ejecutando el siguiente comando:

```bash
source {{nombre_del_entorno_virtual}}/bin/activate
```

5. Ahora estás dentro del entorno virtual de Python. Puedes instalar paquetes y ejecutar tu código Python sin afectar el entorno global de tu sistema.

Recuerda que cuando hayas terminado de trabajar en el entorno virtual, puedes desactivarlo ejecutando el siguiente comando:

```bash
deactivate
```

Esto te sacará del entorno virtual y volverás al entorno global de tu sistema.

¡Y eso es todo! Ahora puedes crear y utilizar entornos virtuales de Python en tu Mac.

```

Esto instalará la última versión de Pillow en tu entorno virtual.

3. Una vez que la instalación se haya completado, puedes verificar si Pillow se instaló correctamente ejecutando el siguiente comando:

```bash
python -c "import PIL; print(PIL.__version__)"
```

Si no se muestra ningún error y se imprime la versión de Pillow, significa que la instalación fue exitosa.

Con respecto a la advertencia sobre la versión de pip, puedes actualizar pip ejecutando el siguiente comando:

```bash
python -m pip install --upgrade pip
```


Explicacion de los metadatos GPS

Ejemplo
```bash
GPS para el archivo EF5E7C7D-BDBD-4778-A0B0-70B0A2327EBC_1_105_c.jpeg
GPS GPSLatitudeRef: N
GPS GPSLatitude: [41, 21, 3437/100]
GPS GPSLongitudeRef: E
GPS GPSLongitude: [2, 5, 5567/100]
GPS GPSAltitudeRef: 0
GPS GPSAltitude: 1844183/32768
GPS GPSSpeedRef: K
GPS GPSSpeed: 0
GPS GPSImgDirectionRef: T
GPS GPSImgDirection: 421925/1343
GPS GPSDestBearingRef: T
GPS GPSDestBearing: 421925/1343
GPS Tag 0x001F: 65
Image GPSInfo: 1960
```
Estos son los metadatos GPS extraídos de un archivo llamado `EF5E7C7D-BDBD-4778-A0B0-70B0A2327EBC_1_105_c.jpeg`. Cada uno de estos metadatos proporciona información sobre la ubicación geográfica y otros detalles relacionados con la imagen. Aquí hay una explicación de algunos de estos metadatos:

1. **GPS GPSLatitudeRef: N**
   - Indica la dirección de latitud, donde "N" representa el hemisferio norte.

2. **GPS GPSLatitude: [41, 21, 3437/100]**
   - Indica la latitud geográfica en grados, minutos y segundos. En este caso, la latitud es aproximadamente 41 grados, 21 minutos y 34.37 segundos.

3. **GPS GPSLongitudeRef: E**
   - Indica la dirección de longitud, donde "E" representa el hemisferio este.

4. **GPS GPSLongitude: [2, 5, 5567/100]**
   - Indica la longitud geográfica en grados, minutos y segundos. En este caso, la longitud es aproximadamente 2 grados, 5 minutos y 55.67 segundos.

5. **GPS GPSAltitudeRef: 0**
   - Indica la referencia de altitud. En este caso, "0" significa que la altitud es medida desde el nivel del mar.

6. **GPS GPSAltitude: 1844183/32768**
   - Indica la altitud en relación con el nivel del mar. El valor 1844183/32768 representa la altitud en una unidad específica.

7. **GPS GPSSpeedRef: K**
   - Indica la referencia de velocidad. En este caso, "K" significa que la velocidad está en kilómetros por hora.

8. **GPS GPSSpeed: 0**
   - Indica la velocidad en kilómetros por hora. El valor "0" podría ser indicativo de que no se ha registrado una velocidad específica.

9. **GPS GPSImgDirectionRef: T**
   - Indica la referencia de dirección de imagen. En este caso, "T" representa la dirección real de la imagen (en sentido horario).

10. **GPS GPSImgDirection: 421925/1343**
    - Indica la dirección de la imagen en grados. El valor "421925/1343" representa una dirección específica de la imagen.

11. **GPS GPSDestBearingRef: T**
    - Indica la referencia de la dirección de destino. En este caso, "T" representa la dirección real del destino (en sentido horario).

12. **GPS GPSDestBearing: 421925/1343**
    - Indica la dirección de destino en grados. El valor "421925/1343" representa una dirección específica del destino.

13. **GPS Tag 0x001F: 65**
    - Este metadato no proporciona información suficiente para determinar su significado sin conocer el contexto.

14. **Image GPSInfo: 1960**
    - Este metadato puede indicar la posición dentro de la imagen donde se almacenan los datos de GPS. El valor "1960" es un índice o desplazamiento dentro de los datos de la imagen.

Estos metadatos proporcionan información detallada sobre la ubicación geográfica y otros aspectos de la imagen que pueden ser útiles para su análisis y visualización en un contexto geoespacial.

Issues:

vas a necesitar:
```bash
brew install libheif
```
Para instalar
```bash
pip3 install pyheif
```

PIL ha sido cambiado por pillow
El error que estás experimentando indica que no se pudo encontrar una versión compatible del paquete PIL (Python Imaging Library) para instalar. Esto puede ocurrir si el paquete no está disponible en los repositorios de Python que estás utilizando.

Sin embargo, PIL ha sido reemplazado por Pillow, una bifurcación compatible y mejorada de PIL. Te recomendaría instalar Pillow en su lugar. Puedes hacerlo siguiendo estos pasos:

1. Asegúrate de estar dentro de tu entorno virtual de Python. Puedes activarlo ejecutando el siguiente comando:

```bash
source {{nombre_del_entorno_virtual}}/bin/activate
```

2. Luego, ejecuta el siguiente comando para instalar Pillow:

```bash
pip install pillow
