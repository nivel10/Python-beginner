class Vehicle:

    # class atribute
    type = 'fou wheeled vehicle.'

    # special method tha build the object
    def __init__(self, mark: str = '', model: str = '', color: str = ''):
        # instance attributes
        self.mark = mark
        self.model = model
        self.color = color

    # current method
    def start_vehicle(self):
        # print(f'The vehicle mark: {self.mark}, model: {self.model}, color: {self.color}. Start')
        print(f'The vehicle mark: {self.mark} and model: {self.model}. Start')

my_auto_1: Vehicle = Vehicle(mark='Ford', model='Bronco', color='blue')
print('')
my_auto_1.start_vehicle()
print(f'Mark: {my_auto_1.mark}')
print(my_auto_1.type)


my_auto_2: Vehicle = Vehicle(mark='Toyota', model='Machito', color='Grey')
print('')
my_auto_2.start_vehicle()
print(f'Mark: {my_auto_2.mark}')
print(my_auto_2.type)
