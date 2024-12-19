class Circle():
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius
    

    
c1 = Circle(10)
print(c1.radius)
c1.radius = 100
print(c1.radius)
    