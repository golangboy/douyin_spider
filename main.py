import asyncio
import time

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
            video_length = await page.evaluate('document.getElementsByTagName("video")[0].children[2].src')
            print(video_length)
            time.sleep(3)
            await page.reload()
        except Exception as e:
            continue


# 调用,无头模式
if __name__ == '__main__':
    # 捕获异常
    asyncio.get_event_loop().run_until_complete(main())
