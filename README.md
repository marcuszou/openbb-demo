# OpenBB Demo

OpenBB is an "investment research for everyone everywhere" per its github repo: https://hithub.com/OpenBB-finance/OpenBB and its Workspace site: https://openbb.co/

Let's get started.

## Initialize the project

We're using `uv` for Python Project Management this time. How to install `uv`? Please go to: https://github.com/marcuszou/uv-demo.

Then, launch terminal:
```shell
mkdir openbb-demo
cd openbb-demo
uv init
```

## Code along and test out
Install the basic module of `openbb` by:
```shell
uv add openbb
```

update the `main.py` as below:
```shell
from openbb import obb

def main():
    output = obb.equity.price.historical("AAPL")
    df = output.to_dataframe()
    print("Hello from openbb!")

if __name__ == "__main__":
    main()
```

Then give a shot:
```shell
uv run main.py
```

## License
MIT