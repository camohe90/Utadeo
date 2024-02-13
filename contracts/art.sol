// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ArtContract is ERC721, ERC721URIStorage, ERC721Burnable, Ownable {
    uint256 private _nextTokenId;

    struct contractInfo{
        string uri;
        address owner;
        address buyer;
        string hash_data;
        
    }

    mapping(uint => string) public artCollection;
    mapping(uint => contractInfo) public contractRegister;

    constructor(address initialOwner)
        ERC721("UTADEONFT", "UTD")
        Ownable(initialOwner)
    {}

    function safeMint(string memory uri) public onlyOwner {
        uint256 tokenId = _nextTokenId++;
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, uri);
        artCollection[tokenId] = uri;
    }

     function createContract(uint256 _tokenId, address buyer,string memory hash_data, string memory uri) public {
        require(msg.sender == ownerOf(_tokenId), "No eres el propietario del NFT" );
        contractRegister[_tokenId].owner = msg.sender;
        contractRegister[_tokenId].buyer = buyer;
        contractRegister[_tokenId].uri = uri;
        contractRegister[_tokenId].hash_data = hash_data;
        transferFrom(msg.sender, buyer,_tokenId );   
    }

    // The following functions are overrides required by Solidity.

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
