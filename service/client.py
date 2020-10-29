class Client():

    def __init__(self, name, last_name, doc_id):
        self.name = name
        self.last_name = last_name
        self.doc_id = doc_id
        self.preexistence = []

    def add_preexistence(self, nPreexistence):
        """ Adds a preexistence to a client """ 
        self.preexistence.append(nPreexistence)
        return len(self.preexistence) - 1
    
    def get_preexistence(self, p_index):
        """Get a preexistence given the index"""
        if p_index >= len(self.preexistence):
            return 'There is no such preexistence'
        
        return self.preexistence[pIndex]

    def get_all_preexistence(self):
        return self.preexistence

    def remove_preexistence(self, nPreexistence):
        self.preexistence.pop(nPreexistence)
        return len(self.preexistence) - 1

    def get_formatted_name(self):
        return self.name + ' ' + self.last_name


if __name__ == '__main__':
    client_instance = Client('uno', 'dos', '113565')
    print('User Abbas has been added with id ', client_instance.get_formatted_name())
