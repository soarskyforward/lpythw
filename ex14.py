from sys import argv

script, user_name = argv
prompt = ">"

print(f"Hi, I'm the {script}, {user_name}")
print("I'd like to ask you some questions")

print(f"{user_name}, I'm the {script} script.")
print("Do you like me?")
likes = input(prompt)

print(f"So, you said {likes}, I'm so happy.")
