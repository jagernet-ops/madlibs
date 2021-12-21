from time import sleep
from os import system, path
from sys import exit
from re import findall

directory = (path.dirname(path.realpath(__file__)))
f = open(f"{directory}/madlibsbanner.txt")
file_contents = f.read()
print(file_contents)
f.close()
sleep(2)

divider = '##################################################\n'
questions = ["Name an adjective: ", "Name another adjective: ",
             "Name a noun: ", "Name another noun: ",
             "Name a verb: ", "Name another verb: ",
             "Write down a person's name: ", "Name another noun: ",
             "Name a liquid: ", "Name a verb ending in -ing: ",
             "Name a part of the body: ", "Name a plural noun: ",
             "Name a verb ending in -ing: ", "Name another noun: "
             ]

responses = []

for q in questions:
    response = input(q)
    responses.append(response)

print(divider)

madlib = (f"It was a {responses[0]}, cold November day. I woke up to the "
          f"{responses[1]} smell of {responses[2]} roasting in the {responses[3]} "
          f"downstairs. I {responses[4]} down the stairs to see if I could help "
          f"{responses[5]} the {responses[2]}. My mom said, 'See if {responses[6]} "
          f"needs a fresh {responses[7]}.' So I carried a tray of glasses full of "
          f"{responses[8]} into the {responses[9]} room. When I got there, I "
          f"couldn't believe my {responses[10]}! There were {responses[11]} "
          f"{responses[12]} on the {responses[13]} ")

print('\n'.join(findall('.{1,%i}' % 50, madlib)) + "\n")
print(divider)
sleep(5)
reset = ""

while True:
    reset = input("Reset?(y/n): ")
    if reset.upper() == 'Y':
        system('clear')
        system(f"python3 {directory}/main.py")
    elif reset.upper() == 'N':
        exit()
