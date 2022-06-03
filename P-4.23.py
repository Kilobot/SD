import os

def find(path,filename):
    for file in os.listdir(path):
        if os.path.isdir(path+'/'+file):
            find(path+'/'+file,filename)
        else:
            if filename == file:
                print(path+'/+file')

find(r'C:\Users\CM\Desktop\RESEARCH_PROGRAM','Barcode Datas')

