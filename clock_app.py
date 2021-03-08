from tkinter import *
from tkinter.ttk import *
from time import strftime

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'write your api key',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  price = data["data"][0]["quote"]["USD"]["price"]
  name = data["data"][0]["symbol"]
  price1 = data["data"][1]["quote"]["USD"]["price"]
  name1 = data["data"][1]["symbol"]
  print(name +"= $"+str(round(price,2)) + "  " +name1+"= $"+str(round(price1,2)))
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
root = Tk()
root.title("BTC & ETH")
root.geometry("600x150")
root.configure(bg="black")
frame = Frame(root)
def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital",80),background="black",foreground="green")
Label(frame,text=name +"= $"+str(round(price,2)) + "       " +name1+"= $"+str(round(price1,2)), font=("ds-digital",20),background="black",foreground="green").pack(fill=X)

label.pack(anchor="center")
frame.pack()
time()

mainloop()