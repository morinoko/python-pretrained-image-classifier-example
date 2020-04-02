#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Felice Forby
# DATE CREATED: March 31, 2020                                 
# REVISED DATE: April 2, 2020
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    filenames = listdir(image_dir)
    labels = dog_labels_from_filenames(filenames)

    results_dic = {}
    
    for i in range(0, len(filenames), 1):
        # Skip hidden files
        if not filenames[i].startswith('.'):
            # Make sure there are no duplicates
            if filenames[i] not in results_dic:
                results_dic[filenames[i]] = [labels[i]]
            else:
                print("Duplicate key warning:", "Key", filenames[i],
                      "already exists in results_dic with value",
                      results_dic[filenames[i]])
        
    return results_dic

def dog_labels_from_filenames(file_list):
    """
    Returns images filenames processed into labels.
        Example: german_shepherd_dog_04890.jpg becomes 'german shepard dog'
        
        Filenames should be words separated by '_'
    """
    labels = []
    
    for filename in file_list:
        words = filename.lower().split("_")
        pet_name = ""
        
        for word in words:
            if word.isalpha():
                pet_name += word + " "
                
        labels.append(pet_name.strip())
    
    return labels
