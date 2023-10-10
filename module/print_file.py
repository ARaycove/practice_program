while True:
    file_name = input('Please enter the file name, or enter exit to exit: ')
    if file_name == 'na na boo boo':
        print('na na boo boo to you - You have been punk\'d')
        continue
    elif file_name == 'exit':
        exit()
    else:
        try:
            fhand = open((file_name))
        except:
            print('File not found, please try again')
        try:
            count = 0
            total = 0
            for line in fhand:
                if line.startswith('X-DSPAM-Confidence:'):
                    parse_line = line.find(':')
                    float_line = float(line[parse_line + 1:])
                    count = count + 1
                    total = total + float_line
                    average_total = total / count
            print("The average spam confidence is: " + average_total)
        except RuntimeError:
            print('error in code')
