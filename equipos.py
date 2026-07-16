"""Funciones para administrar los equipos y guardar su historial."""

import json
from datetime import datetime

from tabulate import tabulate


# Se usan dos archivos para separar el estado actual de los movimientos.
ARCHIVO_EQUIPOS = "equipos.json"
ARCHIVO_HISTORIAL = "historial.json"


def cargar_datos(nombre_archivo):
    """Carga una lista guardada en un archivo JSON.

    Args:
        nombre_archivo (str): Nombre del archivo que se quiere abrir.

    Returns:
        list: Datos encontrados o una lista vacía si ocurre un error.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos

    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}.")
        return []

    except json.JSONDecodeError:
        print(f"El archivo {nombre_archivo} está vacío o dañado.")
        return []

    except OSError:
        print(f"No se pudo abrir el archivo {nombre_archivo}.")
        return []


def guardar_datos(nombre_archivo, datos):
    """Guarda una lista dentro de un archivo JSON.

    Args:
        nombre_archivo (str): Archivo donde se guardarán los datos.
        datos (list): Lista que se quiere guardar.

    Returns:
        bool: True si se guardó correctamente o False si hubo un error.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        return True

    except OSError:
        print(f"No se pudieron guardar los datos en {nombre_archivo}.")
        return False


def obtener_fecha_actual():
    """Devuelve la fecha y hora actuales con un formato legible.

    Returns:
        str: Fecha y hora actuales.
    """
    fecha_actual = datetime.now()
    return fecha_actual.strftime("%d/%m/%Y %H:%M")


def registrar_movimiento(codigo, tipo_movimiento, detalle):
    """Guarda un movimiento en el historial de un equipo.

    Args:
        codigo (str): Código de inventario.
        tipo_movimiento (str): Nombre del movimiento realizado.
        detalle (str): Información sobre el movimiento.

    Returns:
        bool: True si el movimiento se guardó correctamente.
    """
    historial = cargar_datos(ARCHIVO_HISTORIAL)

    movimiento = {
        "codigo": codigo,
        "fecha": obtener_fecha_actual(),
        "movimiento": tipo_movimiento,
        "detalle": detalle
    }

    historial.append(movimiento)

    return guardar_datos(ARCHIVO_HISTORIAL, historial)


def buscar_por_codigo(codigo):
    """Busca un equipo por su código de inventario.

    Args:
        codigo (str): Código que se quiere buscar.

    Returns:
        dict: Equipo encontrado.
        None: Si no existe un equipo con ese código.
    """
    equipos = cargar_datos(ARCHIVO_EQUIPOS)

    for equipo in equipos:
        codigo_actual = equipo.get("codigo", "")

        if codigo_actual.lower() == codigo.lower():
            return equipo

    return None


def buscar_por_numero_serie(numero_serie):
    """Busca un equipo por su número de serie.

    Args:
        numero_serie (str): Número de serie que se quiere buscar.

    Returns:
        dict: Equipo encontrado.
        None: Si no existe un equipo con ese número de serie.
    """
    equipos = cargar_datos(ARCHIVO_EQUIPOS)

    for equipo in equipos:
        numero_actual = equipo.get("numero_serie", "")

        if numero_actual.lower() == numero_serie.lower():
            return equipo

    return None


def buscar_por_usuario(usuario):
    """Busca todos los equipos asignados a un usuario.

    Args:
        usuario (str): Nombre completo o parte del nombre.

    Returns:
        list: Equipos encontrados.
    """
    equipos = cargar_datos(ARCHIVO_EQUIPOS)
    equipos_encontrados = []

    for equipo in equipos:
        usuario_actual = equipo.get("usuario", "")

        if usuario.lower() in usuario_actual.lower():
            equipos_encontrados.append(equipo)

    return equipos_encontrados


def generar_codigo(tipo):
    """Genera el siguiente código de inventario disponible.

    Las PC y notebooks usan EQ.
    Los demás equipos usan HW.

    Args:
        tipo (str): Tipo de equipo que se está agregando.

    Returns:
        str: Nuevo código de inventario.
    """
    equipos = cargar_datos(ARCHIVO_EQUIPOS)

    # Los códigos se separan en equipos principales y hardware adicional.
    if tipo.lower() in ["pc de escritorio", "notebook"]:
        prefijo = "EQ"
    else:
        prefijo = "HW"

    numero_mayor = 0

    # Se busca el número más alto usado con el mismo prefijo.
    for equipo in equipos:
        codigo = equipo.get("codigo", "")

        if codigo.startswith(prefijo):
            partes = codigo.split("-")

            if len(partes) == 2 and partes[1].isdigit():
                numero = int(partes[1])

                if numero > numero_mayor:
                    numero_mayor = numero

    siguiente_numero = numero_mayor + 1

    return f"{prefijo}-{siguiente_numero:04d}"


