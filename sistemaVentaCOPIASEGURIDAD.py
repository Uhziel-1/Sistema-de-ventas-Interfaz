
import tkinter as tk
from tkinter import ttk

# Crear la ventana que tendra todas las funcionalidades del sistema de ventas.
sistemaVentas = tk.Tk()
sistemaVentas.title("Sistema de Ventas")
sistemaVentas.minsize(1200,700)

# Al dar click al bontón registrarse del iniciar sesión
def registrarse1():
    
    marco_registro.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER) # Para hacer aparecer el marco con los widget de registro.
    marco_iniciar_sesion.place_forget() # Para ocultar el marco con los widgets de inciar sesión.

# Al dar click al botón acceder del iniciar sesión
def acceder():

    marco_registro.destroy() # Eliminar el marco con los widgets de registro.
    marco_iniciar_sesion.destroy() # Eliminar el marco con los widgets de incio de sesión.
    marco_principal_derecha.grid(row = 0, column = 0, sticky = "wns") # Se muestra el marco que tendrá los widgets de botónes.
    marco_principal_izquierda.grid(row = 0, column = 1, sticky = "snew") # Se muestra el marco que mostrará todo lo que los botones pidan.
    marco_CRUD_productos.grid(row = 0) # Se muestra el marco donde estaran los widgets del CRUD productos.
    marco_CRUD_clientes.grid(row = 1)
    marco_CRUD_ventas.grid(row = 2) # Se muestra el marco donde estaran los widgets del CRUD ventas.

# Al dar click al botón tengo cuenta del registrarse
def tengo_cuenta():

    marco_registro.place_forget() # Para ocultar el marco con los widgets de registro.
    marco_iniciar_sesion.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER) # Para mostrar el marco con los widgets de incio de sesión.

# Al dar click en el boton de CRUD productos
def activar_CRUD_productos():

    global botones_productos_visibles # La variable es global.

    botones_productos_visibles = not botones_productos_visibles # Cambiar el valor de la variable por su contrario.

    if botones_productos_visibles: # Si la variable es verdadero entonces hacer aparecer los botones y el marco.

        marco_desaparecido3.grid(row = 1, column = 0, rowspan = 3)
        boton_crear_productos.grid(row = 1, column = 1, sticky = "ew")
        boton_buscar_productos.grid(row = 2, column = 1, sticky = "ew")
        boton_editar_productos.grid(row = 3, column = 1, sticky = "ew")
    else: # Si no, entonces desaparecer los botones y el marco.

        marco_desaparecido3.grid_remove()
        boton_crear_productos.grid_remove()
        boton_buscar_productos.grid_remove()
        boton_editar_productos.grid_remove()

def crear_producto():

    marco_crear_producto.grid(row = 0, column = 0, sticky = "swen")
    marco_buscar_producto.grid_remove()
    marco_editar_producto.grid_remove()
    marco_crear_cliente.grid_remove()
    marco_buscar_cliente.grid_remove()
    marco_editar_cliente.grid_remove()
    marco_hacer_venta.grid_remove()
    marco_buscar_venta.grid_remove()
    marco_editar_venta.grid_remove()


def buscar_producto():

    marco_buscar_producto.grid(row = 0, column = 0, sticky = "ewsn")
    marco_crear_producto.grid_remove()
    marco_editar_producto.grid_remove()
    marco_crear_cliente.grid_remove()
    marco_buscar_cliente.grid_remove()
    marco_editar_cliente.grid_remove()
    marco_hacer_venta.grid_remove()
    marco_buscar_venta.grid_remove()
    marco_editar_venta.grid_remove()


def editar_producto():
    marco_editar_producto.grid(row = 0, column = 0, sticky = "ewsn")
    marco_crear_producto.grid_remove()
    marco_buscar_producto.grid_remove()
    marco_crear_cliente.grid_remove()
    marco_buscar_cliente.grid_remove()
    marco_editar_cliente.grid_remove()
    marco_hacer_venta.grid_remove()
    marco_buscar_venta.grid_remove()
    marco_editar_venta.grid_remove()


# Mostrar mensaje
def mostrar_mensaje(mensaje):
    boton_agregar_producto.grid_remove()
    mensaje1.config(text = mensaje)
    mensaje1.grid(row = 10, column = 0)
    marco_central_crear_producto.after(2000, ocultar_mensaje)

# Ocultar mensaje
def ocultar_mensaje():
    boton_agregar_producto.grid()
    mensaje1.grid_forget()

# Agregar datos a la lista productos
def agregar_datos():

    marca = var_marca_producto.get()
    nombre = var_nombre_producto.get()
    modelo = var_modelo_producto.get()
    precio = var_precio_producto.get()
    cantidad = var_cantidad_producto.get()

    if marca and nombre and modelo and precio and cantidad:

        index = len(lista_producto.get_children()) + 1
        lista_producto.insert("", tk.END,iid = index, values = (index, marca, nombre, modelo, precio, cantidad))

        entrada_introducir_marca_producto.delete(0, tk.END)
        entrada_introducir_nombre_producto.delete(0, tk.END)
        entrada_introducir_modelo_producto.delete(0, tk.END)
        entrada_introducir_precio_producto.delete(0, tk.END)
        entrada_introducir_cantidad_producto.delete(0, tk.END)
    else:
        mostrar_mensaje("Por favor, complete todos los campos.")

def activar_CRUD_clientes():

    global botones_clientes_visibles

    botones_clientes_visibles = not botones_clientes_visibles

    if botones_clientes_visibles:

        marco_desaparecido4.grid(row = 1, column = 0, rowspan = 3)
        boton_crear_cliente.grid(row = 1, column = 1, sticky = "ew")
        boton_buscar_cliente.grid(row = 2, column = 1, sticky = "ew")
        boton_editar_cliente.grid(row = 3, column = 1, sticky = "ew")
    else:

        marco_desaparecido4.grid_remove()
        boton_crear_cliente.grid_remove()
        boton_buscar_cliente.grid_remove()
        boton_editar_cliente.grid_remove()

def crear_cliente():

    marco_crear_cliente.grid(row = 0, column = 0, sticky = "swen")
    marco_crear_producto.grid_remove()
    marco_buscar_producto.grid_remove()
    marco_editar_producto.grid_remove()
    marco_buscar_cliente.grid_remove()
    marco_editar_cliente.grid_remove()
    marco_hacer_venta.grid_remove()
    marco_buscar_venta.grid_remove()
    marco_editar_venta.grid_remove()

def buscar_cliente():

    marco_buscar_cliente.grid(row = 0, column = 0, sticky = "ewsn")
    marco_crear_producto.grid_remove()
    marco_buscar_producto.grid_remove()
    marco_editar_producto.grid_remove()
    marco_crear_cliente.grid_remove()
    marco_editar_cliente.grid_remove()
    marco_hacer_venta.grid_remove()
    marco_buscar_venta.grid_remove()
    marco_editar_venta.grid_remove()


def editar_cliente():

    marco_editar_cliente.grid(row = 0, column = 0, sticky = "ewsn")
    marco_crear_producto.grid_remove()
    marco_buscar_producto.grid_remove()
    marco_editar_producto.grid_remove()
    marco_crear_cliente.grid_remove()
    marco_buscar_cliente.grid_remove()
    marco_hacer_venta.grid_remove()
    marco_buscar_venta.grid_remove()
    marco_editar_venta.grid_remove()


def mostrar_mensaje2(mensaje1):
    boton_agregar_cliente.grid_remove()
    mensaje2.config(text = mensaje1)
    mensaje2.grid(row = 10, column = 0)
    marco_central_crear_producto.after(2000, ocultar_mensaje2)

