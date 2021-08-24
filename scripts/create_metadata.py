from brownie import ColorCollectible, network
from metadata import color_metadata
from scripts.helper_script import get_color
from pathlib import Path

def main():
	print("Working on " + network.show_active())
	palette_instance = ColorCollectible[len(ColorCollectible) - 1]
	token_count = palette_instance.tokenCounter()
	print("number of deployed tokens is {}".format(token_count))
	write_metadata(token_count, palette_instance)

def write_metadata(token_count, nft_contract):
	for color_id in range(token_count):
		collectible_metadata = color_metadata.metadata_template
		color = get_color(nft_contract.colorIdToColor(color_id))
		metadata_filename = ("./metadata/{}".format(network.show_active()) + str(color_id) + "-" + color + ".json")
		if Path(metadata_filename).exists():
			print("{} already found".format(metadata_filename))
		else:
			print("Creating metadata file {}".format(metadata_filename))
			collectible_metadata["name"] = get_color(nft_contract.colorIdToColor(color_id))
			collectible_metadata["description"] = "Shades of {}".format(collectible_metadata["name"])
			#collectible_metadata["image"]
			print(collectible_metadata)