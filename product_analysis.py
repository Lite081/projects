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
                         print("Thank you for using this function")
                         break
                else:
                    print('Incorrect input')
        except ValueError:
            print('Invalid Input or EAN does not exist')

def brand_price_scatter():
    while True:
        brand = input('enter the brand whose products prices you want to see').lower().title()
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
                print("Thank you for using this function")
                break
        else:
            print("Brnad not found")


def brand_analysis():
    while True:
            brand = input("Mention the name of your brand: ").lower().title()
            if brand in dataset["Brand"].values:
                df = dataset[dataset["Brand"] == brand]
                max_price = df["Price"].max()
                min_price = df["Price"].min()
                num_products = df["Name"].count()                
                products = df["Name"].to_list()
                print(f'the list of your Brand\'s products names: {products}')
                stocks = df["Stock"].to_list()
                print(f'their respective stocks are: {stocks}')
                    
                mean_price = df["Price"].mean()
                print(f'your brand\'s name is {brand}')
                print(f'{brand}\'s minimum price is {min_price} and maximum price is {max_price}')
                print(f'{brand}\'s mean pricing is {mean_price}')
                print(f'{brand} has a total of {num_products} products')
                ovr_func_check = input('do you want to see the analysis of another brand?answer in yes/no: ').strip().lower()
                if ovr_func_check == 'yes':
                    continue
                elif ovr_func_check == 'no':
                    print("Thank you for using our program!")
                    break
                else:
                    print("Please answer in yes or no")
            else:
                print('brand not in dataset, re-enter')            

def highest_prices():
    while True:
        print("This function allows you to get the highest prices and the products they belong to upto any number")
        try:
            num = int(input("Enter upto which position do you want the highest prices: "))
            largest = dataset.nlargest(n= num, columns= "Price")
            print("Here are your results: ")
            print(largest)
            check = input("Do you want another ranking with different number of rows?(answer in yes or no strictly): ").strip().lower()
            if check == 'yes':
                continue
            elif check == 'no':
                print("thank you for using this function!")
                break
            else:
                print('invalid input')
        except ValueError:
            print("Please enter a suitable number")

def menu():
    while True:
        print("Welcome to my first decent project!")
        print("This project focuses on a pre-built dataset with 100000 rows, so it includes major brands")
        print("You can browse through several functions which will give you real-time analysis of brands and their products")
        print("You have several options: ")
        print("1. information of a particular product with its EAN")
        print("2. scatter plot of a a brand\'s products and their pricing using their internal IDs as identifiers")
        print("3. analysis of a brand and all it's products")
        print("4. a ranking of the highest priced products upto any position")
        check = input("Do you want to start the program?(answer in yes or no only)").strip().lower()
        if check == 'yes':
            try:
                n = int(input("You can enter the serial number of the function you want to use: "))
                if n == 1:
                    product_info_analyser()
                elif n == 2:
                    brand_price_scatter()
                elif n == 3:
                    brand_analysis()
                elif n == 4:
                    highest_prices()
                else:
                    print("please enter 1, 2, 3 or 4 as per the menu")
            except ValueError:
                print("Please adhere to the instructions")
        elif check == 'no':
            print("Thank you for giving this a try!")
            break
        else:
            print('please answer in yes or no')
                
menu()