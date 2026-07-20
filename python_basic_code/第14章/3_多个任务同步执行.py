import asyncio
import time

async def work(n, delay):
    print(f"work{n}开始")
    print(f"work{n}执行中......")
    # await去等待一个协程对象(靠asyncio.sleep方法，返回一个协程对象)
    await asyncio.sleep(delay)
    print("work结束")
    return f"work{n}的返回值"


async def main():
    print("main开始")
    start = time.time()
    # 得到三个协程对象
    coroutine_obj_1 = work(1, 2)
    coroutine_obj_2 = work(2, 2)
    coroutine_obj_3 = work(3, 2)

    # 等待coroutine_obj_1执行完成
    res_1 = await  coroutine_obj_1
    print(res_1)

    # 等待coroutine_obj_2执行完成
    res_2 = await  coroutine_obj_2
    print(res_2)

    # 等待coroutine_obj_3执行完成
    res_3 = await  coroutine_obj_3
    print(res_3)

    print("main结束", time.time() - start)
    return "main的返回值"


result = asyncio.run(main())
print(result)
