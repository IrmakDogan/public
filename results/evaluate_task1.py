from __future__ import division
import os

res_path = 'task1/'
target = open("../task1/task_target.txt","r")
index = open("../task1/task_index.txt","r")
special = []
our = []
baseline = []
common = []
res_folders = []

for filename in os.listdir(res_path):
	res_folders.append(open(res_path+filename,"r"))

#res_folders.append(open(res_path+os.listdir(res_path)[16],"r"))
#print res_folders

for i in range(96):
	case = index.readline()
	mytarget = int(target.readline())
	if 'our' in case:
		for fol in res_folders:
			print fol
			ans = int(fol.readline().split(':')[1])
			if ans == mytarget:
				our.append(1)
			elif ans == -1:
				our.append(-1)
			elif ans != mytarget:
				our.append(0)
	elif 'baseline' in case:
		for fol in res_folders:
			print fol
			ans = int(fol.readline().split(':')[1])
			if ans == mytarget:
				baseline.append(1)
			elif ans == -1:
				baseline.append(-1)
			elif ans != mytarget:
				baseline.append(0)
	elif 'common' in case:	
		for fol in res_folders:
			print fol
			ans = int(fol.readline().split(':')[1])
			if ans == mytarget:
				common.append(1)
			elif ans == -1:
				common.append(-1)
			elif ans != mytarget:
				common.append(0)
	elif 'special' in case:
		for fol in res_folders:
			print fol
			ans = int(fol.readline().split(':')[1])
			if ans == mytarget:
				special.append(1)
			elif ans == -1:
				special.append(-1)
			elif ans != mytarget:
				special.append(0)
print len(our)
print len(baseline)
print len(common)
print len(special)

print 'our correct:',(our.count(1)/len(our))
print 'our false:',(our.count(0)/len(our))
print 'our amb:',(our.count(-1)/len(our))

print 'baseline correct:',(baseline.count(1)/len(baseline))
print 'baseline false:',(baseline.count(0)/len(baseline))
print 'baseline amb:',(baseline.count(-1)/len(baseline))

print 'common correct:',(common.count(1)/len(common))
print 'common false:',(common.count(0)/len(common))
print 'common amb:',(common.count(-1)/len(common))

print 'special correct:',(special.count(1)/len(special))
print 'special false:',(special.count(0)/len(special))
print 'special amb:',(special.count(-1)/len(special))
