function ResultViewer({ prediction }) {
  return (
    <div>
      <h3>Prediction: {prediction > 0.5 ? "Positive" : "Negative"}</h3>
      <img src="/heatmap" alt="AI Heatmap" style={{ maxWidth: "100%" }} />
    </div>
  );
}
export default ResultViewer;
