import tkinter as tk
from tkinter import messagebox
import datetime

open("Jednostavna_Bilježnica.txt", "w").close()

def izbrisi():
    with open("Jednostavna_Bilježnica.txt", "w") as bilježnica:
        bilježnica.write("")
        messagebox.showinfo("Info", "Izbrisali ste bilješke")

def dodaj_biljesku():
    bilj = unos.get()
    try:
        with open("Jednostavna_Bilježnica.txt", "r") as bilježnica:
            linije = [linija for linija in bilježnica if linija.strip()]
            redni_broj = len(linije) + 1
    except FileNotFoundError:
        redni_broj = 1
    with open("Jednostavna_Bilježnica.txt", "a") as bilježnica:
        if bilj.strip() == "":
            messagebox.showwarning("Upozorenje", "Niste upisali bilješku!")
            return
        else:
            bilježnica.write(f"{redni_broj}. {bilj}\n")
            messagebox.showinfo("Info", "Bilješka je uspješno spremljena")

def prikazi_biljeske():
        with open("Jednostavna_Bilježnica.txt", "r") as bilježnica:
            sadrzaj = bilježnica.read()
            if not sadrzaj.strip():
                tekst.delete(1.0, tk.END)
                tekst.insert(tk.END, "Bilježnica je prazna.")
                return
            else:
                tekst.delete(1.0, tk.END)
                tekst.insert(tk.END, sadrzaj)

vrijeme = datetime.datetime.now()

prozor = tk.Tk()
prozor.title("Jednostavna Bilježnica")
prozor.configure(bg="grey")

unos = tk.Entry(prozor, width=50, bg = "darkgrey")
unos.pack(padx=10, pady=10)

dodaj_btn = tk.Button(prozor, text="Dodaj bilješku", bg = "darkgrey" , command=dodaj_biljesku)
dodaj_btn.pack(pady=5)

izbrisi_btn = tk.Button(prozor, text="Izbriši sve", bg = "darkgrey" , command=izbrisi)
izbrisi_btn.pack(pady=5)

prikazi_btn = tk.Button(prozor, text="Prikaži bilješke", bg = "darkgrey" , command=prikazi_biljeske)
prikazi_btn.pack(pady=5)

tekst = tk.Text(prozor, bg="darkgrey" , width=60, height=15)
tekst.pack(padx=10, pady=10)

prozor.mainloop()
