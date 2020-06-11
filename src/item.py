class Item:
    def __init__(self, i_name):
        self.i_name = i_name
    def __str__(self):
        return f"{self.i_name}"
    
    def on_take(self):
        print(f"You have picked up {self.i_name}")
        return self.i_name
        
    def on_drop(self):
        print(f"You have put back {self.i_name}")
        return self.i_name
        
    

