import tkinter as tk
from tkinter import ttk, messagebox
from controller.controller import HospitalController

def iniciar_gui():
    controller = HospitalController()

    root = tk.Tk()
    root.title("Sistema de Información Hospitalaria")
    root.geometry("700x500")

    # ----- Sección Hospital -----
    frm_hospital = tk.LabelFrame(root, text="Crear Hospital", padx=10, pady=10)
    frm_hospital.pack(padx=10, pady=5, fill="x")

    tk.Label(frm_hospital, text="Nombre:").grid(row=0, column=0)
    entry_nombre_hospital = tk.Entry(frm_hospital)
    entry_nombre_hospital.grid(row=0, column=1)

    tk.Label(frm_hospital, text="Dirección:").grid(row=0, column=2)
    entry_direccion = tk.Entry(frm_hospital)
    entry_direccion.grid(row=0, column=3)

    def crear_hospital():
        nombre = entry_nombre_hospital.get()
        direccion = entry_direccion.get()
        if nombre and direccion:
            controller.crear_hospital(nombre, direccion)
            messagebox.showinfo("Éxito", "Hospital creado correctamente.")
        else:
            messagebox.showwarning("Campos vacíos", "Debes llenar todos los campos.")

    tk.Button(frm_hospital, text="Crear", command=crear_hospital).grid(row=0, column=4, padx=10)

    # ----- Sección Doctor -----
    frm_doctor = tk.LabelFrame(root, text="Agregar Doctor", padx=10, pady=10)
    frm_doctor.pack(padx=10, pady=5, fill="x")

    tk.Label(frm_doctor, text="Nombre:").grid(row=0, column=0)
    entry_nombre_doc = tk.Entry(frm_doctor)
    entry_nombre_doc.grid(row=0, column=1)

    tk.Label(frm_doctor, text="Especialidad:").grid(row=0, column=2)
    entry_especialidad = tk.Entry(frm_doctor)
    entry_especialidad.grid(row=0, column=3)

    tk.Label(frm_doctor, text="DNI:").grid(row=0, column=4)
    entry_dni_doc = tk.Entry(frm_doctor)
    entry_dni_doc.grid(row=0, column=5)

    def agregar_doctor():
        nombre = entry_nombre_doc.get()
        especialidad = entry_especialidad.get()
        dni = entry_dni_doc.get()
        if nombre and especialidad and dni:
            controller.agregar_doctor(nombre, especialidad, dni)
            messagebox.showinfo("Éxito", "Doctor agregado.")
        else:
            messagebox.showwarning("Campos vacíos", "Debes llenar todos los campos.")

    tk.Button(frm_doctor, text="Agregar", command=agregar_doctor).grid(row=0, column=6, padx=10)

    # ----- Sección Búsqueda -----
    frm_buscar = tk.LabelFrame(root, text="Buscar Doctor por DNI", padx=10, pady=10)
    frm_buscar.pack(padx=10, pady=5, fill="x")

    tk.Label(frm_buscar, text="DNI:").grid(row=0, column=0)
    entry_buscar_dni = tk.Entry(frm_buscar)
    entry_buscar_dni.grid(row=0, column=1)

    # Tabla de resultados
    tree = ttk.Treeview(root, columns=("Nombre", "Especialidad", "DNI"), show='headings')
    tree.heading("Nombre", text="Nombre")
    tree.heading("Especialidad", text="Especialidad")
    tree.heading("DNI", text="DNI")
    tree.pack(padx=10, pady=5, fill="both", expand=True)

    def buscar_doctor():
        dni = entry_buscar_dni.get()
        doctor = controller.buscar_doctor_por_dni(dni)
        for item in tree.get_children():
            tree.delete(item)
        if doctor:
            tree.insert("", "end", values=(doctor.nombre, doctor.especialidad, doctor.dni))
        else:
            messagebox.showinfo("No encontrado", "No se encontró un doctor con ese DNI.")

    tk.Button(frm_buscar, text="Buscar", command=buscar_doctor).grid(row=0, column=2, padx=10)

    root.mainloop()
