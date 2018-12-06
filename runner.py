"""
Filename: runner.py
Authors: Ikechuckwu A., David A
"""
import os, requests
import pandas as pd

api_key = "14B99EBD-FB07-36A1-A02F-3B0322779DCA"
raw_data_filename = "raw_data.csv"

def main():
  file_exists = True
  try:
    if not os.path.isfile(raw_data_filename):
      print("File [" + raw_data_filename + "] not present. Fetching via http...")
      # src = "http://quickstats.nass.usda.gov/api/api_GET/?key="+ api_key +"&year__GE=1989&year__LE=2018&program=SURVEY&sector=\'ANIMALS & PRODUCTS\'&group=POULTRY&commodity_desc=TURKEYS&category=SLAUGHTERED&data_item__LIKE='F1 - SLAUGHTERED, MEASURED IN HEAD'&format=csv&state_alpha=VA"
      # src = 'http://quickstats.nass.usda.gov/api/api_GET/?key='+ api_key +'&sector_desc="ANIMALS & PRODUCTS"&group_desc=POULTRY&commodity_desc=TURKEYS&short_desc="TURKEYS, YOUNG, SLAUGHTER, FI - SLAUGHTERED, MEASURED IN HEAD"&format=CSV&state_alpha=VA'
      src = "http://quickstats.nass.usda.gov/api/api_GET/?key="+ api_key +"&year__GE=1989&year__LE=2018&source_desc=SURVEY&sector=\'ANIMALS & PRODUCTS\'&group=POULTRY&commodity_desc=TURKEYS&category=SLAUGHTERED&short_desc__LIKE=\'TURKEYS, YOUNG, SLAUGHTER, FI - SLAUGHTERED, MEASURED IN HEAD\'&format=csv&state_alpha=VA"

      file_exists = False
    else:
      print("File [" + raw_data_filename + "] exists. Fetching locally...")
      src = raw_data_filename
    data = pd.read_csv(src)
    print("Finished fetching. Data size: [" + str(data.shape[0]) +" x " + str(data.shape[1]) + "]")
    if not file_exists:
      data.to_csv(raw_data_filename, index=False)

  except Exception as e:
    print("Error " + str(e))

if __name__ == "__main__":
  main()
