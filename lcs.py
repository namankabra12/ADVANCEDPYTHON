MAX = 100
stack = []  # we'll use a plain list; end of list = top of stack

def return_book(book_id):
    if len(stack) == MAX:
        print("Stack overflow! Cannot return more books.")
        return
    stack.append(book_id)  # push
    print(f"Book {book_id} returned (pushed).")

def arrange_book():
    if len(stack) == 0:
        print("Stack is empty! No books to arrange.")
        return
    book_id = stack.pop()  # pop
    print(f"Book {book_id} arranged (popped).")

def top_book():
    if len(stack) == 0:
        print("Stack is empty!")
        return
    print(f"Top book is: {stack[-1]}")  # peek

def display_stack():
    if len(stack) == 0:
        print("Stack is empty!")
        return
    print("Stack (top -> bottom):", " ".join(str(x) for x in reversed(stack)))

def main():
    while True:
        print("\n--- Library Book Stack ---")
        print("1. Return Book (Push)")
        print("2. Arrange Book (Pop)")
        print("3. Top Book (Peek)")
        print("4. Display Stack")
        print("5. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            book_id = int(input("Enter Book ID: "))
            return_book(book_id)
        elif choice == 2:
            arrange_book()
        elif choice == 3:
            top_book()
        elif choice == 4:
            display_stack()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()