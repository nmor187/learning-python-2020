import yfinance as yf
tsla = yf.Ticker("TSLA")
print(tsla.info)
print(tsla.cashflow)
#Fake Stocks and their price
TSLA = 620
AAPL = 130
list = [TSLA, AAPL]
def purchasing_stocks():
	global TSLA
	print("Please fill out the information for the stock you wish to purchase:")
	symbol = raw_input("Symbol? ").upper()
	print("Entered: " + str(symbol))
	if symbol == 'TSLA':
		print("Current Price: " + str(TSLA))
	else:
		print("Error")
purchasing_stocks()
def question():
	purchase = raw_input("Would you like to purchase stocks?").lower()
	if 'y' in purchase:
		purchasing_stocks()
	elif 'n' in purchase:
		print("Okay, have a nice day!")
		exit()
	else:
		print("Invalid input, please try again")
		question()
def event_tsla():
	tsla_shares = float(raw_input("How many shares of tesla would you like to purchase?"))
	print("Purchased " + str(tsla_shares) + " shares of TSLA for " + str(tsla))