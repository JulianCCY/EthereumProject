import json

abi = json.loads("""[
	{
		"inputs": [],
		"stateMutability": "payable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "approved",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "ApprovalForAll",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "itemId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "ipfsHash",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "ipfsUrl",
				"type": "string"
			}
		],
		"name": "DataItemAdded",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "minter",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "nftId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "tokenURI",
				"type": "string"
			}
		],
		"name": "Minted",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_tokenId",
				"type": "uint256"
			}
		],
		"name": "changeOwnerOfToken",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "dataItems",
		"outputs": [
			{
				"internalType": "string",
				"name": "ipfsHash",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "ipfsUrl",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "getApproved",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "getOwnerOfToken",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			}
		],
		"name": "isApprovedForAll",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "tokenURI",
				"type": "string"
			}
		],
		"name": "mint",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "ownerOf",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			},
			{
				"internalType": "bytes",
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "ipfsHash",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "ipfsUrl",
				"type": "string"
			}
		],
		"name": "saveData",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "ipfsHash",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "ipfsUrl",
						"type": "string"
					}
				],
				"internalType": "struct NewDataNFT.DataItem[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "setApprovalForAll",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes4",
				"name": "interfaceId",
				"type": "bytes4"
			}
		],
		"name": "supportsInterface",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "tokenIdToOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "tokenIdToURI",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "tokenURI",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]""")

