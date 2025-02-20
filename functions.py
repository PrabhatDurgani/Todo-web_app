FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list 
    of to do items.
    """
    try:
        with open(filepath,'r') as file_local:
                todos_local=file_local.readlines()
        return todos_local
    except FileNotFoundError:
        with open(filepath, 'w') as file_local:
            return []

def write_todos(todos_arg,filepath=FILEPATH):
    """Write the todo item list in the text file."""
    with open(filepath,'w') as file:
            file.writelines(todos_arg)