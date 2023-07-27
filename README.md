# JPEGRAW2DNG Converter
Script to extract and convert the raw information from RaspiStill JPEG+RAW images to DNGs using an older [PiDNG](https://github.com/schoolpost/PiDNG) version.

## How to use
- Valid extensions are JPEG, JPG and RAW
- The new DNG files will be created next to the original ones using the same filename
### Release version
- Download the Executable version from the `Releases` section (only Windows)
- Drag and drop image files or the folders containing them to the .exe
### Manual installation using a virtual environment and Python (tested with 3.7.7)
- Install virtualenv running `pip install virtualenv`
- On the project folder, create a virtual environment using virtualenv: `python -m venv .venv`
- Load the environment using `.venv\Scripts\activate`
- After the environment is loaded run `pip install -r requirements.txt` to install the dependencies

#### Usage
- Run `python process.py path_to_folder` to convert all the valid images in the folder


