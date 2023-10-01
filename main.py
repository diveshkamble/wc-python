import sys
import os

if len(sys.argv[1:]) == 1:
    file_path = sys.argv[1]
    file_size = os.path.getsize(file_path)
    lines = 0
    word_count = 0
    with open(file_path, "r") as f:
        for line in f:
            lines += 1
            word_count += len(line.split())
    print(f'{lines} {word_count} {file_size} {file_path}')
else:
    file_path = sys.argv[2]
    if sys.argv[1] == '-c':
        file_size = os.path.getsize(file_path)
        print(f'{file_size} {file_path}')
    elif sys.argv[1] == '-l':
        lines = 0
        f = open(file_path, 'r')
        for i in f:
            lines += 1
        print(f'{lines} {file_path}')

    elif sys.argv[1] == '-w':
        word_count = 0
        with open(file_path, "r") as f:
            for line in f:
                word_count += len(line.split())
        print(f'{word_count} {file_path}')
