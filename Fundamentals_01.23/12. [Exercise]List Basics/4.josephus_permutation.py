soldiers = [int(i) for i in input().split()]
person_to_kill = int(input()) - 1

executed_ppl = []

while soldiers:
    for element in range(len(soldiers)):
        if len(soldiers) < person_to_kill:
            person_to_kill -= len(soldiers)

        if element % person_to_kill == 0:
            executed_ppl.append(soldiers[person_to_kill])
            soldiers.pop(person_to_kill)


print(executed_ppl)
