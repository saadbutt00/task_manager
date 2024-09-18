                                                     Task Manager with Linked List, Queue, and Stack (Streamlit)
Overview
This project is a simple task management application built using Streamlit, a Python framework for creating web apps. The application allows users to manage tasks using three different data structures:

Linked List
Queue (FIFO - First In First Out)
Stack (LIFO - Last In First Out)
The user can add tasks to any of these structures and view or remove them as they are completed. Each data structure provides a different approach to task handling, demonstrating how these abstract data types work in practice.

Features
Add Tasks: Users can add tasks to a Linked List, Queue, or Stack.
Display Tasks: Tasks can be viewed in each data structure.
Remove Tasks:
In the Linked List, tasks can be removed based on their task number.
In the Queue, the first task (FIFO) can be removed.
In the Stack, the last task (LIFO) can be removed.
Data Structures Used
Linked List: A series of tasks where each task points to the next. Users can remove any task in the list by selecting the task.
Queue (FIFO): A "First In, First Out" structure, where the task that was added first is removed first.
Stack (LIFO): A "Last In, First Out" structure, where the most recently added task is removed first.
How to Use
Data Structure Selection:
Use the radio buttons to select a data structure (Linked List, Queue, or Stack) where the task will be added.
Add a Task:
Enter a task number and description, then click "Add Task" to add it to the selected data structure.
Display Tasks:
Select the data structure you want to view tasks from using the radio buttons.
The tasks will be displayed according to the logic of the chosen data structure.
Remove a Task:
Tasks can be removed by clicking the "Done" button next to each task. For the Queue, only the first task can be removed, and for the Stack, only the most recent task can be removed.
