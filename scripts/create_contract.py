from brownie import ArtContract, accounts, config
from datetime import date
from fpdf import FPDF
import hashlib
import os
from scripts.texto import *


def create_contract():
    global texto_cesion
    global texto_objeto
    global texto_precio
    global texto_inicial
    global texto_final
    global texto_firma
    pdf = FPDF() 
    account = accounts.add(config["wallets"]["from_key"])
    artContract = ArtContract[-1]
    tokenId = input("ingrese el Id de token del cual desea crear el contrato: ")
    autor = artContract.ownerOf(tokenId)
    buyer = input("Ingrese la dirección del comprador: ")
    uri = artContract.tokenURI(tokenId)
    print(uri, autor)

    texto_inicial = texto_inicial.replace("XXX", str(autor))
    texto_inicial = texto_inicial.replace("$$$", str(buyer))

    texto_objeto = texto_objeto.replace("XXXXXXXX", str(tokenId))
    texto_objeto = texto_objeto.replace("$$$$$", str(uri))
    texto_objeto = texto_objeto.replace("****", str(artContract))
    texto_objeto = texto_objeto.replace("----", str(tokenId))
    
    texto_precio = texto_precio.replace("XXXX", "1 ETH")
    texto_cesion = texto_cesion.replace("XXXXXX",str(tokenId))

    today = date.today() 
    d2 = today.strftime("%B %d, %Y")

    texto_final = texto_final.replace("XXXXXXXX", str(d2))

    texto_firma = texto_firma.replace("XXX", str(autor))
    texto_firma = texto_firma.replace("$$$", str(buyer))

    print("-------Generando contrato y transfiriendo el NFT---------")
    print("---------------------------------------------------------")
    

    with open('contratos/contrato_token'+str(tokenId)+'.txt', 'w') as f:
        
        for letra in texto_inicial:
            f.write(letra)
        
        for letra in texto_objeto:
            f.write(letra)
   
        for letra in texto_precio:
            f.write(letra)

        for letra in texto_regalias:
            f.write(letra)

        for letra in texto_cesion:
            f.write(letra)

        for letra in texto_final:
            f.write(letra)
        
        for letra in texto_firma:
            f.write(letra)
    
    pdf.add_page()
  
  
    pdf.set_font("Arial", size = 12)
    
    f = open('contratos/contrato_token'+str(tokenId)+'.txt', "r")
    
    for x in f:
        pdf.cell(20, 10, txt = x, ln = 2, align = 'L')
    
    pdf.output('contratos/contrato_token'+str(tokenId)+'.pdf')  

    sha256_hash = hashlib.sha256()
    with open('contratos/contrato_token'+str(tokenId)+'.pdf',"rb") as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                    sha256_hash.update(byte_block)
    hash_data=str(sha256_hash.hexdigest())

    artContract.createContract(tokenId, buyer, hash_data, uri,{"from":account})
       
def main():
    create_contract()
    