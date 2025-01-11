import asyncio
import time
import random


async def task(name):
    wait_time_1 = round(random.randint(1000, 5000)/1000, 2)
    wait_time_2 = round(random.randint(1000, 5000)/1000, 2)
    start_time = time.time()
    print(f"#{name}:\tstarted, I'll wait for {wait_time_1}s")
    await asyncio.sleep(wait_time_1)
    print(f"#{name}:\tI'll wait again for {wait_time_2}s")
    await asyncio.sleep(wait_time_2)
    print(f"#{name}:\tfinished")
    end_time = time.time()
    return f"#{name}:\tfinished in {round(end_time - start_time, 2)}"


async def main():
    tasks = [task(f"Task {i}") for i in range(1, 4)]

    start_time = time.time()
    results = await asyncio.gather(*tasks)
    end_time = time.time()

    print(f"gather took {round(end_time - start_time, 2)}s")
    for result in results:
        print(result)
    print(f"Total time {round(time.time() - start_time, 2)}s")


if __name__ == "__main__":
    asyncio.run(main())
