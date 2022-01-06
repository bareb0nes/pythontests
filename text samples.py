print("Welcome to Fonts 3000")

#how to do multiple line breaks without writing down "print" every fucking time

print("Here's a line\nHere's another\nAnd here's a third one. Oh, it's beautiful")

#and here's a single line in multiple print

print("This is the first half", end=". ")
print("And this is the second half.")

#playing with colors

from colorama import Fore
from colorama import Style
print(f"This is {Fore.GREEN}green{Style.RESET_ALL}!")
print(f"This is {Fore.BLUE}blue{Style.RESET_ALL}!")
print(f"This is {Fore.RED}red{Style.RESET_ALL}!")

#timing lines

from time import sleep
sleep(3)
print("And now I see you shiver with antici...")
sleep(2)
print("pation.")
sleep(1)
print("Yeah that's all for now.")