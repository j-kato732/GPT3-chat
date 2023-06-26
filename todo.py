# Initialize an empty dictionary to store tasks
tasks = {}

# Function to add a task


def add_task(name, description):
    """
    {
        "description": "Add a new task",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the task"
                },
                "description": {
                    "type": "string",
                    "description": "The description of the task"
                }
            },
            "required": ["name", "description"]
        },
    }
    """
    if name in tasks:
        print(f"Task '{name}' already exists.")
        return False
    tasks[name] = description
    return f"Task '{name}' added."

# Function to list all tasks


def list_tasks():
    """
    {
        "description": "List all tasks",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
    """
    if not tasks:
        return "No tasks found."

    task_list = []
    for name, description in tasks.items():
        task_list.append(f"Task Name: {name}, Description: {description}")

    return "\n".join(task_list)

# Function to update a task


def update_task(name, new_description):
    """
    {
        "description": "Update an existing task",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the task to update"
                },
                "new_description": {
                    "type": "string",
                    "description": "The new description for the task"
                }
            },
            "required": ["name", "new_description"]
        },
    }
    """
    if name not in tasks:
        return f"Task '{name}' not found."

    tasks[name] = new_description
    return f"Task '{name}' updated."

# Function to delete a task


def delete_task(name):
    """
    {
        "description": "Delete a task",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the task to delete"
                }
            },
            "required": ["name"]
        },
    }
    """
    if name not in tasks:
        return f"Task '{name}' not found."
    del tasks[name]
    return f"Task '{name}' deleted."