def seleccionar_tipo_equipo():
    """Muestra los tipos disponibles y devuelve el seleccionado.

    Returns:
        str: Tipo de equipo seleccionado.
        None: Si la opción ingresada no es válida.
    """
    tipos = [
        "PC de escritorio",
        "Notebook",
        "Monitor",
        "Impresora",
        "Celular",
        "TV"
    ]

    print("\nTIPOS DE EQUIPO")
    print("1. PC de escritorio")
    print("2. Notebook")
    print("3. Monitor")
    print("4. Impresora")
    print("5. Celular")
    print("6. TV")

    opcion = input("\nSeleccione el tipo de equipo: ").strip()

    if opcion.isdigit():
        numero = int(opcion)

        if 1 <= numero <= len(tipos):
            return tipos[numero - 1]

    print("La opción ingresada no es válida.")
    return None


def agregar_equipo():
    """Solicita los datos y agrega un equipo al inventario."""
    equipos = cargar_datos(ARCHIVO_EQUIPOS)
    tipo = seleccionar_tipo_equipo()

    if tipo is None:
        return

    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    numero_serie = input("Número de serie: ").strip()

    if marca == "" or modelo == "" or numero_serie == "":
        print(
            "La marca, el modelo y el número de serie son obligatorios."
        )
        return

    # El número de serie no puede repetirse.
    if buscar_por_numero_serie(numero_serie) is not None:
        print("Ya existe un equipo con ese número de serie.")
        return

    procesador = input("Procesador (opcional): ").strip()
    memoria_ram = input("Memoria RAM (opcional): ").strip()
    almacenamiento = input("Almacenamiento (opcional): ").strip()
    sistema_operativo = input(
        "Sistema operativo (opcional): "
    ).strip()
    observaciones = input(
        "Observaciones (opcional): "
    ).strip()

    codigo = generar_codigo(tipo)

    # Todo equipo nuevo ingresa disponible y queda en depósito.
    nuevo_equipo = {
        "codigo": codigo,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "numero_serie": numero_serie,
        "procesador": procesador,
        "memoria_ram": memoria_ram,
        "almacenamiento": almacenamiento,
        "sistema_operativo": sistema_operativo,
        "estado": "Disponible",
        "ubicacion": "Depósito",
        "usuario": "",
        "sector": "",
        "fecha_asignacion": "",
        "fecha_baja": "",
        "motivo_baja": "",
        "observaciones": observaciones
    }

    equipos.append(nuevo_equipo)

    if guardar_datos(ARCHIVO_EQUIPOS, equipos):
        registrar_movimiento(
            codigo,
            "Alta",
            "Equipo agregado al inventario."
        )

        print("\nEl equipo fue agregado correctamente.")
        print(f"Código asignado: {codigo}")


def mostrar_equipos(equipos):
    """Muestra una lista de equipos en forma de tabla.

    Args:
        equipos (list): Lista de equipos que se quiere mostrar.
    """
    if len(equipos) == 0:
        print("\nNo hay equipos para mostrar.")
        return

    tabla = []

    for equipo in equipos:
        tabla.append([
            equipo.get("codigo", ""),
            equipo.get("tipo", ""),
            equipo.get("marca", ""),
            equipo.get("modelo", ""),
            equipo.get("numero_serie", ""),
            equipo.get("estado", ""),
            equipo.get("ubicacion", ""),
            equipo.get("usuario", "")
        ])

    encabezados = [
        "Código",
        "Tipo",
        "Marca",
        "Modelo",
        "N° de serie",
        "Estado",
        "Ubicación",
        "Usuario"
    ]

    print()
    print(
        tabulate(
            tabla,
            headers=encabezados,
            tablefmt="grid"
        )
    )


def mostrar_todos_los_equipos():
    """Carga y muestra todos los equipos registrados."""
    equipos = cargar_datos(ARCHIVO_EQUIPOS)
    mostrar_equipos(equipos)


