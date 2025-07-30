# OpenBB Demo

OpenBB is an "investment research for everyone everywhere" per its github repo: https://github.com/OpenBB-finance/OpenBB/ and its Workspace site: https://openbb.co/

Let's get started.

## Initialize the project

We're using `uv` for Python Project Management this time. How to install `uv`? Please go to: https://github.com/marcuszou/uv-demo.

Then, launch terminal:
```shell
mkdir openbb-demo
cd openbb-demo
uv init
```
Note, make sure the Project name differs from the project folder name.

## Code along with First test run
Install the basic module of `openbb` by:
```shell
uv add openbb pandas matplotlib
```

update the `main.py` as below:
```python
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
```

Then give a shot:
```shell
uv run main.py
```

## Issue of running a GUI in WSL
When developing in WSL env, most likely you will not be able to run the `main.py` right away due to no interactive backend is installed / enabled. 

The matplotlib usually supports the following interactive backends:

- __TkAgg__: A widely used, lightweight, and cross-platform backend based on Tkinter.
- __QtAgg/Qt5Agg/Qt6Agg__: Backends leveraging the Qt framework for more advanced GUI integration, supporting PyQt and PySide bindings.
- __GTK3Agg/GTK4Agg__: Backends for integration with the GTK+ toolkit.
- __WxAgg__: A backend utilizing the wxWidgets GUI library.
- __MacOSX__: A specific backend for macOS systems.
- __nbAgg/ipympl__: Backends designed for interactive plots within Jupyter Notebooks and other web-based environments.
- __WebAgg__: A backend that serves plots via a web browser.

A few tries enabled me figure out the easiest nackend is `qtagg` supported by Qt5. Here is the way to install the modules:
```shell
sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
```
then install the qt5 into uv venv as below:
```shell
uv add qt5
```
Then create a simple `get_backend.py` as below:
```python
import matplotlib as mpl
print(mpl.get_backend())
```

Run the `python` script to test out:
```shell
uv run get_backend.py
```

## License
MIT