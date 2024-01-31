import asyncio
from time import sleep,strftime


async def outraFuncao(p):
    print(f'teste{p}')
    await asyncio.sleep(1)
    print(f"Momento da função {p}: {strftime('%X')}")
    await asyncio.sleep(1)
    print(f'teste{p}')


async def funcao(p):
    print(f"Iniciou {strftime('%X')}")
    task = asyncio.create_task(outraFuncao(1))
    task2 = asyncio.create_task(outraFuncao(2))
    await task2

    print('teste')
    await task
    print(f"Terminou {strftime('%X')}")


asyncio.run(funcao(1))
