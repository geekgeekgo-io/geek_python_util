# opencc
# to make opencc work , also pip install opencc-python-reimplemented

import opencc


class ChineseConvertUtil():

    def to_simplify_chinese(text):
        """Convert Traditional Chinese to Simplified Chinese."""
        converter = opencc.OpenCC('t2s')
        return converter.convert(text)

    def to_traditional_chinese(text):
        """Convert Simplified Chinese to Traditional Chinese."""
        converter = opencc.OpenCC('s2t')
        return converter.convert(text)
