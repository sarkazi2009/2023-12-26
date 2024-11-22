import inspect


def introspection_info(obj):
    type_ = type(obj)
    attributes = dir(obj)
    methods = [method for method in inspect.getmembers(obj, predicate=inspect.ismethod)]
    module = inspect.getmodule(obj)
    return {'type': type_, 'attributes': attributes, 'methods': methods, 'module': module}


number_info = introspection_info(42)
print(number_info)
