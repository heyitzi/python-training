def turntables(arg):
    if arg == str:
        arg = int(arg)
        return arg
    elif arg == int:
        arg = str(arg)
        return arg
    else:
        return "You have entered the wrong type"
    

print(turntables(5))
# turntables("7")
# turntables([2, 5])

# NEEDS FIXING - DOES NOT WORK