# PiDNG-script
Script to extract the raw information of RaspiStill JPEG images and convert them to DNG using an old [PiDNG](https://github.com/schoolpost/PiDNG) version.

Tested with Python 3.7.7

## Installation (using a virtual environment)
- Install virtualenv running `pip install virtualenv`
- On the project folder, create a virtual environment using virtualenv: `python -m venv .venv`
- Load the environment using `.venv\Scripts\activate`
- After the environment is loaded run `pip install -r requirements.txt` to install the dependencies

## Configuration
- Run `python process.py --help` to display the available options

## Usage
- Add the raw images in the `input` folder
- Run `python process.py` to convert all the images in that folder
- Check the DNG files in `output` folder