def mostrar_equipos_por_estado(estado):
    """Muestra los equipos que tienen un estado determinado.

    Args:
        estado (str): Estado que se quiere buscar.
    """
    equipos = cargar_datos(ARCHIVO_EQUIPOS)
    equipos_encontrados = []

    for equipo in equipos:
        if equipo.get("estado", "") == estado:
            equipos_encontrados.append(equipo)

    print(f"\nEQUIPOS CON ESTADO: {estado.upper()}")
    mostrar_equipos(equipos_encontrados)


def mostrar_detalle_equipo(equipo):
    """Muestra toda la información actual de un equipo.

    Args:
        equipo (dict): Equipo que se quiere mostrar.
    """
    print("\nDATOS DEL EQUIPO")
    print(f"Código: {equipo.get('codigo', '')}")
    print(f"Tipo: {equipo.get('tipo', '')}")
    print(f"Marca: {equipo.get('marca', '')}")
    print(f"Modelo: {equipo.get('modelo', '')}")
    print(f"Número de serie: {equipo.get('numero_serie', '')}")
    print(f"Procesador: {equipo.get('procesador', '')}")
    print(f"Memoria RAM: {equipo.get('memoria_ram', '')}")
    print(f"Almacenamiento: {equipo.get('almacenamiento', '')}")
    print(
        "Sistema operativo: "
        f"{equipo.get('sistema_operativo', '')}"
    )
    print(f"Estado: {equipo.get('estado', '')}")
    print(f"Ubicación: {equipo.get('ubicacion', '')}")
    print(f"Usuario: {equipo.get('usuario', '')}")
    print(f"Sector: {equipo.get('sector', '')}")
    print(
        "Fecha de asignación: "
        f"{equipo.get('fecha_asignacion', '')}"
    )
    print(f"Fecha de baja: {equipo.get('fecha_baja', '')}")
    print(f"Motivo de baja: {equipo.get('motivo_baja', '')}")
    print(f"Observaciones: {equipo.get('observaciones', '')}")


def mostrar_historial_equipo(codigo):
    """Muestra todos los movimientos de un equipo.

    Args:
        codigo (str): Código de inventario del equipo.
    """
    historial = cargar_datos(ARCHIVO_HISTORIAL)
    movimientos = []

    for movimiento in historial:
        codigo_movimiento = movimiento.get("codigo", "")

        if codigo_movimiento.lower() == codigo.lower():
            movimientos.append([
                movimiento.get("fecha", ""),
                movimiento.get("movimiento", ""),
                movimiento.get("detalle", "")
            ])

    print("\nHISTORIAL DEL EQUIPO")

    if len(movimientos) == 0:
        print("El equipo no tiene movimientos registrados.")
        return

    encabezados = [
        "Fecha",
        "Movimiento",
        "Detalle"
    ]

    print(
        tabulate(
            movimientos,
            headers=encabezados,
            tablefmt="grid"
        )
    )


def consultar_equipo_por_codigo():
    """Busca un equipo por código y muestra su historial."""
    codigo = input(
        "Ingrese el código de inventario: "
    ).strip()

    if codigo == "":
        print("Debe ingresar un código.")
        return

    equipo = buscar_por_codigo(codigo)

    if equipo is None:
        print("No se encontró un equipo con ese código.")
        return

    mostrar_detalle_equipo(equipo)
    mostrar_historial_equipo(equipo["codigo"])


def consultar_equipo_por_serie():
    """Busca un equipo por número de serie y muestra su historial."""
    numero_serie = input(
        "Ingrese el número de serie: "
    ).strip()

    if numero_serie == "":
        print("Debe ingresar un número de serie.")
        return

    equipo = buscar_por_numero_serie(numero_serie)

    if equipo is None:
        print("No se encontró un equipo con ese número de serie.")
        return

    mostrar_detalle_equipo(equipo)
    mostrar_historial_equipo(equipo["codigo"])


def consultar_equipos_por_usuario():
    """Busca y muestra los equipos asignados a un usuario."""
    usuario = input(
        "Ingrese el nombre del usuario: "
    ).strip()

    if usuario == "":
        print("Debe ingresar un nombre.")
        return

    equipos = buscar_por_usuario(usuario)

    if len(equipos) == 0:
        print("No se encontraron equipos asignados a ese usuario.")
        return

    mostrar_equipos(equipos)


