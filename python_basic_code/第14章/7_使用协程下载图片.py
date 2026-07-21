import asyncio
import time

import aiohttp


async def download_picture(session, index, url):
    print(f"开始下载：{url}")
    # 发送网络请求，获取这张图片，请求发送出去后，要等待服务器把数据返回，等的这段事件就是IO等待
    response = await session.get(url)
    # 等待数据(图片数据可能分多次传输，需要等待数据全部读完，等的这段时间也是IO等待)
    content = await response.read()
    print(f"下载完毕")
    with open(f"{index}.jpg", "wb") as file:
        file.write(content)
    # 释放连接资源(告诉aiohttp，这个连接我不用了，你可以回收了)
    await  response.release()


async def main():
    stat = time.time()
    url_list = [
        "https://picsum.photos/800/600?random=1",
        "https://picsum.photos/800/600?random=2",
        "https://picsum.photos/800/600?random=3",
        "https://picsum.photos/800/600?random=4",
        "https://picsum.photos/800/600?random=5",
        "https://picsum.photos/800/600?random=6",
        "https://picsum.photos/800/600?random=7",
        "https://picsum.photos/800/600?random=8",
        "https://picsum.photos/800/600?random=9",
        "https://picsum.photos/800/600?random=10",
        "https://picsum.photos/800/600?random=11",
        "https://picsum.photos/800/600?random=12",
        "https://picsum.photos/800/600?random=13",
        "https://picsum.photos/800/600?random=14",
        "https://picsum.photos/800/600?random=15",
        "https://picsum.photos/800/600?random=16",
        "https://picsum.photos/800/600?random=17",
        "https://picsum.photos/800/600?random=18",
        "https://picsum.photos/800/600?random=19",
        "https://picsum.photos/800/600?random=20"
    ]
    # 创建会话对象(发送请求的工具)
    session = aiohttp.ClientSession()
    # 创建多个协程对象
    coroutine_list = [download_picture(session, index, url) for index, url in enumerate(url_list)]
    # 将多个协程对象交给事件循环
    await asyncio.gather(*coroutine_list)
    # 关闭会话
    await session.close()
    print(f"总花费时间{time.time() - stat}")


if __name__ == '__main__':
    asyncio.run(main())
