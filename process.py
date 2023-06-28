import os
import sys
import shutil
import argparse
from colorama import init

from pidng.core import RPICAM2DNG

# fix colorama colors in windows console
init(convert=True)

input_folder = 'input'
output_folder = 'output'

image_extensions = ['.raw', '.jpg', '.jpeg']

parser = argparse.ArgumentParser(description='Script to extract the raw information of RaspiStill JPEG images and convert them to DNG files.')
parser.add_argument('--input', type=str, metavar='Input folder', default=input_folder, help='Folder with the image files (default: %(default)s)')
parser.add_argument('--output', type=str, metavar='Output folder', default=output_folder, help='Folder to export the DNG files (default: %(default)s)')

args = parser.parse_args()

def get_file_extension(filename):
    return os.path.splitext(filename)[1].lower()

def convert_image(path, output_folder):    

    # pass camera reference into the converter.
    file = RPICAM2DNG().convert(path)
    final_file = file.replace(input_folder, output_folder)

    # move file to final destination
    shutil.move(file, final_file)
    return final_file
    
def init():

    if not os.path.exists(output_folder):
        # If it doesn't exist, create it
        os.makedirs(output_folder)

    # Find files in the input folder
    for subdir, dirs, files in os.walk(args.input):
        for file in files:
            filepath = subdir + os.sep + file

            if (get_file_extension(file) in image_extensions): 

                try:
                    print(f'-> CONVERTING FILE {file}')
                    final_file = convert_image(filepath, output_folder)
                    print(f'--> CREATED FILE {final_file}')

                except RuntimeError as e:
                    print(f'ERROR: Unable to convert {filepath}')
                    print(e)
                    sys.exit(1)

if __name__ == '__main__':
    init()