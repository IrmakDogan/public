import random
from shutil import copyfile


our = open("our", "r")
baseline = open("baseline","r")

our_use_exp = []
baseline_use_exp = []
ind = [] 
for i in range(65):
	our_use_exp.append(our.readline())
	baseline_use_exp.append(baseline.readline())
	if baseline_use_exp[-1] != "\n" and baseline_use_exp[-1] != our_use_exp[-1]:
		ind.append(i)
		
		


num = 1
task_expression = open("task2/task_expression.txt","w")
task_target = open("task2/task_target.txt","w")
index = open("task2/task_index.txt","w")

random.shuffle(ind)

for item in ind:
	src = "targets/tar"
	dst = "task2/tar"
	if item < 32:
		src += str(int(item) + 1) + ".png"
		dst += str(num) + ".png"
	else:
		src += str(int(item) + 1) + ".jpg"
		dst += str(num) + ".jpg"
	currtar = random.randint(1,2)
	task_target.write(str(currtar)+'\n')
	if currtar == 1:
		task_expression.write(our_use_exp[item])
		index.write('our image'+str(item+1)+'\n')
		task_expression.write(baseline_use_exp[item])
		index.write('baseline image'+str(item+1)+'\n')
	if currtar == 2:
		task_expression.write(baseline_use_exp[item])
		index.write('baseline image'+str(item+1)+'\n')
		task_expression.write(our_use_exp[item])
		index.write('our image'+str(item+1)+'\n')
	copyfile(src, dst)
	num = num+1
