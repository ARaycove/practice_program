while True:
    file_name = input('Please enter the file name, or enter exit to exit: ')
    if file_name == 'exit':
        exit()
    try:
        print('Enter file name')
        fhand = open((file_name))
        for line in fhand:
            if line.startswith('X-DSPAM-Confidence:'):
                print(line)
    except:
        print('File not found, please try again')