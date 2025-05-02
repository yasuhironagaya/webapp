


def my_decorator(func):
    def wrapper():
        print("前処理")
        func()
        print("後処理")

    return wrapper


@my_decorator
def say_hello():
    print("こんにちは")


say_hello()
