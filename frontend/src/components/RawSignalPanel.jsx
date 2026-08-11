
import React, { useEffect, useState } from 'react';
import { fetchRecordList, api, fetchAnalysis, fetchValidation } from "../api.js";


export default function RawSignalPanel({ rawSignal }) {
  if (!rawSignal) return <p>No data yet — select a record.</p>;

  return (
    <div>
      <h3>Raw Signal</h3>
      {/* TODO: replace with <LineChart data={rawSignal} /> */}
      <p>{rawSignal.length} samples loaded (chart goes here)</p>
    </div>
  );
}
