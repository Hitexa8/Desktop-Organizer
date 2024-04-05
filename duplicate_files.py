from tkinter.filedialog import askdirectory
from tkinter import Tk
import tkinter as tk
import os , hashlib
import check_selection

path =  askdirectory(title="Select a folder")
file_list = os.walk(path)
hash_location = dict()
duplicates = dict()
dup_hash = list()
dup_path = list()
for root, folders, files in file_list:
    for file in files:
        path = os.path.join(root,file)
        fileHash = hashlib.md5(open(path,'rb').read()).hexdigest()
        hash_location[fileHash] = hash_location.get(fileHash, [])
        hash_location[fileHash].append(path)
    # print(root,folders,files)
for key,value in hash_location.items():
    if len(value) > 1:
        duplicates[key] = value
        dup_hash.append(key)
# print(duplicates)
# print(dup_hash)
for i in dup_hash:
    for j in duplicates[i]:
        location = os.path.split(j)[0]
        file = os.path.split(j)[1]
        dup_path.append(j)
        print("Duplicates files",file, "found in folders:",location)
check_selection.abc(dup_path)