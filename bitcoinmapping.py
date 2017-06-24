import json
import requests
import sys

import graphviz as gv

G = gv.Digraph(format='svg')

seed_address = sys.argv[1]
initialreq = "https://blockchain.info/rawaddr/{}".format(seed_address)

firstjson = (requests.get(initialreq)).json()

addresslist = set([seed_address])
usedaddresslist = [seed_address]

for transaction in firstjson["txs"]:
    
    payerlist = [item['prev_out']['addr'] for item in transaction['inputs']]
    recipientlist = [target['addr'] for target in transaction['out']]

    for payer in payerlist:
        for recipient in recipientlist:
            G.node(payer)
            G.node(recipient)
            G.edge(payer,recipient)

G.render('{}'.format(seed_address))
