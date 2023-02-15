current_version = [int(x) for x in input().split('.')]

current_version[2] += 1

if current_version[2] > 9:
    current_version[2] = 0
    current_version[1] += 1

if current_version[1] > 9:
    current_version[1] = 0
    current_version[0] += 1

new_version = [str(ver) for ver in current_version]
print(".".join(new_version))
