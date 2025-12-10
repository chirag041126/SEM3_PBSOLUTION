class Circle:
    def __init__(self,r):
        self.r=r
        self.area()
        self.perimeter()
    def area(self):
        print("area of circle",3.14*((self.r)**2))
    def perimeter(self):
        print("perimeter of circle",(2*3.14*self.r))

s1=Circle(7)    
