# Importante que el codigo se abra en una carpeta con "Open Folder"
# importaciones
import datetime
from datetime import datetime
from getpass import getpass
import os
from random import randint

# diccionario de usuarios con varios usuarios registrados con sus respectivas contraseñas
usuarios={'Steven': '1234', 'Otero':'5678', 'a':'123'}  #usuarios ya registrados para comprobar el inicio de sesión
carritoUnidades={}  #lista con las unidades de cada producto añadido (en orden)
carritoPrecios={}  #diccionario con el precio y el nombre de cada producto añadido (en orden)
class Persona:# Clase persona con los métodos de registro e inicio de sesión

    def __init__(self) -> None:
        self.usuario=None
        self.contraseña=None
        self.repetirContraseña=None

    def registro(self): # Método de registro de usuarios
        while True:
            self.usuario=input('Indique su nombre de usuario: ') # Insercion de nombre de usuario
            for k in usuarios: # Busca en el diccionario "usuarios" si el usuario introducido ya existe
                if k==self.usuario: # Si existe, determina que "u" (variable llamada así por falta de creatividad) es True
                    u=True
                    break
                else: # Si no existe, determina que "u" es False
                    u=False
            if u==True: # Si "u" es True muestra lo siguiente y no te permite seguir adelante hasta que pongas un usuario válido
                os.system('cls')
                print('Ese usuario ya está registrado, por favor, prueba con otro.')
                continue
            else: # Si "u" es False te deja avanzar
                print('El usuario es válido')

            self.contraseña=getpass('Ponga una contraseña: ')
            self.repetirContraseña=getpass('Repita la contraseña: ')
            
            if self.contraseña!=self.repetirContraseña: #si la primera y la segunda contraseña introducidas no coinciden da error 
                os.system('cls')
                print('Las contraseñas no son iguales, por favor introduzca los datos correctamente.')
            else: # si coinciden las dos contraseñas, guarda en un diccionario el usuario como clave y la contraseña como valor  
                usuarios[self.usuario] = self.contraseña
                os.system('cls')
                print(f'----------Bienvenido a la PacoTienda, {self.usuario}----------')
                break
    @staticmethod
    def login(): # Método de inicio de sesión de Usuarios 
        try:
            if usuarios: # Si el diccionario usuarios tiene datos hace lo siguiente, si no, muestra que no hay usuarios registrados
                nombreUsuario=input('Cual es tu nombre de usuario: ')
                contraseña=input('Cual era la contraseña del usuario: ')
                for k,v in usuarios.items(): # Comprueba usuario por usuario si la clave y el valor coinciden con los datos introducidos
                    if k==nombreUsuario and v ==contraseña: # Si coinciden, determina que "a" (variable así llamada por falta de creatividad) es true
                        print('Holii')
                        a=True
                        break
                    else: # Si no coinciden, determina que "a" es False
                        a=False
                if a==False: # Si "a" es False, da error
                    print('El usuario no está registrado o se han introducido mal los datos')
                    exit()
                else: # Si "a" es True te mete en el sistema
                    os.system('cls')
                    print(f'----------¡Bienvenido de nuevo a la PacoTienda, {nombreUsuario}!----------')              
            else: # 
                print('No hay ningun usuario')
                exit()
        except:
            pass
            exit()
p1=Persona() # instanciando la persona
class Productos:
    def __init__(self,nombre,precio) -> None:
        self.nombre=nombre
        self.precio=precio
        self.unidades=None
    def elegirUnidades(self): # Método de elección de unidades
        os.system('cls')
        while True:
            sino=input(f'¿Estas seguro que quieres comprar {self.nombre}?  (Si, cualquier tecla para no) ')
            if sino.lower()=='si': # te pregunta si de verdad quieres comprar el producto
                try:
                    self.unidades=int(input('Indique la cantidad que quiera adquirir: ')) # si es así te pregunta cuantas unidades quieres
                    precioProducto=self.precio*self.unidades # multiplica el precio del producto por las unidades
                    carritoPrecios[self.nombre]=precioProducto # inserta el nombre del producto con su precio en el diccionario carritoPrecios
                    carritoUnidades[self.nombre]=self.unidades # inserta el nombre del producto con sus unidades en el diccionario carritoUnidades
                    break
                except:
                    print('Eso no es una unidad') 
                    exit()
            else: # si no querias comprar el producto te devuelve a la interfaz de antes
                break
# Clases para cada producto heredando de la clase Productos
class Camisas(Productos):
    pass
class Pantalones(Productos):
    pass
class Zapatillas(Productos):
    pass
class Sudaderas(Productos):
    pass
class Chaquetas(Productos):
    pass

