from mascota import Mascota

if __name__ == "__main__":
    m1 = Mascota("Paco", "Loro", 5)
    m2 = Mascota("Tambor", "Conejo", 1)

    m1.mostrar_informacion()
    m1.hacer_sonido()
    
    print("-" * 30)

    m2.mostrar_informacion()
    m2.hacer_sonido()
  
