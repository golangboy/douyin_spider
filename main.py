import asyncio
import time

import requests
from pyppeteer import launch


async def main():
    browser = await launch(headless=False, dumpio=True, autoClose=True,
                           args=['--no-sandbox', '--disable-infobars', '--user-data-dir=./mydata'])  # 进入有头模式
    page = await browser.newPage()  # 打开新的标签页
    # await page.setViewport({'width': 1920, 'height': 1080})  # 页面大小一致
    await page.goto('https://www.douyin.com')  # 访问主页
    while True:
        try:
            title = await page.title()
            print(title)
            if title != "抖音-记录美好生活":
                # 刷新
                await page.reload()
                time.sleep(2)
                continue
            time.sleep(3)
            print(title)
            # 执行js:document.getElementsByTagName("video").length
            video_url = await page.evaluate('document.getElementsByTagName("video")[0].children[2].src')
            # video_url是视频链接，格式是mp4
            # http get实现下载
            # 当前时间日期生成文件名
            file_name = time.strftime("%Y%m%d%H%M%S", time.localtime())
            file_name = file_name + '.mp4'
            r = requests.get(video_url)
            with open("video/" + file_name, 'wb') as f:
                f.write(r.content)

            time.sleep(3)
            await page.reload()
        except Exception as e:
            continue


# 调用,无头模式
if __name__ == '__main__':
    # 捕获异常
    asyncio.get_event_loop().run_until_complete(main())
