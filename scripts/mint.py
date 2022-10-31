from brownie import ArtContract, accounts, config


def mint_art():
    account = accounts.add(config["wallets"]["from_key"])
    artContract = ArtContract[-1]
    uri = input("Ingrese la URL de la metadata: ")
    artContract.safeMint(uri,{"from":account})

def main():
    mint_art()