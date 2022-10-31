from brownie import ArtContract, accounts, config 

def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    artContract = ArtContract.deploy(
        {"from":account},
        publish_source= True)
    return artContract

def main():
    deploy()