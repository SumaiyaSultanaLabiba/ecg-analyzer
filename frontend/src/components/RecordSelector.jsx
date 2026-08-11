
import React, { useEffect, useState } from 'react';
import { fetchRecordList, api, fetchAnalysis, fetchValidation } from "../api.js";


export default function RecordSelector({ onSelect }) {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    fetchRecordList().then(setRecords).catch(console.error);
  }, []);

  return (
    <select onChange={(e) => onSelect(e.target.value)} defaultValue="">
      <option value="" disabled>
        Select an ECG record
      </option>
      {records.map((r) => (
        <option key={r} value={r}>
          Record {r}
        </option>
      ))}
    </select>
  );
}
