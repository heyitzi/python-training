print("WELCOME TO MY TASK MANAGER")

to_do = []
done = []

while True:
    print("-----")
    print("-----")
    print("OPTIONS")
    print("-----")
    print("1. Add a new item")
    print("2. Remove one item")
    print("3. Mark item as Done")
    print("4. View my list")
    print("5. Leave program")
    print("-----")
    print("-----")
    option = int(input("Enter an option (1/2/3/4/5): "))

    if option == 1:
        new_item = input("Write your new task: ")
        to_do.append(new_item)
        print("-----")
        print("You have successfully added a new item!")
        print(to_do)
        print("-----")
    elif option == 2:
        print(to_do)
        remove_item = int(input("Write the index of the item you wish to remove (remember it starts in 0): "))
        to_do.pop(remove_item)
        print("-----")
        print("You have successfully removed an item.")
        print(to_do)
        print("-----")
    elif option == 3:
        print(to_do)
        done_item = int(input("Write the index of the item you have done (remember it starts in 0): "))
        done.append(to_do.pop(done_item))
        print("-----")
        print("Yay! Another task accomplished!!")
        print("-----")
        print("MY TO-DO LIST")
        print(to_do)
        print("DONE PILE")
        print(done)
        print("-----")
    elif option == 4:
        print("-----")
        print("MY TO-DO LIST")
        print(to_do)
        print("DONE PILE")
        print(done)
        print("-----")
    elif option == 5:
        break
    else:
        print("Sorry, enter a valid option")

# TODO fix: si no hay nada, no puedes eliminar. si le doy a enter no deberia salirse. intenta romperlo