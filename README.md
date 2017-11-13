# Python3 Metaclass Example

We need something a little meaningful so the example consists of some simple models in a class heirarchy and an associated heirarchy of model serializers<sup id="n1">[1](#f1).

The [first commit](https://github.com/pwhipp/python_metaclass/commit/97d3b9aaa950f543f77d23dae3f633e5845543ca) shows how serializers need to be accessed for the model classes in order to serialize/deserialize model data.

Maintaining the serializer_class_map quickly becomes cumbersome.

We could define a decorator e.g.
```python
@SetModelClass(ModelSerializer)
class ModelSerializer(Serializer):
    ...
```

but this is repeating the association because its already present in the Meta (so that the serializer can create new models)

We could add a serializer_class field to the models but this is coupling the serializers to the models in an undesirable way. We want to keep the serialization concern to our serializers.

## So how about a metaclass?
If we specify a metaclass for our serializers we can update the serializer_class_map whenever we create a new serializer class.

[This commit](https://github.com/pwhipp/python_metaclass/commit/f1578ba6a66c40e9e15547c94980a68a11ca07d0) shows the use of the `MappedSerializerClass` to maintain the serializer_class_map. This separates out the mapping concern and is a pretty good solution.

## Footnotes

<b id="f1">1</b> This is a loose abstraction of [django models](https://docs.djangoproject.com/en/1.11/topics/db/models/) and the [django rest framework](http://www.django-rest-framework.org/). [↩](#n1)