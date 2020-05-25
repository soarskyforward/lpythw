new_name = ['nobody','wei', 'admin', 'john', 'jack', 'me']
names = ['wei', 'admin', 'john', 'jack', 'me']

for loggings in new_name:
    if loggings in names:
        if loggings == "admin":
            print("Hello admin, would you like to see a staus report")
        if loggings != "admin":
            print(f"welcome back, {loggings}!")
    else:
        print(f"'nobody' not in {names}Who is him?")
