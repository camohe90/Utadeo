from brownie import ArtContract, accounts, config
from datetime import date


texto_inicial = '''CONTRATO DE COMPRAVENTA Y CESIÓN DE DERECHOS
PATRIMONIALES DE UN NFT

Comparecen a la celebración del presente contrato, por una parte: Nombre, cédula o número de billetera XXX quien en adelante se denominará el AUTOR, y por otra: Nombre, cédula o número de billetera $$$ quien se denominará el COMPRADOR, para celebrar el contrato de compraventa y cesión de derechos patrimoniales que se regirá por las siguientes cláusulas
'''

texto_objeto = '''Primera: Objeto. Por medio de este contrato el AUTOR transfiere a título de compraventa al COMPRADOR el NFT con el ID XXXXXXXX, cuya obra se encuentra ubicada en el enlace $$$$$
'''

texto_precio = '''Segunda: Precio. El precio acordado para la presente compraventa es de XXXX.'''

texto_regalias = '''Tercera: Regalías. Se acuerda por las partes que en las futuras reventas del objeto contractual, el AUTOR se hará acreedor de un 8% del precio de la venta a título de regalías.'''

texto_cesion = '''Cuarta. Cesión de derechos. El AUTOR transfiere de manera total y sin limitación alguna al COMPRADOR, los derechos patrimoniales de autor que ostenta por la creación de la obra asociada al NFT con el ID XXXXXX. De tal manera,  se entiende que el COMPRADOR adquiere los derechos de uso, transformación, adaptación y comunicación pública de la obra, de tal suerte, se encuentra facultado para reproducirla, exhibirla, publicarla, transferirla o distribuirla con fines de lucro
'''

texto_final = '''Quinta. Legitimidad. El AUTOR declara que es el único titular de los derechos patrimoniales
que por este acto son cedidos y en consecuencia, puede disponer de ellos sin ningún tipo de limitación
o gravamen. Así mismo, declara que para la creación objeto de la presente cesión, no ha vulnerado
derechos de propiedad intelectual de terceros. En todo caso, El AUTOR acepta que responderá por
cualquier reclamo que en materia de derechos de propiedad intelectual se pueda presentar, exonerando de cualquier responsabilidad al COMPRADOR.

Sexta. Duración y territorio: La presente cesión se realiza a perpetuidad y no se establece una limitación territorial, teniendo en cuenta el fin del presente contrato de compraventa y cesión de derechos.

Séptima. Resolución de conflictos. Cláusula compromisoria: Las Partes Contratantes se comprometen expresa y especialmente a que cualquier controversia o divergencia que ocurra entre ellas por causa de la aplicación, ejecución, terminación o rescisión de este contrato, así como de la compensación de daños y perjuicios resultantes, se resolverá mediante la decisión de un tribunal de arbitramento integrado por un miembro designado por las partes, que funcionará en la ciudad de Bogotá, y que decidirá en Derecho. En lo previsto en esta cláusula se aplicarán las disposiciones pertinentes sobre el Proceso Arbitral.

Octava. Solemnidades especiales.  Como quiera que por virtud del presente contrato se transfiere el derecho de autor, este documento deberá inscribirse en el Registro Nacional de Derechos de Autor, como lo ordena el artículo 30 de La Ley 11450 De 2011.

Para que conste en prueba de conformidad las partes manifiestan su consentimiento el día XXXXXXXX, mediante: firma electrónica'''

def create_contract():
    global texto_cesion
    global texto_objeto
    global texto_precio
    global texto_inicial
    global texto_final
    account = accounts.add(config["wallets"]["from_key"])
    artContract = ArtContract[-1]
    tokenId = input("ingrese el Id de token del cual desea crear el contrato: ")
    #duration = int(input("Ingrese la duración del contrato: "))
    #coverage = input("Ingrese los paises de cobertura")
    autor = artContract.ownerOf(tokenId)
    buyer = input("Ingrese la dirección del comprador")
    uri = artContract.tokenURI(tokenId)
    print(uri, autor)

    texto_inicial = texto_inicial.replace("XXX", str(autor))
    texto_inicial = texto_inicial.replace("$$$", str(buyer))

    texto_objeto = texto_objeto.replace("XXXXXXXX", str(tokenId))
    texto_objeto = texto_objeto.replace("$$$$$", str(uri))
    
    texto_precio = texto_precio.replace("XXXX", "1 ETH")
    texto_cesion = texto_cesion.replace("XXXXXX",str(tokenId))

    today = date.today() 
    d2 = today.strftime("%B %d, %Y")

    texto_final = texto_final.replace("XXXXXXXX", str(d2))

    print("-------Generando contrato y transfiriendo el NFT---------")
    print("---------------------------------------------------------")
    
    

    #artContract.createContract(tokenId, duration , coverage, autor, buyer,{"from":account})

    with open('contrato.txt', 'w') as f:
        
        for letra in texto_inicial:
            f.write(letra)
        f.write("\n")
    
        for letra in texto_objeto:
            f.write(letra)
        f.write("\n")

        for letra in texto_precio:
            f.write(letra)
        f.write("\n")
        f.write("\n")

        for letra in texto_regalias:
            f.write(letra)
        f.write("\n")
        f.write("\n")

        for letra in texto_cesion:
            f.write(letra)
        f.write("\n")

        for letra in texto_final:
            f.write(letra)
        f.write("\n")
    
    

    
       
def main():
    create_contract()
    