def asignar_equipo():
    """Asigna un equipo disponible a un usuario."""
    codigo = input("Ingrese el código del equipo: ").strip()
    equipos = cargar_datos(ARCHIVO_EQUIPOS)
    equipo_encontrado = None

    for equipo in equipos:
        codigo_actual = equipo.get("codigo", "")

        if codigo_actual.lower() == codigo.lower():
            equipo_encontrado = equipo
            break

    if equipo_encontrado is None:
        print("No se encontró un equipo con ese código.")
        return

    if equipo_encontrado.get("estado", "") != "Disponible":
        print("El equipo no se encuentra disponible.")
        return

    usuario = input(
        "Nombre y apellido del usuario: "
    ).strip()
    sector = input("Sector: ").strip()
    observacion = input(
        "Observación de la asignación (opcional): "
    ).strip()

    if usuario == "" or sector == "":
        print(
            "El nombre del usuario y el sector son obligatorios."
        )
        return

    # Al asignarlo deja el depósito y pasa a estar con el usuario.
    equipo_encontrado["estado"] = "Asignado"
    equipo_encontrado["ubicacion"] = "Usuario asignado"
    equipo_encontrado["usuario"] = usuario
    equipo_encontrado["sector"] = sector
    equipo_encontrado["fecha_asignacion"] = obtener_fecha_actual()

    if guardar_datos(ARCHIVO_EQUIPOS, equipos):
        detalle = f"Asignado a {usuario}, sector {sector}."

        if observacion != "":
            detalle += f" Observación: {observacion}"

        registrar_movimiento(
            equipo_encontrado["codigo"],
            "Asignación",
            detalle
        )

        print("El equipo fue asignado correctamente.")


def devolver_equipo():
    """Registra la devolución de un equipo asignado."""
    codigo = input("Ingrese el código del equipo: ").strip()
    equipos = cargar_datos(ARCHIVO_EQUIPOS)
    equipo_encontrado = None

    for equipo in equipos:
        codigo_actual = equipo.get("codigo", "")

        if codigo_actual.lower() == codigo.lower():
            equipo_encontrado = equipo
            break

    if equipo_encontrado is None:
        print("No se encontró un equipo con ese código.")
        return

    if equipo_encontrado.get("estado", "") != "Asignado":
        print("El equipo no se encuentra asignado.")
        return

    usuario_anterior = equipo_encontrado.get("usuario", "")
    sector_anterior = equipo_encontrado.get("sector", "")

    # La devolución libera los datos actuales del usuario.
    # La asignación anterior sigue guardada en el historial.
    equipo_encontrado["estado"] = "Disponible"
    equipo_encontrado["ubicacion"] = "Depósito"
    equipo_encontrado["usuario"] = ""
    equipo_encontrado["sector"] = ""
    equipo_encontrado["fecha_asignacion"] = ""

    if guardar_datos(ARCHIVO_EQUIPOS, equipos):
        detalle = (
            f"Devuelto por {usuario_anterior}, "
            f"sector {sector_anterior}. "
            "Equipo disponible en depósito."
        )

        registrar_movimiento(
            equipo_encontrado["codigo"],
            "Devolución",
            detalle
        )

        print("El equipo fue devuelto correctamente.")
        print("Ahora se encuentra disponible en depósito.")


