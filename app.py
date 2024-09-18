import streamlit as st

# Task class
class Task:
    def __init__(self, task, tno):
        self.task = task
        self.taskno = tno
        self.next = None

# LinkedList implementation
class Linkedlist:
    def __init__(self):
        self.head = None

    def addTask(self, taskno, task):
        new_task = Task(task, taskno)

        if self.head is None:
            self.head = new_task
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_task

    def rmvTask(self, taskno):
        cur = self.head
        prev = None

        if cur and cur.taskno == taskno:
            self.head = cur.next
            return

        while cur:
            if cur.taskno == taskno:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def display(self):
        tasks = []
        cur = self.head
        while cur:
            tasks.append((cur.taskno, cur.task))
            cur = cur.next
        return tasks

# Queue implementation (FIFO)
class Queue:
    def __init__(self):
        self.list = []

    def addTask(self, taskno, task):
        self.list.append((taskno, task))

    def rmvTask(self):
        if self.list:
            self.list.pop(0)

    def display(self):
        return self.list

# Stack implementation (LIFO)
class Stack:
    def __init__(self):
        self.list = []

    def addTask(self, taskno, task):
        self.list.append((taskno, task))

    def rmvTask(self):
        if self.list:
            self.list.pop()

    def display(self):
        return self.list


# Initialize session state for tasks in LinkedList, Queue, and Stack
if 'linkedlist' not in st.session_state:
    st.session_state.linkedlist = Linkedlist()
if 'queue' not in st.session_state:
    st.session_state.queue = Queue()
if 'stack' not in st.session_state:
    st.session_state.stack = Stack()

# Streamlit UI
st.title("Task Manager")

# Data structure selection using radio buttons
task_type = st.radio("Select Data Structure to Add Task", ["Linked List", "Queue", "Stack"])

# Adding tasks
taskno = st.number_input("Task Number", min_value=1)
task_desc = st.text_input("Task Description")

if st.button("Add Task"):
    if task_type == "Linked List":
        st.session_state.linkedlist.addTask(taskno, task_desc)
    elif task_type == "Queue":
        st.session_state.queue.addTask(taskno, task_desc)
    else:
        st.session_state.stack.addTask(taskno, task_desc)

# Display tasks option
st.subheader("Select Data Structure to Display Tasks")

display_type = st.radio("Display Tasks", ["Linked List", "Queue", "Stack"])

# Display tasks for LinkedList, Queue, and Stack
if display_type == "Linked List":
    st.subheader("Tasks in Linked List")
    for taskno, task in st.session_state.linkedlist.display():
        if st.button(f"Done {task}", key=f"ll_{taskno}"):
            st.session_state.linkedlist.rmvTask(taskno)

elif display_type == "Queue":
    st.subheader("Tasks in Queue (FIFO)")
    tasks = st.session_state.queue.display()
    if tasks:
        taskno, task = tasks[0]
        st.write(f"{taskno}: {task}")
        if st.button(f"Done {task}", key="q_done"):
            st.session_state.queue.rmvTask()
    else:
        st.write("No tasks in the queue.")

elif display_type == "Stack":
    st.subheader("Tasks in Stack (LIFO)")
    tasks = st.session_state.stack.display()
    if tasks:
        taskno, task = tasks[-1]
        st.write(f"{taskno}: {task}")
        if st.button(f"Done {task}", key="s_done"):
            st.session_state.stack.rmvTask()
    else:
        st.write("No tasks in the stack.")

# streamlit run "F:\MyProject\Lib\tm DSA.py"
