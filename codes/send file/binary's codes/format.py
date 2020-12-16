
import os

def binary_file (file_address):
    file=open(file_address,'rb')
    data=file.readlines()
    return data

def format_processing2 (path):
    name, extension=os.path.splitext(path)
    return extension
