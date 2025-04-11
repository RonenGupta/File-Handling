# TODO: Open the file "students.txt" in read mode
file = open("students.txt", "r")
    # TODO: Read lines from the file and store them in a list
names = file.readlines()
#TODO: Remove extra spaces and newlines from each name. Use list comprehension to STRIP whitespace
namescleaned = [name.strip() for name in names]
# TODO: Print the list
print(names)
    # TODO: Print the cleaned-up list
print(namescleaned)