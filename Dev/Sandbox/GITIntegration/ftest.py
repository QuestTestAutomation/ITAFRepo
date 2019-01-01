import shutil
import os

source = 'C:\\Devworkspace\\GitWorkspace\\RepoOne\\Rep100\\'
dest1 = 'C:\\Devworkspace\\GitWorkspace\\RepOne\\Rep1000'


files = os.listdir(source)
print(files)

for f in files:
        shutil.move(source+f, dest1)

files = os.listdir(dest1)
print(files)