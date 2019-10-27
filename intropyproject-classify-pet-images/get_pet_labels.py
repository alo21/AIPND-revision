#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Alessandro Losavio
# DATE CREATED: 26/10/2019
# REVISED DATE: 
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


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    files = listdir(image_dir)
    results_dic = {}

    for file in files:
        if file[0] != '.':
            formattedString = file.replace(".jpg", "").replace("_", " ").lower()
            stringWithNoDigits = ''.join([i for i in formattedString if not i.isdigit()]).strip()
            results_dic.update({file: [stringWithNoDigits]})

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
