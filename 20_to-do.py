print("WELCOME TO MY TASK MANAGER")

to_do = []
done = []

while True:
    try:
        print("-----")
        print("OPTIONS")
        print("-----")
        print("1. Add a new item")
        print("2. Remove one item")
        print("3. Mark item as Done")
        print("4. View my list")
        print("5. Leave program")
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
            if len(to_do) == 0:
                print("-----")
                print("There is nothing to delete, your list empty. Please choose another option")
            else:
                print(to_do)
                remove_item = int(input("Write the index of the item you wish to remove (remember it starts in 0): "))
                if remove_item in to_do:
                    to_do.pop(remove_item)
                    print("-----")
                    print("You have successfully removed an item.")
                    print(to_do)
                    print("-----")
                else:
                    print("-----")
                    print("The index you have selected doesn't exist, please choose another one.")
                    print(to_do)
                    print("-----")
        elif option == 3:
            if len(to_do) == 0:
                print("-----")
                print("Nothing new to achieve here, all your tasks are done! Please choose a different option")
            else:
                print(to_do)
                done_item = int(input("Write the index of the item you have done (remember it starts in 0): "))
                if done_item in done:
                    done.append(to_do.pop(done_item))
                    print("-----")
                    print("Yay! Another task accomplished!!")
                    print("-----")
                    print("MY TO-DO LIST")
                    print(to_do)
                    print("DONE PILE")
                    print(done)
                    print("-----")
                else:
                    print("-----")
                    print("The index you have selected doesn't exist, please choose another one.")
                    print(to_do)
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
    
    except ValueError:
        print("Please enter a valid option(1/2/3/4/5)")