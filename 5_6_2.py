import asyncio
import time


async def test_03():
   print("Something")
   return await test_04()


async def test_04():
   print("Hi")
   return await test_05()


async def test_05():
   print("Walk")
   return await test_end()


async def test_end():
   print("Finished!")


async def main():
   await asyncio.gather(test_03(), test_05(), test_04(), test_05(), test_end())


time_start = time.time()
asyncio.run(main())
time_end = time.time()
print("Execution Time: " + str(round(time_end - time_start, 2)) + " seconds")