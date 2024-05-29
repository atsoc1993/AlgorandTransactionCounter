from algosdk.v2client.algod import AlgodClient
import time

# Setup an Algorand node @ https://developer.algorand.org/docs/run-a-node/setup/install/
# Youtube Tutorial to Setup a Node: https://www.youtube.com/watch?v=sbGoXaWOIcA (IGNORE THAT THE TITLE SAYS "RELAY NODE", THIS IS FOR A PARTICIPATION NODE)
# Use 'cat algod.token' and 'cat algod.net' terminal commands in data directory of node to obtain node token and node port respectively
# Port can be manually adjusted by using 'cp config.json.example config.json' and adjusting "EndPointAddress" setting

algod_token = '' #INSERT NODE TOKEN HERE
algod_port = 'http://0.0.0.0:0000' #INSERT NODE PORT HERE
algod_client = AlgodClient(algod_token, algod_port)


last_block = algod_client.status()['last-round']
last_block_tc = algod_client.block_info(last_block)['block']['tc']

while True:
    block_cursor = algod_client.status()['last-round']
    if block_cursor > last_block:
        block_cursor_tc = algod_client.block_info(block_cursor)['block']['tc']
        block_cursor_tc_diff = block_cursor_tc - last_block_tc
        print(f'Total Transactions for Block: {block_cursor}: {block_cursor_tc_diff}')
        print(f'Total Transactions: {block_cursor_tc}\n')
        last_block = block_cursor
        last_block_tc = block_cursor_tc
    time.sleep(1)
        