def modificar_equipo():
    """Permite modificar los datos generales de un equipo."""
    codigo = input("Ingrese el código del equipo: ").strip()
    equipos = cargar_datos(ARCHIVO_EQUIPOS)
    equipo_encontrado = None

    for equipo in equipos:
        codigo_actual = equipo.get("codigo", "")

        if codigo_actual.lower() == codigo.lower():
            equipo_encontrado = equipo
            break

    if equipo_encontrado is None:
        print("No se encontró un equipo con ese código.")
        return

    print("\nPresione Enter para mantener el valor actual.")

    marca = input(
        f"Marca [{equipo_encontrado.get('marca', '')}]: "
    ).strip()

    modelo = input(
        f"Modelo [{equipo_encontrado.get('modelo', '')}]: "
    ).strip()

    numero_serie = input(
        "Número de serie "
        f"[{equipo_encontrado.get('numero_serie', '')}]: "
    ).strip()

    procesador = input(
        "Procesador "
        f"[{equipo_encontrado.get('procesador', '')}]: "
    ).strip()

    memoria_ram = input(
        "Memoria RAM "
        f"[{equipo_encontrado.get('memoria_ram', '')}]: "
    ).strip()

    almacenamiento = input(
        "Almacenamiento "
        f"[{equipo_encontrado.get('almacenamiento', '')}]: "
    ).strip()

    sistema_operativo = input(
        "Sistema operativo "
        f"[{equipo_encontrado.get('sistema_operativo', '')}]: "
    ).strip()

    observaciones = input(
        "Observaciones "
        f"[{equipo_encontrado.get('observaciones', '')}]: "
    ).strip()

    # Antes de cambiar el número de serie se controla que no esté usado.
    if numero_serie != "":
        equipo_misma_serie = buscar_por_numero_serie(numero_serie)

        if (
            equipo_misma_serie is not None
            and equipo_misma_serie["codigo"]
            != equipo_encontrado["codigo"]
        ):
            print(
                "Ya existe otro equipo con ese número de serie."
            )
            return

    # Los campos vacíos conservan el valor que ya tenía el equipo.
    if marca != "":
        equipo_encontrado["marca"] = marca

    if modelo != "":
        equipo_encontrado["modelo"] = modelo

    if numero_serie != "":
        equipo_encontrado["numero_serie"] = numero_serie

    if procesador != "":
        equipo_encontrado["procesador"] = procesador

    if memoria_ram != "":
        equipo_encontrado["memoria_ram"] = memoria_ram

    if almacenamiento != "":
        equipo_encontrado["almacenamiento"] = almacenamiento

    if sistema_operativo != "":
        equipo_encontrado["sistema_operativo"] = sistema_operativo

    if observaciones != "":
        equipo_encontrado["observaciones"] = observaciones

    if guardar_datos(ARCHIVO_EQUIPOS, equipos):
        registrar_movimiento(
            equipo_encontrado["codigo"],
            "Modificación",
            "Se actualizaron los datos generales del equipo."
        )

        print("Los datos fueron modificados correctamente.")


def marcar_como_daniado():
    """Cambia el estado de un equipo a Dañado."""
    codigo = input("Ingrese el código del equipo: ").strip()
    equipos = cargar_datos(ARCHIVO_EQUIPOS)
    equipo_encontrado = None

    for equipo in equipos:
        codigo_actual = equipo.get("codigo", "")

        if codigo_actual.lower() == codigo.lower():
            equipo_encontrado = equipo
            break

    if equipo_encontrado is None:
        print("No se encontró un equipo con ese código.")
        return

    estado_actual = equipo_encontrado.get("estado", "")

    if estado_actual in ["Dado de baja", "Robado"]:
        print(
            f"No se puede modificar un equipo con estado "
            f"{estado_actual}."
        )
        return

    if estado_actual == "Dañado":
        print("El equipo ya se encuentra marcado como dañado.")
        return

    usuario_anterior = equipo_encontrado.get("usuario", "")
    sector_anterior = equipo_encontrado.get("sector", "")

    # Un equipo dañado deja de estar asignado y pasa a reparación.
    equipo_encontrado["estado"] = "Dañado"
    equipo_encontrado["ubicacion"] = "Reparación"
    equipo_encontrado["usuario"] = ""
    equipo_encontrado["sector"] = ""
    equipo_encontrado["fecha_asignacion"] = ""

    if guardar_datos(ARCHIVO_EQUIPOS, equipos):
        detalle = "Equipo enviado a reparación."

        if usuario_anterior != "":
            detalle += (
                f" Estaba asignado a {usuario_anterior}, "
                f"sector {sector_anterior}."
            )

        registrar_movimiento(
            equipo_encontrado["codigo"],
            "Cambio de estado",
            detalle
        )

        print("El equipo fue marcado como dañado.")
        print("Su ubicación actual es Reparación.")


def marcar_como_disponible():
    """Cambia un equipo dañado nuevamente a Disponible."""
    codigo = input("Ingrese el código del equipo: ").strip()
    equipos = cargar_datos(ARCHIVO_EQUIPOS)
    equipo_encontrado = None

    for equipo in equipos:
        codigo_actual = equipo.get("codigo", "")

        if codigo_actual.lower() == codigo.lower():
            equipo_encontrado = equipo
            break

    if equipo_encontrado is None:
        print("No se encontró un equipo con ese código.")
        return

    if equipo_encontrado.get("estado", "") != "Dañado":
        print(
            "Solo se puede cambiar a disponible "
            "un equipo que está dañado."
        )
        return

    # Si fue reparado vuelve a quedar disponible en depósito.
    equipo_encontrado["estado"] = "Disponible"
    equipo_encontrado["ubicacion"] = "Depósito"
    equipo_encontrado["usuario"] = ""
    equipo_encontrado["sector"] = ""
    equipo_encontrado["fecha_asignacion"] = ""

    if guardar_datos(ARCHIVO_EQUIPOS, equipos):
        registrar_movimiento(
            equipo_encontrado["codigo"],
            "Cambio de estado",
            "Equipo reparado y disponible en depósito."
        )

        print("El equipo volvió a estar disponible.")
        print("Su ubicación actual es Depósito.")


