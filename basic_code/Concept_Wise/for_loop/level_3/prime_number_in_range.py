import time
start, end = int(input("enter the starting number: ")), int(input("enter the end number: "))
prime_num = []
non_prime_num = []
time_start = time.time()
for i in range(start, end+1):
    # print(i)
    # count is store that any number is how many number of time divide with other number that result come zero.
    count = 0
    for j in range(1, i+1):
        # i is the each number that prime or not is checking.
        if i % j == 0:
            count += 1
            # this is for the reducing time because it stop the automatically 2 j for loop where if count goes 3 then it automatically stop that loop
            if count > 2:
                break
    # print("count:", count)
    if count == 2:
        # it store the all prime number
        prime_num.append(i)
    else:
        non_prime_num.append(i)
time_end = time.time()
print(f"following are the prime numbers: {prime_num}")
print(f"following are the not prime numbers: {non_prime_num}")
print(f"the total time is taken: {time_end-time_start}")