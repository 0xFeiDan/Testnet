#!/usr/bin/python
import requests
import json
import time
import os

def run_damominer(address):
	os.system('./damominer.sh '+ address)
	print('address -> ' + address + ' is running')

def check_solution(address):
	solution = 0
	while solution == 0:
		response = requests.get("https://client.damominer.hk/api/v1/miner/{}/rewards".format(address))
		rewards = json.loads(response.content)["result"]["total_reward"]
		time.sleep(1)
		print(rewards)
		if rewards == str(0) or rewards == "":
			solution = 0
			print('address -> ' + address + ' check in 5 minutes after')
			time.sleep(300)
		else:
			solution = 1
			print('address -> ' + address + ' is ok')

if __name__ == '__main__':
	f = open("address.txt","r")
	lines = f.readlines()
	for value in lines:
		address = value.strip()
		run_damominer(address)
		check_solution(address)