# Ocultar mensaje
def ocultar_mensaje2():
    boton_agregar_cliente.grid()
    mensaje2.grid_forget()

# Agregar datos a la lista productos
def agregar_datos2():

    nombre_cliente = var_nombre_cliente.get()
    apellido_paterno_cliente = var_apellido_paterno_cliente.get()
    apellido_materno_cliente = var_apellido_materno_cliente.get()
    dni_cliente = var_dni_cliente.get()
    telefono_cliente = var_telefono_cliente.get()

    if nombre_cliente and apellido_paterno_cliente and apellido_materno_cliente and dni_cliente and telefono_cliente:

        index = len(lista_cliente.get_children()) + 1
        lista_cliente.insert("", tk.END,iid = index, values = (index, nombre_cliente, apellido_paterno_cliente, apellido_materno_cliente, dni_cliente, telefono_cliente))

        entrada_introducir_nombre_cliente.delete(0, tk.END)
        entrada_introducir_apellido_paterno_cliente.delete(0, tk.END)
        entrada_introducir_apellido_materno_cliente.delete(0, tk.END)
        entrada_introducir_dni_cliente.delete(0, tk.END)
        entrada_introducir_telefono_cliente.delete(0, tk.END)
    else:
        mostrar_mensaje2("Por favor, complete todos los campos.")


# Funciones de los botones del CRUD Ventas
def activar_CRUD_ventas():

    global botones_ventas_visibles

    botones_ventas_visibles = not botones_ventas_visibles

    if botones_ventas_visibles:
        
        marco_desaparecido5.grid(row = 1, column = 0, rowspan = 2)
        boton_hacer_venta.grid(row = 1, column = 1, sticky = "ew")
        boton_buscar_venta.grid(row = 2, column = 1, sticky = "ew")
        boton_editar_venta.grid(row = 3, column = 1, sticky = "ew")
    else:

        marco_desaparecido5.grid_remove()
        boton_hacer_venta.grid_remove()
        boton_buscar_venta.grid_remove()
        boton_editar_venta.grid_remove()


def hacer_venta():

    marco_hacer_venta.grid(row = 0, column = 0, sticky = "swen")
    marco_crear_producto.grid_remove()
    marco_buscar_producto.grid_remove()
    marco_editar_producto.grid_remove()
    marco_crear_cliente.grid_remove()
    marco_buscar_cliente.grid_remove()
    marco_editar_cliente.grid_remove()
    marco_buscar_venta.grid_remove()
    marco_editar_venta.grid_remove()


def buscar_venta():

    marco_buscar_venta.grid(row = 0, column = 0, sticky = "ewsn")
    marco_crear_producto.grid_remove()
    marco_buscar_producto.grid_remove()
    marco_editar_producto.grid_remove()
    marco_crear_cliente.grid_remove()
    marco_buscar_cliente.grid_remove()
    marco_editar_cliente.grid_remove()
    marco_hacer_venta.grid_remove()
    marco_editar_venta.grid_remove()


def editar_venta():

    marco_editar_venta.grid(row = 0, column = 0, sticky = "ewsn")
    marco_crear_producto.grid_remove()
    marco_buscar_producto.grid_remove()
    marco_editar_producto.grid_remove()
    marco_crear_cliente.grid_remove()
    marco_buscar_cliente.grid_remove()
    marco_editar_cliente.grid_remove()
    marco_hacer_venta.grid_remove()
    marco_buscar_venta.grid_remove()

def mostrar_mensaje3(mensaje4):
    boton_vender.grid_remove()
    mensaje3.config(text = mensaje4)
    mensaje3.grid(row = 10, column = 0)
    marco_central_hacer_venta.after(2000, ocultar_mensaje3)

# Ocultar mensaje
def ocultar_mensaje3():
    boton_vender.grid()
    mensaje3.grid_forget()

# Agregar datos a la lista productos
def agregar_datos3():

    dni_cliente_venta = var_dni_cliente_venta.get()
    marca_producto_venta = var_marca_producto_venta.get()
    nombre_producto_venta = var_nombre_producto_venta.get()
    modelo_producto_venta = var_modelo_producto_venta.get()
    cantidad_venta = var_cantidad_venta.get()

    if dni_cliente_venta and marca_producto_venta and nombre_producto_venta and modelo_producto_venta and cantidad_venta:

        index = len(lista_venta.get_children()) + 1
        lista_venta.insert("", tk.END,iid = index, values = (index, dni_cliente_venta, marca_producto_venta, nombre_producto_venta, modelo_producto_venta, cantidad_venta))

        entrada_buscar_dni_cliente_venta2.delete(0, tk.END)
        entrada_buscar_marca_producto_venta2.delete(0, tk.END)
        entrada_buscar_nombre_producto_venta2.delete(0, tk.END)
        entrada_buscar_modelo_producto_venta2.delete(0, tk.END)
        entrada_cantidad_venta.delete(0, tk.END)
    else:
        mostrar_mensaje3("Por favor, complete todos los campos.")

# Marco principal, donde se podran todos los marcos y widgets.


marco_principal = tk.Frame(sistemaVentas, bg = "#0A007E")
marco_principal.grid(row = 0, column = 0, sticky = "nsew")
marco_principal.grid_rowconfigure(0, weight = 1)
marco_principal.grid_columnconfigure(1, weight = 1)

# Marco para los widgets de iniciar sesión.

marco_iniciar_sesion = tk.Frame(marco_principal, bg = "#E5E5E5")
marco_iniciar_sesion.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

# Dentro del marco iniciar sesion se pone el texto que identifique al marco
texto_iniciar_sesion = tk.Label(marco_iniciar_sesion, text = "INICIAR SESIÓN", bg = "#E5E5E5", highlightbackground = "#939393", highlightthickness=2)
texto_iniciar_sesion.config(width = 13)
texto_iniciar_sesion.grid(row = 0, column = 0)

marco_desaparecido1 = tk.Frame(marco_iniciar_sesion, bg = "#0A007E")
marco_desaparecido1.config(width = 199, height = 25)
marco_desaparecido1.grid(row = 0, column = 1)

marco_central_sesion = tk.Frame(marco_iniciar_sesion, bg = "#E5E5E5", highlightbackground = "#939393", highlightthickness=2)
marco_central_sesion.grid(row = 1, column = 0, columnspan = 2)

texto_usuario = tk.Label(marco_central_sesion, text = " Usuario", bg = "#E5E5E5")
texto_usuario.grid(row = 0, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_usuario = tk.Entry(marco_central_sesion)
entrada_usuario.config(width = 47)
entrada_usuario.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 2)

texto_contraseña = tk.Label(marco_central_sesion, text = " Contraseña", bg = "#E5E5E5")
texto_contraseña.grid(row = 2, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_contraseña = tk.Entry(marco_central_sesion, show = "*")
entrada_contraseña.config(width = 47)
entrada_contraseña.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 2)

boton_registro = tk.Button(marco_central_sesion, text = "Registrarse", bg = "#99B5D1", command = registrarse1)
boton_registro.config(width = 10)
boton_registro.grid(row = 4, column = 0, pady = 10)

boton_acceder = tk.Button(marco_central_sesion, text = "Acceder", bg = "#99B5D1", command = acceder)
boton_acceder.config(width = 10)
boton_acceder.grid(row = 4, column = 1, pady = 10)

sistemaVentas.rowconfigure(0, weight = 1)
sistemaVentas.columnconfigure(0, weight = 1)

# Variables de las entradas de texto de Registro
var_usuario = tk.StringVar()
var_contraseña = tk.StringVar()
var_confirm_contraseña = tk.StringVar()
var_nombres = tk.StringVar()
var_apellido_paterno = tk.StringVar()
var_apellido_materno = tk.StringVar()
var_dni = tk.StringVar()
var_telefono = tk.StringVar()
var_nombre_empresa = tk.StringVar()
var_ubicacion_empresa = tk.StringVar()
var_direccion_empresa = tk.StringVar()

