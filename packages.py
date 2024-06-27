import os
import shutil

print(os.getcwd()) #equivalent to linux pwd

total, used, free = shutil.disk_usage("/")
print(f"total used is: {total // (2**30)} GB")
print("used used is", used // (2**30),"GB")
print("free used is", free // (2**30),"GB") 