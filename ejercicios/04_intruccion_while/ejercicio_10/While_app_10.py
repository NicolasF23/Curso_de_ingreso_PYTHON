import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0 
        max = 0
        min = 0
        while True:
            numero = prompt ("Numero", f"Ingrese un numero ({contador}) ")
            if numero == None:
                break
            if numero.isdigit():
                numero = int(numero)
                if contador == 0:
                    max = numero
                    min = numero
            
            if numero > max:
                max = numero        
            if numero < min:
                min = numero
            else:
                pass
            contador +=1
        
        self.txt_maximo.delete(0,10000)
        self.txt_minimo.delete(0,10000)
        self.txt_maximo.insert(0,max)
        self.txt_minimo.insert(0,min)          

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
