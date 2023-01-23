sun_of_a_beach = input()
to_lower = sun_of_a_beach.lower()

count = to_lower.count("water") + to_lower.count("sand") + to_lower.count("fish") + to_lower.count("sun")

print(count)