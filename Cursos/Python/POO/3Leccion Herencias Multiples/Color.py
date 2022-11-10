class Color:
    def __init__(self, color):
        self._color = color
    
    def __str__(self):
        return f"Color: {self._color})"

    @property
    def color(self):
        #Lamando metodo get color
        return self._color

    @color.setter
    def color(self, color):
        #LLamando metodo set color
        self._color = color