def write_file(file_name, file_content):
    file = str(file_name) + ".txt"
    with open(file, "w") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    file = str(file_name) + ".txt"
    with open(file, "a") as f:
        f.write(append_content)

def read_file(file_name):
    file = str(file_name) + ".txt"
    with open(file, "r") as f:
        return f.read()

