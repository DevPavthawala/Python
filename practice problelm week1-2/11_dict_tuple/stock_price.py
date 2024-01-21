stock_prices = {"info" : [600,630,620],"ril" : [1430,1490,1567],"mtl" : [234,180,160]}

def print_all():
    for stock,price in stock_prices.items():

        print(f'{stock} ==>{price} ==> avg:{round(sum(price)/len(price),2)}')
        # avg can be done using statistics library using mean function

def add():
    stock_ticker = input("Enter the stock ticker :")
    enter_price = input("Enter the price of the stock")
    enter_price= int(enter_price)
    if stock_ticker in stock_prices:
        stock_prices[stock_ticker].append(enter_price)
    else:
        stock_prices[stock_ticker] = [enter_price]
    print_all()


def main():
    enter_input = input("Enter the input 'add' to add the stock ticker of 'print' to print the whole data :")
    enter_input.lower()
    if enter_input == 'print':
        print_all()
    elif enter_input == 'add':
        add()
    else:
        print("You have no enter valid operation pls Enter add/print")

if __name__ == '__main__':
    main()