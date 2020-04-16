#!/usr/bin/python3

import re
import os
import sys
import subprocess
import time
import multiprocessing
import platform

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

projectname = 'justname'

class checkFinished:
    def __init__(self, name, ls=0, pwd=0, id=0):
        self.name = name
        self.ls = 0
        self.pwd = 0
        self.id = 0

with open('list.txt', 'r') as f:
	urlList = f.readlines()

def findDomain(urlList):
	global domainList
	domainList = []
	for url in urlList:
		domainTemp = url.split("//")[-1].split("/")[0]
		domainTemp = domainTemp.replace("\n","")
		domainList.append(domainTemp)

def decideOS():
	global pwd
	global OStype
	tag = 0
	while tag == 0:
		OStype = input("Choose your OS, Windows or Linux?(w/l)")
		if OStype == 'w' or OStype == 'W':
			pwd = os.popen('cd').readlines()[0].replace("\n", "")
			tag = 1
		elif OStype == 'l' or OStype == 'L':
			pwd = os.popen('pwd').readlines()[0].replace("\n", "")
			tag = 1
		else:
			print('Please input w or l')
			pass

def createFolder(domainList):
	try:
		os.mkdir('./'+projectname)
	except:
		pass

	for name in domainList:
		nameReplace = name.replace(':','_')
		try:
			os.mkdir('./'+projectname+'/'+nameReplace)
		except:
			pass

def changePath(target):
	targetReplace = target.replace(':','_')
	if OStype == 'w' or OStype == 'W':
		os.chdir(pwd+'\\'+projectname+'\\'+targetReplace)
	elif OStype == 'l' or OStype == 'L':
		os.chdir(pwd+'/'+projectname+'/'+targetReplace)	

def cmdId(target):
		try:
			os.system('id >> id.txt')
		except:
			os.system('echo "id Failed" >> ./Errorlog.txt')

def cmdPwd(target):
		try:
			os.system('pwd >> pwd.txt')
		except:
			os.system('echo "pwd Failed" >> ./Errorlog.txt')

def cmdLs(target):
		try:
			os.system('ls >> ls.txt')
		except:
			os.system('echo "ls Failed" >> ./Errorlog.txt')

decideOS()
findDomain(urlList)
createFolder(domainList)

tagDict = {}

if os.path.isfile('./'+projectname+'Tag'):
	print("file existed")
else:
	for domain in domainList:
		className = domain+'Tag'
		tagDict[domain] = className
		print(className)
		className = checkFinished(domain)
		print(className.name)
		print(className.ls)

# for domain in domainList:
# 	name = tagDict.get(domain)
# 	print(type(name))
# 	print(name)
# 	print(name.ls)
# 	print(name.id)

for domain in domainList:
	changePath(domain)
	cmdId(domain)
	cmdLs(domain)
	cmdPwd(domain)
