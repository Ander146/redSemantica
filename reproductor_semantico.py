import tkinter as tk
from tkinter import messagebox
import random

# ------------------------------
# RED SEMÁNTICA DEL REPRODUCTOR
# ------------------------------
red_semantica = {
    "Música": ["Rock", "Pop", "Jazz", "Reggaetón"],
    "Rock": ["Bohemian Rhapsody", "Hotel California", "Stairway to Heaven"],
    "Pop": ["Thriller", "Like a Prayer", "Shape of You"],
    "Jazz": ["So What", "Take Five", "Feeling Good"],
    "Reggaetón": ["Gasolina", "Despacito", "Tusa"]
}

# Diccionario para contar las preferencias del usuario
preferencias = {
    "Rock": 0,
    "Pop": 0,
    "Jazz": 0,
    "Reggaetón": 0
}

# ------------------------------
# FUNCIONES DEL PROGRAMA
# ------------------------------

def mostrar_opciones():
    """Muestra un mensaje explicando cómo funciona la interfaz."""
    instrucciones = (
        "Bienvenido al Reproductor Inteligente 🎵\n\n"
        "1. Selecciona una canción de la lista.\n"
        "2. Pulsa 'Me gusta' para que el sistema aprenda tu preferencia.\n"
        "3. Pulsa 'Recomendar' para obtener canciones según tus gustos."
    )
    messagebox.showinfo("Instrucciones", instrucciones)

def actualizar_lista(genero):
    """Muestra las canciones de un género en la lista."""
    lista_canciones.delete(0, tk.END)
    for cancion in red_semantica[genero]:
        lista_canciones.insert(tk.END, cancion)

def registrar_gusto():
    """Registra que al usuario le gustó la canción seleccionada."""
    seleccion = lista_canciones.curselection()
    if not seleccion:
        messagebox.showwarning("Atención", "Debes seleccionar una canción primero.")
        return

    cancion = lista_canciones.get(seleccion)
    # Encontrar a qué género pertenece la canción
    for genero, canciones in red_semantica.items():
        if cancion in canciones:
            preferencias[genero] += 1
            messagebox.showinfo("Gracias", f"Has indicado que te gusta '{cancion}'.")
            break

def recomendar():
    """Recomienda canciones del género con más puntos."""
    if all(valor == 0 for valor in preferencias.values()):
        messagebox.showwarning("Atención", "Primero indica qué canciones te gustan.")
        return

    # Encontrar el género con más puntos
    genero_fav = max(preferencias, key=preferencias.get)

    # Mostrar canciones recomendadas SOLO de ese género
    canciones_recomendadas = red_semantica[genero_fav]
    lista_canciones.delete(0, tk.END)
    for cancion in canciones_recomendadas:
        lista_canciones.insert(tk.END, cancion)

    messagebox.showinfo("Recomendación", f"Te recomendamos canciones de {genero_fav} 🎶")

# ------------------------------
# INTERFAZ GRÁFICA
# ------------------------------
ventana = tk.Tk()
ventana.title("Reproductor Inteligente - Red Semántica")
ventana.geometry("500x400")

# Botón de instrucciones
btn_instrucciones = tk.Button(ventana, text="¿Cómo usar?", command=mostrar_opciones)
btn_instrucciones.pack(pady=5)

# Lista de canciones
lista_canciones = tk.Listbox(ventana, width=50, height=10)
lista_canciones.pack(pady=10)

# Botones para cada género
frame_botones = tk.Frame(ventana)
frame_botones.pack()

for genero in preferencias.keys():
    tk.Button(frame_botones, text=genero, command=lambda g=genero: actualizar_lista(g)).pack(side=tk.LEFT, padx=5)

# Botones de interacción
frame_acciones = tk.Frame(ventana)
frame_acciones.pack(pady=10)

btn_like = tk.Button(frame_acciones, text="Me gusta", command=registrar_gusto)
btn_like.pack(side=tk.LEFT, padx=5)

btn_recomendar = tk.Button(frame_acciones, text="Recomendar", command=recomendar)
btn_recomendar.pack(side=tk.LEFT, padx=5)

ventana.mainloop()
