"""
1.1 基础变量与内置容器
在 Python 3.9+ 中，你可以直接使用内置的 list, dict, tuple 来定义容器内部元素的类型。
"""
# 基础类型
age: int = 25
name: str = "Gemini"
is_active: bool = True

# 容器类型 (Python 3.9+)
users: list[str] = ["Alice", "Bob"]
config: dict[str, float] = {"threshold": 0.8, "rate": 1.5}
coordinate: tuple[int, int, int] = (10, 20, 30)

"""
1.2 联合类型 (Union) 与可选值 (Optional)
这是你提到的 | 符号的用武之地。它在 Python 3.10 中被引入，用来简化旧版的 Union。
| (Union): 表示可以是多种类型之一。
None 处理: 当一个参数可以不传时，通常标注为 Type | None。
"""


# Python 3.10+ 写法 (推荐)
def get_user_id(user_name: str | int) -> str:
    return str(name)


# 默认值为 None 的常见模式
def process_data(data: list[int], limit: int | None = None) -> None:
    if limit:
        print(data[:limit])
    else:
        print(data)


"""
3. 进阶：框架源码中常见的特殊类型
当你深入阅读框架源码（如 FastAPI, LangChain, Pydantic）时，会遇到更复杂的标注：
类型	        含义	          应用场景
Any	        任何类型	      当你无法确定或不想限制类型时使用。
Callable	可调用对象	  当参数是一个函数时，如 callback: Callable[[int], str]。
Sequence	序列	          比 list 更通用，接受 list, tuple, str 等。
TypeVar     泛型	          用于编写可以处理多种类型但保持逻辑一致的代码。
"""
"""
4. 综合实战 Demo
假设我们要写一个处理 AI 提示词的类，结合了你提到的所有语法：
"""
from typing import Callable, Sequence


class PromptManager:
    def __init__(self, default_stop: list[str] | None = None):
        # 属性标注
        self.history: list[dict[str, str]] = []
        self.stop_words: list[str] = default_stop or ["\n"]

    def format_prompts(
            self,
            prompts: Sequence[str],  # 接受列表或元组等字符串序列
            prefix: str | None = None,  # 可选的前缀
            on_complete: Callable[[int], None] | None = None  # 可选的回调函数
    ) -> list[str]:  # 返回字符串列表

        results = []
        for p in prompts:
            formatted = f"{prefix}: {p}" if prefix else p
            results.append(formatted)

        if on_complete:
            on_complete(len(results))

        return results


# 使用例子
mgr = PromptManager(default_stop=["END"])
# IDE 会在这里提醒你 prompts 需要传入序列，prefix 可以是字符串或 None
output = mgr.format_prompts(prompts=["Hello", "Who are you?"], prefix="System")
print(output)

"""
进阶的类型提示（Type Hints）通常出现在需要高度抽象、通用性强或者逻辑严密的代码中（例如 Web 框架或数据处理库）。
以下是几种在 Python 源码中非常常见的进阶用法及其代码示例：
1. 泛型 (Generics / TypeVar)
当你编写一个函数或类，它可以处理多种类型，但你希望输入类型和输出类型保持一致时，就需要用到泛型。
场景：从列表中随机获取一个元素。
"""
from typing import TypeVar, Sequence

# 定义一个类型变量 T，它可以代表任何类型
T = TypeVar('T')


def get_first_element(items: Sequence[T]) -> T:
    """无论输入什么类型的序列，返回值的类型都与序列元素一致"""
    return items[0]


# 使用
n: int = get_first_element([1, 2, 3])  # 自动识别返回 int
s: str = get_first_element(["a", "b"])  # 自动识别返回 str

"""
2. 可调用对象 (Callable)
当你的函数需要接收另一个函数作为参数时（例如回调函数、装饰器），使用 Callable。

语法：Callable[[参数类型1, 参数类型2], 返回类型]
"""
from typing import Callable


def execute_task(data: str, processor: Callable[[str], int]) -> int:
    """接收一个字符串，通过 processor 处理后返回整数"""
    return processor(data)


# 示例：将字符串长度作为处理逻辑
result = execute_task("Hello World", len)

"""
3. 结构化字典 (TypedDict)
普通的 dict[str, Any] 无法约束字典里到底有哪些 Key。TypedDict 可以像定义类一样定义字典的结构。

场景：API 返回的固定 JSON 结构。
"""
from typing import TypedDict


class UserInfo(TypedDict):
    uid: int
    username: str
    is_admin: bool


def save_user(user: UserInfo) -> None:
    print(f"Saving {user['username']}...")


# 如果漏写了 'uid' 或者 'is_admin' 传了字符串，IDE 会直接报错
save_user({"uid": 1, "username": "Alice", "is_admin": True})

"""
4. 协议与鸭子类型 (Protocol)
这是最强大的进阶功能之一。它不要求类继承某个父类，只要类实现了指定的方法，就认为它符合要求。这被称为静态鸭子类型。

场景：任何实现了 .draw() 方法的对象都可以被处理。
"""
from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> None: ...  # 注意这里用 Ellipsis (...)


class Circle:
    def draw(self) -> None: print("Drawing a circle")


class Square:
    def draw(self) -> None: print("Drawing a square")


def render(shape: Drawable) -> None:
    shape.draw()


render(Circle())  # 正常运行
render(Square())  # 正常运行

"""
5. 字面量类型 (Literal)
有时候你希望变量的值不仅仅是某种类型，而必须是几个具体的常量值。

场景：文件打开模式、API 请求方法。
"""
from typing import Literal


def connect_db(env: Literal["dev", "test", "prod"]) -> None:
    print(f"Connecting to {env} database...")


connect_db("dev")  # OK
# connect_db("local") # IDE 会报错，因为 "local" 不在 Literal 中

"""
6. 最终实战：复杂框架风格 Demo
我们将以上几种结合起来，模拟一个简单的插件处理系统：
"""
from typing import TypeVar, Callable, Protocol, Literal


# 1. 定义协议
class Plugin(Protocol):
    name: str

    def run(self, data: str) -> str: ...


# 2. 定义泛型和联合类型
T = TypeVar("T", bound=Plugin)  # T 必须是实现了 Plugin 协议的类


def run_plugin_system(
        plugin: T,
        mode: Literal["sync", "async"],
        on_error: Callable[[Exception], None] | None = None
) -> str:
    try:
        print(f"Mode: {mode}")
        return plugin.run("Initial Data")
    except Exception as e:
        if on_error:
            on_error(e)
        return "Error"


# 实现一个符合协议的类
class UpperPlugin:
    name = "Uppercase Tool"

    def run(self, data: str) -> str:
        return data.upper()


# 调用
run_plugin_system(UpperPlugin(), mode="sync")
