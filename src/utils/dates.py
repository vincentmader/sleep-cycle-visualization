from datetime import datetime as dt


def get_date_from_str(string):
    return dt.strptime(string, "%Y-%m-%d %H:%M:%S")
