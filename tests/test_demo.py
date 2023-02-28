from unittest import mock
import numpy as np

import pytest
from east_text_detector.demo import detect_text_on_image


def test_demo_on_test_image():
    res = detect_text_on_image('test_image.jpg')
    assert np.array_equal(res, [[[426, 127], [427, 106], [357, 103], [356, 124]],
                                [[375, 126], [376, 108], [251, 105], [250, 123]],
                                [[265, 120], [264, 99], [196, 100], [197, 121]]])
