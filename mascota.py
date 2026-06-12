class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Mascota: {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años")

    def hacer_sonido(self):
        if "loro" in self.especie.lower():
            print(f"{self.nombre} dice: ¡Hola! ¡Hola!")
        elif "conejo" in self.especie.lower():
            print(f"{self.nombre} hace: *Sniff sniff*")
        else:
            print(f"{self.nombre} hace un sonido.")
            
