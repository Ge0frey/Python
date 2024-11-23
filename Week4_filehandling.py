def modify_content(content):
    """
    Modify the content read from the file.
    This function can be customized as needed.
    Here, it converts the text to uppercase.
    """
    return content.upper()


def read_and_write_files():
    """
    Reads a file and writes a modified version to a new file.
    Handles errors for file operations.
    """
    # Ask the user for the filename
    input_file = input("Enter the name of the file to read from: ")

    try:
        # Attempt to open the input file for reading
        with open(input_file, "r") as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Write the modified content to a new file
        output_file = input("Enter the name of the new file to write to: ")
        with open(output_file, "w") as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to '{output_file}' successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError as e:
        print(f"Error: Could not read/write the file. Details: {e}")


# Run the program
if __name__ == "__main__":
    read_and_write_files()
