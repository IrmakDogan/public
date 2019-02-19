import os.path



body = open("task2.html", "w") 
body.write("<!DOCTYPE html>\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n\t<title>In this task, each image is provided with an object bounding box. Please write the expression number that you would be more likely to use to describe this object. Please write -1 for none of them and 0 for either one of them. </title>\n\t<link rel=\"stylesheet\" type=\"text/css\"\n</head>\n<body>\n\n\n<table width=\"85%\" border=\"0\" align=\"center\" cellpadding=\"0\" cellspacing=\"0\" style=\"margin-top: 30px;\">\n  <tbody><tr> \n    <td> \n\n\n\n<h1 align=\"center\" style=\"font-size: 24pt;\"><b>In this task, each image is provided with an object bounding box. Please write the expression number that you would be more likely to use to describe this object. Please write -1 for none of them and 0 for either one of them.</b></h1><br>\n\n")
exp = open("./task2/task_expression.txt", "r")
for i in range(31):
	body.write("<center><b> <font size=\"65\"> Image "+str(i+1) + ": </b></center>\n")
	expression1 = exp.readline()
	expression2 = exp.readline() 
	if os.path.isfile("./task2/tar"+str(i+1)+".png"):
		body.write("<center><img src=\"./task2/tar"+str(i+1)+".png\" style=\"width: 80%;\"> </center>\n")
	if os.path.isfile("./task2/tar"+str(i+1)+".jpg"):
		body.write("<center><img src=\"./task2/tar"+str(i+1)+".jpg\" style=\"width: 80%;\"></center>\n")
	body.write("<center><b> <font size=\"32\"> Expression 1: </b>"+ expression1[:-1] + "</center>\n&nbsp;\n")
	body.write("<center><b> <font size=\"32\"> Expression 2: </b>"+ expression2[:-1] + "</center>\n&nbsp;\n")
body.write("<center><b> <font size=\"32\"> End of the second task! Thank you for your participation, don't forget to ask for your movie ticket!</center>\n</td></tr></tbody></table></body></html>\n\n")	
