from threading import Thread

def reading_new_lines(fs):
    res = ""
    for char in fs:
        if char == '\n':
            res += '\n'
        else:
            res += char
    print(res)



def new_line_checking(fs2):
    target = "ERROR"
    count = 0
    for i in fs2:
        if target in i:
            count += 1
            print(count, ":", target)

if __name__ == "__main__":

    fs = open('server_log.txt', 'r')
    fs2 = open('server_log.txt', 'r')


    thread1 = Thread(target=reading_new_lines, args= (fs, ))
    thread2 = Thread(target=new_line_checking, args= (fs2, ))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()