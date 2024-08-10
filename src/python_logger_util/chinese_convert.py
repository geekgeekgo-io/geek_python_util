# opencc
# to make opencc work , also pip install opencc-python-reimplemented

import opencc

class ChineseConvert():

def simplify_chinese(text):
    """Convert Traditional Chinese to Simplified Chinese."""
    converter = opencc.OpenCC('t2s')
    return converter.convert(text)

def traditionalize_chinese(text):
    """Convert Simplified Chinese to Traditional Chinese."""
    converter = opencc.OpenCC('s2t')
    return converter.convert(text)

