# Despre lucrul cu fișiere

#Construiti o histograma in consola, pentru a mapa fisierele existente pe o partitie, prin categoriile de size din intervalul
# [100G,50G) [50G,10G) [10G,1G) [1G,100M) [100M,10M) [1M,100k) [100k,10k).
"""
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
                                                                                 O
[100G-50G) [50G, 10G) [10G, 1G) [1G, 100M) [100M, 10M) [1M, 100k) [100k, 10k) [10k, 0]
--------------------------------------------------------------------------------------------------------------->
"""
# De asemenea generati intr-un fisier, sau in mai multe fisiere, informatii legate de path-ul absolut al fisierelor + dimensiunea
# specifica a acestora, astfel incat daca vreau sa sterg oricare dintre ele, sa pot sa fac asta tot din python, sau manual.


import os
import sys
import numpy as np

# print(len(sys.argv))
# print(sys.argv)

# f = open("fisier.txt", 'r')
# data = f.read()
# f.close()
# with open('fisier.txt', 'r') as f:
#     data = f.read()

# f = open("fisier.txt", 'w')
# data = f.write('\n')
# f.close()
# with open('fisier.txt', 'w') as f:
#     f.write('something')




# files = os.listdir('C:\\')

# print(files)

# for fis in os.listdir('C:\\'):
#     pabs = os.path.join('C:', fis)
#     if os.path.isfile(pabs):
#         size = os.path.getsize(pabs)
#         print(pabs, 'is file :', size / (2 ** 20) )
#     else:
#         print(pabs, 'is folder')





import matplotlib.pyplot as plt
import os
from collections import defaultdict

def draw_histogram(dataset):
    print("Histogram:")
    maxcount = 0
    columns = [0] * 9
    for category, count in dataset.items():
        print(f"{category}: {count} files")
        if maxcount < count:
            maxcount = count
    index = 0
    for category, count in dataset.items():
        columns[index] = count / maxcount * 20
        index += 1
    columns.reverse()
    for i in range(20):
        print("   ", end='')
        for j in range(len(columns)):
            if columns[j] >= 20 - i:
                print("#", end='         ')
        print()
    print("[0,10k) [10k,100k) [100k,1M) [1M,10M) [10M,100M) [100M,1G) [1G,10G) [10G,50G) [50G,100G]")


def get_size_category(size):
    if size >= 100 * 1024 * 1024 * 1024:
        return "[100G, inf)"
    elif size >= 50 * 1024 * 1024 * 1024:
        return "[50G,100G)"
    elif size >= 10 * 1024 * 1024 * 1024:
        return "[10G,50G)"
    elif size >= 1024 * 1024 * 1024:     
        return "[1G,10G)"
    elif size >= 100 * 1024 * 1024:      
        return "[100M,1G)"
    elif size >= 10 * 1024 * 1024:       
        return "[10M,100M)"
    elif size >= 1024 * 1024:            
        return "[1M,10M)"
    elif size >= 100 * 1024:             
        return "[100k,1M)"
    elif size >= 10 * 1024:              
        return "[10k,100k)"
    else:                                
        return "[0,10k)"

def generate_histogram_and_info(directory, output_file):
    histogram = defaultdict(int)
    file_info = []
    arr = []
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            size = os.path.getsize(filepath)
            category = get_size_category(size)
            arr.append(size)
            histogram[category] += 1
            file_info.append((filepath, size, category))

    draw_histogram(histogram)

    a = np.array(arr)
    fig, ax = plt.subplots(figsize = (10, 7))
    ax.hist(a, bins = [0, 25, 50, 75, 100])
    plt.show()

    with open(output_file, 'w') as f:
        for filepath, size, category in file_info:
            filepath.replace('ă', 'a')
            filepath.replace('â', 'a')
            filepath.replace('î', 'i')
            filepath.replace('ș', 's')
            filepath.replace('ț', 't')
            filepath.replace('\u0103', 'a')
            filepath.replace('\u0421', 'C')
            try:
                f.write(f"{filepath} | Size: {size} bytes | Category: {category}\n")
            except Exception as e: pass

if __name__ == "__main__":
    directory_path = "D://AI"
    output_file_path = "file.txt"
    generate_histogram_and_info(directory_path, output_file_path)