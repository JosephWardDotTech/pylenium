# singleton instances of 'global' objects, our config is currently the only use of this meta class
# we want a single config object, instantiated at runtime
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
