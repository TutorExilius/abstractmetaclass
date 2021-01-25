<<<<<<< HEAD
Solution based on https://stackoverflow.com/questions/55309793/python-enforce-specific-method-signature-for-subclasses


A small python metaclass, which enforce subclasses to implement methods with same signature from derived abstract class(es).

All parent classes, which shall be used like an abstract class has to use the metaclass:

class Parent(metaclass=AbstractClassMeta):
    pass

All subclasses will be enforced to implement all callables derived from parent(s).
If one method in the child class is missing or has a different signature, the class creation will be cancelled by
raising an exception.
