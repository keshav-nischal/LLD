def dacorator(func):
    def wrapper():
        print("logging start")
        result = func()
        print("logging end")
        return result
    return wrapper

@dacorator
def funcAlpha():
    print("hello world")

funcAlpha()

# funcAlpha = dacorator(funcAlpha)