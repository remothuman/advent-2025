def read_file_to_list(file_path, convert_to_int=False):
    """
    Read a text file and return each line as a list.
    
    Args:
        file_path (str): Path to the text file
        convert_to_int (bool): If True, convert each line to int. Default is False.
    
    Returns:
        list: List containing each line from the file (as strings or ints)
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Remove trailing newlines and optionally convert to int
    result = []
    for line in lines:
        line = line.strip()  # Remove whitespace and newlines
        if line:  # Skip empty lines
            if convert_to_int:
                result.append(int(line))
            else:
                result.append(line)
    
    return result