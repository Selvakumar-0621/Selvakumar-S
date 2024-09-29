# Program to create a file with currentimestamp

import datetime                                                   #  importing the datetime from inbuilt

def create_timestamp_file():
   
    current_timestamp = datetime.datetime.now()
    timestamp_str = current_timestamp.strftime("%Y%m%d_%H%M%S")   # formatting for the file name
    
    filename = f"{timestamp_str}.txt"
    
    with open(filename, 'w') as file:                             # opening the file
        file.write(f"Current Timestamp: {current_timestamp}\n")   # writing the content of the file
    
    print(f"File '{filename}' created with content:\nCurrent Timestamp: {current_timestamp}")

create_timestamp_file()






# Program to read a txt file and display its content

def read_file_content(filename):                                  

    with open(filename, 'r') as file:                            # To open the file in read only mode
        content = file.read()                                    # To read the content of the file
        print("The File Content is :", content)

filename = "sk.txt"
read_file_content(filename)
