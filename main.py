import numpy as np
import time
import sys
import tkinter as tk
from tkinter import messagebox

# Crea la ventana principal
ventana = tk.Tk()
ventana.title("Batalla Pokémon")

# Crear la clase Pokemon
class Pokemon:
    def __init__(self, nombre, tipo, movimientos, EVs, salud='==================='):
        # save variables as attributes
        self.nombre = nombre
        self.tipo = tipo
        self.movimientos = movimientos
        self.ATAQUE = EVs['ATAQUE']
        self.DEFENSA = EVs['DEFENSA']
        self.salud = salud
        self.barras = 20 # Cantidad de barras de salud


    def pelear(self, Pokemon2):
        # Permite que dos Pokemones peleen entre si

        # Informacion de la pelea
        print("-----BATALLA POKEMON-----")
        print(f"\n{self.nombre}")
        print("TIPO/", self.tipo)
        print("ATAQUE/", self.ATAQUE)
        print("DEFENSA/", self.DEFENSA)
        print("LVL/", 3*(1+np.mean([self.ATAQUE,self.DEFENSA])))
        print("\nVS")
        print(f"\n{Pokemon2.nombre}")
        print("TIPO/", Pokemon2.tipo)
        print("ATAQUE/", Pokemon2.ATAQUE)
        print("DEFENSA/", Pokemon2.DEFENSA)
        print("LVL/", 3*(1+np.mean([Pokemon2.ATAQUE,Pokemon2.DEFENSA])))

        time.sleep(2)

        # Considerando los tipos de ventajas y desventajas
        version = ['Fuego', 'Agua', 'Hoja']
        for i,k in enumerate(version):
            if self.tipo == k:
                # Son del MISMO TIPO
                if Pokemon2.tipo == k:
                    string_1_ATAQUE = '\nNo es muy efectivo...'
                    string_2_ATAQUE = '\nNo es muy efectivo...'

                # Pokemon2 es FUERTE
                if Pokemon2.tipo == version[(i+1)%3]:
                    Pokemon2.ATAQUE *= 2
                    Pokemon2.DEFENSA *= 2
                    self.ATAQUE /= 2
                    self.DEFENSA /= 2
                    string_1_ATAQUE = '\nNo es muy efectivo...'
                    string_2_ATAQUE = '\nEs muy efectivo!'

                # Pokemon2 es DEBIL
                if Pokemon2.tipo == version[(i+2)%3]:
                    self.ATAQUE *= 2
                    self.DEFENSA *= 2
                    Pokemon2.ATAQUE /= 2
                    Pokemon2.DEFENSA /= 2
                    string_1_ATAQUE = '\nEs muy efectivo!'
                    string_2_ATAQUE = '\nNo es muy efectivo...'


        # Para la pelea actual
        # Continuar mientras el Pokemon tenga salud
        while (self.barras > 0) and (Pokemon2.barras > 0):
            # Imprime la salud de cada Pokemon
            print(f"\n{self.nombre}\t\tSALUD\t{self.salud}")
            print(f"{Pokemon2.nombre}\t\tSALUD\t{Pokemon2.salud}\n")

            print(f"{self.nombre} ve!")
            for i, x in enumerate(self.movimientos):
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            delay_print(f"\n{self.nombre} uso {self.movimientos[index-1]}!")
            time.sleep(1)
            delay_print(string_1_ATAQUE)

            # Determinando el daño
            Pokemon2.barras -= self.ATAQUE
            Pokemon2.salud = ""

            # Agregar barras de refuerso por la DEFENSA del Pokemon 
            for j in range(int(Pokemon2.barras+.1*Pokemon2.DEFENSA)):
                Pokemon2.salud += "="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tSALUD\t{self.salud}")
            print(f"{Pokemon2.nombre}\t\tSALUD\t{Pokemon2.salud}\n")
            time.sleep(.5)

            # Revisar si fue derrotado el Pokemon
            if Pokemon2.barras <= 0:
                delay_print("\n..." + Pokemon2.nombre + ' derrotado.')
                break

            # Turno del Pokemon2

            print(f"Go {Pokemon2.nombre}!")
            for i, x in enumerate(Pokemon2.movimientos):
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            delay_print(f"\n{Pokemon2.nombre} used {Pokemon2.movimientos[index-1]}!")
            time.sleep(1)
            delay_print(string_2_ATAQUE)

            # Determinando el daño
            self.barras -= Pokemon2.ATAQUE
            self.salud = ""

            # Agregar barras de refuerso por la DEFENSA del Pokemon
            for j in range(int(self.barras+.1*self.DEFENSA)):
                self.salud += "="

            time.sleep(1)
            print(f"{self.nombre}\t\tSALUD\t{self.salud}")
            print(f"{Pokemon2.nombre}\t\tSALUD\t{Pokemon2.salud}\n")
            time.sleep(.5)

            # Revisar si fue derrotado el Pokemon
            if self.barras <= 0:
                delay_print("\n..." + self.nombre + ' derrotado.')
                break

        money = np.random.choice(5000)
        delay_print(f"\nEl oponente te pago ${money} por haber perdido.\n")




