def get_formatted_name(first_name,last_name):
    full_name = first_name +' ' +last_name
    return full_name.title();

musician = get_formatted_name('jimi','hendrix');
print(musician)

def get_formatted_name1(first_name,last_name,middle_name=''):
    # Python 将非空字符串解读为true
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name1('jimi','hendrix')
print(musician)

musician = get_formatted_name1('john','hooker','lee');
print(musician)