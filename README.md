# Tarea 3: Tradicional vs POO - Emily Pucha

Hice esta actividad para comparar cómo cambia la estructura de un código en Python usando dos formas distintas de programar: el método tradicional con funciones y la programación orientada a objetos (POO). Como ejemplo, usé un registro de mascotas.

## Archivos del proyecto
* **programacion_tradicional/tradicional.py**: El programa que pide los datos por teclado usando funciones simples.
* **programacion_poo/mascota.py**: La clase con los atributos y métodos de la mascota.
* **programacion_poo/main.py**: El archivo principal donde creé los objetos (un loro y un conejo) para probar que todo funcione.

## Mi reflexión sobre las diferencias
* **Orden y estructura:** En el código tradicional todo es más directo pero los datos están sueltos. En cambio, con la POO todo queda bien guardado dentro de la clase `Mascota`, así que el proyecto se ve mucho más limpio y organizado.
* **Reutilizar el código:** Si usara el método tradicional y quisiera registrar 10 animales diferentes, tendría que crear un montón de variables y diccionarios, lo que se vuelve un relajo. Con POO es facilísimo porque la clase funciona como un molde: solo llamo a `Mascota` en una línea y ya tengo un animal nuevo listo con sus propios datos y sonidos.

