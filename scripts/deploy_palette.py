from brownie import ColorCollectible, accounts, network, config
from scripts.helper_script import fund_palette

VRFCoordinatorAddress = config["networks"][network.show_active()]["vrf_coordinator"] 
# network.show_active() returns the currently selected network during the deployment  
LINKTokenAddress = config["networks"][network.show_active()]["link_token"]
KeyHash = config["networks"][network.show_active()]["key_hash"]


def main():
	dev = accounts.add(config["wallets"]["from_key"])
	palette = ColorCollectible.deploy(VRFCoordinatorAddress, LINKTokenAddress, KeyHash, {"from": dev}, publish_source=True)
	fund_palette(palette)
	return palette