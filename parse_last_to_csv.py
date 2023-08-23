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
    log_csv = "user,port,ip,time_start,time_end,duration\n"  # CSV header
    for line in log_file[:-3]:  # Omit last 3 rows (lines)
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
        logtype = sys.argv[1]
        if logtype != "lastb":
            raise Exception("wrong logtype")
    except Exception as e:
        logtype = "last"
    try:
        since = sys.argv[2]
        file_name = f"{logtype}_since_{since.replace(' ', '_')}.csv"
        csv = parse_log_to_csv(get_log(logtype, since))
        with open(file_name, "w") as f:
            f.write(csv)
        print(f"Saved {logtype} login since {since} as: {file_name}")
    except Exception as e:
        print(e)
