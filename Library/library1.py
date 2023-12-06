class Library:
    def __init__(self,name,list,lendict):
        self.name = name
        self.list = list
        self.dict = lendict

    def displaybook(self):
        print("The available books are:")
        for book in self.list:
            print(book)
        return "\t\t\tChoose the book"

    def lendbook(self,book,user):
        if book not in self.list:
            if self.dict.get(book) == None:
                return "\t\t\t"+book.upper() +" book is not available in library"
            else:
                print("\t\t\tSorry! "+book.upper()+" book is not available now!!")
                print("\t\t\t"+book.upper()+" book is with "+self.dict.get(book).upper())
                return " "
        else:
            self.list.remove(book)
            self.dict.update({book:user})
            return "\t\t\tReturn the book in time"
    
    def returnbook(self,book,user):
        if user == self.dict.get(book):
            self.list.append(book)
            return "\t\t\tThank you!"
        else:
            return "\t\t\tYou have not taken this book!!!"
        

    def addbook(self,book):
        self.list.append(book)
        print("Your book is added to library")
        return "\t\t\tThank you!"
    
if __name__ == '__main__':
    l1 = Library("Biraj Library",["physics", "chemistry" ,"maths", "social", "rich dad poor dad", "the Alchemist"
    ,"the Power of Now" ,"sapiens" ,"the Miracle Morning", "start With Why"],{})

    while True:
        print("\n\n\n\n\t\t---------------------WELCOME TO",l1.name.upper()+"-----------------------")
        print("1. Display Book")
        print("2. Lend Book")
        print("3. Return Book")
        print("4. Add/Donate Book\n\n")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            print("Here are the available books:\n")
            print(l1.displaybook())
            
        elif user_choice == "2":
            book = input("Enter the name book: ").lower()
            user = input("Enter your name: ").lower()
            print(l1.lendbook(book,user))

        elif user_choice == "3":
            book = input("Enter the name book: ").lower()
            user = input("Enter your name: ").lower()
            print(l1.returnbook(book,user))

        elif user_choice == "4":
            book = input("Enter the name of book: ")
            print(l1.addbook(book))

        else:
            print("\t\t\tInvalid Input!!!")