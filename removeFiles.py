import os
import shutil

path  = input("Enter your file path: ")
days = int(input("Enter the number of days: ")) * 24 *60 *60

if os.path.exists(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            content = os.path.join(root, name)
            fileStatsObj = os.stat ( content ).st_ctime   
            if fileStatsObj>days:
                os.remove(content)
                shutil.rmtree(content)

else:
    print("path not found")

            
        