def marcar_como_robado():
    """Cambia el estado de un equipo a Robado."""
    codigo = input("Ingrese el código del equipo: ").strip()
    equipos = cargar_datos(ARCHIVO_EQUIPOS)
    equipo_encontrado = None

    for equipo in equipos:
        codigo_actual = equipo.get("codigo", "")

        if codigo_actual.lower() == codigo.lower():
            equipo_encontrado = equipo
            break

    if equipo_encontrado is None:
        print("No se encontró un equipo con ese código.")
        return

    if equipo_encontrado.get("estado", "") == "Robado":
        print("El equipo ya se encuentra marcado como robado.")
        return

    if equipo_encontrado.get("estado", "") == "Dado de baja":
        print("El equipo ya fue dado de baja.")
        return

    confirmar = input(
        "¿Confirma que desea marcar el equipo como robado? S/N: "
    ).strip().lower()

    if confirmar != "s":
        print("La operación fue cancelada.")
        return

    # El equipo queda fuera del stock disponible.
    equipo_encontrado["estado"] = "Robado"
    equipo_encontrado["ubicacion"] = "Baja"
    equipo_encontrado["usuario"] = ""
    equipo_encontrado["sector"] = ""
    equipo_encontrado["fecha_asignacion"] = ""

    if guardar_datos(ARCHIVO_EQUIPOS, equipos):
        registrar_movimiento(
            equipo_encontrado["codigo"],
            "Cambio de estado",
            "Equipo marcado como robado."
        )

        print("El equipo fue marcado como robado.")


def dar_de_baja():
    """Da de baja un equipo y registra el motivo."""
    codigo = input("Ingrese el código del equipo: ").strip()
    equipos = cargar_datos(ARCHIVO_EQUIPOS)
    equipo_encontrado = None

    for equipo in equipos:
        codigo_actual = equipo.get("codigo", "")

        if codigo_actual.lower() == codigo.lower():
            equipo_encontrado = equipo
            break

    if equipo_encontrado is None:
        print("No se encontró un equipo con ese código.")
        return

    if equipo_encontrado.get("estado", "") == "Dado de baja":
        print("El equipo ya se encuentra dado de baja.")
        return

    if equipo_encontrado.get("estado", "") == "Robado":
        print(
            "El equipo está marcado como robado "
            "y no puede darse de baja."
        )
        return

    motivo = input("Motivo de la baja: ").strip()
    observaciones = input(
        "Observaciones de la baja (opcional): "
    ).strip()

    if motivo == "":
        print("Debe ingresar el motivo de la baja.")
        return

    confirmar = input(
        "¿Confirma que desea dar de baja el equipo? S/N: "
    ).strip().lower()

    if confirmar != "s":
        print("La operación fue cancelada.")
        return

    # La baja es definitiva y el equipo deja de estar disponible.
    equipo_encontrado["estado"] = "Dado de baja"
    equipo_encontrado["ubicacion"] = "Baja"
    equipo_encontrado["usuario"] = ""
    equipo_encontrado["sector"] = ""
    equipo_encontrado["fecha_asignacion"] = ""
    equipo_encontrado["fecha_baja"] = obtener_fecha_actual()
    equipo_encontrado["motivo_baja"] = motivo

    if observaciones != "":
        observacion_anterior = equipo_encontrado.get(
            "observaciones",
            ""
        )

        if observacion_anterior != "":
            equipo_encontrado["observaciones"] = (
                observacion_anterior
                + " | Baja: "
                + observaciones
            )
        else:
            equipo_encontrado["observaciones"] = observaciones

    if guardar_datos(ARCHIVO_EQUIPOS, equipos):
        detalle = f"Equipo dado de baja. Motivo: {motivo}."

        if observaciones != "":
            detalle += f" Observaciones: {observaciones}"

        registrar_movimiento(
            equipo_encontrado["codigo"],
            "Baja",
            detalle
        )

        print("El equipo fue dado de baja correctamente.")