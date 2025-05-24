import tkinter as tk
from tkinter import messagebox
import requests

def buscar_episodios():
    anime = entry_anime.get()
    contar_ovas = var_contar_ovas.get()

    if not anime:
        messagebox.showwarning("Invalid input", "Please enter the name of the anime.")
        return

    response = requests.get(
        "http://127.0.0.1:8000/episodes/",
        params={"nome": anime, "contar_ovas": contar_ovas}
    )

    data = response.json()

    if "erro" in data:
        messagebox.showerror("Error", "Anime not found.")
    else:
        resultado_text.set(f"Name: {data['nome']}\n"
                           f"Episodes: {data['episodios']}\n"
                           f"OVAs: {data['ovas']}")


root = tk.Tk()
root.title("Anime search")
root.geometry("400x300")
root.config(bg="#f0f0f0")


titulo = tk.Label(root, text="Anime search", font=("Arial", 16), bg="#f0f0f0")
titulo.pack(pady=10)


label_anime = tk.Label(root, text="Enter the name of the anime:", font=("Arial", 12), bg="#f0f0f0")
label_anime.pack(pady=5)
entry_anime = tk.Entry(root, font=("Arial", 12), width=30)
entry_anime.pack(pady=5)


var_contar_ovas = tk.BooleanVar()
checkbox_ovas = tk.Checkbutton(root, text="Include OVAs", font=("Arial", 12), variable=var_contar_ovas, bg="#f0f0f0")
checkbox_ovas.pack(pady=5)

botao_buscar = tk.Button(root, text="Search", font=("Arial", 12), bg="#4CAF50", fg="white", command=buscar_episodios)
botao_buscar.pack(pady=15)


resultado_text = tk.StringVar()
resultado_label = tk.Label(root, textvariable=resultado_text, font=("Arial", 12), bg="#f0f0f0", justify="left")
resultado_label.pack(pady=10)


root.mainloop()



"""import requests

anime = input("Digite o nome do anime: ")
contar_ovas = input("Deseja contar OVAs também? (s/n): ").lower() == 's'

response = requests.get(
    "http://127.0.0.1:8000/episodios/",
    params={"nome": anime, "contar_ovas": contar_ovas}
)

data = response.json()

if "erro" in data:
    print("Anime não encontrado.")
else:
    print(f"Nome: {data['nome']}")
    print(f"Episódios: {data['episodios']}")
    print(f"OVAs: {data['ovas']}")
"""