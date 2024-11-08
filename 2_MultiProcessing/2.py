from multiprocessing import Process
import csv
import time

def data_aggregation1(data1):
    amounts = 0.0
    transactions = 0
    for i in data1:
        for j in i:
            if '.' in j:
                amounts += float(j)
    transactions += len(data1) - 1
    # print("1st amounts:", amounts)
    # print("1st transactions:", transactions)
    return [amounts, transactions]



def data_aggregation2(data2):
    amounts = 0.0
    transactions = 0
    for i in data2:
        for j in i:
            if '.' in j:
                amounts += float(j)
    transactions += len(data2) - 1
    # print("2nd amounts:", amounts)
    # print("2nd transactions:", transactions)
    return [amounts, transactions]


def data_aggregation3(data3):
    amounts = 0.0
    transactions = 0
    for i in data3:
        for j in i:
            if '.' in j:
                amounts += float(j)
    transactions += len(data3) - 1
    # print("3rd amounts:", amounts)
    # print("3rd transactions:", transactions)
    return [amounts, transactions]




if __name__ == "__main__":
    total_amounts = 0.0
    total_transactions = 0
    ls = []

    f1 = open('transactions_region1.csv', 'r')
    reader1 = csv.reader(f1)
    data1 = list(reader1) # now data is serializable and we'll not have pickle error

    process1 = Process(target=data_aggregation1, args=(data1,))
    res1 = data_aggregation1(data1)

    f2 = open('transactions_region2.csv', 'r')
    reader2 = csv.reader(f2)
    data2 = list(reader2) # now data is serializable and we'll not have pickle error

    process2 = Process(target=data_aggregation2, args=(data2,))
    res2 = data_aggregation2(data2)


    f3 = open('transactions_region3.csv', 'r')
    reader3 = csv.reader(f3)
    data3 = list(reader3) # now data is serializable and we'll not have pickle error

    process3 = Process(target=data_aggregation3, args=(data3,))
    res3 = data_aggregation3(data3)



    process1.start()
    # time.sleep(0.5)

    process2.start()
    # time.sleep(0.5)

    process3.start()

    process1.join()
    # time.sleep(0.5)

    process2.join()
    # time.sleep(0.5)

    process3.join()

    for i in range(len(res1)):
        result1 = res1[i] + res2[i] + res3[i]

    result2 = res1[0] + res2[0] + res3[0]

    

    summary = f"Total transactions count is: {result1}. Total amounts are: {round(result2, 2)}"
    print(summary)