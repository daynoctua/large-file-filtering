import os
import sys
import time
import pathlib

# Check if file path is give in the command argument.
# If it is - skip to filtering.
try:
    target_file = sys.argv[1]
except IndexError:
    print("This script will filter a given file for lines containing 'error', and output a new file with only those lines\n")
    target_file = input("Enter path of file to filter: ")

# Check if file exists.
if not os.path.isfile(target_file):
    print("The path your provided ["+target_file+"] is not a file.")
    exit()

target_file = os.path.abspath(target_file)

# Split the given path into parts for use in generating the new file name.
file_location = os.path.dirname(target_file)
file_name = os.path.basename(target_file)
file_extension = pathlib.Path(target_file).suffix

# Set the name of new file - append _filtered to the original filename.
new_file_name = file_name.replace(file_extension, '')+"_filtered"+file_extension
new_file_path = file_location + "\\" + new_file_name

total_count = 0;
filtered_count = 0
start_time = time.time()
print("Filtering "+file_name+" ...")

with open(new_file_path,'w') as new_file: # create the new file.
    # Open the original file.
    # If a file has unusually encoded characters and throws errors - you can add errors="ignore" to the open() function.
    with open(target_file) as file:
    
        # Add a header if file type is CSV
        if file_extension == '.csv':
            new_file.write(file.readline())

        for line in file: # loop throught lines.
            total_count += 1
            if "error" in line.lower(): # check for errors.
                new_file.write(line) # append new file.
                filtered_count += 1

print("\nFiltered "+str(filtered_count) + " lines out of "+str(total_count)+", in "+str(round((time.time() - start_time), 2))+" s.")
print("Created new file "+new_file_name)
print("Done")