import pptx
from pptx.util import Pt, Inches
import os, sys


def putting(_image_num, _image_list, _slide):
    n = _image_num
    k = Inches(10) / (n + 1)
    _left = k / (n + 1)

    length = (Inches(10) - k) / n
    top = Inches(5) - length / 2
    left = _left

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.getcwd()

    for image in _image_list:
        _image_list[_image_list.index(image)] = application_path + "/images/" + image

    for n in range(n):
        _slide.shapes.add_picture(_image_list[n], left, top, length, length)
        left += (length + _left)