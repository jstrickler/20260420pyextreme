import time
import asyncio
from apod_async import fetch_apod_async

DATES = [f'2023-01-{day:02d}' for day in range(1, 32)]

async def main():
    start_time = time.perf_counter()

    for date in DATES:
        print(f"{date = }")
        await fetch_apod_async(date)

    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"That took {elapsed} seconds")

if __name__ == "__main__":
    asyncio.run(main())