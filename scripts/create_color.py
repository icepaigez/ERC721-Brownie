from brownie import ColorCollectible, accounts, config
from scripts.helper_script import get_color
import time

STATIC_SEED = 124

def main():
	dev = accounts.add(config["wallets"]["from_key"])
	palette_instance = ColorCollectible[len(ColorCollectible) - 1]
	transaction = palette_instance.createColor("None", STATIC_SEED, {"from": dev})
	transaction.wait(1)
	time.sleep(55)
	print (transaction)
	requestId = transaction.events["requestedColor"]["randomId"]
	color_id = palette_instance.requestIdToColorId(requestId)
	color = get_color(palette_instance.colorIdToColor(color_id)) 
	print('Chosen color of color_id {} is {}'.format(color_id, color))