# Crea una etiqueta para mostrar el nombre del Pokémon 1
etiqueta_pokemon1 = tk.Label(ventana, text="Nombre del Pokémon 1:")
etiqueta_pokemon1.pack()

# Crea una caja de texto para ingresar el nombre del Pokémon 1
caja_pokemon1 = tk.Entry(ventana)
caja_pokemon1.pack()

# Crea una etiqueta para mostrar el tipo del Pokémon 1
etiqueta_tipo1 = tk.Label(ventana, text="Ataque del pokemon 1:")
etiqueta_tipo1.pack()

# Crea una caja de texto para ingresar el tipo del Pokémon 1
caja_tipo1 = tk.Label(ventana)
caja_tipo1.pack()

# Crea una etiqueta para mostrar el nombre del Pokémon 2
etiqueta_pokemon2 = tk.Label(ventana, text="Nombre del Pokémon 2:")
etiqueta_pokemon2.pack()

# Crea una caja de texto para ingresar el nombre del Pokémon 2
caja_pokemon2 = tk.Entry(ventana)
caja_pokemon2.pack()

# Crea una etiqueta para mostrar el tipo del Pokémon 2
etiqueta_tipo2 = tk.Label(ventana, text="Ataque del Pokémon 2:")
etiqueta_tipo2.pack()

# Crea una caja de texto para ingresar el tipo del Pokémon 2
caja_tipo2 = tk.Label(ventana)
caja_tipo2.pack()

# Crea una etiqueta para mostrar el resultado de la pelea
etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.pack()

# Crea una caja de texto para mostrar el resultado de la pelea
caja_resultado = tk.Text(ventana, height=10, width=50)
caja_resultado.pack()

# Crea un botón para iniciar la pelea
boton_pelear = tk.Button(ventana, text="Pelear", command="pelear")
boton_pelear.pack()

# Inicia la ventana principal
ventana.mainloop()


# Retraso del texto (saque la idea de un chabon de StackOverflow)

def delay_print(s):
    # Imprime una letra por vez
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)










if __name__ == '__main__':
    #Create Pokemon
    Charizard = Pokemon('Charizard', 'Fuego', ['Lanzallamas', 'Vuelo', 'Anillo Ígneo', 'Puño Fuego'], {'ATAQUE':12, 'DEFENSA': 8})
    Blastoise = Pokemon('Blastoise', 'Agua', ['Disparo Agua', 'Rayo Burbuja', 'Hidrobomba', 'Surf'],{'ATAQUE': 10, 'DEFENSA':10})
    Venusaur = Pokemon('Venusaur', 'Hoja', ['Látigo Cepa', 'Hoja Razor', 'Terremoto', 'Planta loca'],{'ATAQUE':8, 'DEFENSA':12})

    Charmander = Pokemon('Charmander', 'Fuego', ['Brasas', 'Arañar', 'Golpe', 'Puño Fuego'],{'ATAQUE':4, 'DEFENSA':2})
    Squirtle = Pokemon('Squirtle', 'Agua', ['Rayo Burbuja', 'Golpe', 'Golpe Cabeza', 'Surf'],{'ATAQUE': 3, 'DEFENSA':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Hoja', ['Látigo Cepa', 'Hoja Razor', 'Golpe', 'Semilla Sanguijuela'],{'ATAQUE':2, 'DEFENSA':4})

    Charmeleon = Pokemon('Charmeleon', 'Fuego', ['Brasas', 'Arañar', 'Lanzallamas', 'Puño Fuego'],{'ATAQUE':6, 'DEFENSA':5})
    Wartortle = Pokemon('Wartortle', 'Agua', ['Rayo Burbuja', 'Disparo Agua', 'Golpe Cabeza', 'Surf'],{'ATAQUE': 5, 'DEFENSA': 5})
    Ivysaur = Pokemon('Ivysaur\t', 'Hoja', ['Látigo Cepa', 'Hoja razor', 'Semilla Bala', 'Semilla Sanguijuela'],{'ATAQUE':4, 'DEFENSA':6})



    Bulbasaur.pelear(Charizard) # Pelea!
    
    