# Project 1
# Ibrahim Bozkurt
# Database Systems
from mysql_connector import connection 

# finding methods
def findAll():
    cursor = connection.cursor()
    query = "select * from bookmanager.Book;"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        results= None
    return results
    
def findByTitle(title):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title like '%" + title + "%'"
    try:
        cursor.execute(query)    
        results = cursor.fetchall()
    except Exception as e:
        results= None
    return results
    
def findByISBN(ISBN):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where ISBN = '" + ISBN+"'"
    try:
        cursor.execute(query)    
        results = cursor.fetchall()
    except Exception as e:
        results= None
    return results
    
def findByPublisher(publisher):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where published_by like '%" + publisher +"%'"
    try:
        cursor.execute(query)    
        results = cursor.fetchall()
    except Exception as e:
        results= None
    return results
    
def findByYear(year):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where year = " + year 
    try:
        cursor.execute(query)    
        results = cursor.fetchall()
    except Exception as e:
        results= None
    return results
    
def findByPrice(p1, p2):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where price >= " + str(p1) +" and price <= " + str(p2)
    try:
        cursor.execute(query)    
        results = cursor.fetchall()
    except Exception as e:
        results= None
    return results

def findByTP(title, publisher):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title like '%" + title + "%' and published_by like '%" + publisher +"%';"
    try:
        cursor.execute(query)    
        results = cursor.fetchall()
    except Exception as e:
        results= None
    return results


# main-functionality methods
def deleteBook(ISBN):
    flag = True
    cursor = connection.cursor()
    query = "delete from bookmanager.Book where ISBN='" + ISBN+ "' "
    try:
        cursor.execute(query)
        cursor.execute("commit")
    except Exception as e:
        print('Couldn\'t delete the book')
        print(e)
        flag = False
    return flag

def addBook(values):
    flag = True
    cursor = connection.cursor()
    query = "insert into bookmanager.Book values " + values 
    try:
        cursor.execute(query)
        cursor.execute('commit')
    except Exception as e:
        print('Error: Invalid Input')
        print('To understand why refer to the text document.')
        print(e)
        flag = False
    return flag
    
def editBook(val):
    flag = True
    cursor = connection.cursor()
    query = "update bookmanager.Book set title = "+val [1] +", year =" +val[2]+ ", published_by =" +val[3]+", previous_edition = "+val[4]+ ",price = "+ val[5] + " where ISBN = " + val[0] + ""
    try:
        cursor.execute(query)
        cursor.execute('commit')

    except Exception as e:
        print('Error: Invalid Input')
        print('To understand why refer to the text document.')
        print(e)
        flag = False
    return flag
    
def addPublisher(values):
    flag = True
    cursor = connection.cursor()
    query = "insert into bookmanager.Publisher values " + values + ""
    try:
        cursor.execute(query)
        cursor.execute("commit")
    except Exception as e:
        print('Error: Invalid Input')
        print('To understand why refer to the text document.')
        print(e)
        flag = False
    return flag

#checking method to not get an error
def checkISBN(ISBN):
    flag = True
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where ISBN = '"  + ISBN +"'"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        flag = False

    if flag == True and results != []:
        return True
    else:
        return False

def checkPublisher(publisher):
    flag = True
    cursor = connection.cursor()
    query = "select * from bookmanager.Publisher where name = '"  + publisher +"'"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        flag = False

    if flag == True and results != []:
        return True
    else:
        return False

# to close the connection when exitting
def closeConnection():
    connection.close()