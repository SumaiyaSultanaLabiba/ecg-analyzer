
import React, { useEffect, useState } from 'react';
import { fetchRecordList, api, fetchAnalysis, fetchValidation } from "../api.js";


export default function ValidationDashboard({ recordName }) {
  const [validation, setValidation] = useState(null);

  useEffect(() => {
    if (!recordName) return;
    fetchValidation(recordName).then(setValidation).catch(console.error);
  }, [recordName]);

  if (!validation) return <p>No validation data yet.</p>;

  return (
    <div>
      <h3>Detection Accuracy (vs. PhysioNet ground truth)</h3>
      <p>Precision: {(validation.precision * 100).toFixed(1)}%</p>
      <p>Recall: {(validation.recall * 100).toFixed(1)}%</p>
      <p>
        TP: {validation.true_positive_count} | FP: {validation.false_positive_count} | FN:{" "}
        {validation.false_negative_count}
      </p>
    </div>
  );
}
