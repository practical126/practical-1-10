queue = []

while True:
    print("\n1.Enqueue")
    print("\2.Dequeue")
    print("\3.Display")
    print("\4.Exit")

    choice = int(input("Enter your choice:"))

if choice == 1:
    element = input("Enter element:")
    queue.append(element)
    print("Element inserted:")

elif choice == 2:
    if not queue:
        print("Queue is Empty:")
    else:
        print("Deleted element:",queue.pop(0))

elif choice == 3:
    if not queue:
        print("Queue is empty")
    else:
        print("Queue",queue)
        print("Front Element:",queue[0])
        print("Rear Element:",queue[-1])

elif choice == 4:
    print("Program Ended")
    break
else:
    print("Invalid Choice")
    
