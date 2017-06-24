import json
import requests
import sys

z = 0
seed_address = sys.argv[1]
initialreq = "https://blockchain.info/rawaddr/{}".format(seed_address)

firstjson = (requests.get(initialreq)).json()
graphvizlines = set()

addresslist = set([seed_address])
usedaddresslist = [seed_address]

for transaction in firstjson["txs"]:
    
    print("\n{}".format(transaction["hash"]))

    payerlist = [item['prev_out']['addr'] for item in transaction['inputs']]
    recipientlist = [target['addr'] for target in transaction['out']]

    for payer in payerlist:
        for recipient in recipientlist:
            graphvizlines.add('"{}" -> "{};"'.format(payer,recipient))

for t in graphvizlines:
    print(t)

