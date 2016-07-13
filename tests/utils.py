import os

import tests
from django.core.files import File


def create_test_video_file():
    video_file = open(os.path.join(tests.__path__[0], 'small.mp4'), 'rb')
    return File(video_file, name='small.mp4')
