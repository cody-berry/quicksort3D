

class Element:
    def __init__(self, value):
        self.c = color(13, 2, 99)
        self.value = value
        
    def reset_color(self):
        self.c = color(13, 2, 99)
        
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value
    
