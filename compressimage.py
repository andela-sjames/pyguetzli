import subprocess

from shutil import rmtree
from os import path

class PyGuetzli(object):
    """Class defined to compress image."""

    def __init__(self, input_file_or_path, output_file_or_path):
        self.input_file = input_file_or_path
        self.output_file = output_file_or_path

    def check_image_quality(self, quality):
        if quality <= 85:
            return "Image quality too low for compression."
        return

    # method needs to execute guetzli before comparison should/can be made.
    def check_compression_quality(self):
        input_file_size = path.getsize(self.input_file)

        try:
            output_file_size = path.getsize(self.output_file)
        except Exception as e:
            # this typically makes the output file same size as the input file.
            output_file_size = input_file_size

        size_acurate = 100 * input_file_size / input_file_size
        if size_acurate < 100:
            return True
        else:
            return False

    def root_dir_image_compression(self, quality):
        self.check_image_quality(quality)
        command_line = "guetzli --quality {} {} {}".format(
            quality,
            self.input_file,
            self.output_file)



