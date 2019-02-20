import random
from shutil import copyfile

our = open("our", "r")
baseline = open("baseline","r")
targets = open("targets.txt","r")

count = 0
count2 = 0
count3 = 0
our_use_exp = []
baseline_use_exp = []
ind = [] 
tar = []

for i in range(65):
	our_use_exp.append(our.readline())
	baseline_use_exp.append(baseline.readline())
	tar.append(int(targets.readline()))
	if baseline_use_exp[-1] != "\n" and baseline_use_exp[-1] != our_use_exp[-1]:
		ind.append([i,1])
		ind.append([i,2])
	if baseline_use_exp[-1] == our_use_exp[-1]:
		ind.append([i,3])
	if baseline_use_exp[-1] == "\n":
		ind.append([i,4])

for i in range(1, len(ind)):
	if ind[i][0] == ind[i-1][0]:
		random.shuffle(ind)
		i = 1



print len(our_use_exp)
print len(baseline_use_exp)
print len(ind)

num = 1
task_expression = open("task1/task_expression.txt","w")
task_target = open("task1/task_target.txt","w")
index = open("task1/task_index.txt","w")

for i in ind:
	item = i[0]
	src = "target_bounds/image_bounds"
	src1 = "images/image"
	dst = "task1/image_bounds"
	dst1 = "task1/image"
	if item < 32:
		src += str(int(item) + 1) + ".png"
		src1 += str(int(item) + 1) + ".png"
		dst += str(num) + ".png"
		dst1 += str(num) + ".png"
	else:
		src += str(int(item) + 1) + ".jpg"
		src1 += str(int(item) + 1) + ".jpg"
		dst += str(num) + ".jpg"
		dst1 += str(num) + ".jpg"
	if i[1] == 1:
		task_expression.write(our_use_exp[item])
		index.write('our image'+str(item+1)+'\n')
	if i[1] == 2:
		task_expression.write(baseline_use_exp[item])
		index.write('baseline image'+str(item+1)+'\n')
	if i[1] == 3:
		task_expression.write(our_use_exp[item])
		index.write('common image'+str(item+1)+'\n')
	if i[1] == 4:
		task_expression.write(our_use_exp[item])
		index.write('special image'+str(item+1)+'\n')
	task_target.write(str(tar[item])+'\n')
	copyfile(src, dst)
	copyfile(src1,dst1)
	num = num+1
