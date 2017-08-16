import os
import math

def file_sizes(directory):
    for f in os.listdir(directory):
        size_bytes = round(os.path.getsize(directory + f)/ 1000, 2)
        size_name = ["KB", "MB"]
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        print(f.ljust(20) + str(s).ljust(7) + size_name[i])
