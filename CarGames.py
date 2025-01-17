command = ""
is_car_Start = False
while True:
    command = input("> ").lower()
    if command == "start":
        if is_car_Start:
            print("Car already started...")
        else:
            is_car_Start = True
            print("Car Started...")
    elif command == "stop":
        if not is_car_Start:

            print("Car already stopped...")
        else:
            is_car_Start = False
            print("Car Stopped...")
    elif command == "help":
        print('''
start - to start the car
stop  - to stop the car
quit  - to quit
        ''')
    elif command == "quit":
        break
    else:
        print("Sorry! We don't understand this command")
