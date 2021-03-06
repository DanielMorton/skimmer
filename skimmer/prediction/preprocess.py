import numpy as np
import cv2

from efficientnet.tfkeras import preprocess_input
from .config import IMG_SIZE


def read_image(img_file):
    return preprocess_input(square_crop(cv2.cvtColor(cv2.imread(img_file), cv2.COLOR_BGR2RGB)))


def square_crop(img, size=IMG_SIZE):
    rows, cols, _ = img.shape

    # Pad rows to be at least *size* pixels.
    if rows < size:
        row_pad = (size - rows) // 2
        pad_size = rows + 2 * row_pad
        img = cv2.copyMakeBorder(img, row_pad, row_pad + np.sign(size - pad_size),
                                 0, 0, cv2.BORDER_CONSTANT,
                                 value=0)

    # Pad columns to be at least *size* pixels.
    if cols < size:
        col_pad = (size - cols) // 2
        pad_size = cols + 2 * col_pad
        img = cv2.copyMakeBorder(img, 0, 0, col_pad, col_pad + np.sign(size - pad_size),
                                 cv2.BORDER_CONSTANT, value=0)

    # Update dimensions
    rows, cols, _ = img.shape

    # If image is not square, trim larger dimension make it square.
    trim = (max(rows, cols) - min(rows, cols)) // 2
    if trim > 0:
        img = img[trim:rows - trim, :, :] if rows > cols else img[:, trim:cols - trim, :]
        rows, cols, _ = img.shape

        # Drop a row or column to fix one-off errors
        if rows > cols:
            img = img[:-1, :, :]
        elif rows < cols:
            img = img[:, :-1, :]

    # Return central size x size square.
    if rows > size:
        middle = rows // 2
        return img[middle - size // 2:middle + size // 2, middle - size // 2:middle + size // 2, :]
    else:
        return img
