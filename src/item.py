class Item:
    def __init__(self, i_name, i_description):
        self.i_name = i_name
        self.i_description = i_description

    def __str__(self):
        return f"{self.i_name}"
    
    def on_take(self, i_name):
        print(f"You have picked up {i_name}")
        # return self.i_name
        
    def on_drop(self, i_name):
        print(f"You have put {i_name} back ")
        # return self.i_name
        
    

