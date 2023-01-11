from name_function import get_formatted_name

print("please enter 'q' at any time to quit!")
while True:
    first_name = input("please input first name")
    if first_name == 'q':
        break
    last_name = input("please input last name")
    if last_name == 'q':
        break
    formatter_name = get_formatted_name(first_name, last_name)
    print("\tNeatly formatted name: " + formatter_name + '.')