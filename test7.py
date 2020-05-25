def get_formatted_name(first_name, last_name, middle_name=''):
    """what's your name?"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name(input("What's your first name?"), input("And?") , input("Else?"))
print(musician)
