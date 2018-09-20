#Sandra Barba
#ID 80641786
#Prof. Diego Aguirre
#Lab 1A
#CS2302

import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

    # Your code goes here
    #This loop add the files to the lists of dogs and cats respectively
    for i in range (1, len(file_list)):
        #Split the files names by a dot
        split_files = file_list[i].split(".")
        #if the file contains the string dog or cat append to the list
        if split_files[0] == "cat":
            cat_list.append(file_list[i])
        elif split_files[0] == "dog":
            dog_list.append(file_list[i])
    #This loop open the directories recursively
    for j in range (len(dir_list)):
        #Create path to open directories inside the actual directory
        file_path = path +'/'+ dir_list[j]
        #Storage the lists returned from the actual directory and then
        #append the files to cat and dog lists.
        cat_to_append, dog_to_append = process_dir(file_path)
        cat_list.append(cat_to_append)
        dog_list.append(dog_to_append)


    return cat_list, dog_list


def main():
    start_path = './Pictures' # current directory



    print(process_dir(start_path))
    #print(get_dirs_and_files(start_path))


main()
