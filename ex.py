import os

for filename in os.listdir('.'):
    if os.path.isfile(filename) and os.access(filename, os.X_OK):
        print(filename)
