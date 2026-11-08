"""Ejercicio 10 - Agenda de contactos"""

class Agenda:
    def __init__(self):
        self.contactos = []  # lista de diccionarios

    # Agrega un contacto si su DNI no está registrado
    def agregar_contacto(self, nombre, telefono, email, dni):
        if any(contacto["dni"] == dni for contacto in self.contactos):
            print("No se agregó a {}: el DNI {} ya existe".format(nombre, dni))
            return False
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email, "dni": dni})
        return True

    def mostrar_contactos(self):
        print("Agenda de contactos:")
        for c in self.contactos:
            print("- {} | Tel: {} | Email: {} | DNI: {}".format(c["nombre"], c["telefono"], c["email"], c["dni"]))

    # Retorna el contacto con ese DNI o None si no existe
    def buscar_por_dni(self, dni):
        for contacto in self.contactos:
            if contacto["dni"] == dni:
                return contacto
        print("No se encontraron coincidencias para el DNI", dni)
        return None

# Programa principal con datos definidos
agenda = Agenda()
agenda.agregar_contacto("Ana Torres", "987654321", "ana.torres@correo.com", "45678912")
agenda.agregar_contacto("Pedro Ruiz", "912345678", "pedro.ruiz@correo.com", "41234567")
agenda.agregar_contacto("Lucía Vega", "956789123", "lucia.vega@correo.com", "47891234")
agenda.agregar_contacto("Juan Soto", "900111222", "juan.soto@correo.com", "45678912")  # DNI repetido
agenda.mostrar_contactos()

# Búsquedas: una existente y otra inexistente
for dni in ("41234567", "99999999"):
    contacto = agenda.buscar_por_dni(dni)
    if contacto:
        print("Contacto encontrado:", contacto)
