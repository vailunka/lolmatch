def get_api_key():
    file1 = open('api_key.txt', 'r')
    Lines = file1.readlines()
    Lines = Lines[0]
    return Lines

