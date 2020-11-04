
class Agency():
    """Class representing a Sucursal"""

    def __init__(self, nombre, direccion,telefono, sucursal_id):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.sucursal_id = sucursal_id
        self.preexistence = []

    def add_preexistence(self, n_preexistence):
        """Adds a preexistence to a client"""
        self.preexistence.append(n_preexistence)
        return len(self.preexistence) - 1

    def get_preexistence(self, p_index):
        """Get a preexistence given the index"""
        if p_index >= len(self.preexistence):
            return 'There is no such preexistence'
        return self.preexistence[p_index]

    def get_all_preexistence(self):
        """Get all the preexistence"""
        return self.preexistence

    def remove_preexistence(self, n_preexistence):
        """Removes a preexistence given the index"""
        self.preexistence.pop(n_preexistence)
        return len(self.preexistence) - 1

    def get_formatted_nombre(self):
        return self.nombre 

if __name__ == '__main__':
    agency_instance = Agency('CLINICA', 'DIRECCION','6466060', '115')
    print('User Abbas has been added with id ', agency_instance.get_formatted_name())
