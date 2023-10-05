test = "some length of values"
index_test = len(test) - 1
print (index_test)
reverse_test = ""
while index_test >= 0:
    character = test[index_test]
    reverse_test = reverse_test + character
    index_test = index_test - 1
    print(reverse_test)
print(reverse_test)
    