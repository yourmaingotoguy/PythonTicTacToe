class Counter:
    def __init__(self, string):
        self.label = string

    def __str__(self):
        return self.label

# Set up Counter Globals
X = Counter('X')
O = Counter('O')

