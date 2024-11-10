def camel_case:
    #snake_case = ""
    for c in camel_case:
    if c.isupper():
        snake_case += "_" + c.lower()
    else:
        snake_case +=c

    return snake_case

camel_case_input = input("Enter a camelCase variable name: ")

snake_case_output = camel_to_snake(camel_case_input)
print("Snake case:"), snake_case_output)