''' 
Mohamed BEN ALI
LINAGORA_Labs
'''
import os
from os import listdir, getcwd
from os.path import join
if __name__ == '__main__':
    source_folder='JPEGImages/'
    dest='ImageSets/Main/train.txt'
    dest2='ImageSets/Main/val.txt'
    dest3='ImageSets/Main/trainval.txt'
    dest4='ImageSets/Main/test.txt'
    file_list=os.listdir(source_folder)
    train_file=open(dest,'a')
    val_file=open(dest2,'a')
    trainval_file=open(dest3,'a')
    test_file=open(dest4,'a')
    file_num=0
    for file_obj in file_list:
        file_path=os.path.join(source_folder,file_obj)

        file_name,file_extend=os.path.splitext(file_obj)

        if(file_num<4000):

            train_file.write(file_name+'\n')
        else :
            val_file.write(file_name+'\n')
        file_num=file_num+1
    train_file.close()
val_file.close()