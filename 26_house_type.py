class Item:

    def __init__(self, furniture, area):
        self.furniture = furniture
        self.area = area

    def __str__(self):
        return f"{self.furniture}"


class House:

    def __init__(self, h_type, h_surface):
        self.h_type = h_type
        self.h_surface = h_surface
        self.rest_surface = h_surface
        self.items = []


    def add_item(self,item):
        if self.rest_surface >= item.area:
            self.items.append(item)
            self.rest_surface -= item.area
            return f'self.items'
        else:
            print(f"not enough space to add{item.furniture}")

    def __str__(self):

        furniture_list = ', '.join(str(item) for item in self.items)
        return (f"House Type: {self.h_type}, Total Size: {self.h_surface}m², "
                f"Furniture List: [{furniture_list}], Rest of Size: {self.rest_surface}m²")

    # def __str__(self):
    #     furniture_list = ', '.join(str(item) for item in self.items)
    #     return (f"House Type: {self.h_type}, Total Size: {self.h_surface}m², "
    #             f"Furniture List: [{furniture_list}], Rest of Size: {self.rest_surface}m²")

    # Create items
bed = Item('bed', 4)
placard = Item('placard', 2.5)
table = Item('table', 1.5)
    #
    # Create a house

my_house = House('house', 200)

# Add items to the house
my_house.add_item(bed)
my_house.add_item(placard)
my_house.add_item(table)
    # Print house details
print(my_house)
