# AlgorandTransactionCounter
A Simple Python Script that Tracks Algorand Blockchain Transactions (Includes Inner Transactions) [Node Required]
> Note: There is an automatic counter (easy and quick implementation) and a manual transaction counter. The automatic counter takes the difference of the previous block's transaction count and the current block's transaction count (Transaction counts are hardcoded into each block's details). The manual counter reads a transaction in a more intricate fashion, see the ProofOfConcept.py for a better understanding of how the manual counter works. 

# AlgodClient Class Methods Used [Automatic Counter]:
- status()
- block_info(block: int)
  
# AlgodClient Class Methods Used [Manual Counter]:
- status()
- get_block_tx_ids(round_num: int)
- pending_transaction_info(transaction_id: str)

## Installation
To use this script, you need to have an Algorand node running. Follow the instructions in the official documentation to set up your node or watch the Youtube Video Linked.

### Documentation
[Algorand Node Installation Guide](https://developer.algorand.org/docs/run-a-node/setup/install/)

### YouTube Instructions
[Algorand Node Setup Video](https://www.youtube.com/watch?v=sbGoXaWOIcA)
> Note: The video title mentions relay node setup, but it actually covers participation node setup.

## Node Participation
If you want your node to participate in consensus, follow these instructions for upcoming node-running incentives:
[Node Participation Guide](https://epocks.com/onlinenode.html)

## Popular Allo PoP NFTs to Track Participation
[Allo PoP NFTs](https://pop.allo.info/)
