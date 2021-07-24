user_input=" "
while True:
    user_input=input(' Enter 1 to get covid satistics \n Enter 2 to know vaccine information\n Enter 3 to exit\n')
    print("----------------------------------------------------")
    if user_input=="1":
        import statistics
        print(statistics)
    elif user_input=="2":
        import vaccine
        print(vaccine)
    elif user_input=="3":
        break
    else:
       print("-------------------Please enter the correct input---------------------------")
