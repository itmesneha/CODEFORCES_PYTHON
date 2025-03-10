import math
limit = 10**6

def calculate_prime_flag_for_each_number_upto_limit():
    prime_flag = [True] * limit
    prime_flag[0] = prime_flag[1] = False
    for i in range(2, limit):
        if prime_flag[i] == True:
            for j in range(i*i, limit, i):
                prime_flag[j] = False
    return prime_flag

def check_if_a_number_is_t_prime(n):
    if n == 4:
        return True
    if n < 4 or n%2==0:
        return False
    sqrt_n = n**0.5
    if sqrt_n==int(sqrt_n):
        if prime_flag[int(sqrt_n)] == True:
            return True
    return False

prime_flag = calculate_prime_flag_for_each_number_upto_limit()
total_numbers = int(input())
input_array = list(map(int,input().split()))
for i in input_array:
    if check_if_a_number_is_t_prime(i)==True:
        print("YES")
    else:
        print("NO")


# # intuitive code
# import math

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

# def check_perfect_square(n):
#     return int(math.sqrt(n))**2 == n

# t = int(input())
# A = list(map(int, input().split()))
# for num in A:
#     if num < 4:
#         print('NO')
#     elif num == 4:
#         print('YES')
#     elif num % 2 == 0:
#         print('NO')
#     elif check_perfect_square(num) and is_prime(int(math.sqrt(num))):
#         print('YES')
#     else:
#         print('NO')
