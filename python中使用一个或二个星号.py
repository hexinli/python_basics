"""
我们可以把 * 想象成一个拉链：在定义函数时它把散落的参数拉起来凑成一个整体，在调用函数时它把一个整体拉开散成零件。
"""

"""
1. 在函数定义中使用（打包）
当你不知道用户会传入多少个参数时，可以使用 * 将多余的参数收集到一个**元组（tuple）**中。

核心用法：*args
*args 代表 "arguments"（位置参数）。它收集所有未被前面的位置参数捕获的参数
"""
def sum_all(*numbers):
    # numbers 在这里是一个元组 (1, 2, 3, 4)
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_all(1, 2, 3, 4))  # 输出: 10

my_tuple = (1, 2, 3, 4)
print(sum_all(*my_tuple)) #正确的传参方式
# print(sum_all(my_tuple)) #错误的传参方式

"""
进阶用法：强制关键字参数
如果在参数列表中单独使用一个 *，它之后的所有参数都必须以 key=value 的形式传入。
"""
def person_info(name, *, age, city):
    print(f"{name} is {age} years old and lives in {city}")

# person_info("Alice", 25, "NY")      # 报错！
person_info("Alice", age=25, city="NY") # 正确

"""
2. 在函数调用中使用（解包）
如果你手中有一个列表或元组，想把它们作为独立的参数传给函数，就在前面加 *。

核心用法：序列解包
这相当于手动把列表里的每个元素拆出来填进括号里。
"""
def move(x, y, z):
    print(f"Moving to coordinates: {x}, {y}, {z}")

coords = [10, 20, 30]

# 传统的笨办法：move(coords[0], coords[1], coords[2])
# 使用 * 号解包：
move(*coords) # 输出: Moving to coordinates: 10, 20, 30

"""
3. 双星号 ** 的用法（字典/关键字）
单星号处理位置参数，双星号则专门处理关键字参数（Dict）。

A. 定义时（收集成字典）：
"""
def save_user(**data):
    # data 会变成一个字典 {'name': 'Bob', 'id': 1}
    print(data)

save_user(name="Bob", id=1, role="Admin")

"""
B. 调用时（解包字典）：
"""
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

user_info = {"first_name": "Elon", "last_name": "Musk"}
greet(**user_info) # 相当于 greet(first_name="Elon", last_name="Musk")

"""
4. 综合实战案例
在实际开发中，我们经常看到 *args 和 **kwargs 同时出现，这代表该函数可以接收任何形式的参数，通常用于装饰器或代理函数。
"""
def logger_wrapper(func, *args, **kwargs):
    print(f"--- 准备执行函数: {func.__name__} ---")
    # 同时解包位置参数和关键字参数
    result = func(*args, **kwargs)
    print(f"--- 执行结束，结果为: {result} ---")
    return result

def add(a, b, note="None"):
    return a + b

# 调用
logger_wrapper(add, 5, 10, note="Testing star usage")