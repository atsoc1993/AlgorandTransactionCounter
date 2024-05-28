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
    try:
        status = algod_client.status()
        last_block = status.get('last-round', '')
        if last_block_cursor < last_block:
            last_block_cursor = last_block
            block_txs = algod_client.block_info(last_block)['block']['txns']
            print(f"Block Number: {last_block}")

            transaction_counter = 0
            inner_transaction_counter = 0

            for tx in block_txs:
                tx_info = algod_client.pending_transaction_info(tx['tx'])
                
                inner_transactions = tx_info.get('inner-txns', [])
                
                if not inner_transactions:
                    transaction_counter += 1
                else:
                    inner_transaction_counter += len(inner_transactions)
                    
            print(f"Total Transaction Count: {transaction_counter}")
            print(f"Total Inner Transaction Count: {inner_transaction_counter}")
            print(f"Transaction Sum: {transaction_counter + inner_transaction_counter}\n")

    except Exception as e:
        print(f"Error: {e}")
        
    time.sleep(1)
