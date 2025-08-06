import os
def fileCounter(path):
    total = 0
    all_folder = os.listdir(path)
    all_dir_total = []
    older_path = path
    for i in all_folder:
        path = path + i + "/"
        total = total + len(os.listdir(path))
        all_dir_total.append(total)
        # total = curr_total
        path = older_path
    print(all_dir_total)
    return total
# path = "F:/lekha/ML/Gujarati_Digit_DataSets/"
path = "F:/lekha/ML/Gujarati_Alphabet_Datasets/Train/" 
print(fileCounter(path))