# Marco Registro
marco_registro = tk.Frame(marco_principal, bg = "#E5E5E5")

texto_registrarse = tk. Label(marco_registro, text = "REGISTRARSE", bg = "#E5E5E5", highlightbackground = "#939393", highlightthickness=2)
texto_registrarse.config(width = 13)
texto_registrarse.grid(row = 0, column = 0)

marco_desaparecido2 = tk.Frame(marco_registro, bg = "#0A007E")
marco_desaparecido2.config(width = 199, height = 25)
marco_desaparecido2.grid(row = 0, column = 1)

marco_central_registro = tk.Frame(marco_registro, bg = "#E5E5E5", highlightbackground = "#939393", highlightthickness=2)
marco_central_registro.grid(row = 1, column = 0, columnspan = 2)

texto_usuario2 = tk.Label(marco_central_registro, text = " Nombre de Usuario", bg = "#E5E5E5")
texto_usuario2.grid(row = 0, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_usuario2 = tk.Entry(marco_central_registro, textvariable = var_usuario)
entrada_usuario2.config(width = 47)
entrada_usuario2.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 2)

texto_contraseña2 = tk.Label(marco_central_registro, text = " Contraseña", bg = "#E5E5E5")
texto_contraseña2.grid(row = 2, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_contraseña2 = tk.Entry(marco_central_registro, show = "*", textvariable = var_contraseña)
entrada_contraseña2.config(width = 47)
entrada_contraseña2.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 2)

texto_confirm_contraseña = tk.Label(marco_central_registro, text = " Confirmar Contraseña", bg = "#E5E5E5")
texto_confirm_contraseña.grid(row = 4, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_confirm_contraseña = tk.Entry(marco_central_registro, show = "*", textvariable = var_confirm_contraseña)
entrada_confirm_contraseña.config(width = 47)
entrada_confirm_contraseña.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 2)

