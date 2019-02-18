import os.path

body = open("task1_body", "w") 
exp = open("./task1/task_expression.txt", "r")
for i in range(108):
	body.write("<center><b> <font size=\"65\"> Figure "+str(i+1) + ": </b></center>\n")
	expression = exp.readline() 
	if os.path.isfile("./task1/image"+str(i+1)+".png"):
		body.write("<center><img src=\"./task1/image"+str(i+1)+".png\" style=\"width: 80%;\"> <img src=\"./task1/image_bounds"+str(i+1)+ ".png\" style=\"width: 80%;\"> </center>\n")
	if os.path.isfile("./task1/image"+str(i+1)+".jpg"):
		body.write("<center><img src=\"./task1/image"+str(i+1)+".jpg\" style=\"width: 80%;\"> <img src=\"./task1/image_bounds"+str(i+1)+ ".jpg\" style=\"width: 80%;\"> </center>\n")
	body.write("<center><b> <font size=\"32\"> Expression "+str(i+1)+": </b>"+ expression[:-1] + "</center>\n&nbsp;\n")
		
