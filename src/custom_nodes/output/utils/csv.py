# csv.py
import csv
from datetime import datetime

class CSVLogger:
    """A class to log the chosen information into csv dabble results"""

    def __init__(self, file_path, headers, period=1):
        headers.extend(["date"])

        self.csv_file = open(file_path, mode='a+')
        self.writer = csv.DictWriter(self.csv_file, fieldnames=headers)
        self.period = period

        # if file is empty write header
        if self.csv_file.tell() == 0: self.writer.writeheader()

        self.last_write = datetime.now()

    def write(self, content):
        curr_time = datetime.now()
        update_date = {"date": curr_time.strftime("%Y%m%d-%I:%M:%S")}
        content.update(update_date)

        if (curr_time - self.last_write).seconds >= int(self.period):
            self.writer.writerow(content)
            self.last_write = curr_time

    def __del__(self):
        self.csv_file.close()