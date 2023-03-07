def datatype_solution(datatype, args):
    result = None
    if datatype == "int":
        result = 2 * int(args)
    elif datatype == "real":
        result = f"{(1.5 * float(args)):.2f}"
    elif datatype == "string":
        result = "$" + args + "$"

    return result


type_input = input()
value = input()

print(datatype_solution(type_input, value))
