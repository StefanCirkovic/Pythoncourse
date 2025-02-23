

class Car:

    VALID_CARS = {
        "Audi": [
            {"model": "A4", "production_year": 2004},
            {"model": "A5", "production_year": 2003},
            {"model": "A6", "production_year": 2002},
        ],
        "BMW": [
            {"model": "M5", "production_year": 2010},
            {"model": "M3", "production_year": 2008},
        ],
        "Mercedes": [
            {"model": "GLK", "production_year": 2015},
            {"model": "GLE", "production_year": 2017},
        ],
    }


    def __init__(self):
        self.__brand = None
        self.__model = None
        self.__production_year = None


    @property
    def model(self):
        return self.__model


    @model.setter
    def model(self, model):


        if self.__brand is None:
            raise ValueError("Brand is invalid")

        valid_models = []
        for car in Car.VALID_CARS[self.__brand]:
            valid_models.append(car["model"])

        if model not in valid_models:
            raise ValueError("Model is not valid!")

        self.__model = model

        for car_model in Car.VALID_CARS[self.__brand]:
            if car_model["model"] == model:
                self.__production_year = car_model['production_year']



    @property
    def brand(self):
        return self.__brand



    @brand.setter
    def brand(self, brand):

        if brand not in Car.VALID_CARS:
            raise ValueError("Invalid car!")

        self.__brand = brand



    @property
    def production_year(self):
        return self.__production_year



    @production_year.setter
    def production_year(self, year):

        if self.model is None:
            raise ValueError("Production year cannot be set!")

        if self.__model is not None and self.__production_year is not None:
            raise ValueError("Production year cannot be set!")

        self.__production_year = year


audi = Car()

audi.brand = "Audi"
audi.model = "A4"
audi.production_year = 2005
print(audi.production_year)