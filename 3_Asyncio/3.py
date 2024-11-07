import asyncio
import json
import time

async def fetch_names(names):
    return names['name']

async def fetch_purchases(purchases):
    return purchases['purchases']

async def main():
    fs = open(file = 'user_data.json', mode = 'r')
    data = json.load(fs)
    total_amounts = 0

    tasks = [fetch_names(i) for i in data]
    tasks2 = [fetch_purchases(i) for i in data]


    results = await asyncio.gather(*tasks)
    results2 = await asyncio.gather(*tasks2)


    print("Names:")
    time.sleep(0.5)


    for result in results:
        print(result)
        print()
        time.sleep(0.5)

    for result2 in results2:
        print(result2)
        print()
        time.sleep(0.5)
        for i in result2:
            amount = i['amount']
            total_amounts += amount
    
    print(f"Total amounts of purchase: {total_amounts}")
    

if __name__ == '__main__':
    asyncio.run(main())