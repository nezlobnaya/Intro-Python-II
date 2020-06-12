# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room(Item):
    def __init__(self, name, description, i_name = None, i_description = None ):
        super().__init__(i_name, i_description)
        self.name = name
        self.description = description
        self.i_list = None
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
      
    def add_item(self, i_name, i_description, i_list = None ):
        if self.i_list is None:
            self.i_list = {}
        self.i_list[i_name] = i_description
        return f"Room inventory: {self.i_list}"
    
    def remove_item(self, i_name):
        del self.i_list[i_name]
        return f"Room inventory: {self.i_list}"

    def room_inventory(self):
        return self.i_list

    def __str__(self):
        return f"{self.name}:\n{self.description}"