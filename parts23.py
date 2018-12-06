"""
Filename: runner.py
Authors: Ikechuckwu A., David A
"""

# only used during sanity check.
# import scipy.stats as stats

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_data():
  data = pd.read_csv("raw_data.csv")
  return data

# I think this may have been unnecessary, end_code would have sufficed.
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

  # Period where drop occurs between 2002 and 2009
  # plt.plot(x[150: 175], y[150: 175])

  plt.plot(x, y)
  plt.ylabel("Value")
  plt.xlabel("Year-Month")
  plt.show()

  # TODO(anude, awogbemila): Report Mean and Median of the Value grouped by year.
  unique_years = data.year.unique()
  for year in unique_years:
    year_data = data.loc[data["year"] == year]
    year_value = year_data["Value"].apply(lambda val: int(val.replace(",", "")))
    print("year %s has mean %s and median %s" % (year, year_value.mean(), year_value.median()))

def do_november_2017_regression(data):
  data_for_2017 = data.loc[data["year"] == 2017]
  just_till_october = data_for_2017.loc[lambda df: df["reference_period_desc"] != "NOV"]
  just_till_october = just_till_october.loc[lambda df: df["reference_period_desc"] != "DEC"]

  x = list(range(1, 11))
  y = just_till_october["Value"].apply(lambda x: int(x.replace(",", "")))
  y = y.reset_index().drop(["index"], axis=1)

  # (a)
  # Assume y = mx + c
  m, c = np.polyfit(x, y, 1)
  print("slope: %s, intercept: %s" % (m, c))
  
  # (b)
  x = 11
  predicted_november_value = m * x + c
  print("Predicted November value %s" % predicted_november_value)
  
  # (c)
  actual_november_value = data_for_2017.loc[lambda df: df["reference_period_desc"] == "NOV"]["Value"].values[0]
  actual_november_value = int(actual_november_value.replace(",", ""))
  print("Actual November value %s" % actual_november_value)

  abs_error = abs(predicted_november_value - actual_november_value)
  print("Absolute error %s" % abs_error)

  # (d)
  # TODO(anude, awogbemila): compute r-squared value (over what time period?)
  # I'll assume just 2017.
  x = list(range(1, 11))
 
  value_mean = y.mean()
  predictions = pd.DataFrame([m * i + c for i in x], columns=["Value"])
  SSR = sum(((predictions - value_mean).apply(lambda val: val ** 2)).values)[0]
  SSE = sum((y - predictions).apply(lambda val: val ** 2).values)
  SSTO = sum((y - value_mean).apply(lambda val: val ** 2).values)
  r_squared = SSR / SSTO
  print("r-squared", r_squared)

  # Alternate R-Squared method verified to give smae result.
  # r_squared_ = 1 - (SSE / SSTO)
  # print("r-squared_", r_squared_)

  # Sanity check: gives good result. Don't forget to import scipy.stats
  # _, _, sprsq, _, _ = stats.linregress(x, y["Value"])
  # print("scipy r-squared", r_squared)

  # (e)
  # TODO(anude, awogbemila): line plot for 2017
  _, ax = plt.subplots()
  ax.plot(x, y, label="Raw Data") 
  ax.plot(x, predictions, label="Prediction")

  legend = ax.legend()
  plt.xlabel("month index")
  plt.ylabel("Value")
  plt.show()


def main():
  data = get_data()
  create_line_plot(data)
  do_november_2017_regression(data)

if __name__ == "__main__":
  main()
