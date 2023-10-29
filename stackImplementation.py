stack  = []

def push():
    e = input("Enter the element :")
    stack.append(e)
    print("stack is :",stack)

def pop():
    if len(stack) == 0:
        print("stack is empty")
    else:
       stack.pop()
       print(stack)


while True:
    print("Enter the operation 1 for push and 2 for pop 3 for quit")
    choice = int(input())
    if choice == 1:
        print("call the push")
        push()
    elif choice == 2:
        print("call the pop")
        pop()
    elif choice == 3:
        print("End of the program")
        break