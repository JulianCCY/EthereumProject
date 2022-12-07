from flask import Flask, render_template, url_for, request, redirect
from web3 import Web3
import collections
import handleActivity
import handleActivityDetails
import handleOwnNFT
import handleSingleTokenActivity
import handleMetaData

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
w3.eth.default_account = w3.eth.accounts[0]

async def medicalActivity():
  # get all valid transaction history on the chain
  allActivity = await handleActivity.getMedicalActivity(w3)
  
  txn_hash = request.args.get("tx")
  global cType 
  cType = request.args.get("cType")
  
  if txn_hash is not "" and txn_hash is not None:
    print(txn_hash)
    print(cType)
    return redirect(f'/tx/{txn_hash}')
  
  return render_template("medicalActivity.html", Activity=allActivity)

def txDetails(txn_hash):
  typeOfContract = cType
  transactionDetails = handleActivityDetails.getTransactionDetails(w3, typeOfContract, txn_hash)
  
  
  return render_template("transactionDetails.html", details=transactionDetails)

def fakeLogin():
  
  global currentUserAddress
  currentUserAddress = request.args.get("acc_num")
  global userAvatar
  userAvatar = request.args.get("avatar")
  global userIdentity
  userIdentity = request.args.get("id")
  
  if currentUserAddress or userAvatar or userIdentity:
    return redirect('/ownnft')
  
  gan_acc = w3.eth.accounts[:5]
  
  avatar = {
    0: "https://ipfs.io/ipfs/Qmemr6XQy7DqKi6q8SM6XuhJ6VSvEmktYHhvsUPpwWg3Wz",
    1: "https://ipfs.io/ipfs/QmSqhAwm5Yqdyf8Smkp3hpMt7gShDDEa27R51gR14qU7up",
    2: "https://ipfs.io/ipfs/QmPrGrmwkrPEUdyw3A2eoQtysBV8MsZ13VgBt7P4YVaeH9",
    3: "https://ipfs.io/ipfs/QmdVJ34h6GJzsrmxpVuqHvMrembxqpM3Xrtcn7GVnHYWCA",
    4: "https://ipfs.io/ipfs/QmS7rfZQjG135AwpuKjcVkFRgPJ6Fgk5rcYrPKtAfn6T4u",
  }
  
  identity = {
    0: "Doctor",
    1: "Patient",
    2: "Patient",
    3: "Patient",
    4: "Manufacturer"
  }
  
  account = collections.defaultdict(list)
  
  for i, e in enumerate(gan_acc):
    account[e].append(avatar[i])
    account[e].append(identity[i])
    
  
  return render_template("fakeLogin.html", accounts=account)

async def ownNFTs():
  
  user_acc = currentUserAddress
  w3.eth.default_account = user_acc
  
  user_avatar = userAvatar
  
  identity = userIdentity
  
  md, pd, pred, dd = await handleOwnNFT.getOwnNFTs(w3)
  
  # essential for access details page
  contractAddress = request.args.get("ca")
  tokenId = request.args.get("tid")
  
  # another variables for specific page
  global typeOfToken
  typeOfToken = request.args.get("type")
  global icon
  icon = request.args.get("icon")
  global contractOwner
  contractOwner = request.args.get("c_owner")
  global tokenOwner
  tokenOwner = request.args.get("owner")
  global dataContractAddress
  dataContractAddress = request.args.get("dca")
  global prescriptionContractAddress
  prescriptionContractAddress = request.args.get("preca")
  global metaDataUrl
  metaDataUrl = request.args.get("md_url")
  
  if contractAddress:
    return redirect(f'/{contractAddress}/{tokenId}')
  
  return render_template("OwnNFT.html", machine=md, 
                         patient=pd, 
                         prescription=pred, 
                         data=dd,
                         avatar=user_avatar,
                         user=w3.eth.default_account)

async def ownNFTDetails(contract_address, tid):
  
  typeoftoken = "" if typeOfToken is None else typeOfToken
  Icon = "" if icon is None else icon
  contractowner = "" if contractOwner is None else contractOwner
  tokenowner = "" if tokenOwner is None else tokenOwner
  datacontractaddress = "" if dataContractAddress is None else dataContractAddress
  prescriptioncontractaddress = "" if prescriptionContractAddress is None else prescriptionContractAddress
  metadataurl = "" if metaDataUrl is None else metaDataUrl
  metadata = [] # for the graph
  itemHistory = [] 
  
  metadata = []
  
  # if typeOfToken in [""]
  
  if typeOfToken is not None and typeOfToken in ["machine", "prescription", "data"]:
    itemHistory = await handleSingleTokenActivity.getSingleTokenActivity(w3,contract_address, tid, typeOfToken)

  return render_template("OwnNFTDetails.html",
                         contractAddress=contract_address,
                         tokenId=tid,
                         typeOfToken=typeoftoken,
                         icon=Icon,
                         contractOwner=contractowner,
                         tokenOwner=tokenowner,
                         dataContractAddress=datacontractaddress,
                         prescriptionContractAddress=prescriptioncontractaddress,
                         metaDataUrl=metadataurl,
                         metadata=metadata,
                         Activity=itemHistory)
  


# if __name__ == "__main__":
#   app2.run(debug=True)
#   app2.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
  
#  python3.10 -m flask --app app2 --debug run --host 0.0.0.0 --port 4444