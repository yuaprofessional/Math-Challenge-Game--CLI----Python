import random 
import time

operand = ("+","-","*")
min = 2
max = 10
Total_problem = 10


def generate_problem():
    left = random.randint(min,max)
    right = random.randint(min,max)
    operator = random.choice(operand)
    exp = str(left) + " " + operator + " "+ str(right)
    answer = 0
    if operator == "+":
        answer = left + right
    elif operator == "-":
        answer = left - right
    else:
        answer = left * right 
    return exp,answer


def problem():
    wrong = 0
    input("Press enter to start!!! ")
    print("--------------------------------------------")
    start_time = time.time()

    for i in range(Total_problem):
        exp,answer = generate_problem()
        while True:
            guess = input("Problem #  " + str(i + 1) + ": " + exp + " = ")
            if guess == str(answer):
                break
            else:
                wrong = wrong + 1

    end_time = time.time()
    total_time = end_time - start_time
    print("--------------------------------------------")
    print(f"You are wrong {wrong} times")
    print(f"Thank you, You finished in {total_time} seconds")



problem()
