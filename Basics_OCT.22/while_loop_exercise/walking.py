GOAL = 10000
total_steps = 0

while True:
    steps = input()

    if steps == 'Going home':
        steps_to_home = int(input())
        total_steps += steps_to_home

        if total_steps >= GOAL:
            print(f'Goal reached! Good job!\n{total_steps - GOAL} steps over the goal!')
        else:
            print(f'{abs(total_steps - GOAL)} more steps to reach goal.')

        break

    total_steps += int(steps)

    if total_steps >= GOAL:
        print(f'Goal reached! Good job!\n{total_steps - GOAL} steps over the goal!')
        break
