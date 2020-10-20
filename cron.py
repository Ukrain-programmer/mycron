import os
from datetime import datetime
import time
from crontab import CronTab
from croniter import croniter


def child(command):
    #print(command)
    os.system(command)
    os._exit(0)


def parent():
    base = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour,
                    datetime.now().minute)
    word_list=[]
    time_list = []
    iter_list = []
    counters =[]
    cron = CronTab(tabfile='task.tab')
    for word in cron:
        str_word =str(word)
        if str_word[:1] == '#':
            continue
        word_list.append(str_word)

    for i in range(len(word_list)):
        count=0
        for j in word_list[i]:

            # if j == '@':
            #     count = len(word_list[i].split()[0])
            #     print(len(word_list[i].split()[0]))
            if j.isalpha():
                if word_list[i][count-1:count] == '/':
                    count-=1
                counters.append(count)
                break
            count+=1
        iter = croniter(word_list[i][:count], base)
        iter_list.append(iter)

    for j in range(len(word_list)):
        compare_time = iter_list[j].get_next(datetime)
        time_list.append(compare_time)


    size = len(word_list)
    print(word_list)
    print(time_list)
    print(counters)
    print(datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour,
                   datetime.now().minute, datetime.now().second))
    while True:

        i=0
        for i in range(size):
            if time_list[i] == datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour,datetime.now().minute):
                time_list[i] = iter_list[i].get_next(datetime)
                print(datetime.now())
                pid = os.fork()
                if pid == 0:
                    child(word_list[i][counters[i]:])
               
        time.sleep(1)

parent()







