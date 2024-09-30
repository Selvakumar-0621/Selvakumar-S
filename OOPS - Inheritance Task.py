# Program to find areas and perimeters of a circle using OOPS concept


class Circle:

    def __init__(self, radius_list):
        self.radius = radius_list               
        self.__pi = 3.141                        # Private variable for pi

    def Area(self):
        areas = []                               # List to store areas
        for radius in self.radius:
            area = self.__pi * (radius ** 2)
            areas.append(area)
        return areas

    def Perimeter(self):
        perimeters = []                           # List to store perimeters
        for radius in self.radius:
            perimeter = 2 * self.__pi * radius
            perimeters.append(perimeter)
        return perimeters


radius = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius)

# Get the areas and perimeters
areas = circle.Area()
perimeters = circle.Perimeter()

print("The Areas of the circle with list of radius are :", areas)
print("The Perimeters of the circle with list of radius are :", perimeters)


## Program to create a parent class - Base TV, and child classes - LED & Plasma using inheritance concept



class TV:                                                     # Parent Class - TV
    def __init__(self, brand, price, inches):                 # Constructor to details the TV with brand, price, and inches
        self.brand = brand 
        self.channel = 1                                      # Default value
        self.volume = 50                                      # Default value 
        self.price = price
        self.inches = inches
        self.on_off_status = False
    

    def tv_brand(self):                                        # method 1 - Brand
        brand = self.brand
        return brand
    
    def tv_price(self):                                        # method 2 - Price
        price = self.price
        return price
    
    def tv_inches(self):                                       # method 3 - Inches
        inches = self.inches
        return inches
    
    
    def power_on(self):                                        # method 4 - Turn on
        self.on_off_status = True
        print(self.brand, " TV is ON.")
    
    def power_off(self):                                       # method 5 - Turn off
        self.on_off_status = False
        print(self.brand, " TV is OFF.")
    
    def increase_volume(self):                                 # method 6 - Increase volume
        if self.volume < 100:
            self.volume += 1
        print("Volume: ", str(self.volume))
    
    def decrease_volume(self):                                # method 6 - Decraese volume
        if self.volume > 0:
            self.volume -= 1
        print("Volume: ", str(self.volume))
    
    def set_channel(self, new_channel):                       # method 6 - To set channel
        if 1 <= new_channel <= 50:
            self.channel = new_channel
        else:
            print("Invalid channel", str(self.channel))
        print("Channel: ", str(self.channel))
    
    def reset(self):                                          # method 6 - To reset to channel 1 with volume 50
        self.channel = 1
        self.volume = 50
        print("Channel 1 Volume 50.")
    
    def status(self):
        return self.brand, str(self.channel), str(self.volume)
    
print("Base TV Details:")
 
tv = TV(brand = "Brand : SAMSUNG", price = "Price : One Lakh", inches = "Inches : 100 inches")
print(tv.tv_brand())
print(tv.tv_price())
print(tv.tv_inches())
tv.power_on()
tv.increase_volume()
tv.set_channel(8)
print(tv.status())
tv.reset()
tv.power_off()



class LED(TV):                                                                   # Child class 1 - LED inherited from parent class TV
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):        # Constructor for additional properties of LED    
        super().__init__(brand, price, inches)                                                               # Inheriting properties from the parent class TV
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = "Wide"
        self.backlight = "Yes"


    def display_details(self):
        print("LED TV Details:")
        print("Brand: ", self.brand)
        print("Price: ", str(self.price))
        print("Size: ", str(self.inches), " inches")
        print("Screen Thickness: ", str(self.screen_thickness), " mm")
        print("Energy Usage: ", str(self.energy_usage), " watts")
        print("Lifespan: ", str(self.lifespan), " years")
        print("Refresh Rate: ", str(self.refresh_rate), " Hz")
        print("Viewing Angle: ", self.viewing_angle)
        print("Backlight: ", self.backlight)


led_tv = LED("ONIDA", 800, 55, 10, 150, 10, 120)
led_tv.power_on()
led_tv.display_details()
print(led_tv.status())


class Plasma(TV):                                                              # Child class 2 - Plasma inherited from parent class TV
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan):            # Constructor for additional properties of Plasma
        super().__init__(brand, price, inches)                                                      # Inheriting properties from the parent class TV
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.viewing_angle = "Wide"
        self.backlight = "No"
    
    def display_details(self):
        print("Plasma TV Details:")
        print("Brand: ", self.brand)
        print("Price: ", str(self.price))
        print("Size: ", str(self.inches), " inches")
        print("Screen Thickness: ", str(self.screen_thickness), " mm")
        print("Energy Usage: ", str(self.energy_usage), " watts")
        print("Lifespan: ", str(self.lifespan), " years")
        print("Viewing Angle: ", self.viewing_angle)
        print("Backlight: ", self.backlight)




plasma_tv = Plasma("LG", 700, 50, 15, 200, 8)
plasma_tv.power_on()
plasma_tv.display_details()
print(plasma_tv.status())


