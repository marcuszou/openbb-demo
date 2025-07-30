from openbb import obb

def main():
    output = obb.equity.price.historical("AAPL")
    df = output.to_dataframe()
    print("Hello from openbb!")

if __name__ == "__main__":
    main()
