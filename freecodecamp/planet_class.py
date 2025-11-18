class Planet:
    def __init__(self,name,planet_type,star):
        if not isinstance([name,planet_type,star],str):
            raise TypeError("name, planet type, and star must be strings")
        elif name == '' or planet_type == '' or star =='':
            raise ValueError("name, planet_type, and star must be non-empty strings")
        self.name = name
        self.planet_type = planet_type
        self.star = star
        
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."
    
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"
    
planet_1 = Planet("Earth",'type1','Sun')
planet_2 = Planet('Mars','type1','Sun')
planet_3 = Planet('Uranus','type1','Sun')