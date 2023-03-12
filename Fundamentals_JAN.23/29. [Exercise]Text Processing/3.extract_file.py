file_path = input().split("\\")

file = file_path[-1]
filename, extension = file.split(".")

print(f"File name: {filename}")
print(f"File extension: {extension}")

