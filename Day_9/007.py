#The secret auction instructions and Flowchart

import os
def clear():
    os.system('cls')  
    
from art import logo
print(logo)

bidder_data=[]

def add_bidders(bidder_name, bidder_price):
    bidders_list={}
    bidders_list["Name"] = bidder_name
    bidders_list["Bid"] = bidder_price
    bidder_data.append(bidders_list)

name=input("What is your name?: ")
bid=input("What's your bid?: ")

add_bidders(name,bid)
print(bidder_data)