import json
import requests
import sys

z = 0
seed_address = sys.argv[1]
initialreq = "https://blockchain.info/rawaddr/{}".format(seed_address)

firstjson = (requests.get(initialreq)).json()
graphvizlines = []

addresslist = set([seed_address])
usedaddresslist = [seed_address]

for i in range(1,6):
    if z is 1:
        firstjson = (requests.get(initialreq)).json()
    
    for transaction in firstjson["txs"]:
        payerlist = []
        recipientlist = []
        
        print("\n{}".format(transaction["hash"]))

        for item in transaction["inputs"]:
            payerlist.append(item["prev_out"]["addr"])
            addresslist.add(item['prev_out']['addr'])
            #if item["prev_out"]["addr"] not in addresslist:
            #    addresslist.append(item["prev_out"]["addr"])

        for target in transaction["out"]:
            recipientlist.append(target["addr"])
            addresslist.add(target['addr'])
            #if target["addr"] not in addresslist:
            #    addresslist.append(target["addr"])

        for payer in payerlist:
            for recipient in recipientlist:
                a = '"{}" -> "{};"'.format(payer,recipient)
                if a not in graphvizlines:
                    graphvizlines.append(a)
    #i = i + 1    
    z = 1
        

for t in graphvizlines:
    print(t)

