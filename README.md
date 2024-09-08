# Command-Line To-Do List Application

## Overview

This is a simple command-line based To-Do List application that allows you to manage tasks effectively. You can add, view, remove, and mark tasks as completed. The tasks are stored persistently in a JSON file, so your task list remains even after closing the application.

## Features

- **Add Tasks**: Add a new task to the list with a unique ID and description.
- **View Tasks**: View all tasks in the list along with their status (Pending or Completed).
- **Remove Tasks**: Remove tasks from the list by specifying their unique ID.
- **Mark Tasks as Completed**: Mark any task as completed by its ID.
- **Persistent Storage**: All tasks are saved in a JSON file and are reloaded each time the application runs.

## Project Structure

```plaintext
.
├── tasks.json      # Stores tasks persistently
├── todo.py         # The main Python script for the to-do application
└── README.md       # Project documentation (this file)
