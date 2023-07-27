import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring

class App(tkinter.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Simulacro Parcial")

        self.btn_cargar = tkinter.Button(master=self, text="Cargar Pokedex", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
        
        self.btn_mostrar = tkinter.Button(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar = tkinter.Button(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_nombre = []
        self.lista_tipo = []
        self.lista_poder = []

    def btn_cargar_on_click(self):
        for i in range(10):
            nombre = askstring("Ingrese el nombre del Pokemon:")
            tipo = askstring("Ingrese el tipo del Pokemon (Agua, Tierra, Psiquico, Fuego, Electrico):")
            poder = int(askstring("Ingrese la cantidad de poder (entre 50 y 200):"))
            
            # Validating input for power
            while poder < 50 or poder > 200:
                alert("Error", "El poder debe ser mayor a 50 y menor a 200.")
                poder = int(askstring("Ingrese la cantidad de poder (entre 50 y 200):"))
            
            self.lista_nombre.append(nombre)
            self.lista_tipo.append(tipo)
            self.lista_poder.append(poder)

    def btn_mostrar_on_click(self):
        max_power = 0
        max_power_index = None
        
        for i in range(len(self.lista_nombre)):
            if self.lista_tipo[i].lower() in ["fuego", "agua"]:
                if self.lista_poder[i] > max_power:
                    max_power = self.lista_poder[i]
                    max_power_index = i
        
        if max_power_index is not None:
            alert("Pokemon con mayor poder", f"Nombre: {self.lista_nombre[max_power_index]}\nTipo: {self.lista_tipo[max_power_index]}\nPoder: {self.lista_poder[max_power_index]}")
        else:
            alert("No se encontraron pokemones de tipo fuego o agua.", "")

    def btn_informar_on_click(self):
        num_fuego = self.lista_tipo.count("Fuego")
        num_electrico = self.lista_tipo.count("Electrico")

        max_power_index = self.lista_poder.index(max(self.lista_poder))
        min_power_index = self.lista_poder.index(min(self.lista_poder))

        max_power_pokemon_info = f"Nombre: {self.lista_nombre[max_power_index]}\nTipo: {self.lista_tipo[max_power_index]}\nPoder: {self.lista_poder[max_power_index]}"
        min_power_pokemon_info = f"Nombre: {self.lista_nombre[min_power_index]}\nTipo: {self.lista_tipo[min_power_index]}\nPoder: {self.lista_poder[min_power_index]}"
        
        powers_over_100 = sum(1 for power in self.lista_poder if power > 100)
        powers_under_100 = sum(1 for power in self.lista_poder if power < 100)

        tipos = set(self.lista_tipo)
        tipo_mas_comun = max(tipos, key=self.lista_tipo.count)
        tipo_menos_comun = min(tipos, key=self.lista_tipo.count)

        promedio_total = sum(self.lista_poder) / len(self.lista_poder)

        electricos = [power for index, power in enumerate(self.lista_poder) if self.lista_tipo[index] == "Electrico"]
        promedio_electricos = sum(electricos) / len(electricos) if len(electricos) > 0 else 0

        informe = [
            f"0) Cantidad de pokemones de tipo Fuego: {num_fuego}",
            f"1) Cantidad de pokemones de tipo Electrico: {num_electrico}",
            f"2) {max_power_pokemon_info}",
            f"3) {min_power_pokemon_info}",
            f"4) Cantidad de pokemones, con mas de 100 de poder: {powers_over_100}",
            f"5) Cantidad de pokemones, con menos de 100 de poder: {powers_under_100}",
            f"6) Tipo de los pokemones del tipo que mas pokemones posea: {tipo_mas_comun}",
            f"7) Tipo de los pokemones del tipo que menos pokemones posea: {tipo_menos_comun}",
            f"8) El promedio de poder de todos los ingresados: {promedio_total}",
            f"9) El promedio de poder de todos los poquemones de Electrico: {promedio_electricos}"
        ]
        alert("Informe", "\n".join(informe))

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()