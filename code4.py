#assignment 1
with open('aboutme.txt', 'r') as file:
    readcontent= file.read()

with open('updated.txt', 'a') as newfile:
    newfile.write(readcontent + "I live in Bayelsa")


#assignment 2

try:
    filename = input('type the filename:')
    with open(filename, 'r') as userfile:
        print(userfile.read())
        

except FileNotFoundError:
    print("Sorry, file does not exist.")

finally:
    print("have a nice day")