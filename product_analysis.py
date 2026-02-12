import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'C:\Users\lenovo\Downloads\products-100000.csv')

dataset.drop(['Index', 'Description', 'Size'],axis= 1, inplace= True)

def product_info_analyser():
    while True:
        try:
            ean = int(input('enter the EAN of your product'))
            if ean in dataset['EAN'].values:
                df = dataset[dataset['EAN'] == ean]
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
        except ValueError:
            print('Invalid Input or EAN does not exist')

def brand_price_scatter():
    while True:
        brand = input('enter the brand whose products prices you want to see')
        if brand in dataset["Brand"].values:
            df = dataset[dataset["Brand"] == brand]
            prices = df["Price"]
            id = df["Internal ID"]

            plt.scatter(id, prices, color= 'red')
            plt.xlabel("Internal ID")
            plt.ylabel("Price")
            plt.show()
            check = input("Do you want to see the prices summary of another brand?(answer in 'yes' or 'no':)").strip().lower()
            if check == 'yes':
                continue
            else:
                break


def brand_analysis():
    while True:
            brand = input("Mention the name of your brand: ").lower().title()
            if brand in dataset["Brand"].values:
                df = dataset[dataset["Brand"] == brand]
                max_price = df["Price"].max()
                min_price = df["Price"].min()
                num_products = df["Name"].count()
                def products():
                    while True:                   
                        products = df["Name"].to_list()
                        print(f'the list of your Brand\'s products names: {products}')
                        stocks = df["Stock"].to_list()
                        print(f'their respective stocks are: {stocks}')
                        check = input("Do you want to see the prices summary of another brand?(answer in 'yes' or 'no':)").strip().lower()
                        if check == 'yes':
                            continue
                        else:
                            break
                    
                mean_price = df["Price"].mean()
                print(f'your brand\'s name is {brand}')
                print(f'{brand}\'s minimum price is {min_price} and maximum price is {max_price}')
                print(f'{brand}\'s mean pricing is {mean_price}')
                print(f'{brand} has a total of {num_products} products')
                check = input('do you want to see the name and stock of these products?(answer in yes/no): ').strip().lower()
                if check == 'yes':
                    products()
                else:
                    continue
                ovr_func_check = input('do you want to see the analysis of another brand?answer in yes/no: ').strip().lower()
                if check == 'yes':
                    continue
                else:
                    break
            else:
                print('brand not in dataset, re-enter')            
