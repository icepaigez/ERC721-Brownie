from brownie import ColorCollectible, network, accounts, config
from scripts.helper_script import get_color

metadata_dic = {
	"Color_1": "https://ipfs.io/ipfs/QmWaHVazFCVp2crRTB6XGA4oAnhj3NRJAx9ZSpXzHasSTv?filename=color_1.png",
	"Color_2": "https://ipfs.io/ipfs/QmdEnLYdqTWQeSzfYch7F3euvtm7KHeRbJCn9PAttxqHDy?filename=color_2.png",
	"Color_4": "https://ipfs.io/ipfs/QmeKitph5f5poS6iCUc2SPQV2kHqC1nRSfNXPewhh3kM6w?filename=color_4.png"
}

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"


def main():
	print("Working on " + network.show_active())
	palette_instance = ColorCollectible[len(ColorCollectible) - 1]
	token_count = palette_instance.tokenCounter()
	for color_id in range(token_count):
		color = get_color(palette_instance.colorIdToColor(color_id))
		if not palette_instance.tokenURI(color_id).startswith("https://"):
			print("Setting tokenURI of {}".format(color_id))
			set_colorURI(color_id, palette_instance, metadata_dic[color])
		else:
			print("Already set tokenURI {}".format(color_id))

def set_colorURI(color_id, nft_contract, color_uri):
	dev = accounts.add(config["wallets"]["from_key"])
	nft_contract.setColorURI(color_id, color_uri, {"from":dev})
	print("NFT can be viewed at {}".format(OPENSEA_FORMAT.format(nft_contract.address, color_id)))
