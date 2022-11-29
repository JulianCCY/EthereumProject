const inputMachineID = document.querySelector("#machine-id").value;
const inputPrescriptionID = document.querySelector("#prescription-id").value;
const inputDoctorAddress = document.querySelector("#doctor-address").value;
const inputPatientAddress = document.querySelector("#patient-address").value;
const inputFile = document.querySelector(".input-file");
const createButton = document.querySelector(".btn");
const filesUploaded = document.querySelector("#file");

createButton.addEventListener("click", async () => {
  // uploadData();
  uploadMultipleFiles();
});

async function uploadMultipleFiles() {
  const node = await Ipfs.create();

  const resultsArray = [];

  let fileArray = [];
  for (let i = 0; i < filesUploaded.files.length; i++) {
    const fileReader = new FileReader();
    fileReader.readAsArrayBuffer(filesUploaded.files[i]);

    fileReader.onload = async () => {
      let { path } = await node.add(fileReader.result);

      fileArray.push(path);

      console.log("FILE ARRAY", fileArray.toString());
      console.log("PATH", path);

      if (fileArray.length == filesUploaded.files.length) {
        console.log("EOFIHEFOIHEWFI");
        let metaData = {
          image: fileArray.toString(),
          name: "FromMachine",
          attributes: [{ machine: inputMachineID }],
        };

        console.log("Metadata", metaData);

        let allData = {
          metaData: metaData,
          machineId: inputMachineID,
          prescriptionId: inputPrescriptionID,
          doctorAddress: inputDoctorAddress,
          patientAddress: inputPatientAddress,
        };

        let request = new XMLHttpRequest();
        request.open("POST", `/ProcessFilesInfo/${JSON.stringify(allData)}`);
        request.send();
      }
    };
  }

  console.log("RESULTS ARRAY", resultsArray);

  //window.location.reload();
}

function uploadData() {
  console.log(filesUploaded.files);
  const fileReader = new FileReader();
  // Read file as ArrayBuffer
  fileReader.readAsArrayBuffer(filesUploaded.files[0]);
  //  Listen for the onload event
  fileReader.onload = async () => {
    const node = await Ipfs.create();
    // upload the file content
    let { path } = await node.add(fileReader.result);

    console.log("https://ipfs.io/ipfs/" + path + "?" + path);

    const allData = {
      image: path,
      name: machineName.value,
      attributes: [{ department: machineDepartment.value }],
    };

    console.log("test", allData);

    const request = new XMLHttpRequest();
    request.open("POST", `/ProcessInfo/${JSON.stringify(allData)}`);
    request.send();
    window.location.reload();
  };
}
