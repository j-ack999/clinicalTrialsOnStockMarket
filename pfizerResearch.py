# the purpose of this file is to research PFE.

# imports
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
##


# data = yf.download("PFE", start="2020-01-01", end="2021-01-01") # one year of data collected from MRNA
#print(data)

# Clinical Trial Announcement - Pfizer / BioNTech COVID Vaccine announcement 
# 6 Nov 2020 was the last day of trading before the news that their phase three trial showed the vaccine was 90% effective. 

widened_data = yf.download(
    'PFE',
    start='2020-11-02',
    end="2020-11-16",
    auto_adjust=True)

# determine percentage changes between consecutive closing prices 

widened_data['Return'] = widened_data['Close'].pct_change() 

widened_data['Cumulative Return'] = (1 + widened_data['Return']).cumprod() - 1 

print(widened_data[['Close', 'Return', 'Cumulative Return']])
      
# plot the data 

plot_data = widened_data.dropna() # drop all rows that have a value of NaN in *any* column 


plt.plot(plot_data.index, plot_data['Cumulative Return'] * 100)
plt.title("PFE Cumulative Percentage Returns")
plt.axvline(x=pd.Timestamp('2020-11-09'), color='red', linestyle='--', label='Announcement Day') # plot a vertical line at the date where the announcement was made 
plt.ylabel("Percentage change")
plt.xlabel("Date")
plt.tight_layout()
plt.legend()
plt.grid(True)
plt.show()