bytecode = "60806040526040518060400160405280600881526020017f44617461204e46540000000000000000000000000000000000000000000000008152506040518060400160405280600781526020017f446174614e465400000000000000000000000000000000000000000000000000815250816000908051906020019062000088929190620001a9565b508060019080519060200190620000a1929190620001a9565b505050620000c4620000b8620000db60201b60201c565b620000e360201b60201c565b620000d533620000e360201b60201c565b620002be565b600033905090565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600660006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b828054620001b79062000259565b90600052602060002090601f016020900481019282620001db576000855562000227565b82601f10620001f657805160ff191683800117855562000227565b8280016001018555821562000227579182015b828111156200022657825182559160200191906001019062000209565b5b5090506200023691906200023a565b5090565b5b80821115620002555760008160009055506001016200023b565b5090565b600060028204905060018216806200027257607f821691505b602082108114156200028957620002886200028f565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b61373680620002ce6000396000f3fe608060405234801561001057600080fd5b50600436106101585760003560e01c80637f1dd80b116100c3578063ba444fec1161007c578063ba444fec146103ec578063c87b56dd1461041c578063d85d3d271461044c578063e985e9c51461047c578063ec4206a1146104ac578063f2fde38b146104c857610158565b80637f1dd80b146103175780638da5cb5b1461034757806395d89b4114610365578063968a76cf14610383578063a22cb465146103b4578063b88d4fde146103d057610158565b806323b872dd1161011557806323b872dd1461024557806342842e0e146102615780636352211e1461027d5780636e9e48ef146102ad57806370a08231146102dd578063715018a61461030d57610158565b806301ffc9a71461015d5780630221e7851461018d57806306fdde03146101bd578063081812fc146101db578063095ea7b31461020b57806318160ddd14610227575b600080fd5b6101776004803603810190610172919061258f565b6104e4565b6040516101849190612b58565b60405180910390f35b6101a760048036038101906101a291906126aa565b6105c6565b6040516101b49190612b73565b60405180910390f35b6101c5610666565b6040516101d29190612b73565b60405180910390f35b6101f560048036038101906101f091906126aa565b6106f8565b6040516102029190612acf565b60405180910390f35b6102256004803603810190610220919061254f565b61073e565b005b61022f610856565b60405161023c9190612dec565b60405180910390f35b61025f600480360381019061025a9190612439565b61085c565b005b61027b60048036038101906102769190612439565b6108bc565b005b610297600480360381019061029291906126aa565b6108dc565b6040516102a49190612acf565b60405180910390f35b6102c760048036038101906102c291906126aa565b610963565b6040516102d49190612acf565b60405180910390f35b6102f760048036038101906102f291906123cc565b610996565b6040516103049190612dec565b60405180910390f35b610315610a4e565b005b610331600480360381019061032c91906126aa565b610a62565b60405161033e9190612acf565b60405180910390f35b61034f610a79565b60405161035c9190612acf565b60405180910390f35b61036d610aa3565b60405161037a9190612b73565b60405180910390f35b61039d600480360381019061039891906126aa565b610b35565b6040516103ab929190612b95565b60405180910390f35b6103ce60048036038101906103c9919061250f565b610c79565b005b6103ea60048036038101906103e5919061248c565b610c8f565b005b61040660048036038101906104019190612632565b610cf1565b6040516104139190612b36565b60405180910390f35b610436600480360381019061043191906126aa565b610fc3565b6040516104439190612b73565b60405180910390f35b610466600480360381019061046191906125e9565b6110b6565b6040516104739190612dec565b60405180910390f35b610496600480360381019061049191906123f9565b6111c6565b6040516104a39190612b58565b60405180910390f35b6104c660048036038101906104c1919061254f565b61125a565b005b6104e260048036038101906104dd91906123cc565b6112db565b005b60007f80ac58cd000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614806105af57507f5b5e139f000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916145b806105bf57506105be8261135f565b5b9050919050565b600a60205280600052604060002060009150905080546105e5906130c5565b80601f0160208091040260200160405190810160405280929190818152602001828054610611906130c5565b801561065e5780601f106106335761010080835404028352916020019161065e565b820191906000526020600020905b81548152906001019060200180831161064157829003601f168201915b505050505081565b606060008054610675906130c5565b80601f01602080910402602001604051908101604052809291908181526020018280546106a1906130c5565b80156106ee5780601f106106c3576101008083540402835291602001916106ee565b820191906000526020600020905b8154815290600101906020018083116106d157829003601f168201915b5050505050905090565b6000610703826113c9565b6004600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b6000610749826108dc565b90508073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614156107ba576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107b190612dac565b60405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff166107d9611414565b73ffffffffffffffffffffffffffffffffffffffff161480610808575061080781610802611414565b6111c6565b5b610847576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161083e90612dcc565b60405180910390fd5b610851838361141c565b505050565b60085481565b61086d610867611414565b826114d5565b6108ac576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108a390612bec565b60405180910390fd5b6108b783838361156a565b505050565b6108d783838360405180602001604052806000815250610c8f565b505050565b6000806108e883611864565b9050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16141561095a576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161095190612d8c565b60405180910390fd5b80915050919050565b600b6020528060005260406000206000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415610a07576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016109fe90612cec565b60405180910390fd5b600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b610a566118a1565b610a60600061191f565b565b600080610a6e836108dc565b905080915050919050565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b606060018054610ab2906130c5565b80601f0160208091040260200160405190810160405280929190818152602001828054610ade906130c5565b8015610b2b5780601f10610b0057610100808354040283529160200191610b2b565b820191906000526020600020905b815481529060010190602001808311610b0e57829003601f168201915b5050505050905090565b600c8181548110610b4557600080fd5b9060005260206000209060020201600091509050806000018054610b68906130c5565b80601f0160208091040260200160405190810160405280929190818152602001828054610b94906130c5565b8015610be15780601f10610bb657610100808354040283529160200191610be1565b820191906000526020600020905b815481529060010190602001808311610bc457829003601f168201915b505050505090806001018054610bf6906130c5565b80601f0160208091040260200160405190810160405280929190818152602001828054610c22906130c5565b8015610c6f5780601f10610c4457610100808354040283529160200191610c6f565b820191906000526020600020905b815481529060010190602001808311610c5257829003601f168201915b5050505050905082565b610c8b610c84611414565b83836119e5565b5050565b610ca0610c9a611414565b836114d5565b610cdf576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610cd690612bec565b60405180910390fd5b610ceb84848484611b52565b50505050565b6060610cfb6118a1565b6000835111610d3f576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610d3690612ccc565b60405180910390fd5b6000825111610d83576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610d7a90612bcc565b60405180910390fd5b600c60405180604001604052808581526020018481525090806001815401808255809150506001900390600052602060002090600202016000909190919091506000820151816000019080519060200190610ddf9291906121e0565b506020820151816001019080519060200190610dfc9291906121e0565b5050507f6891983d42a48e510754f618abfbc8c414f4b10f9cf5d0f428133dbc60d5eb24600c805490508484604051610e3793929190612e37565b60405180910390a1600c805480602002602001604051908101604052809291908181526020016000905b82821015610fb75783829060005260206000209060020201604051806040016040529081600082018054610e94906130c5565b80601f0160208091040260200160405190810160405280929190818152602001828054610ec0906130c5565b8015610f0d5780601f10610ee257610100808354040283529160200191610f0d565b820191906000526020600020905b815481529060010190602001808311610ef057829003601f168201915b50505050508152602001600182018054610f26906130c5565b80601f0160208091040260200160405190810160405280929190818152602001828054610f52906130c5565b8015610f9f5780601f10610f7457610100808354040283529160200191610f9f565b820191906000526020600020905b815481529060010190602001808311610f8257829003601f168201915b50505050508152505081526020019060010190610e61565b50505050905092915050565b6060610fce82611bae565b61100d576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161100490612d6c565b60405180910390fd5b6000600a6000848152602001908152602001600020805461102d906130c5565b80601f0160208091040260200160405190810160405280929190818152602001828054611059906130c5565b80156110a65780601f1061107b576101008083540402835291602001916110a6565b820191906000526020600020905b81548152906001019060200180831161108957829003601f168201915b5050505050905080915050919050565b60006110c06118a1565b600860008154809291906110d390613128565b9190505550600060085490506110e93382611bef565b6110f38184611c0d565b82600a6000838152602001908152602001600020908051906020019061111a9291906121e0565b5033600b600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055503373ffffffffffffffffffffffffffffffffffffffff167fe7cd4ce7f2a465edc730269a1305e8a48bad821e8fb7e152ec413829c01a53c482856040516111b5929190612e07565b60405180910390a280915050919050565b6000600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b6112626118a1565b61126a610a79565b600960006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506112d7600960009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16838361156a565b5050565b6112e36118a1565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415611353576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161134a90612c2c565b60405180910390fd5b61135c8161191f565b50565b60007f01ffc9a7000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b6113d281611bae565b611411576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161140890612d8c565b60405180910390fd5b50565b600033905090565b816004600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff1661148f836108dc565b73ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92560405160405180910390a45050565b6000806114e1836108dc565b90508073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff161480611523575061152281856111c6565b5b8061156157508373ffffffffffffffffffffffffffffffffffffffff16611549846106f8565b73ffffffffffffffffffffffffffffffffffffffff16145b91505092915050565b8273ffffffffffffffffffffffffffffffffffffffff1661158a826108dc565b73ffffffffffffffffffffffffffffffffffffffff16146115e0576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016115d790612c4c565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415611650576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161164790612c8c565b60405180910390fd5b61165d8383836001611c81565b8273ffffffffffffffffffffffffffffffffffffffff1661167d826108dc565b73ffffffffffffffffffffffffffffffffffffffff16146116d3576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016116ca90612c4c565b60405180910390fd5b6004600082815260200190815260200160002060006101000a81549073ffffffffffffffffffffffffffffffffffffffff02191690556001600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055506001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a461185f8383836001611da7565b505050565b60006002600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b6118a9611414565b73ffffffffffffffffffffffffffffffffffffffff166118c7610a79565b73ffffffffffffffffffffffffffffffffffffffff161461191d576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161191490612d4c565b60405180910390fd5b565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600660006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b8173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff161415611a54576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611a4b90612cac565b60405180910390fd5b80600560008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c3183604051611b459190612b58565b60405180910390a3505050565b611b5d84848461156a565b611b6984848484611dad565b611ba8576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611b9f90612c0c565b60405180910390fd5b50505050565b60008073ffffffffffffffffffffffffffffffffffffffff16611bd083611864565b73ffffffffffffffffffffffffffffffffffffffff1614159050919050565b611c09828260405180602001604052806000815250611f44565b5050565b611c1682611bae565b611c55576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611c4c90612d0c565b60405180910390fd5b80600760008481526020019081526020016000209080519060200190611c7c9291906121e0565b505050565b6001811115611da157600073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff1614611d155780600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254611d0d9190612fdb565b925050819055505b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614611da05780600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254611d989190612f85565b925050819055505b5b50505050565b50505050565b6000611dce8473ffffffffffffffffffffffffffffffffffffffff16611f9f565b15611f37578373ffffffffffffffffffffffffffffffffffffffff1663150b7a02611df7611414565b8786866040518563ffffffff1660e01b8152600401611e199493929190612aea565b602060405180830381600087803b158015611e3357600080fd5b505af1925050508015611e6457506040513d601f19601f82011682018060405250810190611e6191906125bc565b60015b611ee7573d8060008114611e94576040519150601f19603f3d011682016040523d82523d6000602084013e611e99565b606091505b50600081511415611edf576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611ed690612c0c565b60405180910390fd5b805181602001fd5b63150b7a0260e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916817bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614915050611f3c565b600190505b949350505050565b611f4e8383611fc2565b611f5b6000848484611dad565b611f9a576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611f9190612c0c565b60405180910390fd5b505050565b6000808273ffffffffffffffffffffffffffffffffffffffff163b119050919050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415612032576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161202990612d2c565b60405180910390fd5b61203b81611bae565b1561207b576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161207290612c6c565b60405180910390fd5b612089600083836001611c81565b61209281611bae565b156120d2576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016120c990612c6c565b60405180910390fd5b6001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a46121dc600083836001611da7565b5050565b8280546121ec906130c5565b90600052602060002090601f01602090048101928261220e5760008555612255565b82601f1061222757805160ff1916838001178555612255565b82800160010185558215612255579182015b82811115612254578251825591602001919060010190612239565b5b5090506122629190612266565b5090565b5b8082111561227f576000816000905550600101612267565b5090565b600061229661229184612ea1565b612e7c565b9050828152602081018484840111156122b2576122b1613203565b5b6122bd848285613083565b509392505050565b60006122d86122d384612ed2565b612e7c565b9050828152602081018484840111156122f4576122f3613203565b5b6122ff848285613083565b509392505050565b600081359050612316816136a4565b92915050565b60008135905061232b816136bb565b92915050565b600081359050612340816136d2565b92915050565b600081519050612355816136d2565b92915050565b600082601f8301126123705761236f6131fe565b5b8135612380848260208601612283565b91505092915050565b600082601f83011261239e5761239d6131fe565b5b81356123ae8482602086016122c5565b91505092915050565b6000813590506123c6816136e9565b92915050565b6000602082840312156123e2576123e161320d565b5b60006123f084828501612307565b91505092915050565b600080604083850312156124105761240f61320d565b5b600061241e85828601612307565b925050602061242f85828601612307565b9150509250929050565b6000806000606084860312156124525761245161320d565b5b600061246086828701612307565b935050602061247186828701612307565b9250506040612482868287016123b7565b9150509250925092565b600080600080608085870312156124a6576124a561320d565b5b60006124b487828801612307565b94505060206124c587828801612307565b93505060406124d6878288016123b7565b925050606085013567ffffffffffffffff8111156124f7576124f6613208565b5b6125038782880161235b565b91505092959194509250565b600080604083850312156125265761252561320d565b5b600061253485828601612307565b92505060206125458582860161231c565b9150509250929050565b600080604083850312156125665761256561320d565b5b600061257485828601612307565b9250506020612585858286016123b7565b9150509250929050565b6000602082840312156125a5576125a461320d565b5b60006125b384828501612331565b91505092915050565b6000602082840312156125d2576125d161320d565b5b60006125e084828501612346565b91505092915050565b6000602082840312156125ff576125fe61320d565b5b600082013567ffffffffffffffff81111561261d5761261c613208565b5b61262984828501612389565b91505092915050565b600080604083850312156126495761264861320d565b5b600083013567ffffffffffffffff81111561266757612666613208565b5b61267385828601612389565b925050602083013567ffffffffffffffff81111561269457612693613208565b5b6126a085828601612389565b9150509250929050565b6000602082840312156126c0576126bf61320d565b5b60006126ce848285016123b7565b91505092915050565b60006126e38383612a7c565b905092915050565b6126f48161300f565b82525050565b600061270582612f13565b61270f8185612f41565b93508360208202850161272185612f03565b8060005b8581101561275d578484038952815161273e85826126d7565b945061274983612f34565b925060208a01995050600181019050612725565b50829750879550505050505092915050565b61277881613021565b82525050565b600061278982612f1e565b6127938185612f52565b93506127a3818560208601613092565b6127ac81613212565b840191505092915050565b60006127c282612f29565b6127cc8185612f63565b93506127dc818560208601613092565b6127e581613212565b840191505092915050565b60006127fb82612f29565b6128058185612f74565b9350612815818560208601613092565b61281e81613212565b840191505092915050565b6000612836602283612f74565b915061284182613223565b604082019050919050565b6000612859602d83612f74565b915061286482613272565b604082019050919050565b600061287c603283612f74565b9150612887826132c1565b604082019050919050565b600061289f602683612f74565b91506128aa82613310565b604082019050919050565b60006128c2602583612f74565b91506128cd8261335f565b604082019050919050565b60006128e5601c83612f74565b91506128f0826133ae565b602082019050919050565b6000612908602483612f74565b9150612913826133d7565b604082019050919050565b600061292b601983612f74565b915061293682613426565b602082019050919050565b600061294e602383612f74565b91506129598261344f565b604082019050919050565b6000612971602983612f74565b915061297c8261349e565b604082019050919050565b6000612994602e83612f74565b915061299f826134ed565b604082019050919050565b60006129b7602083612f74565b91506129c28261353c565b602082019050919050565b60006129da602083612f74565b91506129e582613565565b602082019050919050565b60006129fd602f83612f74565b9150612a088261358e565b604082019050919050565b6000612a20601883612f74565b9150612a2b826135dd565b602082019050919050565b6000612a43602183612f74565b9150612a4e82613606565b604082019050919050565b6000612a66603d83612f74565b9150612a7182613655565b604082019050919050565b60006040830160008301518482036000860152612a9982826127b7565b91505060208301518482036020860152612ab382826127b7565b9150508091505092915050565b612ac981613079565b82525050565b6000602082019050612ae460008301846126eb565b92915050565b6000608082019050612aff60008301876126eb565b612b0c60208301866126eb565b612b196040830185612ac0565b8181036060830152612b2b818461277e565b905095945050505050565b60006020820190508181036000830152612b5081846126fa565b905092915050565b6000602082019050612b6d600083018461276f565b92915050565b60006020820190508181036000830152612b8d81846127f0565b905092915050565b60006040820190508181036000830152612baf81856127f0565b90508181036020830152612bc381846127f0565b90509392505050565b60006020820190508181036000830152612be581612829565b9050919050565b60006020820190508181036000830152612c058161284c565b9050919050565b60006020820190508181036000830152612c258161286f565b9050919050565b60006020820190508181036000830152612c4581612892565b9050919050565b60006020820190508181036000830152612c65816128b5565b9050919050565b60006020820190508181036000830152612c85816128d8565b9050919050565b60006020820190508181036000830152612ca5816128fb565b9050919050565b60006020820190508181036000830152612cc58161291e565b9050919050565b60006020820190508181036000830152612ce581612941565b9050919050565b60006020820190508181036000830152612d0581612964565b9050919050565b60006020820190508181036000830152612d2581612987565b9050919050565b60006020820190508181036000830152612d45816129aa565b9050919050565b60006020820190508181036000830152612d65816129cd565b9050919050565b60006020820190508181036000830152612d85816129f0565b9050919050565b60006020820190508181036000830152612da581612a13565b9050919050565b60006020820190508181036000830152612dc581612a36565b9050919050565b60006020820190508181036000830152612de581612a59565b9050919050565b6000602082019050612e016000830184612ac0565b92915050565b6000604082019050612e1c6000830185612ac0565b8181036020830152612e2e81846127f0565b90509392505050565b6000606082019050612e4c6000830186612ac0565b8181036020830152612e5e81856127f0565b90508181036040830152612e7281846127f0565b9050949350505050565b6000612e86612e97565b9050612e9282826130f7565b919050565b6000604051905090565b600067ffffffffffffffff821115612ebc57612ebb6131cf565b5b612ec582613212565b9050602081019050919050565b600067ffffffffffffffff821115612eed57612eec6131cf565b5b612ef682613212565b9050602081019050919050565b6000819050602082019050919050565b600081519050919050565b600081519050919050565b600081519050919050565b6000602082019050919050565b600082825260208201905092915050565b600082825260208201905092915050565b600082825260208201905092915050565b600082825260208201905092915050565b6000612f9082613079565b9150612f9b83613079565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03821115612fd057612fcf613171565b5b828201905092915050565b6000612fe682613079565b9150612ff183613079565b92508282101561300457613003613171565b5b828203905092915050565b600061301a82613059565b9050919050565b60008115159050919050565b60007fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b82818337600083830152505050565b60005b838110156130b0578082015181840152602081019050613095565b838111156130bf576000848401525b50505050565b600060028204905060018216806130dd57607f821691505b602082108114156130f1576130f06131a0565b5b50919050565b61310082613212565b810181811067ffffffffffffffff8211171561311f5761311e6131cf565b5b80604052505050565b600061313382613079565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82141561316657613165613171565b5b600182019050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f6d697373696e6720495046532075726c20666f7220746865206461746120697460008201527f656d000000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a2063616c6c6572206973206e6f7420746f6b656e206f776e6560008201527f72206f7220617070726f76656400000000000000000000000000000000000000602082015250565b7f4552433732313a207472616e7366657220746f206e6f6e20455243373231526560008201527f63656976657220696d706c656d656e7465720000000000000000000000000000602082015250565b7f4f776e61626c653a206e6577206f776e657220697320746865207a65726f206160008201527f6464726573730000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a207472616e736665722066726f6d20696e636f72726563742060008201527f6f776e6572000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20746f6b656e20616c7265616479206d696e74656400000000600082015250565b7f4552433732313a207472616e7366657220746f20746865207a65726f2061646460008201527f7265737300000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f766520746f2063616c6c657200000000000000600082015250565b7f6d697373696e672049504653206861736820666f72207468652064617461206960008201527f74656d0000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a2061646472657373207a65726f206973206e6f74206120766160008201527f6c6964206f776e65720000000000000000000000000000000000000000000000602082015250565b7f45524337323155524953746f726167653a2055524920736574206f66206e6f6e60008201527f6578697374656e7420746f6b656e000000000000000000000000000000000000602082015250565b7f4552433732313a206d696e7420746f20746865207a65726f2061646472657373600082015250565b7f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572600082015250565b7f4552433732314d657461646174613a2055524920717565727920666f72206e6f60008201527f6e6578697374656e7420746f6b656e0000000000000000000000000000000000602082015250565b7f4552433732313a20696e76616c696420746f6b656e2049440000000000000000600082015250565b7f4552433732313a20617070726f76616c20746f2063757272656e74206f776e6560008201527f7200000000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f76652063616c6c6572206973206e6f7420746f60008201527f6b656e206f776e6572206f7220617070726f76656420666f7220616c6c000000602082015250565b6136ad8161300f565b81146136b857600080fd5b50565b6136c481613021565b81146136cf57600080fd5b50565b6136db8161302d565b81146136e657600080fd5b50565b6136f281613079565b81146136fd57600080fd5b5056fea264697066735822122067c115f034082432917e31fac66cb53fa14b9c2d9cd71cc9591f84586ea3591464736f6c63430008070033"
