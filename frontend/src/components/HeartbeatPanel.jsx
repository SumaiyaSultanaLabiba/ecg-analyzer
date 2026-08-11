
import React, { useEffect, useState } from 'react';
import { fetchRecordList, api, fetchAnalysis, fetchValidation } from "../api.js";


export default function HeartbeatPanel({ filteredSignal, rPeakIndices, heartRateBpm }) {
  if (!filteredSignal) return <p>No data yet — select a record.</p>;

  return (
    <div>
      <h3>Detected Heartbeats</h3>
      <p>
        <strong>Heart Rate:</strong> {heartRateBpm?.toFixed(1)} BPM
      </p>
      <p>{rPeakIndices?.length} beats detected</p>
      {/* TODO: replace with a chart that overlays markers at rPeakIndices
          on top of the filteredSignal line chart */}
    </div>
  );
}
