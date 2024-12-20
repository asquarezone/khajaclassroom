#import numeric.integer_utils

from numeric.integer_utils import is_even

from euler.problem_1 import solution as prob1_solution
from euler.problem_2 import solution as prob2_solution

def square(x):
    return x * x


result = square(9)
if is_even(result):
    print("even")
else:
    print("odd")

print(prob1_solution())
print(prob2_solution())
