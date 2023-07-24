import os
import sys
import shutil
from colorama import init

from pidng.core import RPICAM2DNG

# fix colorama colors in windows console
init(convert=True)

input_folder = 'input'

image_extensions = ['.raw', '.jpg', '.jpeg']

raw_files = []

def get_file_extension(filename):
    return os.path.splitext(filename)[1].lower()

def convert_image(path):    
    # pass camera reference into the converter.
    file = RPICAM2DNG().convert(path)
    return file
    
def init():
    global raw_files
    try:
        print('''
Raspi RAW to DNG files

''')
        
        for arg in sys.argv[1:]:
            isDir = os.path.isdir(arg)
            if (isDir):
                for f in os.listdir(arg):
                    file_path = os.path.join(arg, f)
                    if os.path.isfile(file_path) and (get_file_extension(f) in image_extensions):                    
                        raw_files.append(file_path)
                
            elif (not isDir) and (get_file_extension(arg) in image_extensions):
                raw_files.append(arg)            
             
        if len(raw_files):
            for raw_file in raw_files:
                # If the file is an MP4, convert it to SRT format
                filepath = raw_file
                print(f'-> CONVERTING FILE {raw_file}')
                final_file = convert_image(filepath)
                print(f'--> CREATED FILE {final_file}')

        else:
            print('No valid files')

    except Exception as e:
        print("An error has ocurred:")
        print(e)
    
    input("Press Enter to Exit...")
        
if __name__ == '__main__':
    init()