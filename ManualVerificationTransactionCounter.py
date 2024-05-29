from algosdk.v2client.algod import AlgodClient
import time

# Setup an Algorand node @ https://developer.algorand.org/docs/run-a-node/setup/install/
# Youtube Tutorial to Setup a Node: https://www.youtube.com/watch?v=sbGoXaWOIcA (IGNORE THAT THE TITLE SAYS "RELAY NODE", THIS IS FOR A PARTICIPATION NODE)
# Use 'cat algod.token' and 'cat algod.net' terminal commands in data directory of node to obtain node token and node port respectively
# Port can be manually adjusted by using 'cp config.json.example config.json' and adjusting "EndPointAddress" setting

algod_token = '' #INSERT NODE TOKEN HERE
algod_port = 'http://0.0.0.0:0000' #INSERT NODE PORT HERE
algod_client = AlgodClient(algod_token, algod_port)

last_block_cursor = 0

while True:
    status = algod_client.status()
    last_block = status.get('last-round', '')
    if last_block_cursor < last_block:
        last_block_cursor = last_block
        block_txs = algod_client.get_block_txids(last_block)['blockTxids']
        print("Block Number: ", {last_block})

        transaction_counter = 0
        inner_transaction_counter = 0
        
        for tx in block_txs:
            tx_info = algod_client.pending_transaction_info(tx)
            inner_transactions = tx_info.get('inner-txns', '')
            
            if inner_transactions == '':
                transaction_counter += 1
            
            else:
                for tx in inner_transactions:
                    inner_transaction_counter += 1
                    
        print("Total Transaction Count: ", {transaction_counter})
        print("Total Inner Transaction Count: ", {inner_transaction_counter})
        print("Transaction Sum: ", {transaction_counter + inner_transaction_counter})
        print('\n')

        
    time.sleep(1)
