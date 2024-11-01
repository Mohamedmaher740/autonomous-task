print("hello, i am a robot and my name is ALex\n=================")
x = 0
y = 0
error =0
command_errors = []
def check_range(min, max):
    while True:
        try:
            global n
            n = int(input(f"enter the number of commands between ({1},{100}) : "))
            if min <= n <= max:
                return n
            else:
                print(f"please try again and check your answer in range.")
        except ValueError:
            print("the inupt is invalid!")
            
def check_commands(length):
    while True:
        try:
            commands = input(f"enter the commands in a string with length {length} : ").upper()
            if len(commands) == length:
                return commands
            else:
                print(f"please try again and check the length o string.")
        except ValueError:
            print("the inupt is invalid!")

commands = check_commands(check_range(1,100))
print(commands)

for command in commands:
    if command == "L":
        x-=1
        print(f"({x},{y})")
    elif command == "R":
        x+=1
        print(f"({x},{y})")
    elif command == "U":
        y+=1
        print(f"({x},{y})")
    elif command == "D":
        y-=1
        print(f"({x},{y})")
    else:
        error +=1
        command_errors.append(command)

the_result = f"i'm now in position({x},{y}) and there {error} errors in your commands input : {command_errors}\n{command_errors} are not in command list."
print(the_result)
