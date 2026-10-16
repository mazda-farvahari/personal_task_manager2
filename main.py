from tasks import show_tasks

name = input("Enter your name: ")
print("welcome",name)

tasks = []
count = int(input("how many tasks do you wants to add? "))

for i in range(count):
    task = input("Enter your task: ")
    tasks.append(task)

show_tasks(tasks)