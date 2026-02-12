import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'C:\Users\lenovo\Downloads\products-100000.csv')

dataset.drop(['Index', 'Description', 'Size'],axis= 1, inplace= True)

def product_infonyser():
    while True:
        id = int(input('enter the EAN of your product'))
        if id in dataset['EAN'].values:
            df = dataset[dataset['EAN'] == id]
            name = df['Name'].iloc[0]
            price = df['Price'].iloc[0]
            currency = df['Currency'].iloc[0]
            availability = df['Availability'].iloc[0]
            stock = df['Stock'].iloc[0]

            print(f"the name of your product is {name}")
            print(f"the price of your product is {price} {currency}")
            print(f"your product is currently {availability}")
            print(f"The stock of your product is {stock}")

            check = input('Do you wish to check another product?Yes or No: ').lower()
            if check in ['yes', 'no']:
                if check == 'yes':
                    continue
                else:
                    break
            else:
                print('Incorrect input')

def brand_price_graph():
    brand = input('enter the brand whose products prices you want to see')
    if brand in dataset["Brand"].values:
        df = dataset[dataset["Brand"] == brand]
        prices = df["Price"]
        id = df["Internal ID"]

        plt.scatter(id, prices, color= 'red')
        plt.xlabel("Internal ID")
        plt.ylabel("Price")
        plt.show()
brand_price_graph()