import psycopg2

#-----------DB Connection
def dbconnection():
    return psycopg2.connect(
        host="localhost",
        database="library",  #Give your Database Name
        user="postgres",
        password="Rithickshan" #Add Your Password Here(123456789)
    )
#------------Class For Books
class Books:
    def __init__(self,title,author,year,isbn):
        self.title=title
        self.author=author
        self.year=year
        self.isbn=isbn
#-------------Class For Library
class Library:
    def __init__(self):
        self.conn=dbconnection()
        self.cursor=self.conn.cursor()

    #-------------Adding Books to Library
    def addBooks(self):
        title=input("Enter the Book Name: ")
        author=input("Enter the Author Name: ")
        year=input("Enter the Published Year: ")
        isbn=input("Enter the ISBN Number: ")

        query="""INSERT INTO BOOKS(name,author,year,isbn)
        values(%s,%s,%s,%s)
        """
        self.cursor.execute(query,(title,author,year,isbn))
        self.conn.commit()
        print("Books Added Successfully")
#-------------Displaying the Books that is Added
    def displayBooks(self):
        query="""SELECT * FROM BOOKS"""
        self.cursor.execute(query)
        books=self.cursor.fetchall()
        if not books:
            print("No Books are Found....")
        for b in books:
            print(f"""
Title: {b[0]}
Author: {b[1]}
Year: {b[2]}
ISBN: {b[3]}""")

def menu():
    lib=Library()
    while(True):
        print("1.Add Books to library...")
        print("2.Display the Books Available...")
        print("3.Exit")
        choice=int(input("Enter your Choice: "))
        if(choice==1):
            lib.addBooks()
        elif(choice==2):
            lib.displayBooks()
        elif(choice==3):
            break

if __name__ == "__main__":
    menu()