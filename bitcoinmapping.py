import json
import requests

z = 0
i = 0
firstpart = "https://blockchain.info/rawaddr/"
initialinput = input("please type the 'seed' address: ")
initialreq = firstpart + initialinput

firstjson = (requests.get(initialreq)).json()
graphvizlines = []

addresslist = []
usedaddresslist = []

addresslist.append(initialinput)
usedaddresslist.append(initialinput)

while i < 6:
    if z is 1:
        initialreq = firstpart + addresslist[i]
        firstjson = (requests.get(initialreq)).json()
    
    for transaction in firstjson["txs"]:
        payerlist = []
        recipientlist = []
        
        print("\n" + transaction["hash"])

        for item in transaction["inputs"]:
            payerlist.append(item["prev_out"]["addr"])
            if item["prev_out"]["addr"] not in addresslist:
                addresslist.append(item["prev_out"]["addr"])

        for target in transaction["out"]:
            recipientlist.append(target["addr"])
            if target["addr"] not in addresslist:
                addresslist.append(target["addr"])

        for payer in payerlist:
            for recipient in recipientlist:
                a = '"' + payer + '"' + " -> " + '"' + recipient + '"' + ";"
                if a not in graphvizlines:
                    graphvizlines.append(a)
    i = i + 1    
    z = 1
        

for t in graphvizlines:
    print(t)

