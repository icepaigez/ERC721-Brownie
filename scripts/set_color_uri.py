from brownie import ColorCollectible, network
from scripts.helper_script import get_color

def main():
	print("Working on " + network.show_active())
	palette_instance = ColorCollectible[len(ColorCollectible) - 1]
	token_count = palette_instance.tokenCounter()
