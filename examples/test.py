import pyfl
from pyfl import underground

client = underground("YOUR API KEY HERE")

async def main():
    print(client.apiKey)
    print(await client.getLineStatus("victoria"))
    print(await client.getLineStatus("b"))

asyncio.get_event_loop().run_until_complete(main())