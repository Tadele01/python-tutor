try:
    with open('file.txt') as f:
        file_data = f.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing')
except PermissionError:
    print('This is not allowed')
except:
    print('some other error occured')

#the generic except did not give us much information about the exception
#so in order to be able to get a good message related to the occured exception
#we use sys module

import sys

try:
    1/0
except:
    err = sys.exc_info()
    for e in err:
        print(e)

#without importing sys module

try:
    1/0
except Exception as err:
    print('some other error occurred', str(err))
#Creating custom exception

class ConnectionError(Exception): #inherit from the generic Exception class
    pass
raise ConnectionError('Cannot connect ... is it time to panic ?')
try:
    raise ConnectionError('Whoops!')
except ConnectionError as err:
    print('Got', str(err))
