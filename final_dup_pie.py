import os
import plotly.graph_objects as go
from tkinter.filedialog import askdirectory
from tkinter import Tk
import tkinter as tk
import os , hashlib
import check_selection

def plot():
    root.destroy()
    def get_file_sizes(directory):
        file_sizes = {}
        total_size = 0
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                size = os.path.getsize(filepath)
                total_size += size
                file_extension = os.path.splitext(filename)[1]
                if file_extension in file_sizes:
                    file_sizes[file_extension] += size
                else: 
                    file_sizes[file_extension] = size
        # print(file_sizes)
        # print(total_size)
        return total_size, file_sizes
    def plot_pie_chart(total_size, file_sizes):
        labels = []
        sizes = []
        for extension, size in file_sizes.items():
            percentage = (size / total_size) * 100
            labels.append(extension)
            sizes.append(percentage)
#         print(labels,sizes)
        fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
        fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers',marker=dict(size=0, color='rgba(0,0,0,0)'),showlegend=True,text=['%s, %1.1f%%' % (l, s) for l, s in zip(labels, sizes)],hoverinfo='text'))
        fig.update_layout(legend=dict(x=1.1, y=1))
        fig.show()
    directory = askdirectory(title="Select a folder")
    total_size, file_sizes = get_file_sizes(directory)
    plot_pie_chart(total_size, file_sizes)

def delete_duplicates():
    root.destroy()
    path =  askdirectory(title="Select a folder")
    file_list = os.walk(path)
    hash_location = dict()
    duplicates = dict()
    dup_hash = list()
    dup_path = list()
    for root1, folders, files in file_list:
        for file in files:
            path = os.path.join(root1,file)
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

root = tk.Tk()
root.title("Choose from Below")
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)
button1 = tk.Button(frame, text="View PIE chart", bg="black", fg="white",command=plot, width=20, font=("Georgia",12))
button1.pack(side=tk.LEFT, padx=10)
button2 = tk.Button(frame, text="Delete duplicate files", bg="black", fg="white",command=delete_duplicates, width=20, font=("Georgia",12))
button2.pack(side=tk.RIGHT, padx=10)
root.mainloop()