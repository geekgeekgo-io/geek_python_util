
import os
class CommonUtil():
    def is_file_exists(self, file_path):
        if os.path.isfile(file_path):
            return True
        else:
            return False

    def write_to_text_file(self, string_write, text_file_path):
        with open(text_file_path, 'w') as text_file:
            text_file.write(string_write)