texto_nombres = tk.Label(marco_central_registro, text = " Nombres", bg = "#E5E5E5")
texto_nombres.grid(row = 6, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_nombres = tk.Entry(marco_central_registro, textvariable = var_nombres)
entrada_nombres.config(width = 47)
entrada_nombres.grid(row = 7, column = 0, columnspan = 2, padx = 5, pady = 2)

texto_apellido_paterno = tk.Label(marco_central_registro, text = " Apellido Paterno", bg = "#E5E5E5")
texto_apellido_paterno.grid(row = 8, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_apellido_paterno = tk.Entry(marco_central_registro, textvariable = var_apellido_paterno)
entrada_apellido_paterno.config(width = 47)
entrada_apellido_paterno.grid(row = 9, column = 0, columnspan = 2, padx = 5, pady = 2)

texto_apellido_materno = tk.Label(marco_central_registro, text = " Apellido Materno", bg = "#E5E5E5")
texto_apellido_materno.grid(row = 10, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_apellido_materno = tk.Entry(marco_central_registro, textvariable = var_apellido_materno)
entrada_apellido_materno.config(width = 47)
entrada_apellido_materno.grid(row = 11, column = 0, columnspan = 2, padx = 5, pady = 2)

texto_dni = tk.Label(marco_central_registro, text = " DNI", bg = "#E5E5E5")
texto_dni.grid(row = 12, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_dni = tk.Entry(marco_central_registro, textvariable = var_dni)
entrada_dni.config(width = 47)
entrada_dni.grid(row = 13, column = 0, columnspan = 2, padx = 5, pady = 2)

texto_telefono = tk.Label(marco_central_registro, text = " Teléfono", bg = "#E5E5E5")
texto_telefono.grid(row = 14, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_telefono = tk.Entry(marco_central_registro, textvariable = var_telefono)
entrada_telefono.config(width = 47)
entrada_telefono.grid(row = 15, column = 0, columnspan = 2, padx = 5, pady = 2)

texto_nombre_empresa = tk.Label(marco_central_registro, text = " Nombre de la Empresa", bg = "#E5E5E5")
texto_nombre_empresa.grid(row = 16, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_nombre_empresa = tk.Entry(marco_central_registro, textvariable = var_nombre_empresa)
entrada_nombre_empresa.config(width = 47)
entrada_nombre_empresa.grid(row = 17, column = 0, columnspan = 2, padx = 5, pady = 2)

texto_ubicacion_empresa = tk.Label(marco_central_registro, text = " Ubicación de la Empresa", bg = "#E5E5E5")
texto_ubicacion_empresa.grid(row = 18, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_ubicacion_empresa = tk.Entry(marco_central_registro, textvariable = var_ubicacion_empresa)
entrada_ubicacion_empresa.config(width = 47)
entrada_ubicacion_empresa.grid(row = 19, column = 0, columnspan = 2, padx = 5, pady = 2)

texto_direccion_empresa = tk.Label(marco_central_registro, text = " Dirección de la Empresa", bg = "#E5E5E5")
texto_direccion_empresa.grid(row = 20, column = 0, columnspan = 2, sticky = "w", pady = 2)

entrada_direccion_empresa = tk.Entry(marco_central_registro, textvariable = var_direccion_empresa)
entrada_direccion_empresa.config(width = 47)
entrada_direccion_empresa.grid(row = 21, column = 0, columnspan = 2, padx = 5, pady = 2)

boton_tengo_cuenta = tk.Button(marco_central_registro, text = "Tengo Cuenta", bg = "#99B5D1", command = tengo_cuenta)
boton_tengo_cuenta.config(width = 10)
boton_tengo_cuenta.grid(row = 22, column = 0, pady = 10)

boton_registrarse = tk.Button(marco_central_registro, text = "Registrarse", bg = "#99B5D1")
boton_registrarse.config(width = 10)
boton_registrarse.grid(row = 22, column = 1, pady = 10)

# Marco Principal División

marco_principal_derecha = tk.Frame(marco_principal, bg = "#0A007E")
marco_principal_izquierda = tk.Frame(marco_principal, bg = "#E5E5E5")
marco_principal_izquierda.grid_rowconfigure(0, weight = 1)
marco_principal_izquierda.grid_columnconfigure(0, weight = 1)

# Marco CRUD Poductos

marco_CRUD_productos = tk.Frame(marco_principal_derecha, bg = "#0A007E")

boton_CRUD_productos = tk.Button(marco_CRUD_productos, text = "CRUD Productos", font = 12, bg = "#0A007E", fg = "white", highlightbackground = "black", highlightthickness = 0, command = activar_CRUD_productos)
boton_CRUD_productos.config(width = 25, height = 4)
boton_CRUD_productos.grid(row = 0, column= 0 , columnspan = 2)

marco_desaparecido3 = tk.Frame(marco_CRUD_productos, bg = "#0A007E")

boton_crear_productos = tk.Button(marco_CRUD_productos, text = "Crear Productos", bg = "#0A007E", fg = "white", highlightbackground = "#0A007E", highlightthickness = 0, command = crear_producto)
boton_crear_productos.config(height = 2)

boton_buscar_productos = tk.Button(marco_CRUD_productos, text = "Buscar Productos", bg = "#0A007E", fg = "white", highlightbackground = "#0A007E", highlightthickness = 0, command = buscar_producto)
boton_buscar_productos.config(height = 2)

boton_editar_productos = tk.Button(marco_CRUD_productos, text = "Editar Productos", bg = "#0A007E", fg = "white", highlightbackground = "#0A007E", highlightthickness = 0, command = editar_producto)
boton_editar_productos.config(height = 2)

botones_productos_visibles = False

# Marco Crear Producto
marco_crear_producto = tk.Frame(marco_principal_izquierda, bg = "#E5E5E5")
marco_crear_producto.grid_columnconfigure(0, weight = 1)
marco_crear_producto.grid_rowconfigure(0, weight = 1)

marco_central_crear_producto = tk.Frame(marco_crear_producto, padx = 100, pady = 100)
marco_central_crear_producto.config(bg = "#E5E5E5")
marco_central_crear_producto.grid(row = 0, column = 0, sticky = "sewn")

var_marca_producto = tk.StringVar()
var_nombre_producto = tk.StringVar()
var_modelo_producto = tk.StringVar()
var_precio_producto = tk.StringVar()
var_cantidad_producto = tk.StringVar()

texto_introducir_marca_producto = tk.Label(marco_central_crear_producto, text = "Introducir Marca del Producto", bg = "#E5E5E5", font = 14)
texto_introducir_marca_producto.grid(row = 0, column = 0, sticky = "w")

entrada_introducir_marca_producto = tk.Entry(marco_central_crear_producto, textvariable = var_marca_producto)
entrada_introducir_marca_producto.config(width = 50)
entrada_introducir_marca_producto.grid(row = 1, column = 0)

texto_introducir_nombre_producto = tk.Label(marco_central_crear_producto, text = "Introducir Nombre del Producto", bg = "#E5E5E5", font = 14)
texto_introducir_nombre_producto.grid(row = 2, column = 0, sticky = "w")

entrada_introducir_nombre_producto = tk.Entry(marco_central_crear_producto, textvariable = var_nombre_producto)
entrada_introducir_nombre_producto.config(width = 50)
entrada_introducir_nombre_producto.grid(row = 3, column = 0)

texto_introducir_modelo_producto = tk.Label(marco_central_crear_producto, text = "Introducir Modelo del Producto", bg = "#E5E5E5", font = 14)
texto_introducir_modelo_producto.grid(row = 4, column = 0, sticky = "w")

entrada_introducir_modelo_producto = tk.Entry(marco_central_crear_producto, textvariable = var_modelo_producto)
entrada_introducir_modelo_producto.config(width = 50)
entrada_introducir_modelo_producto.grid(row = 5, column = 0)

texto_introducir_precio_producto = tk.Label(marco_central_crear_producto, text = "Introducir Precio del Producto", bg = "#E5E5E5", font = 14)
texto_introducir_precio_producto.grid(row = 6, column = 0, sticky = "w")

entrada_introducir_precio_producto = tk.Entry(marco_central_crear_producto, textvariable = var_precio_producto)
entrada_introducir_precio_producto.config(width = 50)
entrada_introducir_precio_producto.grid(row = 7, column = 0)

texto_introducir_cantidad_producto = tk.Label(marco_central_crear_producto, text = "Introducir Cantidad de Productos", bg = "#E5E5E5", font = 14)
texto_introducir_cantidad_producto.grid(row = 8, column = 0, sticky = "w")

entrada_introducir_cantidad_producto = tk.Entry(marco_central_crear_producto, textvariable = var_cantidad_producto)
entrada_introducir_cantidad_producto.config(width = 50)
entrada_introducir_cantidad_producto.grid(row = 9, column = 0)

mensaje1 = ttk.Label(marco_central_crear_producto, text = "", foreground = "red")

boton_agregar_producto = tk.Button(marco_central_crear_producto, text = "Agregar", command = agregar_datos)
boton_agregar_producto.grid(row = 10, column = 0)

# Marco Buscar producto
marco_buscar_producto = tk.Frame(marco_principal_izquierda, bg = "#E5E5E5")
marco_buscar_producto.grid_columnconfigure(0, weight = 1)
marco_buscar_producto.grid_rowconfigure(0, weight = 1)

marco_central_buscar_producto = tk.Frame(marco_buscar_producto, padx = 100, pady = 100)
marco_central_buscar_producto.config(bg = "#E5E5E5")
marco_central_buscar_producto.grid(row = 0, column = 0, sticky = "sewn")

marco_central_buscar_producto.grid_columnconfigure(0, weight = 1)
marco_central_buscar_producto.grid_columnconfigure(1, weight = 1)
marco_central_buscar_producto.grid_columnconfigure(2, weight = 1)
marco_central_buscar_producto.grid_columnconfigure(3, weight = 1)
marco_central_buscar_producto.grid_rowconfigure(2, weight = 1)

texto_buscar_marca = tk.Label(marco_central_buscar_producto, text = "Buscar Marca", bg = "#E5E5E5", font = 14)
texto_buscar_marca.grid(row = 0, column = 0, sticky = "w")

entrada_buscar_marca = tk.Entry(marco_central_buscar_producto)
entrada_buscar_marca.config(width = 30)
entrada_buscar_marca.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "w")

texto_buscar_nombre_producto = tk.Label(marco_central_buscar_producto, text = "Buscar Nombre", bg = "#E5E5E5", font = 14)
texto_buscar_nombre_producto.grid(row = 0, column = 1, sticky = "w")

entrada_buscar_nombre = tk.Entry(marco_central_buscar_producto)
entrada_buscar_nombre.config(width = 30)
entrada_buscar_nombre.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "w")

texto_buscar_modelo = tk.Label(marco_central_buscar_producto, text = "Buscar Modelo", bg = "#E5E5E5", font = 14)
texto_buscar_modelo.grid(row = 0, column = 2, sticky = "w")

entrada_buscar_modelo = tk.Entry(marco_central_buscar_producto)
entrada_buscar_modelo.config(width = 30)
entrada_buscar_modelo.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "w")

texto_buscar_precio = tk.Label(marco_central_buscar_producto, text = "Buscar Precio", bg = "#E5E5E5", font = 14)
texto_buscar_precio.grid(row = 0, column = 3, sticky = "w")

entrada_buscar_precio = tk.Entry(marco_central_buscar_producto)
entrada_buscar_precio.config(width = 30)
entrada_buscar_precio.grid(row = 1, column = 3, padx = 3, pady = 3, sticky = "w")

boton_actualizar_buscar_producto = tk.Button(marco_central_buscar_producto, text = "Actualizar")
boton_actualizar_buscar_producto.config(width = 15, bg = "#99B5D1")
boton_actualizar_buscar_producto.grid(row = 0, column = 4, rowspan = 2)

lista_producto = ttk.Treeview(marco_central_buscar_producto, columns = ("IDP","Marca", "Nombre", "Modelo", "Precio", "Cantidad"), show = "headings")
lista_producto.heading("IDP", text = "IDP")
lista_producto.heading("Marca", text = "Marca")
lista_producto.heading("Nombre", text = "Nombre")
lista_producto.heading("Modelo", text = "Modelo")
lista_producto.heading("Precio", text = "Precio")
lista_producto.heading("Cantidad", text = "Cantidad")
lista_producto.grid(row = 2, column = 0,pady = 10, columnspan = 5, sticky = "esnw")

lista_producto.column("IDP", minwidth = 20, width = 50)
lista_producto.column("Marca", minwidth = 120, width = 180)
lista_producto.column("Nombre", minwidth = 120, width = 180)
lista_producto.column("Modelo", minwidth = 120, width = 180)
lista_producto.column("Precio", minwidth = 120, width = 180)
lista_producto.column("Cantidad", minwidth = 120, width = 180)



# Marco Editar producto
marco_editar_producto = tk.Frame(marco_principal_izquierda, bg = "#E5E5E5")
marco_editar_producto.grid_columnconfigure(0, weight = 1)
marco_editar_producto.grid_rowconfigure(0, weight = 1)

marco_central_editar_producto = tk.Frame(marco_editar_producto, padx = 100, pady = 100)
marco_central_editar_producto.config(bg = "#E5E5E5")
marco_central_editar_producto.grid(row = 0, column = 0, sticky = "sewn")

texto_buscar_IDP = tk.Label(marco_central_editar_producto, text = "Ingrese IDP: ", bg = "#E5E5E5", font = 14)
texto_buscar_IDP.grid(row = 0, column = 0, sticky = "w")

entrada_buscar_IDP = tk.Entry(marco_central_editar_producto)
entrada_buscar_IDP.grid(row = 0, column = 1, sticky = "w")

boton_buscar_IDP = tk.Button(marco_central_editar_producto, text = "Buscar con IDP", width = 20)
boton_buscar_IDP.grid(row = 0,column = 2)

texto_actualizar_marca_producto = tk.Label(marco_central_editar_producto, text = "Actualizar Marca del Producto", bg = "#E5E5E5", font = 14)
texto_actualizar_marca_producto.grid(row = 1, column = 0, sticky = "w")

entrada_actualizar_marca_producto = tk.Entry(marco_central_editar_producto,)
entrada_actualizar_marca_producto.config(width = 50)
entrada_actualizar_marca_producto.grid(row = 2, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_nombre_producto = tk.Label(marco_central_editar_producto, text = "Actualizar Nombre del Producto", bg = "#E5E5E5", font = 14)
texto_actualizar_nombre_producto.grid(row = 3, column = 0, sticky = "w")

entrada_actualizar_nombre_producto = tk.Entry(marco_central_editar_producto)
entrada_actualizar_nombre_producto.config(width = 50)
entrada_actualizar_nombre_producto.grid(row = 4, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_modelo_producto = tk.Label(marco_central_editar_producto, text = "Actualizar Modelo del Producto", bg = "#E5E5E5", font = 14)
texto_actualizar_modelo_producto.grid(row = 5, column = 0, sticky = "w")

entrada_actualizar_modelo_producto = tk.Entry(marco_central_editar_producto)
entrada_actualizar_modelo_producto.config(width = 50)
entrada_actualizar_modelo_producto.grid(row = 6, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_precio_producto = tk.Label(marco_central_editar_producto, text = "Actualizar Precio del Producto", bg = "#E5E5E5", font = 14)
texto_actualizar_precio_producto.grid(row = 7, column = 0, sticky = "w")

entrada_actualizar_precio_producto = tk.Entry(marco_central_editar_producto)
entrada_actualizar_precio_producto.config(width = 50)
entrada_actualizar_precio_producto.grid(row = 8, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_cantidad_producto = tk.Label(marco_central_editar_producto, text = "Actualizar Cantidad de Productos", bg = "#E5E5E5", font = 14)
texto_actualizar_cantidad_producto.grid(row = 9, column = 0, sticky = "w")

entrada_actualizar_cantidad_producto = tk.Entry(marco_central_editar_producto)
entrada_actualizar_cantidad_producto.config(width = 50)
entrada_actualizar_cantidad_producto.grid(row = 10, column = 0, columnspan = 3, sticky = "we")

# Marco CRUD Clientes

marco_CRUD_clientes = tk.Frame(marco_principal_derecha, bg = "#0A007E")

boton_CRUD_clientes = tk.Button(marco_CRUD_clientes, text = "CRUD Clientes", font = 12, bg = "#0A007E", fg = "white", highlightbackground = "black", highlightthickness = 0, command = activar_CRUD_clientes)
boton_CRUD_clientes.config(width = 25, height = 4)
boton_CRUD_clientes.grid(row = 0, column = 0, columnspan = 2)

marco_desaparecido4 = tk.Frame(marco_CRUD_clientes, bg = "#0A007E")

boton_crear_cliente = tk.Button(marco_CRUD_clientes, text = "Crear Cliente", bg = "#0A007E", fg = "white", highlightbackground = "#0A007E", highlightthickness = 0, command = crear_cliente)
boton_crear_cliente.config(height = 2)

boton_buscar_cliente = tk.Button(marco_CRUD_clientes, text = "Buscar Cliente", bg = "#0A007E", fg = "white", highlightbackground = "#0A007E", highlightthickness = 0, command = buscar_cliente)
boton_buscar_cliente.config(height = 2)

boton_editar_cliente = tk.Button(marco_CRUD_clientes, text = "Editar Cliente", bg = "#0A007E", fg = "white", highlightbackground = "#0A007E", highlightthickness = 0, command = editar_cliente)
boton_editar_cliente.config(height = 2)

botones_clientes_visibles = False

# Marco Crear cliente
marco_crear_cliente = tk.Frame(marco_principal_izquierda, bg = "#E5E5E5")
marco_crear_cliente.grid_columnconfigure(0, weight = 1)
marco_crear_cliente.grid_rowconfigure(0, weight = 1)

marco_central_crear_cliente = tk.Frame(marco_crear_cliente, padx = 100, pady = 100)
marco_central_crear_cliente.config(bg = "#E5E5E5")
marco_central_crear_cliente.grid(row = 0, column = 0, sticky = "sewn")

var_nombre_cliente = tk.StringVar()
var_apellido_paterno_cliente = tk.StringVar()
var_apellido_materno_cliente = tk.StringVar()
var_dni_cliente = tk.StringVar()
var_telefono_cliente = tk.StringVar()

texto_introducir_nombre_cliente = tk.Label(marco_central_crear_cliente, text = "Introducir Nombre del Cliente", bg = "#E5E5E5", font = 14)
texto_introducir_nombre_cliente.grid(row = 0, column = 0, sticky = "w")

entrada_introducir_nombre_cliente = tk.Entry(marco_central_crear_cliente, textvariable = var_nombre_cliente)
entrada_introducir_nombre_cliente.config(width = 50)
entrada_introducir_nombre_cliente.grid(row = 1, column = 0)

texto_introducir_apellido_paterno_cliente = tk.Label(marco_central_crear_cliente, text = "Introducir Apellido Paterno del Cliente", bg = "#E5E5E5", font = 14)
texto_introducir_apellido_paterno_cliente.grid(row = 2, column = 0, sticky = "w")

entrada_introducir_apellido_paterno_cliente = tk.Entry(marco_central_crear_cliente, textvariable = var_apellido_paterno_cliente)
entrada_introducir_apellido_paterno_cliente.config(width = 50)
entrada_introducir_apellido_paterno_cliente.grid(row = 3, column = 0)

texto_introducir_apellido_materno_cliente = tk.Label(marco_central_crear_cliente, text = "Introducir Apellido Materno del Cliente", bg = "#E5E5E5", font = 14)
texto_introducir_apellido_materno_cliente.grid(row = 4, column = 0, sticky = "w")

entrada_introducir_apellido_materno_cliente = tk.Entry(marco_central_crear_cliente, textvariable = var_apellido_materno_cliente)
entrada_introducir_apellido_materno_cliente.config(width = 50)
entrada_introducir_apellido_materno_cliente.grid(row = 5, column = 0)

texto_introducir_dni_cliente = tk.Label(marco_central_crear_cliente, text = "Introducir DNI del Cliente", bg = "#E5E5E5", font = 14)
texto_introducir_dni_cliente.grid(row = 6, column = 0, sticky = "w")

entrada_introducir_dni_cliente = tk.Entry(marco_central_crear_cliente, textvariable = var_dni_cliente)
entrada_introducir_dni_cliente.config(width = 50)
entrada_introducir_dni_cliente.grid(row = 7, column = 0)

texto_introducir_telefono_cliente = tk.Label(marco_central_crear_cliente, text = "Introducir Teléfono de Cliente", bg = "#E5E5E5", font = 14)
texto_introducir_telefono_cliente.grid(row = 8, column = 0, sticky = "w")

entrada_introducir_telefono_cliente = tk.Entry(marco_central_crear_cliente, textvariable = var_telefono_cliente)
entrada_introducir_telefono_cliente.config(width = 50)
entrada_introducir_telefono_cliente.grid(row = 9, column = 0)

mensaje2 = ttk.Label(marco_central_crear_cliente, text = "", foreground = "red")

boton_agregar_cliente = tk.Button(marco_central_crear_cliente, text = "Agregar", command = agregar_datos2)
boton_agregar_cliente.grid(row = 10, column = 0)

# Marco Buscar cliente

marco_buscar_cliente = tk.Frame(marco_principal_izquierda, bg = "#E5E5E5")
marco_buscar_cliente.grid_columnconfigure(0, weight = 1)
marco_buscar_cliente.grid_rowconfigure(0, weight = 1)

marco_central_buscar_cliente = tk.Frame(marco_buscar_cliente, padx = 100, pady = 100)
marco_central_buscar_cliente.config(bg = "#E5E5E5")
marco_central_buscar_cliente.grid(row = 0, column = 0, sticky = "sewn")

marco_central_buscar_cliente.grid_columnconfigure(0, weight = 1)
marco_central_buscar_cliente.grid_columnconfigure(1, weight = 1)
marco_central_buscar_cliente.grid_columnconfigure(2, weight = 1)
marco_central_buscar_cliente.grid_columnconfigure(3, weight = 1)
marco_central_buscar_cliente.grid_columnconfigure(4, weight = 1)
marco_central_buscar_cliente.grid_rowconfigure(2, weight = 1)

texto_buscar_nombre_cliente = tk.Label(marco_central_buscar_cliente, text = "Buscar Nombre", bg = "#E5E5E5", font = 14)
texto_buscar_nombre_cliente.grid(row = 0, column = 0, sticky = "w")

entrada_buscar_nombre_cliente = tk.Entry(marco_central_buscar_cliente)
entrada_buscar_nombre_cliente.config(width = 30)
entrada_buscar_nombre_cliente.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "w")

texto_buscar_apellido_paterno_cliente = tk.Label(marco_central_buscar_cliente, text = "Buscar Apellido Paterno", bg = "#E5E5E5", font = 14)
texto_buscar_apellido_paterno_cliente.grid(row = 0, column = 1, sticky = "w")

entrada_buscar_apellido_paterno_cliente = tk.Entry(marco_central_buscar_cliente)
entrada_buscar_apellido_paterno_cliente.config(width = 30)
entrada_buscar_apellido_paterno_cliente.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "w")

texto_buscar_apellido_materno_cliente = tk.Label(marco_central_buscar_cliente, text = "Buscar Apellido Materno", bg = "#E5E5E5", font = 14)
texto_buscar_apellido_materno_cliente.grid(row = 0, column = 2, sticky = "w")

entrada_buscar_apellido_materno_cliente = tk.Entry(marco_central_buscar_cliente)
entrada_buscar_apellido_materno_cliente.config(width = 30)
entrada_buscar_apellido_materno_cliente.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "w")

texto_buscar_dni_cliente = tk.Label(marco_central_buscar_cliente, text = "Buscar DNI", bg = "#E5E5E5", font = 14)
texto_buscar_dni_cliente.grid(row = 0, column = 3, sticky = "w")

entrada_buscar_dni_cliente = tk.Entry(marco_central_buscar_cliente)
entrada_buscar_dni_cliente.config(width = 30)
entrada_buscar_dni_cliente.grid(row = 1, column = 3, padx = 3, pady = 3, sticky = "w")

texto_buscar_telefono_cliente = tk.Label(marco_central_buscar_cliente, text = "Buscar Teléfono", bg = "#E5E5E5", font = 14)
texto_buscar_telefono_cliente.grid(row = 0, column = 4, sticky = "w")

entrada_buscar_telefono_cliente = tk.Entry(marco_central_buscar_cliente)
entrada_buscar_telefono_cliente.config(width = 30)
entrada_buscar_telefono_cliente.grid(row = 1, column = 4, padx = 3, pady = 3, sticky = "w")

boton_actualizar_buscar_cliente = tk.Button(marco_central_buscar_cliente, text = "Actualizar")
boton_actualizar_buscar_cliente.config(width = 15, bg = "#99B5D1")
boton_actualizar_buscar_cliente.grid(row = 0, column = 5, rowspan = 2)

lista_cliente = ttk.Treeview(marco_central_buscar_cliente, columns = ("IDC","Nombre", "Apellido Paterno", "Apellido Materno", "DNI", "Teléfono"), show = "headings")
lista_cliente.heading("IDC", text = "IDC")
lista_cliente.heading("Nombre", text = "Nombre")
lista_cliente.heading("Apellido Paterno", text = "Apellido Paterno")
lista_cliente.heading("Apellido Materno", text = "Apellido Materno")
lista_cliente.heading("DNI", text = "DNI")
lista_cliente.heading("Teléfono", text = "Teléfono")
lista_cliente.grid(row = 2, column = 0,pady = 10, columnspan = 6, sticky = "esnw")

lista_cliente.column("IDC", minwidth = 20, width = 50)
lista_cliente.column("Nombre", minwidth = 120, width = 180)
lista_cliente.column("Apellido Paterno", minwidth = 120, width = 180)
lista_cliente.column("Apellido Materno", minwidth = 120, width = 180)
lista_cliente.column("DNI", minwidth = 120, width = 180)
lista_cliente.column("Teléfono", minwidth = 120, width = 180)

# Marco Editar producto
marco_editar_cliente = tk.Frame(marco_principal_izquierda, bg = "#E5E5E5")
marco_editar_cliente.grid_columnconfigure(0, weight = 1)
marco_editar_cliente.grid_rowconfigure(0, weight = 1)

marco_central_editar_cliente = tk.Frame(marco_editar_cliente, padx = 100, pady = 100)
marco_central_editar_cliente.config(bg = "#E5E5E5")
marco_central_editar_cliente.grid(row = 0, column = 0, sticky = "sewn")

texto_buscar_IDC = tk.Label(marco_central_editar_cliente, text = "Ingrese IDC: ", bg = "#E5E5E5", font = 14)
texto_buscar_IDC.grid(row = 0, column = 0, sticky = "w")

entrada_buscar_IDC = tk.Entry(marco_central_editar_cliente)
entrada_buscar_IDC.grid(row = 0, column = 1, sticky = "w")

boton_buscar_IDC = tk.Button(marco_central_editar_cliente, text = "Buscar con IDP", width = 20)
boton_buscar_IDC.grid(row = 0,column = 2)

texto_actualizar_nombre_cliente = tk.Label(marco_central_editar_cliente, text = "Actualizar Nombre del Cliente", bg = "#E5E5E5", font = 14)
texto_actualizar_nombre_cliente.grid(row = 1, column = 0, sticky = "w")

entrada_actualizar_nombre_cliente = tk.Entry(marco_central_editar_cliente)
entrada_actualizar_nombre_cliente.config(width = 50)
entrada_actualizar_nombre_cliente.grid(row = 2, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_apellido_paterno_cliente = tk.Label(marco_central_editar_cliente, text = "Actualizar Apellido Paterno del Cliente", bg = "#E5E5E5", font = 14)
texto_actualizar_apellido_paterno_cliente.grid(row = 3, column = 0, sticky = "w")

entrada_actualizar_apellido_paterno_cliente = tk.Entry(marco_central_editar_cliente)
entrada_actualizar_apellido_paterno_cliente.config(width = 50)
entrada_actualizar_apellido_paterno_cliente.grid(row = 4, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_apellido_materno_cliente = tk.Label(marco_central_editar_cliente, text = "Actualizar Apellido Materno del Cliente", bg = "#E5E5E5", font = 14)
texto_actualizar_apellido_materno_cliente.grid(row = 5, column = 0, sticky = "w")

entrada_actualizar_apellido_materno_cliente = tk.Entry(marco_central_editar_cliente)
entrada_actualizar_apellido_materno_cliente.config(width = 50)
entrada_actualizar_apellido_materno_cliente.grid(row = 6, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_dni_cliente = tk.Label(marco_central_editar_cliente, text = "Actualizar DNI del Cliente", bg = "#E5E5E5", font = 14)
texto_actualizar_dni_cliente.grid(row = 7, column = 0, sticky = "w")

entrada_actualizar_dni_cliente = tk.Entry(marco_central_editar_cliente)
entrada_actualizar_dni_cliente.config(width = 50)
entrada_actualizar_dni_cliente.grid(row = 8, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_telefono_cliente = tk.Label(marco_central_editar_cliente, text = "Actualizar Teléfono del Cliente", bg = "#E5E5E5", font = 14)
texto_actualizar_telefono_cliente.grid(row = 9, column = 0, sticky = "w")

entrada_actualizar_telefono_cliente = tk.Entry(marco_central_editar_cliente)
entrada_actualizar_telefono_cliente.config(width = 50)
entrada_actualizar_telefono_cliente.grid(row = 10, column = 0, columnspan = 3, sticky = "we")

# Marco CRUD Ventas

marco_CRUD_ventas = tk.Frame(marco_principal_derecha, bg = "#0A007E")

boton_CRUD_ventas = tk.Button(marco_CRUD_ventas, text = "CRUD Ventas", font  = 12, bg = "#0A007E", fg = "white", highlightbackground = "black", highlightthickness = 0, command = activar_CRUD_ventas)
boton_CRUD_ventas.config(width = 25, height = 4)
boton_CRUD_ventas.grid(row = 0, column = 0, columnspan = 2)

marco_desaparecido5 = tk.Frame(marco_CRUD_ventas, bg = "#0A007E")


boton_hacer_venta = tk.Button(marco_CRUD_ventas, text = "Hacer Ventas", bg = "#0A007E", fg = "white", highlightbackground = "#0A007E", highlightthickness = 0, command = hacer_venta)
boton_hacer_venta.config(height = 2)

boton_buscar_venta = tk.Button(marco_CRUD_ventas, text = "Buscar Ventas", bg = "#0A007E", fg = "white", highlightbackground = "#0A007E", highlightthickness = 0, command = buscar_venta)
boton_buscar_venta.config(height = 2)

boton_editar_venta = tk.Button(marco_CRUD_ventas, text = "Editar Ventas", bg = "#0A007E", fg = "white", highlightbackground = "#0A007E", highlightthickness = 0, command = editar_venta)
boton_editar_venta.config(height = 2)

botones_ventas_visibles = False

# Marco Hacer Venta
marco_hacer_venta = tk.Frame(marco_principal_izquierda, bg = "#E5E5E5")
marco_hacer_venta.grid_columnconfigure(0, weight = 1)
marco_hacer_venta.grid_rowconfigure(0, weight = 1)

marco_central_hacer_venta = tk.Frame(marco_hacer_venta, padx = 100, pady = 100)
marco_central_hacer_venta.config(bg = "#E5E5E5")
marco_central_hacer_venta.grid(row = 0, column = 0, sticky = "sewn")

var_dni_cliente_venta = tk.StringVar()
var_marca_producto_venta = tk.StringVar()
var_nombre_producto_venta = tk.StringVar()
var_modelo_producto_venta = tk.StringVar()
var_cantidad_venta = tk.StringVar()

texto_buscar_dni_cliente_venta = tk.Label(marco_central_hacer_venta, text = "Buscar DNI del Cliente", bg = "#E5E5E5", font = 14)
texto_buscar_dni_cliente_venta.grid(row = 0, column = 0, sticky = "w")

entrada_buscar_dni_cliente_venta = tk.Entry(marco_central_hacer_venta, textvariable = var_dni_cliente_venta)
entrada_buscar_dni_cliente_venta.config(width = 50)
entrada_buscar_dni_cliente_venta.grid(row = 1, column = 0)

texto_buscar_marca_producto_venta = tk.Label(marco_central_hacer_venta, text = "Buscar Marca del Producto", bg = "#E5E5E5", font = 14)
texto_buscar_marca_producto_venta.grid(row = 2, column = 0, sticky = "w")

entrada_buscar_marca_producto_venta = tk.Entry(marco_central_hacer_venta, textvariable = var_marca_producto_venta)
entrada_buscar_marca_producto_venta.config(width = 50)
entrada_buscar_marca_producto_venta.grid(row = 3, column = 0)

texto_buscar_nombre_producto_venta = tk.Label(marco_central_hacer_venta, text = "Buscar Nombre del Producto", bg = "#E5E5E5", font = 14)
texto_buscar_nombre_producto_venta.grid(row = 4, column = 0, sticky = "w")

entrada_buscar_nombre_producto_venta = tk.Entry(marco_central_hacer_venta, textvariable = var_nombre_producto_venta)
entrada_buscar_nombre_producto_venta.config(width = 50)
entrada_buscar_nombre_producto_venta.grid(row = 5, column = 0)

texto_buscar_modelo_producto_venta = tk.Label(marco_central_hacer_venta, text = "Buscar Modelo del Producto", bg = "#E5E5E5", font = 14)
texto_buscar_modelo_producto_venta.grid(row = 6, column = 0, sticky = "w")

entrada_buscar_modelo_producto_venta = tk.Entry(marco_central_hacer_venta, textvariable = var_modelo_producto_venta)
entrada_buscar_modelo_producto_venta.config(width = 50)
entrada_buscar_modelo_producto_venta.grid(row = 7, column = 0)

texto_cantidad_venta = tk.Label(marco_central_hacer_venta, text = "Cantidad", bg = "#E5E5E5", font = 14)
texto_cantidad_venta.grid(row = 8, column = 0, sticky = "w")

entrada_cantidad_venta = tk.Entry(marco_central_hacer_venta, textvariable = var_cantidad_venta)
entrada_cantidad_venta.config(width = 50)
entrada_cantidad_venta.grid(row = 9, column = 0)

mensaje3 = ttk.Label(marco_central_hacer_venta, text = "", foreground = "red")

boton_vender = tk.Button(marco_central_hacer_venta, text = "Hacer Venta", command = agregar_datos3)
boton_vender.grid(row = 10, column = 0)

# Marco Buscar Venta

marco_buscar_venta = tk.Frame(marco_principal_izquierda, bg = "#E5E5E5")
marco_buscar_venta.grid_columnconfigure(0, weight = 1)
marco_buscar_venta.grid_rowconfigure(0, weight = 1)

marco_central_buscar_venta = tk.Frame(marco_buscar_venta, padx = 100, pady = 100)
marco_central_buscar_venta.config(bg = "#E5E5E5")
marco_central_buscar_venta.grid(row = 0, column = 0, sticky = "sewn")

marco_central_buscar_venta.grid_columnconfigure(0, weight = 1)
marco_central_buscar_venta.grid_columnconfigure(1, weight = 1)
marco_central_buscar_venta.grid_columnconfigure(2, weight = 1)
marco_central_buscar_venta.grid_columnconfigure(3, weight = 1)
marco_central_buscar_venta.grid_columnconfigure(4, weight = 1)
marco_central_buscar_venta.grid_rowconfigure(2, weight = 1)

texto_buscar_dni_cliente_venta2 = tk.Label(marco_central_buscar_venta, text = "Buscar DNI del Cliente", bg = "#E5E5E5", font = 14)
texto_buscar_dni_cliente_venta2.grid(row = 0, column = 0, sticky = "w")

entrada_buscar_dni_cliente_venta2 = tk.Entry(marco_central_buscar_venta)
entrada_buscar_dni_cliente_venta2.config(width = 30)
entrada_buscar_dni_cliente_venta2.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "w")

texto_buscar_marca_producto_venta2 = tk.Label(marco_central_buscar_venta, text = "Buscar Marca del Producto", bg = "#E5E5E5", font = 14)
texto_buscar_marca_producto_venta2.grid(row = 0, column = 1, sticky = "w")

entrada_buscar_marca_producto_venta2 = tk.Entry(marco_central_buscar_venta)
entrada_buscar_marca_producto_venta2.config(width = 30)
entrada_buscar_marca_producto_venta2.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "w")

texto_buscar_nombre_producto_venta2 = tk.Label(marco_central_buscar_venta, text = "Buscar Nombre del Producto", bg = "#E5E5E5", font = 14)
texto_buscar_nombre_producto_venta2.grid(row = 0, column = 2, sticky = "w")

entrada_buscar_nombre_producto_venta2 = tk.Entry(marco_central_buscar_venta)
entrada_buscar_nombre_producto_venta2.config(width = 30)
entrada_buscar_nombre_producto_venta2.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "w")

texto_buscar_modelo_producto_venta2 = tk.Label(marco_central_buscar_venta, text = "Buscar Modelo del Producto", bg = "#E5E5E5", font = 14)
texto_buscar_modelo_producto_venta2.grid(row = 0, column = 3, sticky = "w")

entrada_buscar_modelo_producto_venta2 = tk.Entry(marco_central_buscar_venta)
entrada_buscar_modelo_producto_venta2.config(width = 30)
entrada_buscar_modelo_producto_venta2.grid(row = 1, column = 3, padx = 3, pady = 3, sticky = "w")

texto_buscar_codigo_venta = tk.Label(marco_central_buscar_venta, text = "Buscar Código de Venta", bg = "#E5E5E5", font = 14)
texto_buscar_codigo_venta.grid(row = 0, column = 4, sticky = "w")

entrada_buscar_codigo_venta = tk.Entry(marco_central_buscar_venta)
entrada_buscar_codigo_venta.config(width = 30)
entrada_buscar_codigo_venta.grid(row = 1, column = 4, padx = 3, pady = 3, sticky = "w")

boton_actualizar_buscar_venta = tk.Button(marco_central_buscar_venta, text = "Actualizar")
boton_actualizar_buscar_venta.config(width = 15, bg = "#99B5D1")
boton_actualizar_buscar_venta.grid(row = 0, column = 5, rowspan = 2)

lista_venta = ttk.Treeview(marco_central_buscar_venta, columns = ("IDV","DNI Cliente", "Detalles Venta", "Código Venta", "Importe Venta", "Fecha"), show = "headings") # Detalles venta es una lista de compras del cliente
lista_venta.heading("IDV", text = "IDV")
lista_venta.heading("DNI Cliente", text = "DNI Cliente")
lista_venta.heading("Detalles Venta", text = "Detalles Venta")
lista_venta.heading("Código Venta", text = "Código Venta")
lista_venta.heading("Importe Venta", text = "Importe Venta")
lista_venta.heading("Fecha", text = "Fecha")
lista_venta.grid(row = 2, column = 0,pady = 10, columnspan = 6, sticky = "esnw")

lista_venta.column("IDV", minwidth = 20, width = 50)
lista_venta.column("DNI Cliente", minwidth = 120, width = 180)
lista_venta.column("Detalles Venta", minwidth = 120, width = 180)
lista_venta.column("Código Venta", minwidth = 120, width = 180)
lista_venta.column("Importe Venta", minwidth = 120, width = 180)
lista_venta.column("Fecha", minwidth = 120, width = 180)


# Marco Editar producto
marco_editar_venta = tk.Frame(marco_principal_izquierda, bg = "#E5E5E5")
marco_editar_venta.grid_columnconfigure(0, weight = 1)
marco_editar_venta.grid_rowconfigure(0, weight = 1)

marco_central_editar_venta = tk.Frame(marco_editar_venta, padx = 100, pady = 100)
marco_central_editar_venta.config(bg = "#E5E5E5")
marco_central_editar_venta.grid(row = 0, column = 0, sticky = "sewn")

texto_buscar_IDV = tk.Label(marco_central_editar_venta, text = "Ingrese IDV: ", bg = "#E5E5E5", font = 14)
texto_buscar_IDV.grid(row = 0, column = 0, sticky = "w")

entrada_buscar_IDV = tk.Entry(marco_central_editar_venta)
entrada_buscar_IDV.grid(row = 0, column = 1, sticky = "w")

boton_buscar_IDV = tk.Button(marco_central_editar_venta, text = "Buscar con IDV", width = 20)
boton_buscar_IDV.grid(row = 0,column = 2)

texto_actualizar_dni_cliente_venta = tk.Label(marco_central_editar_venta, text = "Actualizar DNI del Cliente para Venta", bg = "#E5E5E5", font = 14)
texto_actualizar_dni_cliente_venta.grid(row = 1, column = 0, sticky = "w")

entrada_actualizar_dni_cliente_venta = tk.Entry(marco_central_editar_venta)
entrada_actualizar_dni_cliente_venta.config(width = 50)
entrada_actualizar_dni_cliente_venta.grid(row = 2, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_marca_producto_venta = tk.Label(marco_central_editar_venta, text = "Actualizar Marca del Producto para Venta", bg = "#E5E5E5", font = 14)
texto_actualizar_marca_producto_venta.grid(row = 3, column = 0, sticky = "w")

entrada_actualizar_marca_producto_venta = tk.Entry(marco_central_editar_venta)
entrada_actualizar_marca_producto_venta.config(width = 50)
entrada_actualizar_marca_producto_venta.grid(row = 4, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_nombre_producto_venta = tk.Label(marco_central_editar_venta, text = "Actualizar Nombre del Producto para Venta", bg = "#E5E5E5", font = 14)
texto_actualizar_nombre_producto_venta.grid(row = 5, column = 0, sticky = "w")

entrada_actualizar_nombre_producto_venta = tk.Entry(marco_central_editar_venta)
entrada_actualizar_nombre_producto_venta.config(width = 50)
entrada_actualizar_nombre_producto_venta.grid(row = 6, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_modelo_producto_venta = tk.Label(marco_central_editar_venta, text = "Actualizar Modelo del Producto para Venta", bg = "#E5E5E5", font = 14)
texto_actualizar_modelo_producto_venta.grid(row = 7, column = 0, sticky = "w")

entrada_actualizar_modelo_producto_venta = tk.Entry(marco_central_editar_venta)
entrada_actualizar_modelo_producto_venta.config(width = 50)
entrada_actualizar_modelo_producto_venta.grid(row = 8, column = 0, columnspan = 3, sticky = "we")

texto_actualizar_cantidad_venta = tk.Label(marco_central_editar_venta, text = "Actualizar Cantidad para Venta", bg = "#E5E5E5", font = 14)
texto_actualizar_cantidad_venta.grid(row = 9, column = 0, sticky = "w")

entrada_actualizar_cantidad_venta = tk.Entry(marco_central_editar_venta)
entrada_actualizar_cantidad_venta.config(width = 50)
entrada_actualizar_cantidad_venta.grid(row = 10, column = 0, columnspan = 3, sticky = "we")

sistemaVentas.mainloop()
