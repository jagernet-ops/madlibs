import time 
import os
import sys
import re

directory = (os.path.dirname(os.path.realpath(__file__)))
f = open(f"{directory}/madlibsbanner.txt")
file_contents = f.read()
print(file_contents)
f.close()

time.sleep(2)
print()

while True:
    adjective_one = input("Name an adjective: ")
    if adjective_one != "":
        break

while True:
    adjective_two = input("Name another adjective: ")
    if adjective_two != "":
        break

while True:
    verb_one = input("Name a verb: ")
    if verb_one != "":
        break

while True:
    verb_two = input("Name yet another verb: ")
    if verb_two != "":
        break

while True:
    noun_one = input("Name a noun: ")
    if noun_one != "":
        break

while True:
    noun_two = input("Name another noun: ")
    if noun_two != "":
        break

while True:
    noun_three = input("Name another noun: ")
    if noun_three != "":
        break

while True:
    noun_four = input("Name another noun: ")
    if noun_four != "":
        break

while True:
    person_name = input("Write down a person's name: ")
    if person_name != "":
        break

while True:
    liquid_one = input("Name a liquid: ")
    if liquid_one != "":
        break

while True:
    verb_three = input("Name a verb ending in -ing: ")
    if verb_three != "":
        break

while True:
    part_of_the_body = input("Name a part of the body: ")
    if part_of_the_body != "":
        break

while True:
    noun_five = input("Name a plural noun: ")
    if noun_five != "":
        break

while True:
    verb_four = input("Name a verb ending in -ing: ")
    if verb_four != "":
        break

while True:
    noun_six = input("Name another noun: ")
    if noun_six != "":
        break

verb_three = verb_three.upper()
noun_six = noun_six.upper()
noun_one = noun_one.upper()
person_name = person_name.upper()
noun_two = noun_two.upper()
noun_three = noun_three.upper()
noun_four = noun_four.upper()
verb_one = verb_one.upper()
verb_two = verb_two.upper()
adjective_one = adjective_one.upper()
adjective_two = adjective_two.upper()
liquid_one = liquid_one.upper()
divider = '##################################################'

print(divider)
print()
madlib = (f"It was a {adjective_one}, cold November day. I woke up to the {adjective_two} smell of {noun_one} roasting in the {noun_two} downstairs. I {verb_one} down the stairs to see if I could help {verb_two} the {noun_one}. My mom said, 'See if {person_name} needs a fresh {noun_four}.' So I carried a tray of glasses full of {liquid_one} into the {verb_three} room. When I got there, I couldn't believe my {part_of_the_body}! There were {noun_five} {verb_four} on the {noun_six}")
n = 50
print('\n'.join(re.findall('.{1,%i}' % n, madlib)))
print()
print(divider)
print()

time.sleep(5)
reset = ""

while True:
    reset = input("Reset?(y/n): ")
    if reset == 'y':
        os.system('clear')
        os.system(f"python3 {directory}/main.py")
    elif reset == 'n':
        sys.exit()
