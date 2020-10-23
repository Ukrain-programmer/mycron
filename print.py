#!/usr/bin/python3
import datetime
def main():
	with open ('file.txt','wt',encoding = 'utf-8') as inFile:
		inFile.write(str(datetime.datetime.now().time()))




if __name__ == '__main__':
	main()


# def child(command):
#    # print(command)
#     os.system(command)
#     os._exit(0)
#
#
# def parent():
#     base = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour,
#                     datetime.now().minute)
#     word_list=[]
#     time_list = []
#     iter_list = []
#     cron = CronTab(tabfile='task.tab')
#     for word in cron:
#         print(word)
#         str_word =str(word)
#         match = re.match("^[/d]")
#         if str_word[:1].:
#             continue
#         word_list.append(str_word)
#     print(word_list)
#     for i in range(len(word_list)):
#         #print(word_list[i][:10])
#         iter = croniter(word_list[i][:10], base)
#         iter_list.append(iter)
#
#     for j in range(len(word_list)):
#         compare_time = iter_list[j].get_next(datetime)
#         time_list.append(compare_time)
#
#     #print(time_list)
#     size = len(word_list)
#
#     while True:
#         print(datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour,
#                        datetime.now().minute, datetime.now().second))
#         i=0
#         for i in range(size):
#             if time_list[i] == datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour,datetime.now().minute):
#                 time_list[i] = iter_list[i].get_next(datetime)
#                 pid = os.fork()
#                 if pid == 0:
#                     child(word_list[i][10:])
#                 #os.system(word_list[i][10:])
#
#                     # child(word_list[i][10:])
#         time.sleep(1)
#
#
# parent()

# base =datetime(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().hour,datetime.now().minute)
# iter = croniter(rec_time,base)
# while True:
#     m_time = iter.get_next(datetime)
#     print("NEXT ", m_time)
#     while True:
#         print(datetime(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().hour,datetime.now().minute,datetime.now().second))
#         if m_time == datetime(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().hour,datetime.now().minute):
#             os.system(command)
#             break
#         time.sleep(1)
# os.exit(0)