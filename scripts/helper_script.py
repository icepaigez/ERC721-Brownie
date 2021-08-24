from brownie import ColorCollectible, accounts, network, config, interface

def get_color(color_number):
	switch = {0: 'Color_1', 1:'Color_2', 2: 'Color_3', 3: 'Color_4', 4 : 'Color_5'}
	return switch[color_number]


def fund_palette(nft_contract):
	dev = accounts.add(config["wallets"]["from_key"])
	link_token = interface.LinkTokenInterface(config["networks"][network.show_active()]["link_token"])
	link_token.transfer(nft_contract, 1 * 10 ** 18, {"from": dev}) 