import os,math
import pandas as pd

class Util:

    @staticmethod
    def get_row_count(csv_file):
        df = pd.read_csv(csv_file)
        rows = len(df.index)
        del df
        return rows

    @staticmethod
    def delete_swap_file(file):
        if os.path.exists(file):
            # removing the file using the os.remove() method
            os.remove(file)
        else:
            # file not found message
            print("File not found in the directory")

    @staticmethod
    def get_relative_path(full_path):
        return os.path.dirname(full_path)
    
    @staticmethod
    def get_base_name(full_path):
        # Get the filename only from the initial file path.
        filename = os.path.basename(full_path)
        # Use splitext() to get filename and extension separately.
        (file, ext) = os.path.splitext(filename)
        return file

    @staticmethod
    def round_up(n, decimals=0): 
        multiplier = 10 ** decimals 
        return math.ceil(n * multiplier) / multiplier

