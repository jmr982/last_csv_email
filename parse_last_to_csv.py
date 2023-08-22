#!/bin/python3

import sys
import subprocess


def get_log(logtype="last", since="yesterday"):
    raw_log = subprocess.run(["sudo", logtype, "-F", "-s", since],
                             stdout=subprocess.PIPE)
    log = raw_log.stdout.decode("utf-8")
    return log


def parse_log_to_csv(log_file):
    log_file = log_file.split("\n")
    log_csv = "user,port,ip,time_start,time_end,duration\n"  # Header
    for line in log_file[:-3]:
        parsed_line = ""
        prev_value = 0
        for value in [9, 22, 39, 63, 66, 90, 120]:
            if prev_value != 63:
                parsed_line += line[prev_value:value].strip() + ","
            prev_value = value
        log_csv += parsed_line[:-1] + "\n"
    return log_csv


if __name__ == "__main__":
    try:
        file_name = "last_since_yesterday.csv"
        csv = parse_log_to_csv(get_log())
        with open(file_name, "w") as f:
            f.write(csv)
        print(f"Saved last login since yesterday as: {file_name}")
    except Exception as e:
        print(e)
