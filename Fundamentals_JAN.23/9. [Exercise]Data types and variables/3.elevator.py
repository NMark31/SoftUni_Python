persons = int(input())
max_load = int(input())


if persons % max_load == 0:

    courses = int(persons / max_load)

else:
    courses = (persons // max_load) + 1

print(courses)
