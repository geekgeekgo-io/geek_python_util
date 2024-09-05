
import os
class CommonUtil():
    def is_file_exists(self, file_path):
        if os.path.isfile(file_path):
            return True
        else:
            return False

