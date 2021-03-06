import aiohttp


async def add_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://python.org') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
