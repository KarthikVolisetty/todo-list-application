# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:18:13 2024

@author: karth
"""

import json
import argparse

# Function to find the next available ID
def get_next_task_id(task_list):
    if not task_list:
        return 1  # If the list is empty, return 1
    existing_ids = {task['id'] for task in task_list}  # Create a set of existing task IDs
    for i in range(1, len(task_list) + 2):  # Check from 1 upwards for missing ID
        if i not in existing_ids:
            return i

def add_task(task_list, description):
    task_id = get_next_task_id(task_list)
    task = {'id': task_id, 'description': description, 'completed': False}
    task_list.append(task)

def remove_task(task_list, task_id):
    task_list[:] = [task for task in task_list if task['id'] != task_id]

def view_tasks(task_list):
    if not task_list:
        print("There are no tasks in the list")
    else:
        for task in task_list:
            status = "Completed" if task['completed'] else "Pending"
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {status}")

def mark_task_completed(task_list, task_id):
    for task in task_list:
        if task['id'] == task_id:
            task['completed'] = True

def save_tasks(task_list, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(task_list, file)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    parser = argparse.ArgumentParser(description='Command-line To-Do List Application')
    parser.add_argument('command', choices=['add', 'remove', 'view', 'complete'], help='Command to execute')
    parser.add_argument('--description', help='Description of the task')
    parser.add_argument('--id', type=int, help='ID of the task')
    args = parser.parse_args()

    task_list = load_tasks()

    if args.command == 'add':
        add_task(task_list, args.description)
    elif args.command == 'remove':
        remove_task(task_list, args.id)
    elif args.command == 'view':
        view_tasks(task_list)
    elif args.command == 'complete':
        mark_task_completed(task_list, args.id)

    save_tasks(task_list)

if __name__ == '__main__':
    main()
