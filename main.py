"""Menú principal del sistema de gestión de equipamiento."""

import os

from colorama import Fore, init
from pyfiglet import figlet_format

from codigos_qr import solicitar_codigo_para_qr
from equipos import (
    agregar_equipo,
    asignar_equipo,
    buscar_por_codigo,
    consultar_equipo_por_codigo,
    consultar_equipo_por_serie,
    consultar_equipos_por_usuario,
    dar_de_baja,
    devolver_equipo,
    marcar_como_daniado,
    marcar_como_disponible,
    marcar_como_robado,
    modificar_equipo,
    mostrar_equipos_por_estado,
    mostrar_todos_los_equipos
)


# Permite que los colores vuelvan a su estado normal después de usarlos.
init(autoreset=True)


def limpiar_pantalla():
    """Limpia la consola de Windows."""
    os.system("cls")


def pausar():
    """Espera que el usuario presione Enter para continuar."""
    input(
        Fore.YELLOW
        + "\nPresione Enter para continuar..."
    )


def mostrar_titulo(texto):
    """Muestra un título dentro de una sección del programa.

    Args:
        texto (str): Texto que se quiere mostrar como título.
    """
    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.CYAN + texto.upper())
    print(Fore.CYAN + "=" * 60)


def mostrar_encabezado():
    """Muestra el nombre principal del programa."""
    titulo = figlet_format(
        "Gestion de Equipos",
        font="small"
    )

    print(Fore.CYAN + titulo)
    print(
        Fore.WHITE
        + "Sistema de inventario y seguimiento de equipamiento"
    )


def mostrar_menu_principal():
    """Muestra las opciones principales del sistema."""
    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.CYAN + "MENÚ PRINCIPAL")
    print(Fore.CYAN + "=" * 60)

    print("1. Ver inventario")
    print("2. Agregar equipo")
    print("3. Buscar equipo")
    print("4. Asignar equipo")
    print("5. Devolver equipo")
    print("6. Modificar equipo")
    print("7. Cambiar estado")
    print("8. Ver equipos por estado")
    print("9. Generar etiqueta QR")
    print("10. Salir")


def mostrar_menu_busqueda():
    """Muestra las opciones disponibles para buscar equipos."""
    print("\n1. Buscar por código")
    print("2. Buscar por número de serie")
    print("3. Buscar por usuario")
    print("4. Volver al menú principal")


def ejecutar_busqueda():
    """Ejecuta el menú de búsqueda de equipos."""
    while True:
        limpiar_pantalla()
        mostrar_titulo("Buscar equipo")
        mostrar_menu_busqueda()

        opcion = input(
            "\nSeleccione una opción: "
        ).strip()

        # Cada opción utiliza un dato distinto para buscar.
        if opcion == "1":
            limpiar_pantalla()
            mostrar_titulo("Buscar por código")
            consultar_equipo_por_codigo()
            pausar()

        elif opcion == "2":
            limpiar_pantalla()
            mostrar_titulo("Buscar por número de serie")
            consultar_equipo_por_serie()
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            mostrar_titulo("Buscar por usuario")
            consultar_equipos_por_usuario()
            pausar()

        elif opcion == "4":
            break

        else:
            print(
                Fore.RED
                + "\nLa opción ingresada no es válida."
            )
            pausar()


def mostrar_menu_estados():
    """Muestra las opciones para cambiar el estado de un equipo."""
    print("\n1. Marcar como dañado")
    print("2. Marcar como disponible")
    print("3. Marcar como robado")
    print("4. Dar de baja")
    print("5. Volver al menú principal")


def ejecutar_cambio_estado():
    """Ejecuta el menú para cambiar el estado de un equipo."""
    while True:
        limpiar_pantalla()
        mostrar_titulo("Cambiar estado")
        mostrar_menu_estados()

        opcion = input(
            "\nSeleccione una opción: "
        ).strip()

        if opcion == "1":
            limpiar_pantalla()
            mostrar_titulo("Equipo dañado")
            marcar_como_daniado()
            pausar()

        elif opcion == "2":
            limpiar_pantalla()
            mostrar_titulo("Equipo disponible")
            marcar_como_disponible()
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            mostrar_titulo("Equipo robado")
            marcar_como_robado()
            pausar()

        elif opcion == "4":
            limpiar_pantalla()
            mostrar_titulo("Dar de baja")
            dar_de_baja()
            pausar()

        elif opcion == "5":
            break

        else:
            print(
                Fore.RED
                + "\nLa opción ingresada no es válida."
            )
            pausar()


def mostrar_menu_listados():
    """Muestra los estados disponibles para consultar."""
    print("\n1. Disponibles")
    print("2. Asignados")
    print("3. Dañados")
    print("4. Dados de baja")
    print("5. Robados")
    print("6. Volver al menú principal")


def ejecutar_listados():
    """Muestra los equipos filtrados por estado."""
    while True:
        limpiar_pantalla()
        mostrar_titulo("Equipos por estado")
        mostrar_menu_listados()

        opcion = input(
            "\nSeleccione una opción: "
        ).strip()

        if opcion == "1":
            limpiar_pantalla()
            mostrar_equipos_por_estado("Disponible")
            pausar()

        elif opcion == "2":
            limpiar_pantalla()
            mostrar_equipos_por_estado("Asignado")
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            mostrar_equipos_por_estado("Dañado")
            pausar()

        elif opcion == "4":
            limpiar_pantalla()
            mostrar_equipos_por_estado("Dado de baja")
            pausar()

        elif opcion == "5":
            limpiar_pantalla()
            mostrar_equipos_por_estado("Robado")
            pausar()

        elif opcion == "6":
            break

        else:
            print(
                Fore.RED
                + "\nLa opción ingresada no es válida."
            )
            pausar()


def ejecutar_programa():
    """Ejecuta el programa hasta que el usuario elija salir."""
    while True:
        limpiar_pantalla()
        mostrar_encabezado()
        mostrar_menu_principal()

        opcion = input(
            "\nSeleccione una opción: "
        ).strip()

        # Cada opción llama a una función o a un submenú.
        if opcion == "1":
            limpiar_pantalla()
            mostrar_titulo("Inventario")
            mostrar_todos_los_equipos()
            pausar()

        elif opcion == "2":
            limpiar_pantalla()
            mostrar_titulo("Agregar equipo")
            agregar_equipo()
            pausar()

        elif opcion == "3":
            ejecutar_busqueda()

        elif opcion == "4":
            limpiar_pantalla()
            mostrar_titulo("Asignar equipo")
            asignar_equipo()
            pausar()

        elif opcion == "5":
            limpiar_pantalla()
            mostrar_titulo("Devolver equipo")
            devolver_equipo()
            pausar()

        elif opcion == "6":
            limpiar_pantalla()
            mostrar_titulo("Modificar equipo")
            modificar_equipo()
            pausar()

        elif opcion == "7":
            ejecutar_cambio_estado()

        elif opcion == "8":
            ejecutar_listados()

        elif opcion == "9":
            limpiar_pantalla()
            mostrar_titulo("Generar etiqueta QR")
            solicitar_codigo_para_qr(buscar_por_codigo)
            pausar()

        elif opcion == "10":
            print(
                Fore.GREEN
                + "\nPrograma finalizado."
            )
            break

        else:
            print(
                Fore.RED
                + "\nLa opción ingresada no es válida."
            )
            pausar()


# Esta condición evita que el programa se ejecute al importar el archivo.
if __name__ == "__main__":
    ejecutar_programa()