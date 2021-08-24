from brownie import ColorCollectible, network

def main():
	print("Working on " + network.show_active())
	palette_instance = ColorCollectible[len(ColorCollectible) - 1]
	token_count = palette_instance.tokenCounter()
	print(token_count)
