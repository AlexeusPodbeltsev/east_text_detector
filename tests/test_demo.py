import numpy as np
import os

import pytest
from east_text_detector.demo import detect_text_on_image


def test_demo_on_test_image():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    res = detect_text_on_image(os.path.join(current_dir, 'test_image.jpg'))
    assert np.array_equal(res, [[[426, 127], [427, 106], [357, 103], [356, 124]],
                                [[375, 126], [376, 108], [251, 105], [250, 123]],
                                [[265, 120], [264, 99], [196, 100], [197, 121]]])
