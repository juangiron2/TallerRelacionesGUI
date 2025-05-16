import json
from model.doctor import Doctor

class Hospital:
    def __init__(self, nombre, direccion):
        self._nombre = nombre
        self._direccion = direccion
        self._doctores = []
        
    @property
    def nombre(self):
        return self._nombre
        
    @property
    def direccion(self):
        return self._direccion
        
    @property
    def doctores(self):
        return self._doctores

    def agregar_doctor(self, doctor):
        self._doctores.append(doctor)

    def buscar_doctor_por_dni(self, dni):
        for doctor in self._doctores:
            if doctor.dni == dni:
                return doctor
        return None

    def to_dict(self):
        return {
            "nombre": self._nombre,
            "direccion": self._direccion,
            "doctores": [doc.to_dict() for doc in self.doctores]
        }

    @staticmethod
    def from_dict(data):
        hospital = Hospital(data["nombre"], data["direccion"])
        for doc_data in data["doctores"]:
            hospital.agregar_doctor(Doctor.from_dict(doc_data))
        return hospital
