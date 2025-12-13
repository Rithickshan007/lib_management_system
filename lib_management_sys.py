import psycopg2

#-----------DB Connection
def dbconnection():
    return psycopg2.connect(
        host="localhost",
        database="library",
        user="postgres",
        password="Rithickshan"
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
        values(%s %s %s %s)
        """
        self.cursor.execute(query,(title,author,year,isbn))
        self.conn.commit
def menu():
    lib=Library()
    while(True):
        print("1.Add Books to library...")
        print("2.Exit")
        choice=int(input("Enter your Choice: "))
        if(choice==1):
            lib.addBooks()
        elif(choice==2):
            break

if __name__ == "__main__":
    menu()