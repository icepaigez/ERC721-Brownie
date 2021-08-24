pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract ColorCollectible is ERC721, VRFConsumerBase {

	bytes32 internal keyHash;
    uint256 internal fee;
    uint256 public tokenCounter;

    enum Pallet{Color_1, Color_2, Color_3, Color_4, Color_5}
    
    uint256 public randomResult;

    mapping (bytes32 => address) public colorCreator;
    mapping (bytes32 => string) public creatorTokenURI;
    mapping (uint256 => Pallet) public colorIdToColor;
    mapping (bytes32 => uint256) public requestIdToColorId;

    event requestedColor(bytes32 indexed randomId);

    constructor(address _VRFCoordinator, address _LINKToken, bytes32 _keyHash) ERC721("COLORS", "COLOR") VRFConsumerBase(_VRFCoordinator, _LINKToken) public {
    	keyHash = _keyHash;
    	fee = 0.1 * 10 ** 18;
    	tokenCounter = 0;
    }

    function createColor(string memory tokenURI, uint256 seed) public returns (bytes32) {
    	bytes32 requestId = requestRandomness(keyHash, fee, seed);
    	colorCreator[requestId] = msg.sender;
    	creatorTokenURI[requestId] = tokenURI;
    	emit requestedColor(requestId);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
		address colorOwner = colorCreator[requestId];
		string memory colorURI = creatorTokenURI[requestId];
		uint256 colorId = tokenCounter;
		_safeMint(colorOwner, colorId);
		_setTokenURI(colorId, colorURI);
		Pallet color = Pallet(randomness % 5);
		colorIdToColor[colorId] = color;
		requestIdToColorId[requestId] = colorId;
		tokenCounter = tokenCounter + 1;
    }

    function setColorURI(uint256 colorId, string memory _colorURI) public {
    	require(_isApprovedOrOwner(_msgSender(), colorId), "ERC721: caller is neither owner nor approved");
    	_setTokenURI(colorId, _colorURI);
    }
}