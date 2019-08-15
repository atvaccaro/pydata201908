import asyncio

import requests

async def async_get():
    event_loop = asyncio.get_event_loop()
    
    def get(url):
        requests.get(url)
        print('done')
    
    futures = []
    
    for _ in range(20):
        futures.append(event_loop.run_in_executor(None, get, 'https://google.com'))
    
    for f in asyncio.as_completed(futures):
        await f

loop = asyncio.get_event_loop()
loop.run_until_complete(async_get())
