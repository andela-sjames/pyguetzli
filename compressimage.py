import subprocess

from shutil import rmtree
from os import path

class PyGuetzli(object):
    """Class defined to compress image."""

    @classmethod
    def check_image_quality(cls, quality):
        if quality <= 85:
            return "Image quality too low for compression."
        return

    @classmethod
    def check_compression_quality(cls, input_file, output_file):
        input_file_size = path.getsize(input_file)
        output_file_size = path.getsize(output_file)
        pass

    @classmethod
    def root_dir_image_compression(cls, quality, input_file, output_file):
        ss
        cls().check_image_quality(quality)
        command_line = "guetzli --quality {} {} {}".format(quality, input_file, output_file)



