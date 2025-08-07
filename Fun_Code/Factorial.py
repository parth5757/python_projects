import matplotlib.pyplot as plt
import timeit
def RecursiveFactorial(n):
  if n <= 1:
    return 1
  return n * RecursiveFactorial(n - 1)

def ItrativeFactorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

Factorail1 = [5, 25, 50, 100, 200, 400, 600, 700, 850, 920, 973]
Factorail2 = [5, 25, 50, 100, 200, 400, 600, 800, 1000, 1200, 1400, 1558]

FactorialVal = [20,]
Recursive_Factorial = []
Itrative_Factorial = []

def Test(Factorailval1,Factorailval2):
#   print("Recursion Factorial")
  for i in Factorailval1:
    Recursive_Factorial.append(RecursiveFactorial(i))
    # print("\n")
#   print("Itrative Factorial")
  for i in Factorailval2:
    Itrative_Factorial.append(ItrativeFactorial(i))
    # print("\n")

Test(Factorail1,Factorail2)

print("Recursive Factorials:", Recursive_Factorial)
print("Iterative Factorials:", Itrative_Factorial)


Recursive_Factorial_Time = []
Itrative_Factorial_Time = []
print("\nTiming Recursive Factorial:")
for i in Factorail1:
    try:
        time_taken = timeit.timeit(lambda: RecursiveFactorial(i), number=1)
        Recursive_Factorial_Time.append(time_taken)
        print(f"n = {i:<4} --> {time_taken:.6f} seconds")
    except RecursionError:
        print(f"n = {i:<4} --> RecursionError")

print("\nTiming Iterative Factorial:")
for i in Factorail2:
    time_taken = timeit.timeit(lambda: ItrativeFactorial(i), number=1)
    Itrative_Factorial_Time.append(time_taken)
    print(f"n = {i:<4} --> {time_taken:.6f} seconds")



plt.plot(Factorail1, Recursive_Factorial_Time, label="Recursion")
plt.plot(Factorail2, Itrative_Factorial_Time, label="Itrative")
plt.legend()
plt.show()