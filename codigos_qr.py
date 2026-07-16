"""Funciones para generar etiquetas con códigos QR."""

import os

import qrcode


CARPETA_ETIQUETAS = "etiquetas"


def generar_etiqueta_qr(codigo):
    """Genera una imagen QR con el código de inventario.

    Args:
        codigo (str): Código de inventario que se guardará en el QR.

    Returns:
        str: Ruta del archivo generado.
        None: Si ocurrió un error.
    """
    try:
        if not os.path.exists(CARPETA_ETIQUETAS):
            os.makedirs(CARPETA_ETIQUETAS)

        nombre_archivo = f"{codigo.upper()}.png"
        ruta_archivo = os.path.join(
            CARPETA_ETIQUETAS,
            nombre_archivo
        )

        imagen_qr = qrcode.make(codigo.upper())
        imagen_qr.save(ruta_archivo)

        return ruta_archivo

    except OSError:
        print("No se pudo crear o guardar la etiqueta QR.")
        return None


def solicitar_codigo_para_qr(buscar_equipo):
    """Solicita un código y genera el QR si el equipo existe.

    Args:
        buscar_equipo (function): Función utilizada para buscar el equipo.
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
            "Puede abrir la imagen e imprimirla desde Windows."
        )