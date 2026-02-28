import os

file_name = "tasks.txt"

def add_task(task, status):
    with open(file_name, "a") as file:
        file.write(f"{task} - {status}\n")

def show_tasks():
    if not os.path.exists(file_name):
        print("No tasks yet.")
        return
    
    with open(file_name, "r") as file:
        tasks = file.readlines()
    
    completed = 0x
    print("\nYour Tasks:")
    for t in tasks:
        print(t.strip())
        if "Completed" in t:
            completed += 1
    
    print(f"\nTotal Completed: {completed}")

task = input("Enter today's focus task: ")
done = input("Did you complete it? (yes/no): ")

status = "Completed" if done.lower() == "yes" else "Not Completed"

add_task(task, status)
show_tasks()