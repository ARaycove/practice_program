while True:
    print('Enter a number')
    user_input = input()
    if user_input == 'done':
        break
    else:
        try:
            float(user_input)
            print(user_input)
        except:
            print('bad data')
