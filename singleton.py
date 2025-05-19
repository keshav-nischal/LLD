def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


# @singleton
class SimpleSingleton:
    def __init__(self):
        print("Init once!")

# Usage
SimpleSingleton = singleton(SimpleSingleton) 
a = SimpleSingleton()
b = SimpleSingleton()

print(a is b)  # True
