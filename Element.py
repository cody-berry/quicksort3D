

class Element:
    def __init__(self, value):
        self.c = color(13, 2, 99, 40)
        self.value = value
        # the done variable represents if it is sorted
        # we assume that it is false during the beginning of the sort                      
        self.done = False
        
    def reset_color(self):
        self.c = color(13, 2, 99, 40)
        
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value
    
