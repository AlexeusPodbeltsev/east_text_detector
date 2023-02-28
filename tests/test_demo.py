import os

from east_text_detector.demo import detect_text_on_image


def test_demo_on_test_image():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    res = detect_text_on_image(os.path.join(current_dir, 'test_image.jpg'))
    assert len(res) == 3
