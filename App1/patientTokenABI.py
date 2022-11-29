import json

abi = json.loads("""[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "patient",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "dataContract",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "prescriptionContract",
				"type": "address"
			}
		],
		"name": "addNewPatient",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
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
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "bool",
				"name": "success",
				"type": "bool"
			}
		],
		"name": "ContractOwnershipChanged",
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
				"name": "patient",
				"type": "address"
			}
		],
		"name": "checkIfPatientExists",
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
				"internalType": "address",
				"name": "patient",
				"type": "address"
			}
		],
		"name": "getPatient",
		"outputs": [
			{
				"internalType": "address",
				"name": "dataContract",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "prescriptionContract",
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
		"name": "numberOfPatients",
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
	}
]""")

bytecode = "60806040526000600860006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055503480156200005357600080fd5b506040518060400160405280600c81526020017f50617469656e74546f6b656e00000000000000000000000000000000000000008152506040518060400160405280600381526020017f50544b00000000000000000000000000000000000000000000000000000000008152508160009080519060200190620000d8929190620001f9565b508060019080519060200190620000f1929190620001f9565b50505062000114620001086200012b60201b60201c565b6200013360201b60201c565b62000125336200013360201b60201c565b6200030e565b600033905090565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600660006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b8280546200020790620002a9565b90600052602060002090601f0160209004810192826200022b576000855562000277565b82601f106200024657805160ff191683800117855562000277565b8280016001018555821562000277579182015b828111156200027657825182559160200191906001019062000259565b5b5090506200028691906200028a565b5090565b5b80821115620002a55760008160009055506001016200028b565b5090565b60006002820490506001821680620002c257607f821691505b60208210811415620002d957620002d8620002df565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b612af2806200031e6000396000f3fe608060405234801561001057600080fd5b506004361061012c5760003560e01c80638da5cb5b116100ad578063c87b56dd11610071578063c87b56dd14610330578063c8f0096a14610360578063e87ab7fe14610390578063e985e9c5146103ac578063f2fde38b146103dc5761012c565b80638da5cb5b1461028b57806395d89b41146102a9578063a22cb465146102c7578063b5368e20146102e3578063b88d4fde146103145761012c565b806342842e0e116100f457806342842e0e146101e75780636352211e1461020357806366fd838c1461023357806370a0823114610251578063715018a6146102815761012c565b806301ffc9a71461013157806306fdde0314610161578063081812fc1461017f578063095ea7b3146101af57806323b872dd146101cb575b600080fd5b61014b60048036038101906101469190611f26565b6103f8565b604051610158919061228f565b60405180910390f35b6101696104da565b60405161017691906122aa565b60405180910390f35b61019960048036038101906101949190611f80565b61056c565b6040516101a691906121ff565b60405180910390f35b6101c960048036038101906101c49190611ee6565b6105b2565b005b6101e560048036038101906101e09190611dd0565b6106ca565b005b61020160048036038101906101fc9190611dd0565b61072a565b005b61021d60048036038101906102189190611f80565b61074a565b60405161022a91906121ff565b60405180910390f35b61023b6107d1565b604051610248919061240c565b60405180910390f35b61026b60048036038101906102669190611d10565b6107d7565b604051610278919061240c565b60405180910390f35b61028961088f565b005b6102936108a3565b6040516102a091906121ff565b60405180910390f35b6102b16108cd565b6040516102be91906122aa565b60405180910390f35b6102e160048036038101906102dc9190611ea6565b61095f565b005b6102fd60048036038101906102f89190611d10565b610975565b60405161030b92919061221a565b60405180910390f35b61032e60048036038101906103299190611e23565b610a9e565b005b61034a60048036038101906103459190611f80565b610b00565b60405161035791906122aa565b60405180910390f35b61037a60048036038101906103759190611d10565b610b68565b604051610387919061228f565b60405180910390f35b6103aa60048036038101906103a59190611d7d565b610c1e565b005b6103c660048036038101906103c19190611d3d565b610d9f565b6040516103d3919061228f565b60405180910390f35b6103f660048036038101906103f19190611d10565b610e33565b005b60007f80ac58cd000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614806104c357507f5b5e139f000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916145b806104d357506104d282610e7f565b5b9050919050565b6060600080546104e990612600565b80601f016020809104026020016040519081016040528092919081815260200182805461051590612600565b80156105625780601f1061053757610100808354040283529160200191610562565b820191906000526020600020905b81548152906001019060200180831161054557829003601f168201915b5050505050905090565b600061057782610ee9565b6004600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b60006105bd8261074a565b90508073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff16141561062e576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610625906123cc565b60405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff1661064d610f34565b73ffffffffffffffffffffffffffffffffffffffff16148061067c575061067b81610676610f34565b610d9f565b5b6106bb576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016106b2906123ec565b60405180910390fd5b6106c58383610f3c565b505050565b6106db6106d5610f34565b82610ff5565b61071a576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610711906122cc565b60405180910390fd5b61072583838361108a565b505050565b61074583838360405180602001604052806000815250610a9e565b505050565b60008061075683611384565b9050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff1614156107c8576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107bf906123ac565b60405180910390fd5b80915050919050565b60075481565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415610848576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161083f9061236c565b60405180910390fd5b600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b6108976113c1565b6108a1600061143f565b565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b6060600180546108dc90612600565b80601f016020809104026020016040519081016040528092919081815260200182805461090890612600565b80156109555780601f1061092a57610100808354040283529160200191610955565b820191906000526020600020905b81548152906001019060200180831161093857829003601f168201915b5050505050905090565b61097161096a610f34565b8383611505565b5050565b6000806109806113c1565b60005b600980549050811015610a97578373ffffffffffffffffffffffffffffffffffffffff16600982815481106109bb576109ba612739565b5b906000526020600020906003020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415610a8457600060098281548110610a1f57610a1e612739565b5b906000526020600020906003020190508060010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168160020160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16935093505050610a99565b8080610a8f90612663565b915050610983565b505b915091565b610aaf610aa9610f34565b83610ff5565b610aee576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610ae5906122cc565b60405180910390fd5b610afa84848484611672565b50505050565b6060610b0b82610ee9565b6000610b156116ce565b90506000815111610b355760405180602001604052806000815250610b60565b80610b3f846116e5565b604051602001610b509291906121db565b6040516020818303038152906040525b915050919050565b6000610b726113c1565b6000805b600980549050811015610c14578373ffffffffffffffffffffffffffffffffffffffff1660098281548110610bae57610bad612739565b5b906000526020600020906003020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415610c0157600191505b8080610c0c90612663565b915050610b76565b5080915050919050565b610c266113c1565b6001600754610c3591906124c0565b600781905550600960405180606001604052808573ffffffffffffffffffffffffffffffffffffffff1681526020018473ffffffffffffffffffffffffffffffffffffffff1681526020018373ffffffffffffffffffffffffffffffffffffffff16815250908060018154018082558091505060019003906000526020600020906003020160009091909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060408201518160020160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505050505050565b6000600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b610e3b6113c1565b610e448161143f565b7f05654f36e2550343773cc40980261000be3091f4642ecb17b89d3fc29d3aec816001604051610e74919061228f565b60405180910390a150565b60007f01ffc9a7000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b610ef2816117bd565b610f31576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610f28906123ac565b60405180910390fd5b50565b600033905090565b816004600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff16610faf8361074a565b73ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92560405160405180910390a45050565b6000806110018361074a565b90508073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff16148061104357506110428185610d9f565b5b8061108157508373ffffffffffffffffffffffffffffffffffffffff166110698461056c565b73ffffffffffffffffffffffffffffffffffffffff16145b91505092915050565b8273ffffffffffffffffffffffffffffffffffffffff166110aa8261074a565b73ffffffffffffffffffffffffffffffffffffffff1614611100576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016110f79061230c565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415611170576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016111679061232c565b60405180910390fd5b61117d83838360016117fe565b8273ffffffffffffffffffffffffffffffffffffffff1661119d8261074a565b73ffffffffffffffffffffffffffffffffffffffff16146111f3576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016111ea9061230c565b60405180910390fd5b6004600082815260200190815260200160002060006101000a81549073ffffffffffffffffffffffffffffffffffffffff02191690556001600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055506001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a461137f8383836001611924565b505050565b60006002600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b6113c9610f34565b73ffffffffffffffffffffffffffffffffffffffff166113e76108a3565b73ffffffffffffffffffffffffffffffffffffffff161461143d576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016114349061238c565b60405180910390fd5b565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600660006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b8173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff161415611574576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161156b9061234c565b60405180910390fd5b80600560008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c3183604051611665919061228f565b60405180910390a3505050565b61167d84848461108a565b6116898484848461192a565b6116c8576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016116bf906122ec565b60405180910390fd5b50505050565b606060405180602001604052806000815250905090565b6060600060016116f484611ac1565b01905060008167ffffffffffffffff81111561171357611712612768565b5b6040519080825280601f01601f1916602001820160405280156117455781602001600182028036833780820191505090505b509050600082602001820190505b6001156117b2578080600190039150507f3031323334353637383961626364656600000000000000000000000000000000600a86061a8153600a858161179c5761179b6126db565b5b04945060008514156117ad576117b2565b611753565b819350505050919050565b60008073ffffffffffffffffffffffffffffffffffffffff166117df83611384565b73ffffffffffffffffffffffffffffffffffffffff1614159050919050565b600181111561191e57600073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff16146118925780600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825461188a9190612516565b925050819055505b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff161461191d5780600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825461191591906124c0565b925050819055505b5b50505050565b50505050565b600061194b8473ffffffffffffffffffffffffffffffffffffffff16611c14565b15611ab4578373ffffffffffffffffffffffffffffffffffffffff1663150b7a02611974610f34565b8786866040518563ffffffff1660e01b81526004016119969493929190612243565b602060405180830381600087803b1580156119b057600080fd5b505af19250505080156119e157506040513d601f19601f820116820180604052508101906119de9190611f53565b60015b611a64573d8060008114611a11576040519150601f19603f3d011682016040523d82523d6000602084013e611a16565b606091505b50600081511415611a5c576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611a53906122ec565b60405180910390fd5b805181602001fd5b63150b7a0260e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916817bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614915050611ab9565b600190505b949350505050565b600080600090507a184f03e93ff9f4daa797ed6e38ed64bf6a1f0100000000000000008310611b1f577a184f03e93ff9f4daa797ed6e38ed64bf6a1f0100000000000000008381611b1557611b146126db565b5b0492506040810190505b6d04ee2d6d415b85acef81000000008310611b5c576d04ee2d6d415b85acef81000000008381611b5257611b516126db565b5b0492506020810190505b662386f26fc100008310611b8b57662386f26fc100008381611b8157611b806126db565b5b0492506010810190505b6305f5e1008310611bb4576305f5e1008381611baa57611ba96126db565b5b0492506008810190505b6127108310611bd9576127108381611bcf57611bce6126db565b5b0492506004810190505b60648310611bfc5760648381611bf257611bf16126db565b5b0492506002810190505b600a8310611c0b576001810190505b80915050919050565b6000808273ffffffffffffffffffffffffffffffffffffffff163b119050919050565b6000611c4a611c458461244c565b612427565b905082815260208101848484011115611c6657611c6561279c565b5b611c718482856125be565b509392505050565b600081359050611c8881612a60565b92915050565b600081359050611c9d81612a77565b92915050565b600081359050611cb281612a8e565b92915050565b600081519050611cc781612a8e565b92915050565b600082601f830112611ce257611ce1612797565b5b8135611cf2848260208601611c37565b91505092915050565b600081359050611d0a81612aa5565b92915050565b600060208284031215611d2657611d256127a6565b5b6000611d3484828501611c79565b91505092915050565b60008060408385031215611d5457611d536127a6565b5b6000611d6285828601611c79565b9250506020611d7385828601611c79565b9150509250929050565b600080600060608486031215611d9657611d956127a6565b5b6000611da486828701611c79565b9350506020611db586828701611c79565b9250506040611dc686828701611c79565b9150509250925092565b600080600060608486031215611de957611de86127a6565b5b6000611df786828701611c79565b9350506020611e0886828701611c79565b9250506040611e1986828701611cfb565b9150509250925092565b60008060008060808587031215611e3d57611e3c6127a6565b5b6000611e4b87828801611c79565b9450506020611e5c87828801611c79565b9350506040611e6d87828801611cfb565b925050606085013567ffffffffffffffff811115611e8e57611e8d6127a1565b5b611e9a87828801611ccd565b91505092959194509250565b60008060408385031215611ebd57611ebc6127a6565b5b6000611ecb85828601611c79565b9250506020611edc85828601611c8e565b9150509250929050565b60008060408385031215611efd57611efc6127a6565b5b6000611f0b85828601611c79565b9250506020611f1c85828601611cfb565b9150509250929050565b600060208284031215611f3c57611f3b6127a6565b5b6000611f4a84828501611ca3565b91505092915050565b600060208284031215611f6957611f686127a6565b5b6000611f7784828501611cb8565b91505092915050565b600060208284031215611f9657611f956127a6565b5b6000611fa484828501611cfb565b91505092915050565b611fb68161254a565b82525050565b611fc58161255c565b82525050565b6000611fd68261247d565b611fe08185612493565b9350611ff08185602086016125cd565b611ff9816127ab565b840191505092915050565b600061200f82612488565b61201981856124a4565b93506120298185602086016125cd565b612032816127ab565b840191505092915050565b600061204882612488565b61205281856124b5565b93506120628185602086016125cd565b80840191505092915050565b600061207b602d836124a4565b9150612086826127bc565b604082019050919050565b600061209e6032836124a4565b91506120a98261280b565b604082019050919050565b60006120c16025836124a4565b91506120cc8261285a565b604082019050919050565b60006120e46024836124a4565b91506120ef826128a9565b604082019050919050565b60006121076019836124a4565b9150612112826128f8565b602082019050919050565b600061212a6029836124a4565b915061213582612921565b604082019050919050565b600061214d6020836124a4565b915061215882612970565b602082019050919050565b60006121706018836124a4565b915061217b82612999565b602082019050919050565b60006121936021836124a4565b915061219e826129c2565b604082019050919050565b60006121b6603d836124a4565b91506121c182612a11565b604082019050919050565b6121d5816125b4565b82525050565b60006121e7828561203d565b91506121f3828461203d565b91508190509392505050565b60006020820190506122146000830184611fad565b92915050565b600060408201905061222f6000830185611fad565b61223c6020830184611fad565b9392505050565b60006080820190506122586000830187611fad565b6122656020830186611fad565b61227260408301856121cc565b81810360608301526122848184611fcb565b905095945050505050565b60006020820190506122a46000830184611fbc565b92915050565b600060208201905081810360008301526122c48184612004565b905092915050565b600060208201905081810360008301526122e58161206e565b9050919050565b6000602082019050818103600083015261230581612091565b9050919050565b60006020820190508181036000830152612325816120b4565b9050919050565b60006020820190508181036000830152612345816120d7565b9050919050565b60006020820190508181036000830152612365816120fa565b9050919050565b600060208201905081810360008301526123858161211d565b9050919050565b600060208201905081810360008301526123a581612140565b9050919050565b600060208201905081810360008301526123c581612163565b9050919050565b600060208201905081810360008301526123e581612186565b9050919050565b60006020820190508181036000830152612405816121a9565b9050919050565b600060208201905061242160008301846121cc565b92915050565b6000612431612442565b905061243d8282612632565b919050565b6000604051905090565b600067ffffffffffffffff82111561246757612466612768565b5b612470826127ab565b9050602081019050919050565b600081519050919050565b600081519050919050565b600082825260208201905092915050565b600082825260208201905092915050565b600081905092915050565b60006124cb826125b4565b91506124d6836125b4565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0382111561250b5761250a6126ac565b5b828201905092915050565b6000612521826125b4565b915061252c836125b4565b92508282101561253f5761253e6126ac565b5b828203905092915050565b600061255582612594565b9050919050565b60008115159050919050565b60007fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b82818337600083830152505050565b60005b838110156125eb5780820151818401526020810190506125d0565b838111156125fa576000848401525b50505050565b6000600282049050600182168061261857607f821691505b6020821081141561262c5761262b61270a565b5b50919050565b61263b826127ab565b810181811067ffffffffffffffff8211171561265a57612659612768565b5b80604052505050565b600061266e826125b4565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8214156126a1576126a06126ac565b5b600182019050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f4552433732313a2063616c6c6572206973206e6f7420746f6b656e206f776e6560008201527f72206f7220617070726f76656400000000000000000000000000000000000000602082015250565b7f4552433732313a207472616e7366657220746f206e6f6e20455243373231526560008201527f63656976657220696d706c656d656e7465720000000000000000000000000000602082015250565b7f4552433732313a207472616e736665722066726f6d20696e636f72726563742060008201527f6f776e6572000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a207472616e7366657220746f20746865207a65726f2061646460008201527f7265737300000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f766520746f2063616c6c657200000000000000600082015250565b7f4552433732313a2061646472657373207a65726f206973206e6f74206120766160008201527f6c6964206f776e65720000000000000000000000000000000000000000000000602082015250565b7f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572600082015250565b7f4552433732313a20696e76616c696420746f6b656e2049440000000000000000600082015250565b7f4552433732313a20617070726f76616c20746f2063757272656e74206f776e6560008201527f7200000000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f76652063616c6c6572206973206e6f7420746f60008201527f6b656e206f776e6572206f7220617070726f76656420666f7220616c6c000000602082015250565b612a698161254a565b8114612a7457600080fd5b50565b612a808161255c565b8114612a8b57600080fd5b50565b612a9781612568565b8114612aa257600080fd5b50565b612aae816125b4565b8114612ab957600080fd5b5056fea2646970667358221220ce47e925698b3b5482ecd7c16f89d3b9d8f9f975bcbecb210e1f517a4cae236464736f6c63430008070033"