# instanciar los productos
camisa1=Camisas('Camisa Roja',23)
camisa2=Camisas('Camisa Azul',20)
pantalon1=Pantalones('Pantalones Naranjas', 19.99)
pantalon2=Pantalones('Pantalones Azules', 19)
zapatillas1=Zapatillas('Zapatillas Negras', 14.99)
zapatillas2=Zapatillas('Zapatillas Blancas', 16)
sudadera1=Sudaderas('Sudadera Morada', 24.99)
sudadera2=Sudaderas('Sudadera Blanca', 22)
chaquetas1=Chaquetas('Chaqueta Amarilla', 10)
chaquetas2=Chaquetas('Chaqueta Azul', 10.95)

class Factura: # Clase factura para calcular totales y hacer un archivo de texto con todos los datos
    @staticmethod 
    def factura(): # Método para calcular la factura y meterla en un archivo de texto
        sumaPrecio=0
        nacionalidad=input('Inserte el páis de procedencia (Si es de fuera de España inserte "internacional"): ') # Aqui te pide la nacionalidad
        try: 
            if nacionalidad.lower()=='españa': # Si la nacionalidad introducida es España entonces el IVA es del 21%
                iva=21
            else: # Si la nacionalidad introducida no es España entonces el iva es 15%
                iva=15
        except:
            print('Algo ha ido mal')
        nombre=input('Nombre: ')
        apellidos=input('Apellidos: ')
        Email=input('Correo electronico: ')
        dni=input('DNI: ')
        telefono=input('Teléfono: ')
        ciudad=input('Ciudad de residencia: ')
        direccion=input('Indique su dirección: ')
        cp=input('Indique su codigo postal: ')
        numeroTarjeta=input('Número de su tarjeta: ')

        for k,v in carritoPrecios.items(): # Aqui busca producto por producto en el diccionario "carritoPrecios" para sumar todos los precio
            sumaPrecio=sumaPrecio+v
        ivaTotal=(sumaPrecio*iva)/100 # Calcula el IVA en base al total
        totalconIVA=sumaPrecio+ivaTotal # Suma el IVA calculado con el total de de todos los precios
        os.system('cls')
        # print(carrito)
        hoy=datetime.now() # Aqui pone la fecha de hoy en la variable "Hoy"
        hoyFormateado=hoy.strftime('%d/%m/%Y') # Aqui le da formato para que quede de la forma que yo quiera
        with open('factura.txt','w') as f: # Aqui escribe todos los apartados antes mencionados en un documento de texto
            f.write(f'FACTURA\n')
            f.write(f'----------------------------\n')
            f.write(f'Datos del cliente:\n')
            f.write(f'{nombre} {apellidos}\n')
            f.write(f'{dni}\n')
            f.write(f'{cp}, {ciudad}\n')
            f.write(f'{direccion}\n')
            f.write(f'{telefono}\n')
            f.write(f'----------------------------\n')
            f.write(f'Numero de la factura: {randint(5000,6000)}\n')
            f.write(f'Fecha de la factura: {hoyFormateado}\n')
            f.write(f'----------------------------\n')
            for k,v in carritoPrecios.items():
                f.write(f'Producto: {k}         Cantidad:{carritoUnidades[k]}      Precio: {round(v,2)}€\n')
            f.write(f'----------------------------\n')
            f.write(f'Total Base Imponible: {round(sumaPrecio,2)}€\n')
            f.write(f'Total I.V.A. {iva}%: {round(ivaTotal,2)}€\n')
            f.write(f'TOTAL: {round(totalconIVA,2)}€\n')
            f.write(f'----------------------------\n')        
        print(f'Se ha efectuado tu compra. ¡Gracias por confiar en nosotros!')
        print(f'Te acabamos de mandar la factura al correo {Email} y un SMS al telefono {telefono} para confirmar su pedido')
        print(f'Hasta la proxima')
        exit()
factura1=Factura() # instanciando la factura

