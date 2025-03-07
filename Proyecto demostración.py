# Importamos ABC y abstractmethod para definir una clase abstracta
from abc import ABC, abstractmethod

# ---------------------------- CLASE BASE (HERENCIA) ----------------------------

class Vehiculo(ABC):  
    """
    Clase base abstracta que representa un vehículo genérico.
    Se usa una clase abstracta para establecer una estructura común para todos los vehículos.
    """

    def __init__(self, marca, modelo, año):
        # Encapsulación: Atributos protegidos (convención: _atributo)
        self._marca = marca  
        self._modelo = modelo
        self._año = año

    @abstractmethod
    def descripcion(self):
        """
        Método abstracto que obliga a las subclases a definir su propia descripción.
        Esto es un ejemplo de polimorfismo, ya que cada subclase tendrá una implementación diferente.
        """
        pass

    def encender(self):
        """
        Método común a todos los vehículos. No es abstracto porque su implementación 
        es la misma para cualquier tipo de vehículo.
        """
        print(f"{self._marca} {self._modelo} ({self._año}) está encendido.")

# ---------------------------- SUBCLASES (HERENCIA Y POLIMORFISMO) ----------------------------

class Automovil(Vehiculo):
    """
    Subclase que representa un automóvil.
    Hereda de la clase Vehiculo y añade un nuevo atributo: número de puertas.
    """

    def __init__(self, marca, modelo, año, puertas):
        # Se llama al constructor de la clase padre para reutilizar su código
        super().__init__(marca, modelo, año)
        self._puertas = puertas  # Atributo protegido

    def descripcion(self):
        """
        Implementación del método abstracto.
        Aquí se demuestra el polimorfismo, ya que se redefine para automóviles.
        """
        return f"Automóvil: {self._marca} {self._modelo}, Año: {self._año}, Puertas: {self._puertas}"


class Motocicleta(Vehiculo):
    """
    Subclase que representa una motocicleta.
    Hereda de Vehiculo y añade un nuevo atributo: cilindrada.
    """

    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self._cilindrada = cilindrada  # Atributo protegido

    def descripcion(self):
        """
        Implementación del método abstracto.
        Se personaliza la salida para motocicletas, demostrando polimorfismo.
        """
        return f"Motocicleta: {self._marca} {self._modelo}, Año: {self._año}, Cilindrada: {self._cilindrada}cc"


# ---------------------------- POLIMORFISMO ----------------------------

def mostrar_descripcion(vehiculo):
    """
    Función que recibe cualquier tipo de vehículo y muestra su descripción.
    Ejemplo de polimorfismo: se puede pasar un Automovil o una Motocicleta,
    y la función llamará automáticamente su respectivo método descripcion().
    """
    print(vehiculo.descripcion())


# ---------------------------- LISTA DE VEHÍCULOS ----------------------------

# Lista para almacenar los vehículos registrados
vehiculos = []  

def agregar_vehiculo():
    """
    Permite al usuario agregar un nuevo vehículo al sistema.
    Se solicita información por teclado y se crea una instancia de Automovil o Motocicleta.
    """
    tipo = input("Ingrese el tipo de vehículo (auto/moto): ").strip().lower()

    # Se piden datos generales para cualquier vehículo
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    año = input("Año: ").strip()

    # Se determina el tipo de vehículo y se instancian los objetos correspondientes
    if tipo == "auto":
        puertas = int(input("Número de puertas: "))
        vehiculo = Automovil(marca, modelo, año, puertas)
    elif tipo == "moto":
        cilindrada = int(input("Cilindrada (cc): "))
        vehiculo = Motocicleta(marca, modelo, año, cilindrada)
    else:
        print("Tipo de vehículo no reconocido. Intente nuevamente.")
        return  # Se sale de la función sin agregar nada

    # Se almacena el objeto en la lista de vehículos
    vehiculos.append(vehiculo)
    print("Vehículo agregado con éxito.")

def listar_vehiculos():
    """
    Muestra una lista de todos los vehículos registrados en el sistema.
    """
    if not vehiculos:
        print("No hay vehículos registrados.")
    else:
        print("\nListado de vehículos:")
        for i, vehiculo in enumerate(vehiculos, start=1):
            print(f"{i}. {vehiculo.descripcion()}")  # Se usa polimorfismo

# ---------------------------- MENÚ INTERACTIVO ----------------------------

while True:
    """
    Se implementa un menú interactivo que permite al usuario
    agregar vehículos o listar los registrados.
    """
    print("\n--- SISTEMA DE GESTIÓN DE VEHÍCULOS ---")
    print("1. Agregar un vehículo")
    print("2. Listar vehículos")
    print("3. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_vehiculo()
    elif opcion == "2":
        listar_vehiculos()
    elif opcion == "3":
        print("Saliendo del programa...")
        break  # Termina el bucle y finaliza el programa
    else:
        print("Opción no válida. Intente de nuevo.")
