import asyncio


async def sum(a, b):
    return a + b


async def print_sum(a, b):
    result = await sum(a, b)
    print(f"Result: {result}")


# Event Loop
# coro = sum(3, 5)    
coro = print_sum(3, 5)
event_loop = asyncio.new_event_loop()
result = event_loop.run_until_complete(coro)
# print(f"Result: {result}")

# print_sum(3, 5)
