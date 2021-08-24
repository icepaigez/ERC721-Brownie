from brownie import ColorCollectible, network
from metadata import color_metadata
from scripts.helper_script import get_color
from pathlib import Path
import os
import requests
import json

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
		metadata_filename = ("./metadata/{}/".format(network.show_active()) + str(color_id) + "-" + color + ".json")
		if Path(metadata_filename).exists():
			print("{} already found".format(metadata_filename))
		else:
			print("Creating metadata file {}".format(metadata_filename))
			collectible_metadata["name"] = get_color(nft_contract.colorIdToColor(color_id))
			collectible_metadata["description"] = "Shades of {}".format(collectible_metadata["name"])
			image_to_upload = None

			if os.getenv("UPLOAD_IPFS") == "true":
				image_path = "./img/{}.png".format(color.lower())
				image_to_upload = upload_to_ipfs(image_path)
				collectible_metadata["image"] = image_to_upload
			with open(metadata_filename, "w") as file:
				json.dump(collectible_metadata, file)
			if os.getenv("UPLOAD_IPFS") == "true":
				upload_to_ipfs(metadata_filename)



def upload_to_ipfs(filepath):
	with Path(filepath).open("rb") as fp:
		image_binary = fp.read()
		ipfs_url = "http://localhost:5001"
		response = requests.post(ipfs_url + "/api/v0/add", files={"file": image_binary})
		ipfs_hash = response.json()["Hash"]
		filename = filepath.split("/")[-1:][0]
		image_uri = "https://ipfs.io/ipfs/{}?filename={}".format(ipfs_hash, filename)
		print(image_uri)
		return image_uri 
	return None