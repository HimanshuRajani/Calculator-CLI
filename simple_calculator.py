print("Welcome to the python simple calculator which data storing feature")

while(True):
    num_1, num_2, opt = int(input("Enter the first numbers: ")),int(input("Enter the second numbers: ")), input("Enter your choice add, sub, mul, div:- ").strip().lower()

    if(opt == "add"):
        print(f"{num_1} + {num_2} = {num_1+num_2}")
        
    elif(opt == "sub"): 
        print(f"{num_1} - {num_2} = {num_1-num_2}")
        
    elif(opt == "mul"):
        print(f"{num_1} * {num_2} = {num_1*num_2}")
        
    elif(opt == "div"):
        print(f"{num_1} / {num_2} = {num_1/num_2}")
        
    else:
        print("Please Enter valid input!!!")
        continue

    repeat = input("Do you want to continue {1 for yes and 0 for no}: ")

    if repeat == "0" or repeat != "1":
        break