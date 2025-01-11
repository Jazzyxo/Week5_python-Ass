# Base class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        return f"{self.brand} {self.model} is now powered on."

# Subclass: Smartphone (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)  # Initialize parent class attributes
        self.storage = storage
        self.__camera_megapixels = camera_megapixels  # Encapsulated attribute

    # Getter for encapsulated attribute
    def get_camera_megapixels(self):
        return self.__camera_megapixels

    # Method to display smartphone details
    def display_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Camera: {self.get_camera_megapixels()}MP"

# Create an object of Smartphone
my_phone = Smartphone("Samsung", "Z flip4", 256, 12)

# Using methods
print(my_phone.power_on())  # Inherited method
print(my_phone.display_specs())  # Smartphone-specific method
