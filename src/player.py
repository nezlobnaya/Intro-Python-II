# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player(Item):
    def __init__(self, name, current_room, i_name = None, i_list = None):
        super().__init__(i_name)
        self.name = name
        self.i_list = i_list
        self.current_room = current_room

    def get_current_room(self):
        return self.current_room

    def set_current_room(self, room):
        self.current_room = room
    
    def player_inventory(self):
        return self.i_list
        
    def added_to_inventory(self, i_name):
        self.i_list.append(i_name)
        return self.i_list
        
    def __str__(self):
        return f"Player {self.name} is in {self.current_room} room"
    
    