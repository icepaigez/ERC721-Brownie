from brownie import ColorCollectible
from scripts.helper_script import fund_palette

def main():
	palette_instance = ColorCollectible[len(ColorCollectible) - 1] #brownie returns an array of contract instances, and this returns the most recently deployed
	fund_palette(palette_instance)

