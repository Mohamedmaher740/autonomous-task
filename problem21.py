


# grid = []
# treasure_counter = 0
# visited_positions = [[False] * 5 for _ in range(5)]

# #grid dimensions process
# def grid_dimensions(min, max):
#     while True:
#         try:
#             n = int(input(f"enter the number of rows between ({1},{10}) : "))
#             m = int(input(f"enter the number of columns between ({1},{10}) : "))
#             if min <= n <= max and min<= m <=max:
#                 return n , m
#             else:
#                 print(f"please try again and check your answer in range.")
#         except ValueError:
#             print("the inupt is invalid!")

# #starting position process
# def starting_position(min, max_x, max_y):
#     while True:
#         try:
#             Sx = int(input(f"enter the starting x position : "))
#             Sy = int(input(f"enter the starting y position : "))
#             if min <= Sx <= max_x and min<= Sy <=max_y:
#                 return Sx , Sy
#             else:
#                 print(f"please try again and check your answer in range.")
#         except ValueError:
#             print("the inupt is invalid!")  


# # dimension and starting variables
# n,m = grid_dimensions(1,10)
# # m = grid_dimensions(1,10)[1]
# sx, sy = starting_position(1,m,n)
# # sy = starting_position(1,m,n)[1]
# # dim = grid_dimensions(1,10)
# # start_pos = starting_position(1,dim[1],dim[0])


# # fill the grid
# for i in range(1,(n+1)):
#     check = True
#     while check == True:
#         row = input(f"enter a row number{i} : ")
#         if len(row) == m:
#             grid.append(row)
#             check = False
#         else:
#             print(f"your input invalid! please enter {m} characters.\n====================")
# #check the process is correct
# print(grid)
# print(visited_positions)

# #current position process
# def check_starting_position(x,y):
#     space = grid[x][y]
#     visited_positions[x][y] = True
#     if space == 'T':
#         treasure_counter +=1
#     elif space == '#':
#         return "no solution"
    
# print(check_starting_position(sx-1,sy-1))

# def check_current_position(x,y):
#     space = grid[x][y]
#     visited_positions[x][y] = True
#     if space == 'T':
#         treasure_counter +=1
#         return True
#     elif space == '.':
#         return True
#     elif space == '#':
#         return False


# print(visited_positions)
# print(treasure_counter)



# def check_next_position(x,y):
#     nx = x
#     ny = y
#     commands = ['U','R','L','D']
#     for command in commands:
#         if command == 'U':
#             nx = x+1
#             ny = y
#             check_current_position(nx,ny)
#         elif command == 'R':
#             nx = x
#             ny = y+1
#         elif command == 'L':
#             nx = x+1
#             ny = y
#         elif command == 'D'
#             nx = x+1
#             ny = y
    



# while check_starting_position(sx-1,sy-1):
#     cx, cy = (sx-1), (sy-1)
#     nx,ny = cx,cy

# print("no solutions")


# def check_position(command,x,y):
#     xt = x
#     yt = y
#     if command == 'U':
#         xt += 1
#     elif command == 'R':
#         yt += 1
#     elif command == 'L':
#         yt -= 1
#     elif command == 'D':
#         xt -= 1
#     #check limit
#     if 