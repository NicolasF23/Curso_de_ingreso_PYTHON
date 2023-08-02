import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
A) El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con 
algunos pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)
    
-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar, se debera mostrar el pokemon (nombre, tipo y poder) de tipo fuego o agua con mas poder

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

*******Tener en cuenta que pueden no haber ingresos o egresos**********
C) Al presionar el boton Informar 
    # 0) - Cantidad de pokemones de tipo Fuego
    # 1) - Cantidad de pokemones de tipo Electrico
    # 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    # 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    # 4) - Cantidad de pokemones, con mas de 100 de poder.
    # 5) - Cantidad de pokemones, con menos de 100 de poder
    # 6) - tipo de los pokemones del tipo que mas pokemones posea 
    # 7) - tipo de los pokemones del tipo que menos pokemones posea 
    # 8) - el promedio de poder de todos los ingresados
    # 9) - el promedio de poder de todos los poquemones de Electrico 

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Simulacro Parcial")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_nombre = []
        self.lista_tipo = []
        self.lista_poder = []
    
    def btn_cargar_on_click(self):
        for i in range(10):
            nombre = prompt("Nombre","Ingrese el nombre del Pokemon:")
            tipo = prompt("Tipo", "Ingrese el tipo del Pokemon (Agua, Tierra, Psiquico, Fuego, Electrico):")
            poder = int(prompt("Poder", "Ingrese la cantidad de poder (entre 50 y 200):"))
            
            while poder < 50 or poder > 200:
                alert("Error", "El poder debe ser mayor a 50 y menor a 200.")
                poder = int(prompt("Ingrese la cantidad de poder (entre 50 y 200):"))
            
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
            alert("Dato no existente", "No se encontraron pokemones de tipo fuego o agua.")
        

#C) Al presionar el boton Informar 
    
    # 7) - tipo de los pokemones del tipo que menos pokemones posea 
    
    def btn_informar_on_click(self):

        tipos = set(self.lista_tipo)
        tipo_menos_comun = min(tipos, key=self.lista_tipo.count)

        informe = [

            f"7) Tipo de los pokemones del tipo que menos pokemones posea: {tipo_menos_comun}",

        ]
        alert("Informe", "\n".join(informe))
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
