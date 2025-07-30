import axios from 'axios';

function UploadForm({ setPrediction }) {
  const handleUpload = (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('file', file);
    axios.post('/upload', formData).then(res => {
      setPrediction(res.data.prediction);
    });
  };
  return <input type="file" onChange={handleUpload} />;
}
export default UploadForm;
