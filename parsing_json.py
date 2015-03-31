#!/usr/bin/env python3
import sys
import json 

data_list = json.load(open('Job.json', 'r'))

def main():
	for data in data_list:

		key_lst = []
		v_lst = []
		
		for k,v in data.items():
			#print k
			key_lst.append(k)
			#print v
			v_lst.append(v)

		sql = "INSERT INTO Job ("

		
		for i in range(len(key_lst)):
			if i == len(key_lst)-1:
				sql = sql + str(key_lst[i]) + " )" 
			else:
				sql = sql + str(key_lst[i]) + " ,"

		sql = sql + " VALUES ("
		for i in range(len(v_lst)):
			if i == len(v_lst)-1:
				sql = sql + str(v_lst[i]) + " )" 
			else:
				print v_lst[i]
				sql = sql + str(v_lst[i]) + " , "
		print sql

main()
