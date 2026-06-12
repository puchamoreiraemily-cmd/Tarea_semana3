def registrar():
    print("--- REGISTRO DE MASCOTA ---")
    nom = input("Nombre: ")
    esp = input("Especie (ej. Loro, Conejo): ")
    edad = input("Edad: ")
    return nom, esp, edad

def mostrar(nom, esp, edad):
    print("\n--- DATOS DE LA MASCOTA ---")
    print(f"Nombre:  {nom}")
    print(f"Especie: {esp}")
    print(f"Edad:    {edad} años")

if __name__ == "__main__":
    n, e, ed = registrar()
    mostrar(n, e, ed)
    
