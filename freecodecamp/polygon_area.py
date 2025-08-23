# Freecodecamp - Scientific Calc. Python - Project No. 4

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
    def set_width(self,width):
        self.width=width
    
    def set_height(self,height):
        self.height=height

    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        dif_string=""
        if self.height>50 or self.width > 50:
            return 'Too big for picture.'
        else:
            for i in range(self.height):
                dif_string+=("*"*self.width+"\n")
            return dif_string
    
    def get_amount_inside(self,shape):
        horizontal_num=round( self.width / shape.width,0)
        vertical_num=round(self.height / shape.height,0)
        return horizontal_num*vertical_num
        
class Square(Rectangle):
    def  __init__(self,side):
        self.width=side
        self.height=side
        self.side=side
    
    def __str__(self):
        return f"Square(side={self.side})"
        
    def set_side(self,side):
        self.width=side
        self.height=side
        self.side=side
    
    def set_width(self,width):
        self.width=width
        self.height=width
        self.side=width
        
    
    def set_height(self,height):
        self.height=height
        self.width=height
        self.side=height
        
    def get_picture(self):
        dif_string=""
        if self.side > 50:
            return 'Too big for picture.'
        else:
            for i in range(self.side):
                dif_string+=("*"*self.side+"\n")
            return dif_string
    
            