class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.area()
    def area(self):
        print(self.length*self.width)
s1=Rectangle(10,7)