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

    # 把多个协程对象同时丢给事件循环，并在全部执行完毕后，一次性拿到所有的结果。
    result1 = await asyncio.gather(work(1, 2), work(2, 2), work(3, 2))
    print(result1)


    print("main结束", time.time() - start)
    return "main的返回值"


result = asyncio.run(main())
print(result)
