# some simple models


class Model(object):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name


class Building(Model):
    def __init__(self, name, address) -> None:
        super().__init__(name)
        self.address = address


class Ship(Model):
    travels_on = 'water'


class Car(Model):
    travels_on = 'land'


# Serializers are responsible for serializing some model class:
class Serializer(object):
    class Meta:
        model_class = None

    def __init__(self, model=None) -> None:
        super().__init__()
        self.model = model

    # noinspection PyUnusedLocal
    def create(self, serialized_data):
        self.model = self.Meta.model_class()

    def serialize(self):
        return {}


class ModelSerializer(Serializer):
    class Meta:
        model_class = Model

    def serialize(self):
        return {**super().serialize(), 'name': self.model.name}


class VehicleSerializer(ModelSerializer):

    def serialize(self):
        return {**super().serialize(), 'travels_on': self.model.travels_on}


class ShipSerializer(VehicleSerializer):
    class Meta:
        model_class = Ship


class CarSerializer(VehicleSerializer):
    class Meta:
        model_class = Car


class BuildingSerializer(ModelSerializer):
    class Meta:
        model_class = Building

    def serialize(self):
        return {**super().serialize(), 'address': self.model.address}


# Test it
serialized_models_in = {'vanilla1': {'class': Model},
                        'building1': {'class': Building,
                                      'address': 'adventure.minus.sea'},
                        'ship1': {'class': Ship},
                        'car1': {'class': Car}}

serializer_class_map = {Model: ModelSerializer,
                        Building: BuildingSerializer,
                        Car: CarSerializer,
                        Ship: ShipSerializer}


def make_model(name, spec):
    model_class = spec.pop('class')
    return model_class(name, **spec)


models = {name: make_model(name, spec) for name, spec in serialized_models_in.items()}


def get_serializer_class(model):
    return serializer_class_map[type(model)]


serialized_models_out = {name: get_serializer_class(model)(model).serialize() for name, model in models.items()}


