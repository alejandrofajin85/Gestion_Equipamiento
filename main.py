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


init(autoreset=True)


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def mostrar_titulo(texto):
    """Muestra un título grande para identificar el módulo.

    Args:
        texto (str): Texto que se desea mostrar.
    """
    print(Fore.CYAN + figlet_format(texto))


def pausar():
    """Espera a que el usuario presione Enter."""
    input("\nPresione Enter para continuar...")


def mostrar_menu_principal():
    """Muestra las opciones principales del sistema."""
    limpiar_pantalla()
    mostrar_titulo("Gestion")

    print("GESTIÓN DE EQUIPAMIENTO\n")
    print("1. Ver todos los equipos")
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
    """Muestra las opciones de búsqueda disponibles."""
    limpiar_pantalla()
    mostrar_titulo("Buscar")

    print("BÚSQUEDA DE EQUIPOS\n")
    print("1. Buscar por código de inventario")
    print("2. Buscar por número de serie")
    print("3. Buscar por usuario")
    print("4. Volver al menú principal")


def mostrar_menu_estados():
    """Muestra las opciones para cambiar el estado de un equipo."""
    limpiar_pantalla()
    mostrar_titulo("Estados")

    print("CAMBIO DE ESTADO\n")
    print("1. Marcar como dañado")
    print("2. Marcar como disponible")
    print("3. Marcar como robado")
    print("4. Dar de baja")
    print("5. Volver al menú principal")


def mostrar_menu_listados():
    """Muestra los listados disponibles según el estado."""
    limpiar_pantalla()
    mostrar_titulo("Listados")

    print("VER EQUIPOS POR ESTADO\n")
    print("1. Disponibles")
    print("2. Asignados")
    print("3. Dañados")
    print("4. Dados de baja")
    print("5. Robados")
    print("6. Volver al menú principal")


def ejecutar_busqueda():
    """Ejecuta el menú de búsqueda."""
    while True:
        mostrar_menu_busqueda()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            mostrar_titulo("Codigo")
            consultar_equipo_por_codigo()
            pausar()

        elif opcion == "2":
            limpiar_pantalla()
            mostrar_titulo("Serie")
            consultar_equipo_por_serie()
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            mostrar_titulo("Usuario")
            consultar_equipos_por_usuario()
            pausar()

        elif opcion == "4":
            break

        else:
            print(Fore.RED + "\nLa opción ingresada no es válida.")
            pausar()


def ejecutar_cambio_estado():
    """Ejecuta el menú de cambios de estado."""
    while True:
        mostrar_menu_estados()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            mostrar_titulo("Daniado")
            marcar_como_daniado()
            pausar()

        elif opcion == "2":
            limpiar_pantalla()
            mostrar_titulo("Disponible")
            marcar_como_disponible()
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            mostrar_titulo("Robado")
            marcar_como_robado()
            pausar()

        elif opcion == "4":
            limpiar_pantalla()
            mostrar_titulo("Baja")
            dar_de_baja()
            pausar()

        elif opcion == "5":
            break

        else:
            print(Fore.RED + "\nLa opción ingresada no es válida.")
            pausar()


def ejecutar_listados():
    """Ejecuta el menú de listados por estado."""
    while True:
        mostrar_menu_listados()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            mostrar_titulo("Disponibles")
            mostrar_equipos_por_estado("Disponible")
            pausar()

        elif opcion == "2":
            limpiar_pantalla()
            mostrar_titulo("Asignados")
            mostrar_equipos_por_estado("Asignado")
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            mostrar_titulo("Daniados")
            mostrar_equipos_por_estado("Dañado")
            pausar()

        elif opcion == "4":
            limpiar_pantalla()
            mostrar_titulo("Bajas")
            mostrar_equipos_por_estado("Dado de baja")
            pausar()

        elif opcion == "5":
            limpiar_pantalla()
            mostrar_titulo("Robados")
            mostrar_equipos_por_estado("Robado")
            pausar()

        elif opcion == "6":
            break

        else:
            print(Fore.RED + "\nLa opción ingresada no es válida.")
            pausar()


def ejecutar_programa():
    """Ejecuta el programa hasta que el usuario elija salir."""
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            mostrar_titulo("Inventario")
            mostrar_todos_los_equipos()
            pausar()

        elif opcion == "2":
            limpiar_pantalla()
            mostrar_titulo("Alta")
            agregar_equipo()
            pausar()

        elif opcion == "3":
            ejecutar_busqueda()

        elif opcion == "4":
            limpiar_pantalla()
            mostrar_titulo("Asignar")
            asignar_equipo()
            pausar()

        elif opcion == "5":
            limpiar_pantalla()
            mostrar_titulo("Devolver")
            devolver_equipo()
            pausar()

        elif opcion == "6":
            limpiar_pantalla()
            mostrar_titulo("Modificar")
            modificar_equipo()
            pausar()

        elif opcion == "7":
            ejecutar_cambio_estado()

        elif opcion == "8":
            ejecutar_listados()

        elif opcion == "9":
            limpiar_pantalla()
            mostrar_titulo("Etiqueta")
            solicitar_codigo_para_qr(buscar_por_codigo)
            pausar()

        elif opcion == "10":
            print(Fore.GREEN + "\nPrograma finalizado.")
            break

        else:
            print(Fore.RED + "\nLa opción ingresada no es válida.")
            pausar()


if __name__ == "__main__":
    ejecutar_programa()