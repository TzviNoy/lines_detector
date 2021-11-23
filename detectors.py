def lines_detector(detector, image):
    return detector(image)


def harris_corner_detector():
    pass


def laplacian():
    pass


def create_detectors_dict():

    """return a dict with methods as names and functions which implement those methods as values """

    detectors_dict = {"harris_corner_detector": harris_corner_detector,
                      "laplacian": laplacian}

    return detectors_dict
