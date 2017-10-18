from __future__ import division, print_function, absolute_import
from os import listdir
# unrarlib = ctypes.WinDLL('C:/Program Files (x86)/UnrarDLL/UnRAR.lib')
from unrar import rarfile


def extract_images():
    DATA_FOLDER = '/datasets/Histology_DB_Uppsala_4_Cls_1000_each_Jan_2010/test/'
    archives = listdir(DATA_FOLDER)

    file = open('./tflearn/data/info.txt', 'w')
    for file_dir in archives:
        rf = rarfile.RarFile(DATA_FOLDER + file_dir)
        rf.extract(rf.namelist()[0], './tflearn/data')
        class_type = 1 if '_n_' in file_dir else 0
        print(rf.namelist()[0])
        file.write('./data/' + rf.namelist()[0] + ' ' + str(class_type) + '\n')
    file.close()

extract_images()
