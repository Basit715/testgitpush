# def cal_add(x):
#     def add(y):
#         return x+y
#     return add
#
#
# var = cal_add(10)
# sum = var(20)
# print(sum)
def hello_decorator(func):
    def inner(a, b):
        print("We are inside inner and calling func")
        value = func(a, b)
        print("we have called the func")
        return value

    return inner



@hello_decorator
def sum_of_two_numbers(x, y):
    return x + y

y = sum_of_two_numbers(10,20)
print(y)
