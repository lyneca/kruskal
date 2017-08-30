class Box:
    def __init__(self, size):
        self.size = size
    
    def __add__(self, other):
        return self.size + other.size
