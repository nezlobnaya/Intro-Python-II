# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def get_current_room(self):
        return self.current_room

    def set_current_room(self, room):
        self.current_room = room
    
    def __str__(self):
        return f"Player {self.name} is in {self.current_room} room"
    
    