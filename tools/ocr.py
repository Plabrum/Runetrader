from PIL import Image
import numpy as np
import pytesseract
import pyautogui
import cv2
import PIL
import time

CTN_DICT = {'o': '0',
            'O': '0',
            'l': '1',
            'I': '1',
            'i': '1',
            'M': '000000',
            "B": '8',
            'K': '000',
            'm': '000000',
            'k': '000',
            's': '5',
            'S': '5',
            'W': '40',
            '.': ' ',
            ',': ''}


def recognize_int(region):
    time.sleep(1)
    image = pyautogui.screenshot(region=region)
    image = np.array(image)
    image = cv2.resize(image, (0, 0), fx=2, fy=2)
    image = PIL.Image.fromarray(image)
    txt = pytesseract.image_to_string(image, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

    txt_list = [CTN_DICT[t] if t in list(CTN_DICT.keys()) else t for t in txt]
    txt_list = [str(x) for x in txt_list if x.isdigit()]
    txt_list = ''.join(txt_list)

    return txt_list


def get_order_info(exchange):
    quantity = recognize_int(exchange.quantity_info)
    price = recognize_int(exchange.price_info)

    print("DEBUG: Quantity {0}, PRICE {1}".format(quantity, price))

    return quantity, price