def carrito(): # funcion del carrito
    while True:
        if carritoPrecios: # Si el diccionario de carrito tiene valores dentro hace el siguiente proceso
            os.system('cls')
            print(f'Tu Carrito')
            print(f'----------------------------')
            for k,v in carritoPrecios.items(): # muestra uno por uno los productos que hemos introducido en el carrito con sus unidades y su precio
                print(f'Producto: {k}         Cantidad:{carritoUnidades[k]}      Precio: {round(v,2)}€\n')
            print(f'---------------------------')
            print(f'| 1. Seguir comprando     |')
            print(f'| 2. Pagar ya             |')
            print(f'| 3. Eliminar un producto |')
            print(f'---------------------------')
            opcion=input('Elije una opción: ') # elije una opcion de las mostradas
            match opcion:
                case '1': # Si elije la primera le devuelve a la tienda
                    os.system('cls')
                    break
                case '2':
                    factura1.factura() # Si elije la segunda se va a pagar
                    
                case '3': # si elije la tercera se le muestra un menu para introducir el producto que desea eliminar
                    while True:
                        print('----------------Eliminar producto-----------------')
                        eliminarProduco=input('Escriba el nombre del producto que quiera eliminar: ')
                        for k,v in carritoPrecios.items(): # busca el producto introducido entre los diferentes productos que hay
                            if k==eliminarProduco: # si el producto está, elimina el producto y define la variable "a" como True y acaba el bucle
                                carritoPrecios.pop(eliminarProduco)
                                carritoUnidades.pop(eliminarProduco)
                                print('Se ha eliminado el producto')
                                a=True
                                break
                            else: # si el producto no está, define la variable "a" como False
                                a=False
                        if a==True: # Si "a" es True, se acaba el bucle
                            break
                        else: # si a no es true, el bule sigue porque significa que no se ha introducido bien el producto
                            print('No se encuentra el producto elegido, introduzca bien el nombre del producto')
        else: # si el diccionario de carrito está vacio muestra el siguiente proceso y vuelve a la tienda
            os.system('cls')
            print('Tu carrito')
            print('----------------------------')
            print('Tu carrito esta vacio')
            print('----------------------------')                    
            print('')
            break
# Apartado del menú e inputs para este
try:
    def interfaz_menu():    #funcion del menu
        os.system('cls')
        print('--------- Menú ---------')
        print('| 1. Crea una cuenta   |')
        print('| 2. Iniciar sesión    |')
        print('------------------------')
    interfaz_menu()
    decisionMenu=int(input('Escoja una opción del menú: ')) # elige entre las 2 opciones
    os.system('cls')
    if decisionMenu==1: # si elige la primera opcion se va a la funcion de registro
        p1.registro()
    elif decisionMenu==2: # si elige la segunda opcion se va a la funcion de login
        p1.login()
    else: # si no es ninguna de las opciones anteriores no se ejecuta nada
        print('No hay ninguna opción así')
        exit()
except:
    print()
    exit()

class seguir: # clase para seguir comprando
    @staticmethod
    def seguirComprando():
        print('-----------------------------')
        print('| 1. Seguir comprando       |')
        print('| 2. Ver carrito            |')
        print('| 3. Pagar ya               |')
        print('-----------------------------')
        seguirComprando=input('Eliga una opción: ') # elige una opcion
        if seguirComprando=='1': # si elige la primera opcion vuelve a la tienda para seguir comprando
            os.system('cls')
            elegir()
        elif seguirComprando=='2': # si elige la segunda opcion va a la funcion del carrito
            carrito()
        else: # si es la tercera opcion se va a la funcion de factura en la clase factura
            factura1.factura()
