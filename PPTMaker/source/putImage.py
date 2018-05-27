import pptx
from pptx.util import Pt, Inches
import os


def putting(_image_num, _image_list, _slide):
    n = _image_num
    k = Inches(10) / (n + 1)
    _left = k / (n + 1)

    length = (Inches(10) - k) / n
    top = Inches(5) - length / 2
    left = _left

    path = os.getcwd()

    for image in _image_list:
        _image_list[_image_list.index(image)] = path + "/" + image

    for n in range(n):
        _slide.shapes.add_picture(_image_list[n], left, top, length, length)
        left += (length + _left)