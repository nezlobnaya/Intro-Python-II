# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room(Item):
    def __init__(self, name, description, i_name = None, i_list = None, n_to = None, s_to = None, e_to = None, w_to = None):
        super().__init__(i_name)
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
      
    def add_item(self, i_list, i_name):
        if i_list is None:
            self.i_list = []
        self.i_list.append(i_name)
        return f"Room inventory: {self.i_list}"
    
    def remove_item(self, i_name):
        self.i_list.remove(i_name)
        return f"Room inventory: {self.i_list}"

    def __str__(self):
        return f"{self.name}:\n{self.description}"