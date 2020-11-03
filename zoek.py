import psycopg2, time

conn = psycopg2.connect(
	host="localhost",
	database="Project C",
	user="postgres",
	password="OK0Shirroh"
	)

cur = conn.cursor()

def createQuery(title, categoryList, orderBy):

	#Adds order by
	orderStr=""
	if orderBy != "":
		orderStr = "ORDER BY {orderBy}"

	#Adds title to query	
	titleStr=""
	if title != "":
		titleStr='"Plant"."Name" LIKE \'%' + title + '%\''
		print(titleStr)

	#Adds category tuple values to string
	catStr = ""
	if len(categoryList) > 0:
		i = 0
		if titleStr != "":
			catStr += " AND "
		for cat in categoryList:
			strList += 'Plant."' + cat[0] + '" LIKE \'' + cat[1] + '\''
			if i != 0 and i != len(categoryList-1):
				strList += " AND "
			i += 1

	queryStr = "SELECT \"Name\", \"Description\", \"PlantSize\", \"Timestamp\" FROM \"Project C\".\"Plant\" "

	if titleStr or catStr != "":
		queryStr+= "WHERE " + titleStr + catStr	 

	#add ASC or DESC options
	if orderBy != "":
		queryStr += " ORDER BY {orderBy}"

	return queryStr

def queryMenu():
	f = lambda x : input("[No input to continue] Please enter " + x + ": ")
	title = f("title")
	orderBy = f("ORDER BY")
	categoryList = []
	if input("Add category filter? Y|N:  ") == "Y":	
		while True:
			cat = f("category")
			catType = f("{cat} type")
			categoryList.append((cat,catType))
			if input("Add another category? Y|N  ") != "Y":
				break
	return createQuery(title, categoryList, orderBy)

print("Welcome\n\n")
time.sleep(1)
while True:
	menu = input("\n1. Perform search.\n2. Exit\n\nYour option: ")
	if int(menu) == 1:
		cur.execute(queryMenu())
		print(cur.fetchone())
	else:
		exit()