import asyncio
import time


async def work(n, delay):
    print(f"work{n}开始")
    print(f"work{n}执行中......")
    # await去等待一个协程对象(靠asyncio.sleep方法，返回一个协程对象)
    await asyncio.sleep(delay)
    print(f"work{n}结束")
    return f"work{n}的返回值"


async def main():
    print("main开始")
    start = time.time()

    # asyncio.create_task会把一个协程对象包装成一个可被事件循环调度的任务，并注册到事件循环中
    task_1 = asyncio.create_task(work(1, 1))
    task_2 = asyncio.create_task(work(2, 2))
    task_3 = asyncio.create_task(work(3, 3))

    # 等待task_1执行完成
    res_1 = await  task_1
    print(res_1)

    # 等待task_2执行完成
    res_2 = await  task_2
    print(res_2)

    # 等待task_3执行完成
    res_3 = await  task_3
    print(res_3)

    print("main结束", time.time() - start)
    return "main的返回值"


result = asyncio.run(main())
print(result)
