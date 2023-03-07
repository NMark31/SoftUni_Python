k, l, m, n = int(input()), int(input()), int(input()), int(input())
substitude_count = 0

for f_f in range(k, 9):
    if f_f % 2 != 0:
        continue
    for f_s in range(9, l-1, -1):
        if f_s % 2 == 0:
            continue
        for s_f in range(m, 9):
            if s_f % 2 != 0:
                continue
            for s_s in range(9, n-1, -1):
                if s_s % 2 == 0:
                    continue

                if str(f_f) + str(f_s) == str(s_f) + str(s_s):
                    print('Cannot change the same player.')
                    
                else:
                    print(f'{f_f}{f_s} - {s_f}{s_s}')
                    substitude_count += 1

                    if substitude_count == 6:
                        exit()
                        