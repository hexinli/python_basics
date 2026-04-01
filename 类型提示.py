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
