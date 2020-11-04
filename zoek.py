import psycopg2, time

conn = psycopg2.connect(
	host="localhost",
	database="Project C",
	user="postgres",
	password="OK0Shirroh"
	)

cur = conn.cursor()

def categoryMenu():
	categoryMenu = {
	"PlantSize": ["Little", "Medium", "Large"],
	"Shadow": ["Little", "Medium", "Large"],
	"Type": ["Flower", "Tree"],
	"YoungOrOld": ["Old", "Young", "Medium"],
	"Season": ["all-year", "Winter", "Spring"],
	"Edible": ["true", "false"],
	"AmountOfWater": ["Large", "Small"],
	"Color": ["Green", "Red", "Orange", "Blue", "Pink"]
	}


	i = 0	
	for key, val in categoryMenu.items():
		i+=1
		print(str(i) + ". " + key)
	menuInput = input("What option?\n\n")

	j = 0
	for key, val in categoryMenu.items():
		j += 1
		if j == int(menuInput):
			i = 0
			for cat in categoryMenu[key]:
				print(str(i) + ". " + cat)
				i +=1 
			menuInput = input("What option?\n\n")
			return (key, categoryMenu[key][int(menuInput)])


def createQuery(title, categoryList, orderBy):
	#Adds order by
	orderStr=""
	if orderBy != "":
		orderStr = "ORDER BY {orderBy}"

	#Adds title to query	
	titleStr=""
	if title != "":
		titleStr='"Plant"."Name" LIKE \'%' + title + '%\''


	#Adds category tuple values to string
	catStr = ""
	if len(categoryList) > 0:
		i = 0
		if titleStr != "":
			catStr += " AND "
		for cat in categoryList:
			catStr += '"Plant"."' + cat[0] + '" LIKE \'' + cat[1] + '\''
			if i != 0 and i != len(categoryList-1):
				catStr += " AND "
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
			categoryList.append(categoryMenu())
			if input("Add another category? Y|N  ") != "Y":
				break
	return createQuery(title, categoryList, orderBy)

print("Welcome\n\n")
time.sleep(1)
while True:
	menu = input("\n1. Perform search.\n2. Exit\n\nYour option: ")
	if int(menu) == 1:
		cur.execute(queryMenu())
		resultList = cur.fetchall()
		print("----Search Results:   ")
		if len(resultList) == 0:
			print("No results.")
		for result in resultList:
			print(result[0])
	else:
		exit()