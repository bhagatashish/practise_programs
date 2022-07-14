class car:
    car_model = 'alto'
    def __init__(self, wieght, model):
        self.car_model = 'city' # class variable can be accessed by intanse variable
        self.wieght = 3
        self.model='suzuki'

car1 = car(4,'kia')
print(car1.car_model)
print(car1.model)