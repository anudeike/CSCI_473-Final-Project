"""
Filename: runner.py
Authors: Ikechuckwu A., David A
"""
import csv, os, requests
import pandas as pd

api_key = "14B99EBD-FB07-36A1-A02F-3B0322779DCA"
raw_data_filename = "raw_data.csv"

def main():
  src = "https://quickstats.nass.usda.gov/api/api_GET?key="+ api_key +"&short_desc=TURKEYS, YOUNG, SLAUGHTER, FI - SLAUGHTERED, MEASURED IN HEAD&freq_desc=MONTHLY&year__GE=1989&year__LT=2018&state_alpha=VA&format=CSV"
  try:
    data = requests.get(src)
    data = data.content.decode("utf-8")
    data = csv.reader(data.splitlines(), delimiter=",")
    with open(raw_data_filename, "w") as f:
      writer = csv.writer(f)
      for row in data:
        writer.writerow(row)
    data = pd.read_csv(raw_data_filename)
    print("Got data with shape: ", data.shape)

  except Exception as e:
    print("Error: %s" % e) 

if __name__ == "__main__":
  main()
