A small python metaclass, which enforce subclasses to implement methods with same signature from derived abstract class(es).

All parent classes, which shall be used like an abstract class has to use the metaclass:

class Parent(metaclass=AbstractClassMeta):
    pass

All subclasses will be enforced to implement all callables derived from parent(s).
If one method is missing or has not the same signature, like its parent, an exception occurs.
