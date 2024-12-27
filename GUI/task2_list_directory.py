import os

def list_directory(directory, gui=False):
    if not os.path.exists(directory):
        message = f"Error: The directory '{directory}' does not exist (-_-;)・・・"
        if gui:
            return message
        else:
            print(message)
            return

    contents = os.listdir(directory)
    output = f"Contents of '{directory}':\n"
    for item in contents:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            output += f"Directory: {item}\n"
        elif os.path.isfile(item_path):
            output += f"File: {item}\n"
        else:
            output += f"Other: {item}\n"
    
    if gui:
        return output
    else:
        print(output)
