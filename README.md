# my_wallet_BTC
Wallet_btc_python
Bitcoin wallets are essential tools for securely storing and managing your cryptocurrency holdings. Whether you're a beginner or an experienced user, setting up a Bitcoin wallet is a fundamental step in entering the world of decentralized finance. In this guide, we'll walk you through the process of creating a Bitcoin wallet using the bitcoinlib library in Python.

Step 1: Install bitcoinlib
First, ensure you have Python installed on your system. Open a terminal and install the bitcoinlib library using the following command:

pip install bitcoinlib
Step 2: Importing Required Modules
Before we dive into the code, we need to import the necessary modules. We'll be using Wallet from bitcoinlib.wallets to manage our Bitcoin wallet and Mnemonic from bitcoinlib.mnemonic to generate a secure passphrase.

from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic
Step 3: Creating the Bitcoin Wallet
Now, let's get to the exciting part - creating our Bitcoin wallet! We'll define a function create_bitcoin_wallet that takes a wallet_name as input and optionally allows specifying the network (defaulting to "testnet").

def create_bitcoin_wallet(wallet_name, network="testnet"):
    try:
        # Generate a random mnemonic passphrase
        passphrase = Mnemonic().generate()
        print("Mnemonic passphrase:", passphrase)

        # Create the wallet using the generated passphrase
        wallet = Wallet.create(wallet_name, keys=passphrase, network=network)
        wallet_address = wallet.get_key().address()
        print(f"Wallet '{wallet_name}' created with address: {wallet_address}")
    except Exception as e:
        if "already exists" in str(e):
            print(f"Wallet '{wallet_name}' already exists.")
        else:
            print(f"Error creating wallet: {e}")
Step 4: Main Execution
Lastly, we put everything together in the main execution block. Here, we specify the name of our wallet and call the create_bitcoin_wallet and generate_new_address functions to create the wallet and generate a new address, respectively.

if __name__ == "__main__":
    wallet_name = "my_bitcoin_wallet_42"
    create_bitcoin_wallet(wallet_name)
    generate_new_address(wallet_name)
Now, you have a basic Bitcoin wallet set up with the ability to generate new addresses.

Additional Resources
Bitcoinlib Documentation:

Bitcoin Wallets: A Comprehensive Guide

[Bitcoin.org - Choose your Wallet](https://bitcoin.org/en/choose-your-wallet
