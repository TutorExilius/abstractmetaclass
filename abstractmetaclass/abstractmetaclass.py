import inspect
from types import FunctionType


class BadSignatureException(Exception):
    pass

# based on https://stackoverflow.com/questions/55309793/python-enforce-specific-method-signature-for-subclasses
class SignatureCheckerMeta(type):
    def __new__(cls, name, base_classes, d, base_class_method_names={}):
        # For each method in d, check to see if any base class already
        # defined a method with that name. If so, make sure the
        # signatures are the same.
        for method_name in d:
            f = d[method_name]

            if not isinstance(f, FunctionType):
                continue
            for base_class in base_classes:
                try:
                    f_signature = inspect.signature(f)
                    f_base = getattr(base_class, method_name)
                    f_base_signature = inspect.signature(f_base)
                    if not f_signature == f_base_signature:
                        raise BadSignatureException(
                            f"{name}.{method_name}{f_signature}"
                            f"\nExpected: {name}.{method_name}{f_base_signature}"
                        )
                except AttributeError:
                    # This method was not defined in this base class,
                    # So just go to the next base class.
                    continue

        # For each method in Parent, check if any of them
        # is implemented in Child class.
        if len(base_class_method_names):
            for base_class, methods in base_class_method_names.items():
                for method_name, method in methods:
                    if not callable(method) or method_name in d:
                        continue
                    else:
                        method_signature = inspect.signature(method)
                        raise NotImplementedError(
                            f"missing {name}.{method_name}{method_signature}"
                            f"\nfrom derived parent: {base_class.__name__}.{method_name}{method_signature}"
                        )

        return super().__new__(cls, name, base_classes, d)


class AbstractClassMeta(SignatureCheckerMeta):
    def __new__(cls, name, base_classes, d):
        if len(base_classes):
            base_class_method_names = {}
            for base_class in base_classes:
                if base_class not in base_class_method_names:
                    base_class_method_names[base_class] = [method_name for method_name in base_class.__dict__.items()]

            return super().__new__(cls, name, base_classes, d, base_class_method_names)
        else:
            return super().__new__(cls, name, base_classes, d)
