import tkinter as tk
import time

def guncelle():
    saat.config(text=time.strftime("%H:%M:%S"))
    tarih.config(text=time.strftime("%d/%m/%Y"))
    pencere.after(1000,guncelle)

pencere=tk.Tk()
pencere.title("Dijital Saat")
pencere.geometry("420x220")
saat=tk.Label(pencere,font=("Arial",36,"bold"))
saat.pack(pady=20)
tarih=tk.Label(pencere,font=("Arial",18))
tarih.pack()
guncelle()
pencere.mainloop()
