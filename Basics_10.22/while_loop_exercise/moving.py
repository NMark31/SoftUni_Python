a = int(input())
b = int(input())
c = int(input())

total_free_space = a * b * c
boxes_count = 0

while boxes_count < total_free_space:
    boxes_moved = input()

    if boxes_moved == 'Done':
        print(f'{total_free_space - boxes_count} Cubic meters left.')
        break

    boxes_count += int(boxes_moved)

else:
    print(f'No more free space! You need {boxes_count - total_free_space} Cubic meters more.')