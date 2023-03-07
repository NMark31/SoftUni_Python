electrons = int(input())
shell = []
layer = 1

while electrons:
    if electrons < 2 * (layer ** 2):
        e = electrons
    else:
        e = 2 * (layer ** 2)

    shell.append(e)
    electrons -= e
    layer += 1

print(shell)
