print('Please enter a list of numbers')
user_input = input()
# print(type(user_input))
number_list = user_input.split()
# print(type(number_list))
try:
    number_list = [float(num) for num in number_list]
    # print(number_list)
    print(min(number_list))
    print(max(number_list))
except:
    print('enter numbers only')