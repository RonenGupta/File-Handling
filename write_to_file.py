# TODO: Open "movies.txt" in write mode
file = open("movies.txt", "w")
        # TODO: Ask the user for a favourite movie THREE TIMES. Be efficient in your code.
for i in range(1, 4, 1):
    user_input = input("What is your favorite movie? ")
        # TODO: Write the movie to the file with a newline
    file.write(user_input + "\n")
# TODO: Let the user know movies have been saved to file
print("Your favorite movies have been saved!")
# TODO: Check the file and ensure it worked!
file = open("movies.txt", "r")
contents = file.read()
print(contents)