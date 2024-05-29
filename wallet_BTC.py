from block_io import BlockIo
import jmespath
import json

version = 2
block_io = BlockIo('Api-Key', "Api_PAssword", version)

print("WELCOME TO MY BITCOIN WALLET DEMO")
#Username function
def username(name):
    return name

Name = username(input("Enter Username: "))

#greet user using created name
greet = ("HELLO" " " + username(name=Name))
print(greet)

# Generate a new wallet address with name
def gen_wallet(_name):
    generate_wa = block_io.get_new_address(label=_name)
    return generate_wa

gen_Wa = gen_wallet(Name)
print("++++++++++++++++Welcome!" + username(name=Name) + " " + "Your Account Details are below+++++++++")
print(gen_Wa)

#get wallet address by username
def get_wallet_by_name(fill):
    lol = json.dumps(block_io.get_address_by_label(label=(fill)))
    lol_ = json.loads(lol)
    wallet_addy = jmespath.search("data.address", lol_)
    return wallet_addy + " This is my wallet addy"

g_w_name = (get_wallet_by_name(input("Please Enter your Username: ")))
print(g_w_name + " This is your wallet address")

print("++++++++To Get Your Wallet Balance++++++++++")

#get wallet balance by using wallet address
def get_wallet_balance_by_addy(wallet_add):
    gadd = block_io.get_address_balance(address=(wallet_add))
    gadd_ = jmespath.search("data.available_balance", gadd)
    return gadd_

g_wallet = (get_wallet_balance_by_addy(input("Please Enter Your Address: ")))
print(g_wallet)

#amount to be sent
Amount_to = (input("Enter amount to send: "))

#address to send bitcoin to
addy_to = (input("Address to send to: "))

#Function to send transaction
def send_transfer(amount, recipient_address):
    _amount = amount
    to_address = recipient_address
    preparetx = block_io.prepare_transaction(amounts=_amount, to_addresses=to_address)
    signtx = block_io.create_and_sign_transaction(preparetx)

    response = block_io.submit_transaction(transaction_data=signtx)
    return response


send_t = send_transfer(Amount_to, addy_to)
status = jmespath.search("status", send_t)
if status == "success":
    print("Transaction sent ✅🚀")
else:
    print("not successful❌")
