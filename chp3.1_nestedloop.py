message = input('Enter a message (blank to quit): ') # Read the first message from the user

while message != " ":
    n = int(input('How many times should it be repeatd? ')) # Read the number of times the message should be displayed
    for i in range(n):   # Display the message the number of times requested
        print(message)
    message = input('Enter a message (blank to quit): ')  # Read the next message from the user

