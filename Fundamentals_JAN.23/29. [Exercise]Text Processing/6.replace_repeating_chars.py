from itertools import groupby

line = list(input())

removed_duplicates = [char[0] for char in groupby(line)]
print(*removed_duplicates, sep="")