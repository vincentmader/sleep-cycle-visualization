from datetime import datetime as dt


def load_file_to_line_list(filepath):
    with open(filepath, "r") as fp:
        lines = fp.readlines()
    return lines


def get_date_from_str(string):
    return dt.strptime(string, "%Y-%m-%d %H:%M:%S")
