from multiprocessing import Process
import csv

def data_aggregation1(reader1):
    count_of_transactions = 0
    total_amount = 0
    for i in reader1:
        if type(i) == float:
            total_amount += i
    for j in reader1:
        if type(j) == int:
            count_of_transactions += 1
    return total_amount, count_of_transactions

def data_aggregation2(reader2):
    count_of_transactions = 0
    total_amount = 0
    for i in reader2:
        if type(i) == float:
            total_amount += i
    for j in reader2:
        if type(j) == int:
            count_of_transactions += 1
    return total_amount, count_of_transactions

def data_aggregation3(reader3):
    count_of_transactions = 0
    total_amount = 0
    for i in reader3:
        if type(i) == float:
            total_amount += i
    for j in reader3:
        if type(j) == int:
            count_of_transactions += 1
    return total_amount, count_of_transactions


    

if __name__ == "__main__":
    with open('transactions_region1.csv', 'r') as f1:
        reader1 = csv.reader(f1)
    process1 = Process(target=data_aggregation1, args=(reader1,))
    with open('transactions_region2.csv', 'r') as f2:
        reader2 = csv.reader(f2)
    process2 = Process(target=data_aggregation2, args=(reader2,))
    with open('transactions_region3.csv', 'r') as f3:
        reader3 = csv.reader(f3)
    process3 = Process(target=data_aggregation3, args=(reader3,))

    process1.start()
    