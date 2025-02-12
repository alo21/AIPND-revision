#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Alessandro Losavio
# DATE CREATED: 26/10/2019
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 
def get_input_args():

    parser = argparse.ArgumentParser(description='Use a Pre-trained Image Classifier to Identify Dog Breeds')

    parser.add_argument("--dir", help='Specify images directory', default ='pet_images/')
    parser.add_argument("--arch", help='Specify the model you want to use', default ='vgg')
    parser.add_argument("--dogfile", help='Specify the file that contains dognames', default='dognames.txt')

    return parser.parse_args()
