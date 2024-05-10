# Project 1
# Ibrahim Bozkurt
# Database Systems
import sys
import book_dao

#dictionaries for menu options
menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
    1: 'All books',
    2: 'Title',
    3: 'ISBN',
    4: 'Publisher',
    5: 'Price Range',
    6: 'Year',
    7: 'Title and Publisher',
    8: 'Return to the previous menu',
}



# print methods
def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()

def print_search_menu():
    print()
    print("Please select what to search with")
    for key in search_menu_options.keys():
        print (str(key)+'.', search_menu_options[key], end = "  ")
    print()
    print("The end of search options")
    print()

def print_results(result):
    print()
    print("The following are the ISBN, title, year, publisher, previous edition ISBN, and price all books matching the search criteria.")
    for line in result:
        for p in line:
            print(p,end=" ")
        print()
    print('End of results.')





# option methods
def option1():
    print()
    print('1. Add a Publisher: Please enter the name, phone, and city of the publisher you want to add in (\'name\',\'phone\',\'city\') format.')
    print('For empty values write null without \'.')
    print('Enter 0 to return to the previous menu.\n')
    opIn = input('Input:')

    if opIn=='0':
        return
    else:
        response = book_dao.addPublisher(opIn)
        if response:
            print('Publisher successfully added.')

def option2():
    print()
    print('2. Add a Book: Please enter the ISBN, title, year, publisher, ISBN of the previous edition, and price of the book you want to add')
    print('in (\'ISBN\', \'title\', year, \'publisher\', \'previous edition ISBN\', price) format.')
    print('For empty values write null without any \'.')
    print('Enter 0 to return to the previous menu.\n')
    opIn = input('Input:')

    val=opIn.replace('(','').replace(')','').split(',')
    for i in range(0,len(val)):
        val[i] = val[i].lstrip()
        val[i] = val[i].rstrip()
    print(val[3])
    if opIn=='0'or len(val)<6:
        return
    if book_dao.checkISBN(val[0].replace('\'','')):
        print("Book exists.")
        return
    elif book_dao.checkISBN(val[4].replace('\'','').replace('\"','')) or val[4].upper().find('NULL') != -1:
        if book_dao.checkPublisher(val[3].replace('\'','')) : 
            response = book_dao.addBook(opIn)
            if response:
                print('Book successfully added.')
        else:
            print('Publisher doesn\'t exist.')
    else: 
        print('Previous edition ISBN doesn\'t exist.')


def option3():
    print()
    print('3. Edit a Book: Please enter the ISBN, title, year, publisher, ISBN of the previous edition, and price of the book you want to edit' )
    print('in (\'ISBN\', \'title\', year, \'publisher\', \'previous edition ISBN\', price) format.')
    print('Only the book with matching ISBN will be edited. To edit the ISBN of a book you can delete the book and add it again with correct ISBN.')
    print('For empty values write null without any \'.')
    print('Enter 0 to return to the previous menu.\n')
    
    opIn = input('Input:')
    val=opIn.replace('(','').replace(')','').split(',')
    for i in range(0,len(val)):
        val[i] = val[i].lstrip()
        val[i] = val[i].rstrip()
    if opIn=='0':
        return
    elif book_dao.checkISBN(val[0].replace('\'','')):
        response = book_dao.editBook(val)
        if response:
            print('The book is succesfully edited.')
    else: 
        print('The book you are trying to edit does not exist.')

def option4():
    print()
    print('4. Delete a Book: Please enter the ISBN of the book you want to delete.' )
    print('Enter 0 to return to the previous menu\n')
    opIn = input('ISBN:')
    
    if opIn.find('\'') != -1:
        opIn = opIn.replace('\'','')

    if opIn=='0':
        return
    elif book_dao.checkISBN(opIn):
        response = book_dao.deleteBook(opIn)
        if response:
            print('The book is succesfully deleted.')
    else :
        print("No book with that ISBN number exists.")

def option5():
    print()
    print_search_menu()

    try:
        sOption = int(input('Enter your choice: '))
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
    except:
        print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
    if sOption == 1:
        search_all_books()
    elif sOption == 2:
        search_by_title()
    elif sOption == 3:
        search_by_ISBN()
    elif sOption == 4:
        search_by_publisher()
    elif sOption == 5:
        search_by_price()
    elif sOption == 6:
        search_by_year()
    elif sOption == 7:
        search_by_title_and_publisher()
    elif sOption == 8:
        pass
    else:
        print('Invalid option. Please enter a number between 1 and 8.')    



# search methods

def search_all_books():
    print();
    results = book_dao.findAll()

    # Display results
    print("The following are the ISBNs and titles of all books.")
    for item in results:
        print(item[0], item[1])
    print("The end of books.")

def search_by_title():
    print()
    print('Please enter the title to search for, without any \' (if not in the title).')
    title = input('Title:')
    result = book_dao.findByTitle(title)
    print_results(result)

def search_by_ISBN():
    print()
    print('Please enter the ISBN to search for, without any \'.')
    ISBN = input('ISBN:')
    result = book_dao.findByISBN(ISBN)
    print_results(result)

def search_by_publisher():
    print()
    print('Please enter the publisher to search for, without any \'.')
    publisher = input('Publisher:')
    result = book_dao.findByPublisher(publisher)
    print_results(result)

def search_by_price():
    print()
    try:
        p1 =int(input('Please enter the minimum price:'))
        p2 =int(input('Please enter the maximum price:'))
    except:
        print("Please enter a number")
        return
    result = book_dao.findByPrice(p1,p2)
    print_results(result)

def search_by_year():
    print()
    print('Please enter the year to search for, without any \'.')
    year = input('Year:')
    result = book_dao.findByYear(year)
    print_results(result)

def search_by_title_and_publisher():
    print()
    print('Please enter the title and year to search for, without any \'.')
    title= input('Title:')
    publisher = input('Publisher:')
    result = book_dao.findByTP(title, publisher)
    print_results(result)

# main method
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            book_dao.closeConnection()
            print('Thanks your for using our database services! Bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')











