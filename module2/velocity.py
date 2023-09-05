
# Task 1: Ask user for the time
print('What is the time?')
my_time = input()
my_time = int(my_time) # convert to int
# Task 2: Ask user for distance
my_dist = float(input('How far did they go?: ')) # cast directly as float
# Task 3: Calculate velocity, and display it
my_vel = my_dist/my_time
print('Your time was', my_time)
print('Your distance was', my_dist)
print('Your velocity is:', my_vel)
