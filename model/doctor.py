class Doctor:
    def __init__(self, nombre, especialidad, dni):
        self._nombre = nombre
        self._especialidad = especialidad
        self._dni = dni
        
    @property
    def nombre(self):
        return self._nombre
        
    @property
    def especialidad(self):
        return self._especialidad
        
    @property
    def dni(self):
        return self._dni

    def to_dict(self):
        return {
            "nombre": self._nombre,
            "especialidad": self._especialidad,
            "dni": self._dni
        }

    @staticmethod
    def from_dict(data):
        return Doctor(data["nombre"], data["especialidad"], data["dni"])
