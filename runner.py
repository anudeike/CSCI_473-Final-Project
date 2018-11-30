"""
Filename: runner.py
Authors: Ikechuckwu A., David A
"""
import pandas as pd

api_key = "14B99EBD-FB07-36A1-A02F-3B0322779DCA"

def get_data(src=""):
  return pd.read_csv(src)

def main():
  try:
    src = "http://quickstats.nass.usda.gov/api/api_GET/?key="+ api_key +"&year__GE=1989&year__LE=2018&program=SURVEY&sector=\'ANIMALS & PRODUCTS\'&group=POULTRY&commodity_desc=TURKEYS&category=SLAUGHTERED&data_item__LIKE='F1 - SLAUGHTERED, MEASURED IN HEAD'&format=csv&state_alpha=VA"
    data = pd.read_csv(src, nrows=100)
    print(data.columns)
    print(data.shape)
    print(data['load_time'].describe())
    #http://quickstats.nass.usda.gov/api/api_GET/?key=14B99EBD-FB07-36A1-A02F-3B0322779DCA&year__GE=1989&year__LE=2018&program=SURVEY&sector=\'ANIMALS & PRODUCTS\'&group=POULTRY&commodity=TURKEYS&category=SLAUGHTERED&data_item__LIKE='F1 - SLAUGHTERED, MEASURED IN HEAD'&format=csv&state=VA
    print(data.head())
  except Exception as e:
    print("Error " + str(e))
  pass

if __name__ == "__main__":
  main()
