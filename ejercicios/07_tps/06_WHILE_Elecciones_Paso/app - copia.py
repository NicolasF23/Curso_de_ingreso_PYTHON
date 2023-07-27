'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        import tkinter 
'''

from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre (validar que no sea None), la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)
'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Pedir Datos", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Datos", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=6, pady=20, columnspan=2, sticky="nsew")
        self.lista_de_nombres = ['Pelusa', 'Freya', 'Sirius', 'Pepe Peposo', 'Hooper'] 
        self.lista_de_edades = [33, 28, 29, 26, 42] 
        self.lista_de_votos_por_candidato = [120, 9, 20, 1090, 2491]
        
    def btn_validar_on_click(self):
        
        nombre_ingresado = prompt(None, 'Ingresa tu nombre')
        while nombre_ingresado == None:
            nombre_ingresado = prompt('Error', 'Ingresa tu nombre')
        self.lista_de_nombres.append(nombre_ingresado)
        
        edad_ingresada = int(prompt(None, 'Ingresa tu edad'))
        while edad_ingresada < 26:
            edad_ingresada = int(prompt('Error', 'Ingresa tu edad'))
        self.lista_de_edades.append(edad_ingresada)
        
        cantidad_de_votos_ingresados = int(prompt(None, 'Ingrese la cantidad de votos'))
        while cantidad_de_votos_ingresados < 0:
            cantidad_de_votos_ingresados = int(prompt('Error', 'Ingrese la cantidad de votos'))
        self.lista_de_votos_por_candidato.append(cantidad_de_votos_ingresados)
            
    def btn_mostrar_on_click(self):
        
        largo = len(self.lista_de_votos_por_candidato)
        mayor_cantidad_de_votos = None
        nombre_candidato_mayor_cantidad_de_votos = ''
        menor_cantidad_votos = None
        nombre_candidato_menor = ''
        edad_candidato_menor = 0
        acumulador_edades = 0
        acumulador_votos = 0
        
        
        for i in range(largo):
            #punto A
            if mayor_cantidad_de_votos == None or mayor_cantidad_de_votos < self.lista_de_votos_por_candidato[i]:
                mayor_cantidad_de_votos = self.lista_de_votos_por_candidato[i]
                nombre_candidato_mayor_cantidad_de_votos = self.lista_de_nombres[i]
            #punto A
            
            #punto B
            if menor_cantidad_votos == None or menor_cantidad_votos > self.lista_de_votos_por_candidato[i]:                  
                menor_cantidad_votos = self.lista_de_votos_por_candidato[i]
                edad_candidato_menor = self.lista_de_edades[i]
                nombre_candidato_menor = self.lista_de_nombres[i]
            #punto B
            
            #punto C
            acumulador_edades += self.lista_de_edades[i]
            #punto C
            
            #punto D
            acumulador_votos += self.lista_de_votos_por_candidato[i]
            #punto D
        
        #punto C
        promedio_edades = acumulador_edades / largo
        #punto C

        mensaje_salida = f'El nombre del candidato con mas votos es: {nombre_candidato_mayor_cantidad_de_votos}, con {mayor_cantidad_de_votos}. El nombre del candidato con menos votos es: {nombre_candidato_menor}, tiene {edad_candidato_menor} años de edad y obtuvo una cantidad de {menor_cantidad_votos}. El promedio de edad entre todos los candidatos es de: {promedio_edades}. El total de votos emitidos es de: {acumulador_votos}'
        
        print(mensaje_salida)
        
            
        
        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
