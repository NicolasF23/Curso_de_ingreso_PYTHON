import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

#Nombre: Nicolas Faryd
#Apellido: Couso Ponsoni
#D.N.I: 48.683.647
#Comison: B

#Enunciado del parcial:
#Una distribuidora de bebidas llena 10 comiones con sus productos y necesita guardar ciertos datos de cada una:
#-Nombre del conductor
#-Cantidad de litros de agua transportada($300 el litro)
#-Cantidad de litros de gaseosa transportada ($600 el litro)
#-Cantidad de litros de cerveza transportada ($800 el litro)
#-Cantidad de litros de vino transportada ($1000 el litro)

#Obligatorio: Informar el promedio de litros por camion.

#Por  terminación de DNI:
#deberá realizar dos informes,
#para determinar que informe hacer, tenga en cuenta lo siguiente:

#    1- Tome el último número de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

#    2- Tome el último número de su DNI Personal (Ej 4), y restarle al número 9 (Ej 9-4 = 5).
#    Realiza el informe correspondiente al número obtenido.

#EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR.

#0)Debemos mostrar que tipo de bebida se transportó en mayor cantidad (cerveza, agua, gaseosa o vino).
#1)Debemos mostrar el total de facturación del agua y la gaseosa vendida que estará dado por cada litro de gaseosa $600 y cada litro de agua a $300.
#-->2)Debemos mostrar el total de facturación de la cerveza y el vino vendido que estará dado por cada litro de cerveza $800 y cada litro de vino a $1000.
#3)Si la empresa supera la facturación de 350000 pesos deberá pagar un 8% de ingresos brutos. Informar si lo paga y de ser así el monto del impuesto.
#4)Si la empresa supera la facturación de 700000 pesos deberá pagar un 15% de impuesto a las ganancias. Informar si lo paga y de ser así el monto del impuesto.
#5)Debemos mostrar que tipo de bebida se transportó en menor cantidad (cerveza, agua, gaseosa o vino).
#6)Informar el porcentaje de agua transportada y de gaseosa transportada en relación al total de litros transportados.
#-->7)Informar el porcentaje de cerveza transportada y de vino transportado en relación al total de litros transportados.
#8)Informar el primer ingreso (camion) que transporte mas de 100 litros.
#9)Informar el primer ingreso (camion) que transporte menos de 50 litros.

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Simulacro Parcial")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Datos", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_nombre = []
        self.lista_producto = []
        self.lista_promedio = []
    
    def btn_cargar_on_click(self):
        for i in range(10):
            nombre_conductor = prompt("Nombre","Ingrese el nombre del conductor:")
            litros_agua = float(prompt("Agua","Ingrese la cantidad de litros de agua transportada:"))
            litros_gaseosa = float(prompt("Gaseosa","Ingrese la cantidad de litros de gaseosa transportada:"))
            litros_cerveza = float(prompt("Cerveza","Ingrese la cantidad de litros de cerveza transportada:"))
            litros_vino = float(prompt("Vino","Ingrese la cantidad de litros de vino transportada:"))

            self.lista_nombre.append(nombre_conductor)
            self.lista_producto.append([litros_agua, litros_gaseosa, litros_cerveza, litros_vino])
            self.lista_promedio.append(litros_agua + litros_gaseosa + litros_cerveza + litros_vino)
        
        
    def btn_mostrar_on_click(self):
        total_litros = sum(self.lista_promedio)
        promedio_litros = total_litros / len(self.lista_promedio)
    
        total_facturacion_cerveza = sum(self.lista_producto[i][2] * 800 for i in range(len(self.lista_producto)))
        total_facturacion_vino = sum(self.lista_producto[i][3] * 1000 for i in range(len(self.lista_producto)))

        alert("Resultado", f"Promedio de litros por camión: {promedio_litros:.2f}\n"
                        f"Total facturación de cerveza: {total_facturacion_cerveza:.2f}\n"
                        f"Total facturación de vino: {total_facturacion_vino:.2f}")


    def btn_informar_on_click(self):
        total_litros = sum(self.lista_promedio)
        total_cerveza = sum(self.lista_producto[i][2] for i in range(len(self.lista_producto)))
        total_vino = sum(self.lista_producto[i][3] for i in range(len(self.lista_producto)))

        porcentaje_cerveza = total_cerveza / total_litros * 100
        porcentaje_vino = total_vino / total_litros * 100

        alert("Información", f"Porcentaje de cerveza transportada: {porcentaje_cerveza:.2f}%\n"
                            f"Porcentaje de vino transportado: {porcentaje_vino:.2f}%")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
