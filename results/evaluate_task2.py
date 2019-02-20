from __future__ import division
import os

res_path = 'task2/'
target = open("../task2/task_target.txt","r")
res_folders = []
selections = []

for filename in os.listdir(res_path):
	res_folders.append(open(res_path+filename,"r"))

#res_folders.append(open(res_path+os.listdir(res_path)[8],"r"))
#print res_folders
for i in range(31):
	mytarget = int(target.readline())
	for fol in res_folders:
		ans = int(fol.readline().split(':')[1])
		if mytarget == 1 and ans == 1:
			selections.append(1)
		elif mytarget == 1 and ans == 2:
			selections.append(2)
		elif mytarget == 2 and ans == 2:
			selections.append(1)
		elif mytarget == 2 and ans == 1:
			selections.append(2)
		elif ans == -1:
			selections.append(-1)
		elif ans == 0:
			selections.append(0)

print len(selections)

print 'our method:',(selections.count(1)/len(selections))
print 'baseline:',(selections.count(2)/len(selections))
print 'none of them:',(selections.count(-1)/len(selections))
print 'either of them:',(selections.count(0)/len(selections))
