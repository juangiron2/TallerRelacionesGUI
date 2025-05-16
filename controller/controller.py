import json
import os
from model.hospital import Hospital
from model.doctor import Doctor

class HospitalController:
    def __init__(self, data_file="data/hospital_data.json"):
        self._hospital = None
        self._data_file = data_file
        self._cargar_datos()

    def crear_hospital(self, nombre, direccion):
        self._hospital = Hospital(nombre, direccion)
        self._guardar_datos()

    def agregar_doctor(self, nombre, especialidad, dni):
        if self._hospital:
            doctor = Doctor(nombre, especialidad, dni)
            self._hospital.agregar_doctor(doctor)
            self._guardar_datos()

    def buscar_doctor_por_dni(self, dni):
        if self._hospital:
            return self._hospital.buscar_doctor_por_dni(dni)
        return None

    def _guardar_datos(self):
        if self._hospital:
            with open(self._data_file, 'w') as f:
                json.dump(self._hospital.to_dict(), f, indent=4)

    def _cargar_datos(self):
        if os.path.exists(self._data_file):
            with open(self._data_file, 'r') as f:
                contenido = f.read().strip()
                if contenido:
                    data = json.loads(contenido)
                    self._hospital = Hospital.from_dict(data)

