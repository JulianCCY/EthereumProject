const image = document.querySelector('.image');
const inputFile = document.querySelector('.input-file');
const inputText = document.querySelector('.input-text');
const createButton = document.querySelector('.create-button');
const connectButton = document.querySelector('.connect-button');
const machineName = document.querySelector('#name');
const machineDepartment = document.querySelector('#department');
const filesUploaded = document.querySelector('#file');

function uploadImage() {
  const fileReader = new FileReader();
  // Read file as ArrayBuffer
  fileReader.readAsArrayBuffer(filesUploaded.files[0]);
  //  Listen for the onload event
  fileReader.onload = async () => {
    const node = await Ipfs.create();
    // upload the file content
    let { path } = await node.add(fileReader.result);

    console.log('https://ipfs.io/ipfs/' + path + '?' + path);

    const allData = {
      image: path,
      name: machineName.value,
      attributes: [{ department: machineDepartment.value }],
    };

    console.log('test', allData);
    const request = new XMLHttpRequest();
    request.open('POST', `/ProcessMachineInfo/${JSON.stringify(allData)}`);
    request.send();
    window.location.reload();
  };
}

inputFile.onchange = function (evt) {
  var tgt = evt.target || window.event.srcElement,
    files = tgt.files;

  // FileReader support
  if (FileReader && files && files.length) {
    var fr = new FileReader();
    fr.onload = function () {
      document.querySelector('.image').src = fr.result;
    };
    fr.readAsDataURL(files[0]);
  }
  // Not supported
  else {
    console.log('File reader not supported');
  }
};

async function connectToMetamask() {
  if (typeof window.ethereum !== 'undefined') {
    ethereum.request({ method: 'eth_requestAccounts' });
  }
}

createButton.addEventListener('click', async () => {
  uploadImage();
});

connectButton.addEventListener('click', () => {
  connectToMetamask();
});
