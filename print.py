#!/usr/bin/python3
import datetime
def main():
	with open ('file.txt','wt',encoding = 'utf-8') as inFile:
		inFile.write(str(datetime.datetime.now().time()))




if __name__ == '__main__':
	main()


