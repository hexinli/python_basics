# 1，协程函数(coroutine Function)：使用 async 关键字修饰的函数，就是协程函数。
# 2. 协程对象(coroutine Object): 调用协程函数，就会得到协程对象
import asyncio


# 注意：调用协程函数，并不会执行协程函数中的代码

async def work():
    print("work开始")
    print("work执行中......")
    print("work结束")
    return "工作结果"


# 调用协程函数，会得到协程对象
coroutine_object = work()
print(coroutine_object)

# asyncio.run 方法做了3件事情
# 1.创建一个事件循环。
# 2.将接收到的协程对象，包装成一个任务(task),交给事件循环。
# 3.启动事件循环。
result = asyncio.run(coroutine_object)

print(result)
