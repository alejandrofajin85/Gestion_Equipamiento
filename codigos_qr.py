"""Funciones para generar etiquetas QR de los equipos."""

import os

import qrcode


# Carpeta donde se guardan las imágenes generadas.
CARPETA_ETIQUETAS = "etiquetas"


def generar_etiqueta_qr(codigo):
    """Genera una imagen QR con el código de inventario.

    Args:
        codigo (str): Código que se guardará dentro del QR.

    Returns:
        str: Ruta donde se guardó la imagen.
        None: Si ocurrió un error.
    """
    try:
        # Si la carpeta no existe, se crea antes de guardar la imagen.
        if not os.path.exists(CARPETA_ETIQUETAS):
            os.makedirs(CARPETA_ETIQUETAS)

        nombre_archivo = f"{codigo.upper()}.png"

        ruta_archivo = os.path.join(
            CARPETA_ETIQUETAS,
            nombre_archivo
        )

        # El QR guarda solo el código.
        # El resto de la información queda en los archivos JSON.
        imagen_qr = qrcode.make(codigo.upper())
        imagen_qr.save(ruta_archivo)

        return ruta_archivo

    except OSError:
        print("No se pudo crear o guardar la etiqueta QR.")
        return None


def solicitar_codigo_para_qr(buscar_equipo):
    """Solicita un código y genera el QR si el equipo existe.

    Args:
        buscar_equipo (function): Función usada para buscar el equipo.
    """
    codigo = input(
        "Ingrese el código de inventario: "
    ).strip()

    if codigo == "":
        print("Debe ingresar un código.")
        return

    equipo = buscar_equipo(codigo)

    if equipo is None:
        print("No se encontró un equipo con ese código.")
        return

    ruta_archivo = generar_etiqueta_qr(
        equipo["codigo"]
    )

    if ruta_archivo is not None:
        print("\nLa etiqueta QR fue generada correctamente.")
        print(f"Archivo guardado en: {ruta_archivo}")
        print(
            "La imagen puede abrirse e imprimirse desde Windows."
        )