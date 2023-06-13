import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def iniciar_simulacion():
    try:
        posicion_inicial = float(entry_posicion_inicial.get())
        velocidad = float(entry_velocidad.get())
        tiempo_total = float(entry_tiempo_total.get())

        fig, ax = plt.subplots()
        ax.set_xlim(0, tiempo_total)
        ax.set_ylim(0, posicion_inicial + velocidad * tiempo_total)

        linea, = ax.plot([], [], 'o-')

        def actualizar_animacion(tiempo):
            nueva_posicion = posicion_inicial + velocidad * tiempo
            linea.set_data([0, tiempo], [posicion_inicial, nueva_posicion])
            return linea,

        animacion = animation.FuncAnimation(fig, actualizar_animacion, frames=int(tiempo_total*100), interval=10, blit=True)
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")


ventana = tk.Tk()
ventana.title("Simulación de Movimiento Rectilíneo Uniforme")
ventana.geometry("300x200")


label_posicion_inicial = tk.Label(ventana, text="Posición inicial:")
label_posicion_inicial.pack()
entry_posicion_inicial = tk.Entry(ventana)
entry_posicion_inicial.pack()

label_velocidad = tk.Label(ventana, text="Velocidad:")
label_velocidad.pack()
entry_velocidad = tk.Entry(ventana)
entry_velocidad.pack()

label_tiempo_total = tk.Label(ventana, text="Tiempo total:")
label_tiempo_total.pack()
entry_tiempo_total = tk.Entry(ventana)
entry_tiempo_total.pack()


btn_iniciar = tk.Button(ventana, text="Iniciar simulación", command=iniciar_simulacion)
btn_iniciar.pack()

ventana.mainloop()