seguir1=seguir()
# Mostrar los productos
def elegir(): # Funcion del catálogo
    while True:
        print('----------Productos----------')
        print('| 1. Camisas                |')
        print('| 2. Pantalones             |')
        print('| 3. Zapatillas             |')
        print('| 4. Sudaderas              |')
        print('| 5. Chaquetas              |')
        print('-----------------------------')
        print('| 6. Ver carrito            |')
        print('| 7. Salir                  |')
        print('-----------------------------')
        decisionMenu_Productos=input('Elija una opción: ') #elige una de las opciones
        match decisionMenu_Productos:
            case '1': # si elige la primera muestra las camisas
                os.system('cls')
                print('--------------------------')
                print('| 1. Camisa Roja - 23€ |')
                print('| 2. Camisa Azul - 20€ |')
                print('--------------------------')
                print('3. Volver')
                print('4. Salir')
                print('--------------------------')
                opcionCami=input('Elija una opción: ')
                match opcionCami:
                    case '1': # si elige la primera se va a la función de elección de unidades en la clase camisa
                        camisa1.elegirUnidades()
                        seguir1.seguirComprando()
                    case '2': # si elige la segunda se va a la función de eleccion de unidades en la clase camisa
                        camisa2.elegirUnidades()
                        seguir1.seguirComprando()
                    case '3':# si elige la tercera vuelve a mostrar la sección de antes
                        os.system('cls') 
                        continue
                    case '4': # si elige la cuarta termina el programa
                        print('¡Hasta la proxima!')
                        exit()
                    case _: # si elige cualquier otra cosa vuelve
                        os.system('cls')
                        pass
            case '2': # si elige la segunda muestra los pantalones
                os.system('cls')
                print('-----------------------------------')
                print('| 1. Pantalones Naranjas - 19.99€ |')
                print('| 2. Pantalones Azules - 19€      |')
                print('-----------------------------------')
                print('3. Volver')
                print('4. Salir')
                print('--------------------------')
                opcionPanta=input('Elija una opción: ')
                match opcionPanta:
                    case '1':# si elige la primera se va a la función de elección de unidades en la clase pantalón
                        pantalon1.elegirUnidades()
                        seguir1.seguirComprando()
                    case '2':# si elige la segunda se va a la función de eleccion de unidades en la clase pantalón
                        pantalon2.elegirUnidades()
                        seguir1.seguirComprando()
                    case '3':# si elige la tercera vuelve a mostrar la sección de antes
                        os.system('cls')
                        continue
                    case '4':# si elige la cuarta termina el programa
                        print('¡Hasta la proxima!')
                        exit()
                    case _:# si elige cualquier otra cosa vuelve
                        os.system('cls')
                        pass
            case '3': # si elige la tercera muestra las zapatillas
                os.system('cls')
                print('---------------------------------')
                print('| 1. Zapatillas Negras - 14.99€ |')
                print('| 2. Zapatillas Blancas - 16€   |')
                print('---------------------------------')
                print('3. Volver')
                print('4. Salir')
                print('--------------------------')
                opcionZapa=input('Elija una opción: ')
                match opcionZapa:
                    case '1':# si elige la primera se va a la función de elección de unidades en la clase zapatillas
                        zapatillas1.elegirUnidades()
                        seguir1.seguirComprando()
                    case '2':# si elige la segunda se va a la función de eleccion de unidades en la clase zapatillas
                        zapatillas2.elegirUnidades()
                        seguir1.seguirComprando()
                    case '3':# si elige la tercera vuelve a mostrar la sección de antes
                        os.system('cls')
                        continue
                    case '4':# si elige la cuarta termina el programa
                        print('¡Hasta la proxima!')
                        exit()
                    case _:# si elige cualquier otra cosa vuelve
                        os.system('cls')
                        pass
            case '4': # si elige la cuarta muestra las sudaderas
                os.system('cls')
                print('-------------------------------')
                print('| 1. Sudadera Morada - 24.99€ |')
                print('| 2. Sudadera Blanca - 22€    |')
                print('-------------------------------')
                print('3. Volver')
                print('4. Salir')
                print('--------------------------')
                opcionSudadera=input('Elija una opción: ')
                match opcionSudadera:
                    case '1':# si elige la primera se va a la función de elección de unidades en la clase sudadera
                        sudadera1.elegirUnidades()
                        seguir1.seguirComprando()
                    case '2':# si elige la segunda se va a la función de eleccion de unidades en la clase sudadera
                        sudadera2.elegirUnidades()
                        seguir1.seguirComprando()
                    case '3':# si elige la tercera vuelve a mostrar la sección de antes
                        os.system('cls')
                        continue
                    case '4':# si elige la cuarta termina el programa
                        print('¡Hasta la proxima!')
                        exit()
                    case _:# si elige cualquier otra cosa vuelve
                        os.system('cls')
                        pass
            case '5':  # si elige la quinta muestra las chaquetas
                os.system('cls')
                print('------------------------------')
                print('| 1. Chaqueta Amarilla - 10€ |')
                print('| 2. Chaqueta Azul - 10.95€  |')
                print('------------------------------')
                print('3. Volver')
                print('4. Salir')
                print('--------------------------')
                opcionChaqueta=input('Elija una opción: ')
                match opcionChaqueta:
                    case '1':# si elige la primera se va a la función de elección de unidades en la clase chaquetas
                        chaquetas1.elegirUnidades()
                        seguir1.seguirComprando()
                    case '2':# si elige la segunda se va a la función de eleccion de unidades en la clase chaquetas
                        chaquetas2.elegirUnidades()
                        seguir1.seguirComprando()
                    case '3':# si elige la tercera vuelve a mostrar la sección de antes
                        os.system('cls')
                        continue
                    case '4':# si elige la cuarta termina el programa
                        print('¡Hasta la proxima!')
                        exit()
                    case _:# si elige cualquier otra cosa vuelve
                        os.system('cls')
                        pass
            case '6':  # si elige la sexta muestra el carrito
                carrito()      
            case '7': # si elige la septima acaba el programa
                print('¡Hasta la proxima!')
                exit()
            case _:  # si elige cualquie otra cosa muestra un error
                os.system('cls')
                print('No se encuentra esa opcion, por favor, elija una opción: ')               
elegir()
