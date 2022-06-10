from os import system

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


end_auction = False
auction_list = {}

system("cls")
print(logo)

while not end_auction:
    name = input("What is your name? ")
    bid = float(input("What's your bid? $"))
    
    auction_list[name] = bid

    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    system("cls")

    if choice != 'yes':
        end_auction = True

winning_name = None
winning_bid = None

for name in auction_list:
    curr_name = name
    curr_bid = auction_list[name]

    if(winning_bid == None):
        winning_name = curr_name
        winning_bid = curr_bid
    else:
        if(winning_bid < curr_bid):
            winning_bid = curr_bid
            winning_name = curr_name

print(f"The winner is {winning_name} with a bid of $%.2f" %winning_bid)
    

