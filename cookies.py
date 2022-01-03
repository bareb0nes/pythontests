answer = 0
cookies = 0

def scene():
    print("Have a sample cookie. Do you want another?")
    global answer
    global cookies
    cookies += 1
    answer = input()
    consequence()
    
def option1():
    print("Here, have one more cookie.")
    global cookies
    cookies += 1
    print(f"You now have {cookies} cookies")
    scene()

def option2():
    print("Your loss.")
    print(f"You now have {cookies} cookies")
    scene()

def freedom():
    print("You're free now.")
    
def consequence():
    if answer == "yes":
        option1()
    elif answer == "stop":
        freedom()
    else:
        option2()

scene()



