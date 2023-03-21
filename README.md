# Python Thumbnail Generator
Python Thumbnail Generator is a simple program that helps you create thumbnails for your images in just a few lines of code. This program uses the Python Imaging Library (PIL) to manipulate images and create thumbnails.

## Prerequisites

1. ) Python 3.6 or higher
2. ) PIL (Python Imaging Library)

## Installation
Clone this repository: `git clone https://github.com/itachi1621/PythonThumbnailGenerator.git`
Install PIL:```
Copy code pip install pillow```

## Usage
1.) Open your terminal and navigate to the directory where you have cloned this repository.
2.) Run `python thumbnail_generator.py -h` to see the list of available commands and options.

```Copy code 
usage: thumbnail_generator.py [-h] [--width WIDTH] [--height HEIGHT] input_dir output_dir

Create thumbnails for images in a directory.

positional arguments:
  input_dir        Input directory containing images to be used for thumbnails
  output_dir       Output directory for thumbnails to be placed

options:
  -h, --help       show this help message and exit
  --width WIDTH    Width of the thumbnail
  --height HEIGHT  Height of the thumbnail

```
3.) To create a thumbnail, `run python thumbnail_creator.py  /path/to/images /path/to/thumbnails` .
This command will create thumbnails for all images in the /path/to/images directory as well as in any subdirectories.


## License
This program is licensed under the MIT License. See the LICENSE file for details.