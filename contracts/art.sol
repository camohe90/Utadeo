// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract ArtContract is ERC721, ERC721URIStorage, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;

    struct contractInfo{
        uint duration;
        string coverage;
        string uri;
        address autor;
        
    }

    mapping(uint => string) public artCollection;
    mapping(uint => contractInfo) public contractRegister;



    Counters.Counter private _tokenIdCounter;

    constructor() ERC721("MyToken", "MTK") {}

    function safeMint(string memory uri) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, uri);
        artCollection[tokenId] = uri;
    }

    function createContract(uint256 _tokenId, uint _duration, string memory _coverage, address _autor, address buyer) public {
        contractRegister[_tokenId].duration =_duration;
        contractRegister[_tokenId].coverage =_coverage;
        contractRegister[_tokenId].autor =_autor;
        contractRegister[_tokenId].uri = artCollection[_tokenId];
        transferFrom(msg.sender, buyer,_tokenId );   
    }

    // The following functions are overrides required by Solidity.

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }
}