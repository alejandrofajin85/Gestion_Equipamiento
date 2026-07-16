# Gestión de Equipamiento

Proyecto final de Programación en Python.

El programa permite administrar el inventario de equipos informáticos de una empresa, controlar su estado actual y consultar el historial de movimientos de cada equipo.

## Funciones principales

El sistema permite:

- Ver todos los equipos registrados.
- Agregar nuevos equipos.
- Generar códigos de inventario automáticamente.
- Buscar equipos por código de inventario.
- Buscar equipos por número de serie.
- Buscar equipos asignados a un usuario.
- Asignar equipos a usuarios.
- Registrar la devolución de equipos.
- Modificar los datos generales de un equipo.
- Cambiar el estado de un equipo.
- Consultar equipos según su estado.
- Ver el historial completo de cada equipo.
- Generar etiquetas con códigos QR.

## Tipos de equipos

El programa permite registrar:

- PC de escritorio.
- Notebook.
- Monitor.
- Impresora.
- Celular.
- TV.

## Códigos de inventario

Los códigos se generan automáticamente.

Para PC de escritorio y notebook:

```text
EQ-0001
EQ-0002
```

Para monitor, impresora, celular y TV:

```text
HW-0001
HW-0002
```

El programa busca el último código utilizado y genera el siguiente.

## Estados disponibles

Los equipos pueden tener los siguientes estados:

- Disponible.
- Asignado.
- Dañado.
- Dado de baja.
- Robado.

La ubicación cambia según el estado:

| Estado | Ubicación |
|---|---|
| Disponible | Depósito |
| Asignado | Usuario asignado |
| Dañado | Reparación |
| Dado de baja | Baja |
| Robado | Baja |

## Historial

Cada equipo guarda un historial de movimientos.

Algunos movimientos posibles son:

- Alta.
- Asignación.
- Devolución.
- Modificación.
- Cambio de estado.
- Baja.

El historial permite conocer los usuarios anteriores que tuvieron asignado el equipo y las fechas de cada movimiento.

## Código QR

El programa permite generar una etiqueta QR para cada equipo.

El código QR contiene únicamente el código de inventario, por ejemplo:

```text
EQ-0001
```

Al leer o ingresar ese código en el programa, se puede consultar la información actual y el historial del equipo.

Las etiquetas se guardan dentro de la carpeta:

```text
etiquetas
```

## Archivos del proyecto

```text
Gestion_Equipamiento
│
├── main.py
├── equipos.py
├── codigos_qr.py
├── equipos.json
├── historial.json
├── requirements.txt
├── README.md
├── .gitignore
└── etiquetas
```

### main.py

Contiene el menú principal y permite acceder a las distintas opciones del sistema.

### equipos.py

Contiene las funciones relacionadas con:

- alta de equipos;
- búsquedas;
- asignaciones;
- devoluciones;
- modificaciones;
- cambios de estado;
- historial;
- lectura y escritura de archivos JSON.

### codigos_qr.py

Contiene las funciones necesarias para generar las etiquetas QR.

### equipos.json

Guarda la información actual de los equipos.

### historial.json

Guarda todos los movimientos realizados sobre los equipos.

## Librerías utilizadas

### Colorama

Se utiliza para mostrar mensajes con colores en la consola.

### Tabulate

Se utiliza para mostrar los equipos y el historial en forma de tabla.

### QRCode

Se utiliza para generar los códigos QR de los equipos.

### Pillow

Es utilizada por QRCode para crear y guardar las imágenes.

### Pyfiglet

Se utiliza para mostrar títulos grandes en el menú y en los diferentes módulos.

## Instalación

Primero se debe crear un entorno virtual:

```powershell
python -m venv .venv
```

Activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las librerías:

```powershell
pip install -r requirements.txt
```

## Ejecución

Para iniciar el programa:

```powershell
python main.py
```

## Datos de ejemplo

El proyecto incluye:

- 15 PC o notebooks.
- 10 equipos de hardware.
- Equipos disponibles.
- Equipos asignados.
- Equipos dañados.
- Equipos dados de baja.
- Equipos robados.
- Historiales de asignaciones y devoluciones.

Estos datos permiten probar las funciones del programa sin tener que cargar todo desde cero.

## Manejo de errores

El programa utiliza validaciones y bloques `try` y `except` para evitar cierres inesperados.

Se controlan situaciones como:

- archivos inexistentes;
- archivos JSON dañados;
- errores al guardar información;
- códigos inexistentes;
- números de serie repetidos;
- opciones inválidas;
- asignación de equipos no disponibles;
- devolución de equipos que no están asignados.

## Autor

Alejandro Fajin