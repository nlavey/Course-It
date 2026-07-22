from data import courses

cs101 = courses[0]
math201 = courses[1]

section1 = cs101.sections[0]
section2 = math201.sections[0]
section3 = math201.sections[1]

print(section1)
print(section2)
print(section3)

print()

print("Conflict?")
print(section1.conflicts_with(section3))