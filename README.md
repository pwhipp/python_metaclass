# Python3 Metaclass Example

We need something a little meaningful so the example consists of some simple models in a class heirarchy and an associated heirarchy of model serializers<sup id="n1">[1](#f1).

The ??first commit shows how serializers need to be accessed for the model classes in order to serialize/deserialize model data.

Maintaining the serializer_class_map quickly becomes cumbersome.

We could define a decorator e.g.
```python
@SetModelClass(ModelSerializer)
class ModelSerializer(Serializer):
    ...
```

but this is repeating the association because its already present in the Meta (so that the serializer can create new models)

We could add a serializer_class field to the models but this is coupling the serializers to the models in an undesirable way. We want to keep the serialization concern to our serializers.

So how about a metaclass?
If we specify a metaclass for our serializers we can update the serializer_class_map whenever we create a new serializer class.

## Footnotes

<b id="f1">1</b> This is a loose abstraction of django models and the django rest framework. [↩](#n1)