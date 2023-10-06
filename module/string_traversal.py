# test = "some length of values"
# index_test = len(test) - 1
# print (index_test)
# reverse_test = ""
# while index_test >= 0:
#     character = test[index_test]
#     reverse_test = reverse_test + character
#     index_test = index_test - 1
#     print(reverse_test)
# print(reverse_test)
#################
# word = 'banana'
# print(word.count('a'[:]))
# boolean = True
# while boolean == True:
#         index_list = []
#         count = 0
#         index = word.find('a', count)
#         count = list(index + 1)
#         index_list = index_list + index
#         print (index_list)
######################
string = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string
# into a floating point number
parse_string = string.find(':')
float_string = string[parse_string+1:]
float_string = float(float_string)
print(float_string)
print(type(float_string))