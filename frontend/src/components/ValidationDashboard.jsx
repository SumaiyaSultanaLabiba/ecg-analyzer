import React from "react";

function ResultItem({ label, value }) {
  return (
    <div className="result-item">
      <span className="result-value">{label} : {value}</span>
    </div>
  );
}

export default function ValidationDashboard({ validation }) {
  return (
    <aside className="ecg-results">
      <h2>Analysis Result</h2>
      {validation ? (
        <>
          <h3>
            Detection Accuracy
            <br />
            <span style={{ fontWeight: 400, color: "#00897b" }}>(vs. PhysioNet ground truth)</span>
          </h3>
          <ResultItem label="Precision" value={`${(validation.precision * 100).toFixed(1)}%`} />
          <ResultItem label="Recall" value={`${(validation.recall * 100).toFixed(1)}%`} />
          <div className="results-divider" />
          <ResultItem label="True Positives" value={validation.true_positive_count} />
          <ResultItem label="False Positives" value={validation.false_positive_count} />
          <ResultItem label="False Negatives" value={validation.false_negative_count} />
        </>
      ) : (
        <p className="results-empty">Run analysis to see results.</p>
      )}
    </aside>
  );
}
