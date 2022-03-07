import asyncio


async def io_intensive():
    sleep_time = 1
    await asyncio.sleep(sleep_time)
    print(f"slept {sleep_time}")
    return sleep_time + 3


async def get_stuff():
    print(f"getting stuff")
    return await io_intensive()


async def main():
    print("main")
    got = await asyncio.gather(
        get_stuff(),
        get_stuff(),
        get_stuff()
    )
    print(f"got: {got}")


asyncio.run(main())
