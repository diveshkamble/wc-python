import sys
import os

if len(sys.argv[1:]) == 1:
    pass
else:
    file_path = sys.argv[2]
    if sys.argv[1] == '-c':
        file_size = os.path.getsize(file_path)
        print(f'{file_size} {file_path}')
    elif sys.argv[1] == '-l':
        print('Lines')
    elif sys.argv[1] == '-w':
        print('Words')
