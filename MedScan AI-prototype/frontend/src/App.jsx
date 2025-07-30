import React, { useState } from 'react';
import UploadForm from './UploadForm';
import ResultViewer from './ResultViewer';

function App() {
  const [prediction, setPrediction] = useState(null);
  return (
    <>
      <h2>Medical AI Scanner</h2>
      <UploadForm setPrediction={setPrediction} />
      {prediction && <ResultViewer prediction={prediction} />}
    </>
  );
}
export default App;
