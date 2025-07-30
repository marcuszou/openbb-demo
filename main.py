## OpenBB Demo Project
## by Marcus Zou
## Refer to the official site https://openbb.co for more information

from openbb import obb
#import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('qtagg')

def main():
    output = obb.equity.price.historical("MSFT", "2023-01-01", "2025-06-30")
    df = output.to_dataframe()

    #df.set_index('date', inplace=True)

    # Scatter plot using Matplotlib
    plt.figure(figsize=(15, 5))
    plt.style.use('ggplot')
    plt.plot(df.index, df['close'], label='Close Price', color='blue')
    plt.fill_between(df.index, df['close'], color='blue', alpha=0.1)
    plt.legend()
    plt.grid(True)
    plt.title('Historical Close Price of MSFT')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
