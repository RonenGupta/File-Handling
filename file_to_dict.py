# TODO: Open "student_data.txt" in read mode (Made my own)
file = open("student_data.txt", "r")
    # TODO: Create dictionary student_dict 
student_dict = {}
    # TODO: For each line, split line into name and age (separated by comma)
for line in file: # Iterating each line in the file
    name, age = line.strip().split(", ") # Removes whitespaces and seperates with comma and space after
        # TODO: Store in the dictionary with the name as the key and age as the value
    student_dict[name] = int(age) # Store each name as a key for each age
# TODO: Print the dictionary
print(student_dict)