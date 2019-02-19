import os.path

body = open("task1.html", "w") 
body.write("<!DOCTYPE html>\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n\t<title>In the first task, the images are provided with and without object bounding boxes. Please write the bounding box number of the described object in the scene. If the expression is ambiguous, please write -1.</title>\n\t<link rel=\"stylesheet\" type=\"text/css\"\n</head>\n<body>\n\n\n<table width=\"85%\" border=\"0\" align=\"center\" cellpadding=\"0\" cellspacing=\"0\" style=\"margin-top: 30px;\">\n  <tbody><tr> \n    <td> \n\n\n\n<h1 align=\"center\" style=\"font-size: 24pt;\"><b>In the first task, the images are provided with and without object bounding boxes. Please write the bounding box number of the described object in the scene. If the expression is ambiguous, please write -1.</b></h1><br>\n\n")
exp = open("./task1/task_expression.txt", "r")
for i in range(25):
	body.write("<center><b> <font size=\"65\"> Image "+str(i+1) + ": </b></center>\n")
	expression = exp.readline() 
	if os.path.isfile("./task1/image"+str(i+1)+".png"):
		body.write("<center><img src=\"./task1/image"+str(i+1)+".png\" style=\"width: 80%;\"> <img src=\"./task1/image_bounds"+str(i+1)+ ".png\" style=\"width: 80%;\"> </center>\n")
	if os.path.isfile("./task1/image"+str(i+1)+".jpg"):
		body.write("<center><img src=\"./task1/image"+str(i+1)+".jpg\" style=\"width: 80%;\"> <img src=\"./task1/image_bounds"+str(i+1)+ ".jpg\" style=\"width: 80%;\"> </center>\n")
	body.write("<center><b> <font size=\"32\"> Expression "+str(i+1)+": </b>"+ expression[:-1] + "</center>\n&nbsp;\n")
body.write("<center><a href=\"task1_2.html\">Next page</a><center>\n</td></tr></tbody></table></body></html>\n")


body1 = open("task1_2.html", "w")
body1.write("<!DOCTYPE html>\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n\t<title>Write the label number of the described target (-1 if expression is ambiguous)</title>\n\t<link rel=\"stylesheet\" type=\"text/css\"\n</head>\n<body>\n\n\n<table width=\"85%\" border=\"0\" align=\"center\" cellpadding=\"0\" cellspacing=\"0\" style=\"margin-top: 30px;\">\n  <tbody><tr> \n    <td> \n")
for i in range(25,50):
	body1.write("<center><b> <font size=\"65\"> Image "+str(i+1) + ": </b></center>\n")
	expression = exp.readline() 
	if os.path.isfile("./task1/image"+str(i+1)+".png"):
		body1.write("<center><img src=\"./task1/image"+str(i+1)+".png\" style=\"width: 80%;\"> <img src=\"./task1/image_bounds"+str(i+1)+ ".png\" style=\"width: 80%;\"> </center>\n")
	if os.path.isfile("./task1/image"+str(i+1)+".jpg"):
		body1.write("<center><img src=\"./task1/image"+str(i+1)+".jpg\" style=\"width: 80%;\"> <img src=\"./task1/image_bounds"+str(i+1)+ ".jpg\" style=\"width: 80%;\"> </center>\n")
	body1.write("<center><b> <font size=\"32\"> Expression "+str(i+1)+": </b>"+ expression[:-1] + "</center>\n&nbsp;\n")
body1.write("<center><a href=\"task1.html\">Previous page</a> &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <a href=\"task1_3.html\">Next page</a><center>\n</td></tr></tbody></table></body></html>\n")
	
body2 = open("task1_3.html", "w")
body2.write("<!DOCTYPE html>\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n\t<title>Write the label number of the described target (-1 if expression is ambiguous)</title>\n\t<link rel=\"stylesheet\" type=\"text/css\"\n</head>\n<body>\n\n\n<table width=\"85%\" border=\"0\" align=\"center\" cellpadding=\"0\" cellspacing=\"0\" style=\"margin-top: 30px;\">\n  <tbody><tr> \n    <td> \n") 
for i in range(50,75):
	body2.write("<center><b> <font size=\"65\"> Image "+str(i+1) + ": </b></center>\n")
	expression = exp.readline() 
	if os.path.isfile("./task1/image"+str(i+1)+".png"):
		body2.write("<center><img src=\"./task1/image"+str(i+1)+".png\" style=\"width: 80%;\"> <img src=\"./task1/image_bounds"+str(i+1)+ ".png\" style=\"width: 80%;\"> </center>\n")
	if os.path.isfile("./task1/image"+str(i+1)+".jpg"):
		body2.write("<center><img src=\"./task1/image"+str(i+1)+".jpg\" style=\"width: 80%;\"> <img src=\"./task1/image_bounds"+str(i+1)+ ".jpg\" style=\"width: 80%;\"> </center>\n")
	body2.write("<center><b> <font size=\"32\"> Expression "+str(i+1)+": </b>"+ expression[:-1] + "</center>\n&nbsp;\n")
body2.write("<center><a href=\"task1_2.html\">Previous page</a> &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <a href=\"task1_4.html\">Next page</a><center>\n</td></tr></tbody></table></body></html>\n")	
	
body3 = open("task1_4.html", "w")
body3.write("<!DOCTYPE html>\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n\t<title>Write the label number of the described target (-1 if expression is ambiguous)</title>\n\t<link rel=\"stylesheet\" type=\"text/css\"\n</head>\n<body>\n\n\n<table width=\"85%\" border=\"0\" align=\"center\" cellpadding=\"0\" cellspacing=\"0\" style=\"margin-top: 30px;\">\n  <tbody><tr> \n    <td> \n\n")  
for i in range(75,108):
	body3.write("<center><b> <font size=\"65\"> Image "+str(i+1) + ": </b></center>\n")
	expression = exp.readline() 
	if os.path.isfile("./task1/image"+str(i+1)+".png"):
		body3.write("<center><img src=\"./task1/image"+str(i+1)+".png\" style=\"width: 80%;\"> <img src=\"./task1/image_bounds"+str(i+1)+ ".png\" style=\"width: 80%;\"> </center>\n")
	if os.path.isfile("./task1/image"+str(i+1)+".jpg"):
		body3.write("<center><img src=\"./task1/image"+str(i+1)+".jpg\" style=\"width: 80%;\"> <img src=\"./task1/image_bounds"+str(i+1)+ ".jpg\" style=\"width: 80%;\"> </center>\n")
	body3.write("<center><b> <font size=\"32\"> Expression "+str(i+1)+": </b>"+ expression[:-1] + "</center>\n&nbsp;\n")
body3.write("\n<center><a href=\"task1_3.html\">Previous page</a><center>\n<center><b> <font size=\"32\"> End of the first task! Please contact us for the second task which is much more shorter than this one. Thank you for your participation, don't forget to ask for your movie ticket after the second task! </center>\n</td></tr></tbody></table></body></html>\n\n")	
