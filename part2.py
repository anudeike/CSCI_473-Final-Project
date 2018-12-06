"""
Filename: runner.py
Authors: Ikechuckwu A., David A
"""
import matplotlib.pyplot as plt
import pandas as pd

def get_data():
  data = pd.read_csv("raw_data.csv")
  return data

year_index = {
  "JAN": 1,
  "FEB": 2,
  "MAR": 3,
  "APR": 4,
  "MAY": 5,
  "JUN": 6,
  "JUL": 7,
  "AUG": 8,
  "SEP": 9,
  "OCT": 10,
  "NOV": 11,
  "DEC": 12
}

def create_line_plot(data):
  """
  We sort the data here by year and then month so that the line
  plot is shown in chronological order."
  """
  data["month_index"] = data["reference_period_desc"].apply(lambda x: year_index[x])
  data = data.sort_values(by=["year", "month_index"])
  value_data = data["Value"]
  
  # Prepare line plot input
  x = data["year"].apply(lambda x: str(x) + "\n") + data["reference_period_desc"] 
  y = value_data.apply(lambda x: int(x.replace(",", "")))

  plt.plot(x, y)
  plt.ylabel("Value")
  plt.xlabel("Year-Month")
  plt.show()

def main():
  data = get_data()
  create_line_plot(data)
  pass

if __name__ == "__main__":
  main()